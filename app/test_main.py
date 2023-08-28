import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_human_age",
    [
        pytest.param(0, 0, [0, 0], id="Zero age should return 0"),
        pytest.param(14, 14, [0, 0], id="Age before 15 should return 0"),
        pytest.param(
            15, 15, [1, 1], id="Age between 15 and 23 should return 1"
        ),
        pytest.param(
            23, 23, [1, 1], id="Age between 15 and 23 should return 1"
        ),
        pytest.param(
            27, 28, [2, 2], id="Dog and cat have different boundaries(27,28)"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="Test the first time age is calculated on the third year",
        ),
        pytest.param(
            100, 100, [21, 17], id="Test if big age is calculated correctly"
        ),
        pytest.param(-5, -5, [0, 0], id="Negative data should return 0"),
    ],
)
def test_get_human_age(
    cat_age: int, dog_age: int, expected_human_age: list[int]
) -> None:
    goals = get_human_age(cat_age, dog_age)
    assert goals == expected_human_age


def test_type_error_if_string_is_given() -> None:
    with pytest.raises(TypeError):
        get_human_age("18", "four")


def test_type_error_if_not_enough_values() -> None:
    with pytest.raises(TypeError):
        get_human_age(1)
