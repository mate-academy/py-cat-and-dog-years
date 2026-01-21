import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(14, 14, [0, 0], id="1 human year"),
        pytest.param(24, 23, [2, 1], id="2 human year"),
        pytest.param(28, 29, [3, 3], id="3 human year"),

        pytest.param(28.3, 28, [3, 2], id="cat age is double"),
        pytest.param(28.3, 28, [3, 2], id="dog age is double"),

        pytest.param(1000, 1000, [246, 197], id="large ages"),

        pytest.param(-1000, 1000, [0, 197], id="negative age"),
        pytest.param(0, 0, [0, 0], id="zero age"),

    ]
)
def test_dog_and_cat_years_should_convert(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,error_type",
    [
        pytest.param("28", 29, TypeError, id="string and integer"),
        pytest.param(28, "29", TypeError, id="integer and string"),

        pytest.param(None, 28, TypeError, id="None and integer"),
        pytest.param(29, None, TypeError, id="integer and None"),

        pytest.param((1.5,), 28, TypeError, id="tuple and integer")
    ],
)
def test_cannot_add_str_and_int(
        cat_age: int,
        dog_age: int,
        error_type: Exception
) -> None:
    with pytest.raises(error_type):
        get_human_age(cat_age, dog_age)
