import pytest
from pydantic import ValidationError

from app.v1.models.operations_request import OperationsRequest, Task


def test_task_enum_values():
    assert Task.detect.value == "detect"
    assert Task.annotate.value == "annotate"
    assert Task("detect") is Task.detect
    assert Task("annotate") is Task.annotate


def test_valid_minimal_request():
    req = OperationsRequest(
        text="قل هو الله احد",
        tasks=[Task.detect]
    )
    # Required fields
    assert req.text == "قل هو الله احد"
    assert req.tasks == [Task.detect]
    # Defaults
    assert req.find_errors is True
    assert req.find_missing is True
    assert req.allowed_error_percentage == 0.25
    assert req.min_match == 3
    assert req.return_json is False
    assert req.delimiters is None


def test_valid_full_request():
    req = OperationsRequest(
        text="الجهاد بالقوة، من ذلك قوله تعالى: {لا يستوي القاعدون من المؤمنين غير أولي الضرر والمجاهدون في سبيل الله بأموالهم وأنفسهم فضل الله المجاهدين بأموالهم وأنفسهم على القاعدين درجة وكلا وعد الله الحسنى وفضل الله المجاهدين على القاعدين أجرا عظيما}",
        tasks=[Task.detect, Task.annotate],
        find_errors=False,
        find_missing=False,
        allowed_error_percentage=0.5,
        min_match=5,
        return_json=True,
        delimiters=r"[,\.\;\:]+"
    )
    assert req.tasks == [Task.detect, Task.annotate]
    assert req.find_errors is False
    assert req.find_missing is False
    assert req.allowed_error_percentage == 0.5
    assert req.min_match == 5
    assert req.return_json is True
    assert req.delimiters == r"[,\.\;\:]+"


@pytest.mark.parametrize("payload, error_field", [
    ({}, "text"),  # missing both
    ({"text": "foo"}, "tasks"),  # missing tasks
    ({"tasks": ["detect"]}, "text"),  # missing text
])
def test_missing_required_fields(payload, error_field):
    with pytest.raises(ValidationError) as exc:
        OperationsRequest(**payload)
    errors = exc.value.errors()

    assert errors[0]["loc"] == (error_field,)
    assert errors[0]["type"] == "missing"


def test_invalid_task_entry():
    with pytest.raises(ValidationError) as exc:
        OperationsRequest(text="foo", tasks=["invalid"])
    errors = exc.value.errors()
    assert errors[0]["loc"] == ("tasks", 0)
    assert errors[0]["type"].startswith("enum")


@pytest.mark.parametrize("bad_pct, expected_type", [
    (-0.1, "greater_than_equal"),
    (1.1, "less_than_equal"),
])
def test_allowed_error_percentage_out_of_bounds(bad_pct, expected_type):
    with pytest.raises(ValidationError) as exc:
        OperationsRequest(
            text="foo",
            tasks=[Task.detect],
            allowed_error_percentage=bad_pct
        )
    errors = exc.value.errors()
    assert errors[0]["loc"] == ("allowed_error_percentage",)
    assert errors[0]["type"] == expected_type


def test_empty_tasks_allowed_by_model():
    req = OperationsRequest(text="foo", tasks=[])
    assert req.tasks == []
