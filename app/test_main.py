import pytest

from app import main


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(-1, -1, [0, 0], id="negative age"),
        pytest.param(0, 0, [0, 0], id="zero age"),
        pytest.param(14, 14, [0, 0], id="less than fifteen"),
        pytest.param(15, 15, [1, 1], id="first human year"),
        pytest.param(23, 23, [1, 1], id="before second human year"),
        pytest.param(24, 24, [2, 2], id="second human year"),
        pytest.param(27, 27, [2, 2], id="before additional years"),
        pytest.param(28, 28, [3, 2], id="cat gets third human year"),
        pytest.param(28, 29, [3, 3], id="dog gets third human year"),
        pytest.param(100, 100, [21, 17], id="large age"),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param("0", 0, id="string"),
        pytest.param(0, {0: 1}, id="dictionary"),
        pytest.param([0], 0, id="list"),
        pytest.param(0, (0,), id="tuple"),
        pytest.param({0}, 0, id="set"),
        pytest.param(0, None, id="none"),
    ],
)
def test_should_raise_error_when_age_is_not_integer(
    cat_age: object,
    dog_age: object,
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
