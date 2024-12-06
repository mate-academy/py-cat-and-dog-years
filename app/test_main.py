import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(0, 0, [0, 0],
                     id="human age should be 0 when cat or dog age = 0"),
        pytest.param(14, 14, [0, 0],
                     id="human age should be 0 when cat or dog age < 15"),
        pytest.param(23, 15, [1, 1],
                     id="human age should be 1 "
                        "when 15 <= cat or dog age < 24"),
        pytest.param(24, 27, [2, 2],
                     id="human age should be 2 "
                        "when 24 <= cat age < 28 or 24 <= dog age <= 28"),
        pytest.param(28, 28, [3, 2],
                     id="human age should be greater than 2 "
                        "when cat age >= 28 or dog age > 28"),
        pytest.param(100, 100, [21, 17],
                     id="human age should increase by 1 "
                        "every 4 cat's years when cat age >= 28 "
                        "and every 5 dog's years when dog age >= 29")
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param("0", 0, id="cat or dog age is str"),
        pytest.param(0, {0: 1}, id="cat or dog age is dict"),
        pytest.param([0], 0, id="cat or dog age is list"),
        pytest.param(0, (0,), id="cat or dog age is tuple"),
        pytest.param({0}, 0, id="cat or dog age is set"),
        pytest.param(True, 0, id="cat or dog age is bool"),
        pytest.param(0, None, id="cat or dog age is None")
    ]
)
def test_should_raise_error_when_cat_or_dog_age_is_not_number(
        cat_age: int,
        dog_age: int
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
