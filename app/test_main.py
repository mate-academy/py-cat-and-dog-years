import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_age_in_human",
    [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3])
    ],
    ids=[
        "14 cat/dog years should convert into 0 human age.",
        "15 cat/dog years should convert into 1 human age.",
        "23 cat/dog years should convert into 1 human age.",
        "24 cat/dog years should convert into 2 human age.",
        "27/28 cat/dog years should convert into 2 human age.",
        "28/29 cat/dog years should convert into 3 human age."
    ]
)
def test_returning_correct_values(
    cat_age: int,
    dog_age: int,
    expected_age_in_human: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_age_in_human


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        (0, 0, [0, 0]),
        (-1, -1, [0, 0])
    ],
    ids=[
        "0 cat/dog years should return 0 in human age",
        "negative cat/dog years should return 0 in human age"
    ]
)
def test_behaviour_when_data_out_of_normal_range(
    cat_age: int,
    dog_age: int,
    expected_result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_error",
    [
        (
            "11",
            11,
            TypeError
        )
    ],
    ids=[
        "should raise error when incorrect input data type "
    ]
)
def test_raising_correct_error(
    cat_age: str,
    dog_age: int,
    expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
