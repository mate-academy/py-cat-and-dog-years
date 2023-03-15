import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(0, 0, [0, 0],
                     id="when given 0 cat/dog age"),
        pytest.param(-15, -15, [0, 0],
                     id="when given negative cat/dog age"),
        pytest.param(14, 14, [0, 0],
                     id="check first human year with cat/dog"),
        pytest.param(15, 15, [1, 1],
                     id="check second human year with cat/dog"),
        pytest.param(27, 28, [2, 2],
                     id="check third human year with cat/dog"),
        pytest.param(31, 33, [3, 3],
                     id="check fourth human year with cat/dog"),
        pytest.param(35, 38, [4, 4],
                     id="check fifth human year with cat/dog"),


    ]
)
def test_checking_the_correct_result(
        cat_age: int,
        dog_age: int,
        expected: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected
