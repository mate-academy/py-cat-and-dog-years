import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,cat_human,dog_human",
    [
        pytest.param(14, 14, 0, 0, id="the animal is zero year old"),
        pytest.param(23, 15, 1, 1, id="the animal is one year old"),
        pytest.param(24, 27, 2, 2, id="the animal is two year old"),
        pytest.param(28, 29, 3, 3, id="test_each_subsequent_year")
    ]
)
def test_the_animal_old(cat_age: int,
                        dog_age: int,
                        cat_human: int,
                        dog_human: int
                        ) -> None:
    assert get_human_age(cat_age, dog_age) == [cat_human, dog_human]


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        pytest.param(-14, -14, id="negative age"),
        pytest.param(100, 90, id="age exceeded"),
        pytest.param("20", "27", id="invalid age"),
    ]
)
def test_check_value_correctness(cat_age: int,
                                 dog_age: int,
                                 ) -> None:

    if not isinstance(cat_age, int) or not isinstance(dog_age, int):
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

    elif get_human_age(cat_age, dog_age) < [-14, -14]:
        with pytest.raises(ValueError):
            get_human_age(cat_age, dog_age)

    elif cat_age > 100 or dog_age > 90:
        with pytest.raises(ValueError):
            get_human_age(cat_age, dog_age)
