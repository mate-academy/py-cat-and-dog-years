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
