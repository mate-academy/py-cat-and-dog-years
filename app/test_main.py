from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_output",
    [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (29, 35, [3, 4]),
    ],
    ids=[
        "check negative values",
        "check zero values",
        "check correct dividing conversion format",
        "check correct 15 to 1 human year conversion",
        "check correct 23 to 1 human years conversion",
        "check correct 24 to 2 human years conversion",
        "check correct 3+ human years conversion"
    ]
)
def test_correct_dog_and_cat_to_human_age_convertion(
        cat_age: int,
        dog_age: int,
        expected_output: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_output


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(
            "12",
            "27",
            TypeError,
            id="check if TypeError is raised if ages are not integers"
        ),
    ]
)
def test_raising_type_error_correctly(
        cat_age: str,
        dog_age: str,
        expected_error: type[Exception]
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
