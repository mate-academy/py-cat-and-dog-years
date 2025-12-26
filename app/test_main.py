import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(0, 0, [0, 0],
                     id="zero ages for pets the same for human"),
        pytest.param(14, 14, [0, 0],
                     id="not enough human age for 1 year pets"),
        pytest.param(15, 15, [1, 1],
                     id="first 15 pets years give 1 human year"),
        pytest.param(23, 23, [1, 1],
                     id="not enough human age for 2 year pets"),
        pytest.param(24, 24, [2, 2],
                     id="the next 9 pets years give 1 more human year"),
        pytest.param(27, 27, [2, 2],
                     id="pets years give 2 human years"),
        pytest.param(28, 28, [3, 2],
                     id="years for cat equal 3 human age, for dog is 2"),
        pytest.param(100, 100, [21, 17],
                     id="for higher ages should calculated correctly")
    ]
)
def test_verify_pets_age_in_human(cat_age: int,
                                  dog_age: int,
                                  human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_age_pets_if_not_integer() -> None:
    with pytest.raises(TypeError):
        get_human_age("1", "1")
