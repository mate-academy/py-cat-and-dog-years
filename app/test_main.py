import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="test when zero years"),
        pytest.param(
            14,
            14,
            [0, 0],
            id="test when age less then minimal"),
        pytest.param(
            15,
            15,
            [1, 1],
            id="test when age equal first human age"),
        pytest.param(
            23,
            23,
            [1, 1],
            id="test when age before second human age"),
        pytest.param(
            24,
            24,
            [2, 2],
            id="test when age equal second human age"),
        pytest.param(
            27,
            27,
            [2, 2],
            id="test when one age before third human age"),
        pytest.param(
            28,
            28,
            [3, 2],
            id="test when one age equal to third human age"),
        pytest.param(
            100,
            100,
            [21, 17],
            id="test higher age case ")
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
