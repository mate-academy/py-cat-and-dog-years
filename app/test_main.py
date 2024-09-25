import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    pytest.param(0, 0, [0, 0], id="Test with zero ages"),
    pytest.param(15, 15, [1, 1], id="Test the boundary of the first segment"),
    pytest.param(23, 23, [1, 1], id="Test just before the second segment"),
    pytest.param(24, 24, [2, 2], id="Test the boundary of the second segment"),
    pytest.param(27, 28, [2, 2], id="Test just before the third segment"),
    pytest.param(28, 28, [3, 2],
                 id="Test at the third segment "
                 "start for cat and just before for dog"),
    pytest.param(30, 29, [3, 3], id="Test the third segment"),
    pytest.param(35, 34, [4, 4],
                 id="Test another step within the third segment"),
    pytest.param(100, 100, [21, 17], id="Test with high ages")
])
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
