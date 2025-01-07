import pytest
from app.main import get_human_age

@pytest.mark.parametrize("cat_age, expected_human_age", [
    (0, 0),
    (14, 0),
    (15, 1),
    (23, 1),
    (24, 2),
    (27, 2),
    (28, 3),
    (100, 21)
])
def test_get_human_age(cat_age, expected_human_age):
    result = get_human_age(cat_age, 0)  # Только для кошек, собачий возраст не используется в этих тестах
    assert result[0] == expected_human_age
