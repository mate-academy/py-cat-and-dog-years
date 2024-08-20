from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (23, 23, [1, 1]),
        (15, 15, [1, 1]),
        (14, 14, [0, 0]),
        (0, 0, [0, 0]),
        (15, 24, [1, 2]),
        (28, 36, [3, 4]),
        (48, 56, [8, 8]),
        (64, 72, [12, 11]),
        (100, 100, [21, 17])
    ])
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


def test_type_errors() -> None:
    with pytest.raises(TypeError):
        assert get_human_age("cat_age", "dog_age")
