import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, human_age",
    [
        pytest.param(-1, -1, [0, 0],
                     id="negative cat and dog years give 0 human year"),
        pytest.param(0, 0, [0, 0],
                     id="zero cat and dog years give 0 human year"),
        pytest.param(14, 14, [0, 0],
                     id="under first 15 cat and dog years give 0 human year"),
        pytest.param(15, 15, [1, 1],
                     id="first 15 cat and dog years give 1 human year"),
        pytest.param(23, 23, [1, 1],
                     id="first 15 cat and dog years give 1 human year"),
        pytest.param(24, 24, [2, 2],
                     id="next 9 cat and dog years give 1 more human year;"),
        pytest.param(28, 29, [3, 3],
                     id="every 4 cat and 5 dog years give 1 extra human year"),
        pytest.param(10000, 10000, [2496, 1997],
                     id="should work with really large numbers"),
    ]
)
def test_can_get_proper_human_age(cat_age: int,
                                  dog_age: int,
                                  human_age: list
                                  ) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


def test_ages_type_error() -> None:
    with pytest.raises(TypeError):
        get_human_age("28", "29")
