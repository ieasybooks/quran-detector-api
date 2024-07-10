import pytest
from pydantic import ValidationError

from app.v1.models.correction import Correction


def test_valid_correction():
    corr = Correction(
        ayah_index=1,
        original="أَلِف",
        corrected="أَلِفْ",
        position=5
    )
    assert corr.ayah_index == 1
    assert corr.original == "أَلِف"
    assert corr.corrected == "أَلِفْ"
    assert corr.position == 5


@pytest.mark.parametrize("missing_field", [
    "ayah_index", "original", "corrected", "position"
])
def test_missing_required_fields(missing_field):
    data = {
        "ayah_index": 1,
        "original": "orig",
        "corrected": "corr",
        "position": 0
    }
    data.pop(missing_field)
    with pytest.raises(ValidationError) as exc:
        Correction(**data)
    errors = exc.value.errors()
    assert errors[0]["loc"] == (missing_field,)
    assert errors[0]["type"] == "missing"
