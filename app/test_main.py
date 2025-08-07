import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age,dog_age,human_age", [
    pytest.param(0, 0, [0, 0], id="animal_age_0"),
    pytest.param(14, 14, [0, 0], id="animal_age_14"),
    pytest.param(15, 15, [1, 1], id="animal_age_15"),
    pytest.param(23, 23, [1, 1], id="animal_age_23"),
    pytest.param(24, 24, [2, 2], id="animal_age_24"),
    pytest.param(27, 27, [2, 2], id="animal_age_27"),
    pytest.param(28, 28, [3, 2], id="animal_age_28"),
    pytest.param(100, 100, [21, 17], id="animal_age_100")
])
def test_animal_age(cat_age: int, dog_age: int, human_age: int) -> None:
    assert get_human_age(cat_age, dog_age) == human_age
