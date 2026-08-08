import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        pytest.param(
            0, 0, [0, 0],
            id="return zeros when age are zero"),
        pytest.param(
            14, 14, [0, 0],
            id="test 14 years returns 0 human years"),
        pytest.param(
            15, 15, [1, 1],
            id="test 15 years returns 1 human year"),
        pytest.param(
            23, 23, [1, 1],
            id="test 23 years returns 1 human year"),
        pytest.param(
            24, 24, [2, 2],
            id="test 24 years returns 2 human years"),
        pytest.param(
            27, 27, [2, 2],
            id="test 27 years returns 2 human years"),
        pytest.param(
            28, 29, [3, 3],
            id="test 28 and 29 years returns 3 human years"),
        pytest.param(
            100, 100, [21, 17],
            id="test max age edge case"),
    ]
)
def test_human_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_exception",
    [
        pytest.param(
            -1, 10, ValueError,
            id="test negative cat age raises ValueError"),
        pytest.param(
            10, -1, ValueError,
            id="test negative dog age raises ValueError"),
        pytest.param(
            101, 10, ValueError,
            id="test cat age greater than 100 raises ValueError"),
        pytest.param(
            10, 101, ValueError,
            id="test dog age greater than 100 raises ValueError"),
        pytest.param(
            "ten", 10, TypeError,
            id="test non-integer cat age raises TypeError"),
        pytest.param(
            10, "ten", TypeError,
            id="test non-integer dog age raises TypeError"),
    ]
)
def test_human_age_exceptions(
    cat_age: int,
    dog_age: int,
    expected_exception: Exception
) -> None:

    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
