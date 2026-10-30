import pytest

from app import main


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(-1, -1, [0, 0], id="negative ages give 0"),
        pytest.param(0, 0, [0, 0], id="zero ages give zero human years"),
        pytest.param(14, 14, [0, 0], id="less than 15 years gives 0"),
        pytest.param(15, 15, [1, 1], id="first 15 years give 1 human year"),
        pytest.param(23, 23, [1, 1], id="23 years is still 1 human year"),
        pytest.param(24, 24, [2, 2], id="next 9 years give 1 more year"),
        pytest.param(27, 27, [2, 2], id="remainder is discarded"),
        pytest.param(28, 28, [3, 2], id="every 4 cat years give 1 year"),
        pytest.param(29, 29, [3, 3], id="every 5 dog years give 1 year"),
        pytest.param(100, 100, [21, 17], id="big ages convert correctly"),
        pytest.param(1000, 1000, [246, 197], id="very large ages"),
    ],
)
def test_converts_animal_years_to_human_years(
        cat_age: int,
        dog_age: int,
        expected: list[int],
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


def test_cat_and_dog_ages_are_independent() -> None:
    assert main.get_human_age(28, 0) == [3, 0]
    assert main.get_human_age(0, 29) == [0, 3]


def test_returns_list() -> None:
    assert isinstance(main.get_human_age(15, 15), list)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param("15", 15, id="cat age as string"),
        pytest.param(15, "15", id="dog age as string"),
        pytest.param(None, 15, id="cat age as None"),
        pytest.param(15, [15], id="dog age as list"),
    ],
)
def test_raises_type_error_for_invalid_types(
        cat_age: object,
        dog_age: object,
) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(cat_age, dog_age)
