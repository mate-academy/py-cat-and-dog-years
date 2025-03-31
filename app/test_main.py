import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "dog_age,cat_age,expected_result",
    [
        (
            14, 14,
            [0, 0]
        ),
        (
            23, 23,
            [1, 1]
        ),
        (
            28, 28,
            [3, 2]
        ),
        (
            100, 100,
            [21, 17]
        )
        ]
)
def test_convert_age_correctly(
        dog_age: int,
        cat_age: int,
        expected_result: list[int]
):
    assert get_human_age(dog_age, cat_age) == expected_result


@pytest.mark.parametrize(
    "dog_age,cat_age,expected_error",
    [
        pytest.param(
            "dog",
            ["cat"],
            TypeError
        ),
        pytest.param(
            {"dog"},
            ("cat"),
            TypeError
        )
    ]
)
def test_should_raise_type_error_when_wrong_argument(
        dog_age, cat_age, expected_error) -> None:
    with pytest.raises(expected_error):
        get_human_age(dog_age, cat_age)
