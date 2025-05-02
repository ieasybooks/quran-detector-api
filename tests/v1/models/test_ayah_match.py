import pytest
from pydantic import ValidationError

from app.v1.models.ayah_match import AyahMatch
from app.v1.models.correction import Correction


def test_valid_ayah_match(ayah_match_dict):
    match = AyahMatch(**ayah_match_dict)
    assert match.surah_name == ayah_match_dict["surah_name"]
    assert match.surah_number == ayah_match_dict["surah_number"]
    assert match.ayah_start == ayah_match_dict["ayah_start"]
    assert match.ayah_end == ayah_match_dict["ayah_end"]
    assert match.ayah_text == ayah_match_dict["ayah_text"]
    assert isinstance(match.corrections, list)
    assert isinstance(match.corrections[0], Correction)
    assert match.start_index == ayah_match_dict["start_index"]
    assert match.end_index == ayah_match_dict["end_index"]


@pytest.mark.parametrize("missing_field", [
    "surah_name", "surah_number", "ayah_start", "ayah_end",
    "ayah_text", "corrections", "start_index", "end_index"
])
def test_missing_required_fields(missing_field, ayah_match_dict):
    ayah_match_dict.pop(missing_field)
    with pytest.raises(ValidationError) as exc:
        AyahMatch(**ayah_match_dict)
    errors = exc.value.errors()
    assert errors[0]["loc"] == (missing_field,)
    assert errors[0]["type"] == "missing"
