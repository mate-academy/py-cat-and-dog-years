import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(0, 0, [0, 0], id="zero"),
        pytest.param(-5, -2, [0, 0], id="negative scenarios"),
        pytest.param(14, 14, [0, 0], id="before first human year"),
        pytest.param(15, 15, [1, 1], id="first human year"),
        pytest.param(23, 23, [1, 1], id="before second human year"),
        pytest.param(24, 24, [2, 2], id="after second human year"),
        pytest.param(27, 27, [2, 2], id="before third human year for cats"),
        pytest.param(28, 28, [3, 2],
                     id="third human year for cats, but not for dogs"),
        pytest.param(100, 100, [21, 17],
                     id="third human year for cats, but not for dogs"),
        pytest.param(100, 50, [21, 7], id="different_ages")
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == result
