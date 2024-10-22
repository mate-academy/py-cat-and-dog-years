import pytest


from app.main import get_human_age
@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(
            14,
            14,
            [0, 0],
            id="test should return zero before 15 animals years"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="test should return human year after 24 animal years"
        ),
        pytest.param(
            36,
            28,
            [5, 2],
            id="test should return human years if cat years equals 36"
        ),
        pytest.param(
            36,
            44,
            [5, 6],
            id="test should return human years if dog years equals 44"
        )
    ]
)
def test_func_should_return_correctly_result(
        cat_age,
        dog_age,
        result):
    assert get_human_age(cat_age, dog_age) == result
