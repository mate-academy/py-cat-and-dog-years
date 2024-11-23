from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "init_cat_age,init_dog_age,expected_result",
    [
        pytest.param(24, 24, [2, 2], id="24/24 cat/dog age"),
        pytest.param(14, 14, [0, 0], id="14/14 cat/dog age"),
        pytest.param(15, 15, [1, 1], id="15/15 cat/dog age"),
        pytest.param(23, 23, [1, 1], id="23/23 cat/dog age"),
        pytest.param(27, 28, [2, 2], id="27/28 cat/dog age"),
        pytest.param(28, 29, [3, 3], id="28/29 cat/dog age"),
    ]
)
def test_get_human_age(init_cat_age: int,
                       init_dog_age: int,
                       expected_result: list) -> None:
    cat_age = init_cat_age
    dog_age = init_dog_age
    result = get_human_age(cat_age=cat_age, dog_age=dog_age)
    assert result == expected_result
