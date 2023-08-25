import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    (
        pytest.param(0, 0, [0, 0], id="animal ages are zeros"),
        pytest.param(
            13, 6, [0, 0], id="any num lower than 15 should return 0"
        ),
        pytest.param(
            15, 15, [1, 1], id="check for 15 dog/cat ages is 1 for human"
        ),
        pytest.param(
            24, 24, [2, 2], id="check that next 9 years calculated correctly"
        ),
        pytest.param(23, 23, [1, 1], id="23 is still 1 human year"),
        pytest.param(
            29, 30, [3, 3], id="check that next 4/5 years calculated correctly"
        ),
        pytest.param(
            100, 100, [21, 17], id="correct calculating for big ages"
        ),
    ),
)
def test_correct_work_of_get_human_age(
    cat_age: int, dog_age: int, result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "unnormal_value",
    (
        pytest.param("15", id="for str"),
        pytest.param({24}, id="for set"),
        pytest.param({15: 15}, id="for dict"),
    ),
)
def test_correct_exceptions_for_get_human_age(
    unnormal_value: str | dict | set,
) -> None:
    with pytest.raises(TypeError):
        assert get_human_age(unnormal_value, unnormal_value) == TypeError
