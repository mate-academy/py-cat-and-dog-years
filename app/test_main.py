import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param(-14, -14, id="negative age"),
        pytest.param(100, 90, id="age exceeded"),
    ]
)
def test_the_animal_old(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param(-14, -14, id="negative age"),
        pytest.param(100, 90, id="age exceeded"),
        pytest.param("20", "27", id="invalid age"),
    ]
)
def test_check_value_correctness(cat_age: int, dog_age: int) -> None:

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

    elif cat_age < 0 or dog_age < 0:
        with pytest.raises(ValueError):
            get_human_age(cat_age, dog_age)

    elif cat_age > 100 or dog_age > 90:
        with pytest.raises(ValueError):
            get_human_age(cat_age, dog_age)
