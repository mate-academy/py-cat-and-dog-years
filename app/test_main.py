import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        pytest.param(-1, -1, [0, 0],
                     id="negative ages should result in 0 human years"),
        pytest.param(0, 0, [0, 0],
                     id="zero ages should result in 0 human years"),
        pytest.param(14, 14, [0, 0],
                     id="ages just below the threshold should "
                        "result in 0 human years"),
        pytest.param(15, 15, [1, 1],
                     id="ages at the first threshold should "
                        "result in 1 human year"),
        pytest.param(23, 23, [1, 1],
                     id="ages in the second year span should "
                        "still result in 1 human year"),
        pytest.param(27, 27, [2, 2],
                     id="ages at the second threshold should "
                        "result in 2 human years"),
        pytest.param(100, 100, [21, 17],
                     id="higher ages should calculate correctly"),
    ]
)
def test_can_get_proper_human_age(
        cat_age: int,
        dog_age: int,
        human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_ages_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("1", "1")
