import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_result",
    [
        pytest.param(
            -1,
            -1,
            [0, 0],
            id="should return 0 for negative dog/cat age",
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id=("14 dog/cat years should convert to 0 human years"),
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="15 dog/cat years should convert to 1 human year",
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="23 dog/cat years should convert to 1 human year",
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="24 dog/cat years should convert to 2 human years",
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id=(
                "should correctly convert dog/cat age after "
                "the equivalence of the first two human years"
            ),
        ),
    ],
)
def test_get_human_age(
    cat_age: int, dog_age: int, expected_result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result
