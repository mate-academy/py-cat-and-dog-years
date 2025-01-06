import pytest
from app.main import get_human_age

@pytest.mark.parametrize(
    "animal_type, animal_age, expected_result",
    [
        ("cat", 0, 0),
        ("dog", 0, 0),
        ("cat", 14, 0),
        ("dog", 14, 0),
        ("cat", 15, 1),
        ("dog", 15, 1),
        ("cat", 24, 1),
        ("dog", 24, 1),
        ("cat", 28, 2),
        ("dog", 28, 2),
        ("cat", 100, 21),
        ("dog", 100, 17),
    ]
)
def test_get_human_age(animal_type, animal_age, expected_result):
    result = get_human_age(animal_type, animal_age)
    assert result == expected_result
