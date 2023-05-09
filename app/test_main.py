import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_result",
    [
        pytest.param(14, 14, [0, 0],
                     id="Check when cat's and dog's "
                        "age less than one human year"),
        pytest.param(15, 15, [1, 1],
                     id="Check when cat's and dog's"
                        " age is equal to one human year"),
        pytest.param(24, 24, [2, 2],
                     id="Check when cat's and dog's"
                        " age is equal to two human years"),
        pytest.param(28, 28, [3, 2],
                     id="Check one extra human year for cat"),
        pytest.param(100, 100, [21, 17],
                     id="Check extra human years for all animals")

    ]
)
def test_check_animal_age_for_human(cat_age: int, dog_age: int,
                                    human_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == human_result
