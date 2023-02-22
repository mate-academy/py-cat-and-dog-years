import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(0, 14, [0, 0], id="animals' age is less then 15"),
        pytest.param(
            15, 23, [1, 1], id="animals' age more then 15 less then 24"
        ),
        pytest.param(28, 23, [3, 1], id="cat's age is more then 24"),
        pytest.param(15, 29, [1, 3], id="dog's age is more then 24"),
    ],
)
def test_function_return_expected_values(
    cat_age: int, dog_age: int, result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result
