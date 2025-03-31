import pytest

from app.main import get_human_age


def test_should_return_list() -> None:
    goals = get_human_age(5, 5)
    assert isinstance(goals, list)


def test_should_return_list_of_given_length() -> None:
    goals = get_human_age(5, 5)
    assert len(goals) == 2


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(-12, -100, [0, 0],
                     id="Negative values should return zeros"),
        pytest.param(0, 0, [0, 0],
                     id="Zero values should return zeros"),
        pytest.param(14, 14, [0, 0],
                     id="Value of ages are less than 15"),
        pytest.param(15, 15, [1, 1],
                     id="15 should return 1 year per value"),
        pytest.param(24, 24, [2, 2],
                     id="24 should return 2 year per value"),
        pytest.param(28, 28, [3, 2],
                     id="28 should return 3 for cat and 2 for dog"),
        pytest.param(100, 100, [21, 17],
                     id="100 should return 21 for cat and 17 for dog"),
    ]
)
def test_should_return_expected_goals(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), f"Transformation {cat_age} and {dog_age} should be equal to {result}"


@pytest.mark.parametrize(
    "cat_age,dog_age,error",
    [
        ("100", 100, TypeError)
    ],
    ids=["all parameters should be int"]
)
def test_get_human_age(cat_age: int, dog_age: int, error: TypeError) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
