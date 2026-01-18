import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age,  result",
    [
        pytest.param(0, 0, [0, 0], id="example 1, less then first check"),
        pytest.param(-2, -3, [0, 0], id="example 0, less then zero check"),
        pytest.param(14, 14, [0, 0], id="example 2, less then first check"),
        pytest.param(15, 15, [1, 1], id="example 3, equal first check"),
        pytest.param(23, 23, [1, 1],
                     id="example 4, equal first check under second"),
        pytest.param(24, 24, [2, 2], id="example 5, equal second check"),
        pytest.param(27, 28, [2, 2],
                     id="example 6, equal second check under third"),
        pytest.param(28, 29, [3, 3], id="example 7, equal third check"),
        pytest.param(100, 100, [21, 17],
                     id="example 8, critical big value check"),
    ]
)
def test_should_return_list_with_human_age(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result
