import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [

        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (150, 38, [33, 4]),
        (-5, -10, [0, 0]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 29, [3, 3]),
    ],
    ids=[
        "small_age_output_0",
        "middle_age_output_1",
        "huge_age_right_result",
        "negative_age_output_0",
        "first_border_age_output_1",
        "second_border_age_output_2",
        "third_under_border_age_output_2",
        "third_border_age_output_3",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected, (
        f"Function 'get_human_age' should return {expected} "
        f"when cat age is {cat_age} and dog age is {dog_age}"
    )
