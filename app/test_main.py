import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        (-7, -1, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 29, [3, 3]),
    ],
    ids=[
        "Should return 0 if age is negative",
        "Should return 0 for both value if both animal age is 0",
        "Should return 0 for both value if both animal age is 14",
        "Should return 1 for both value if both animal age is 15",
        "Should return 1 for both value if both animal age is 23",
        "Should return 2 for both value if both animal age is 24",
        "Should return 2 for both value if both animal age is 27",
        "Should return 3 for both value if cat age is 28 and dog age is 29",
    ]
)
def test_list_elements_should_be_in_order_and_calculation_correctly(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    cat_to_human, dog_to_human = result
    assert (
        get_human_age(cat_age, dog_age) == [cat_to_human, dog_to_human]
    ), "List elements should be in order and calculation should be correct"
