import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    ("cat_age", "dog_age", "expected"),
    [
        pytest.param(0, 0, [0, 0], id="zero ages"),
        pytest.param(14, 14, [0, 0], id="before first year"),
        pytest.param(15, 15, [1, 1], id="first human year"),
        pytest.param(23, 23, [1, 1], id="before second year"),
        pytest.param(24, 24, [2, 2], id="second human year"),
        pytest.param(-1, -1, [0, 0], id="negative ages"),
        pytest.param(25, 25, [2, 2], id="same result at age 25"),
        pytest.param(26, 26, [2, 2], id="same result at age 26"),
        pytest.param(27, 27, [2, 2], id="incomplete extra period"),
        pytest.param(28, 28, [3, 2], id="cat third year"),
        pytest.param(28, 29, [3, 3], id="dog third year"),
        pytest.param(15, 14, [1, 0], id="different ages"),
        pytest.param(100, 100, [21, 17], id="large ages"),
    ],
)
def test_get_human_age(
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    assert get_human_age(cat_age=cat_age, dog_age=dog_age) == expected


@pytest.mark.parametrize(
    ("cat_age", "dog_age"),
    [
        pytest.param("15", 15, id="cat age is string"),
        pytest.param(15, "15", id="dog age is string"),
        pytest.param(15.5, 15, id="cat age is float"),
        pytest.param(15, 15.5, id="dog age is float"),
    ],
)
def test_get_human_age_raises_type_error(
    cat_age: object,
    dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age=cat_age, dog_age=dog_age)
