import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(0, 0, [0, 0], id="cats amd dogs age is 0"),
        pytest.param(14, 14, [0, 0], id="cats amd dogs age less than 15"),
        pytest.param(27, 27, [2, 2], id="cats amd dogs age is 27"),
        pytest.param(100, 100, [21, 17], id="cats amd dogs age is 100"),
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), f"Result should be equal to {result}"
