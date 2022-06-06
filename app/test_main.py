import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "animal_age, excpected_cat_age, excpected_dog_age",
    [
        pytest.param(10, 0, 0, id="should equal zero"),
        pytest.param(15, 1, 1, id="should equal one"),
        pytest.param(24, 2, 2, id="should equal two"),
        pytest.param(28, 3, 2, id="should equal two"),
        pytest.param(100, 21, 17, id="should equal two"),
    ]
)
def test_get_human_age(animal_age, excpected_cat_age, excpected_dog_age):
    human_age = get_human_age(animal_age, animal_age)
    assert human_age == [excpected_cat_age, excpected_dog_age]
