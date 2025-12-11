import math
import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "a,b,result",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_examples(a: int, b: int, result: list[int]) -> None:
    out = get_human_age(a, b)
    assert isinstance(out, list), "Return type must be list"
    assert len(out) == 2, "Return list must have exactly two elements"
    assert all(isinstance(x, int) for x in out), "Both elements must be ints"
    assert out == result, f"Human ages {a} and {b} should be {result}"


@pytest.mark.parametrize(
    "a,b,before,after",
    [
        (14, 14, [0, 0], [1, 1]),
        (23, 23, [1, 1], [2, 2]),
        (27, 27, [2, 2], [3, 2]),
    ],
)
def test_boundaries_change_only_at_thresholds(a, b, before, after):
    assert get_human_age(a, b) == before
    assert get_human_age(a + 1, b + 1) == after


@pytest.mark.parametrize(
    "x,expected_at_x,expected_at_x_plus_1",
    [
        (14, [0, 0], [1, 1]),
        (23, [1, 1], [2, 2]),
        (27, [2, 2], [3, 2]),
    ],
)
def test_each_arg_independently_at_boundaries(x, expected_at_x, expected_at_x_plus_1):
    out1 = get_human_age(x, 0)
    out2 = get_human_age(x + 1, 0)
    assert [out1[0], out1[1]] == [expected_at_x[0], 0]
    assert [out2[0], out2[1]] == [expected_at_x_plus_1[0], 0]

    out3 = get_human_age(0, x)
    out4 = get_human_age(0, x + 1)
    assert [out3[0], out3[1]] == [0, expected_at_x[1]]
    assert [out4[0], out4[1]] == [0, expected_at_x_plus_1[1]]


@pytest.mark.parametrize(
    "cat_years,dog_years,expected",
    [
        (28, 28, [3, 2]),
        (29, 28, [3, 2]),
        (32, 28, [4, 2]),
        (36, 28, [5, 2]),
        (28, 29, [3, 2]),
        (28, 33, [3, 3]),
        (28, 38, [3, 4]),
    ],
)
def test_progression_after_thresholds(cat_years, dog_years, expected):
    assert get_human_age(cat_years, dog_years) == expected


@pytest.mark.parametrize("a,b", [(-1, 0), (0, -1), (-5, -10)])
def test_negative_values_raise_value_error(a, b):
    with pytest.raises(ValueError):
        get_human_age(a, b)


@pytest.mark.parametrize(
    "a,b",
    [
        (14.0, 14),
        (14, 14.0),
        ("14", 14),
        (14, "14"),
        (None, 14),
        (14, None),
        (True, 14),
        (14, False),
    ],
)
def test_non_integer_inputs_raise_type_error(a, b):
    with pytest.raises(TypeError):
        get_human_age(a, b)


@pytest.mark.parametrize(
    "a,b",
    [
        (10**6, 10**6),
        (10**9, 10**9),
    ],
)
def test_very_large_values(a, b):
    out = get_human_age(a, b)
    assert isinstance(out, list) and len(out) == 2 and all(isinstance(x, int) for x in out)
    out_prev = get_human_age(a - 1, b - 1)
    assert out[0] >= out_prev[0]
    assert out[1] >= out_prev[1]
