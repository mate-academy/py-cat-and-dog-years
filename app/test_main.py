import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(0, 0, [0, 0], id="animals' age is 0"),
        pytest.param(0, 14, [0, 0], id="cat's age is less than 15"),
        pytest.param(14, 0, [0, 0], id="dog's age is less than 15"),
        pytest.param(15, 0, [1, 0], id="dog's age is 15"),
        pytest.param(0, 15, [0, 1], id="cat's age is 15"),
        pytest.param(
            16, 0, [1, 0], id="cat's age is more than 15 less than 24"
        ),
        pytest.param(
            0, 23, [0, 1], id="dog's age is more than 15 less than 24"
        ),
        pytest.param(24, 23, [2, 1], id="cat's age is 24"),
        pytest.param(15, 24, [1, 2], id="dog's age is 24"),
        pytest.param(28, 23, [3, 1], id="cat's age is more than 24"),
        pytest.param(15, 29, [1, 3], id="dog's age is more than 24"),
    ],
)
def test_function_return_expected_values(
        cat_age: int, dog_age: int, result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_cannot_pass_other_types_to_function() -> None:
    with pytest.raises(TypeError):
        get_human_age("12", "_")
    with pytest.raises(TypeError):
        get_human_age(["12"], ["_"])
    with pytest.raises(TypeError):
        get_human_age({"12"}, {"_"})
