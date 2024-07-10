import pytest


@pytest.fixture
def correction_dict():
    return {
        "ayah_index": 0,
        "original": "رب العالمن",
        "corrected": "رب العالمين",
        "position": 10
    }


@pytest.fixture
def ayah_match_dict(correction_dict):
    return {
        "surah_name": "الفاتحة",
        "surah_number": 1,
        "ayah_start": 2,
        "ayah_end": 2,
        "ayah_text": ["الحمد لله رب العالمين"],
        "corrections": [correction_dict],
        "start_index": 19,
        "end_index": 46
    }
