import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(14, 14, [0, 0], id="zero human year"),
        pytest.param(15, 15, [1, 1], id="one human year"),
        pytest.param(24, 24, [2, 2], id="two human years"),
        pytest.param(28, 29, [3, 3], id="tree human years"),
        pytest.param(28, 28, [3, 2],
                     id="three human years for cat and two for dog"),
    ]
)
def test_convert_to_human_age(
        cat_age: int,
        dog_age: int,
        human_age: list | Exception
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,error",
    [
        pytest.param("16", 14, TypeError,
                     id="type of variable should be integer")
    ]
)
def test_receives_incorrect_type(
    cat_age: int,
    dog_age: int,
    error: Exception
) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
