import pytest
from pydantic import ValidationError

from app.v1.models.operations_response import OperationsResponse
from app.v1.models.ayah_match import AyahMatch


def test_default_response():
    resp = OperationsResponse()
    assert resp.annotated_text is None
    assert resp.matches is None


def test_valid_annotated_text_only():
    resp = OperationsResponse(annotated_text="some annotated text")
    assert resp.annotated_text == "some annotated text"
    assert resp.matches is None


def test_valid_matches_only(ayah_match_dict):
    resp = OperationsResponse(matches=[ayah_match_dict])
    assert resp.annotated_text is None
    assert isinstance(resp.matches, list)
    assert isinstance(resp.matches[0], AyahMatch)
    assert resp.matches[0].surah_name == ayah_match_dict["surah_name"]
    assert resp.matches[0].start_index == ayah_match_dict["start_index"]


def test_valid_full_response(ayah_match_dict):
    resp = OperationsResponse(
        annotated_text="text here",
        matches=[ayah_match_dict],
    )
    assert resp.annotated_text == "text here"
    assert len(resp.matches) == 1


@pytest.mark.parametrize("bad_annot", [123, True, [], {}])
def test_invalid_annotated_text_type(bad_annot):
    with pytest.raises(ValidationError):
        OperationsResponse(annotated_text=bad_annot)


def test_invalid_matches_not_a_list():
    with pytest.raises(ValidationError):
        OperationsResponse(matches="not a list")
