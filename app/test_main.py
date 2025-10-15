from __future__ import annotations

from typing import Any

import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    ("cat_age", "dog_age", "expected"),
    [
        (0, 0, [0, 0]),
        (23, 23, [1, 1]),
        (100, 100, [21, 17]),
    ],
)
def test_examples(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    ("cat_age", "expected_cat"),
    [
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 3),
    ],
)
def test_cat_boundaries(cat_age: int, expected_cat: int) -> None:
    cat_human, dog_human = get_human_age(cat_age, 0)
    assert dog_human == 0
    assert cat_human == expected_cat


@pytest.mark.parametrize(
    ("dog_age", "expected_dog"),
    [
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (28, 2),
        (29, 3),
        (30, 3),
    ],
)
def test_dog_boundaries(dog_age: int, expected_dog: int) -> None:
    cat_human, dog_human = get_human_age(0, dog_age)
    assert cat_human == 0
    assert dog_human == expected_dog


@pytest.mark.parametrize(("cat_age", "dog_age"),
                         [(0, 0), (10, 7), (15, 15), (40, 33)])
def test_result_shape_and_types(cat_age: int, dog_age: int) -> None:
    res = get_human_age(cat_age, dog_age)
    assert isinstance(res, list)
    assert len(res) == 2
    assert all(isinstance(x, int) for x in res)


def test_monotonicity() -> None:
    for aa in range(0, 60):
        c_prev, d_prev = get_human_age(aa, 0)
        c_next, d_same = get_human_age(aa + 1, 0)
        assert d_same == 0
        assert c_next >= c_prev

        c_same, d_prev = get_human_age(0, aa)
        c_same2, d_next = get_human_age(0, aa + 1)
        assert c_same == c_same2 == 0
        assert d_next >= d_prev


@pytest.mark.parametrize(
    ("cat_age", "dog_age"),
    [
        ("1", 0),
        (0, "2"),
        (1, None),
    ],
)
def test_invalid_types_raise(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(("cat_age", "dog_age"), [(1.5, 2.0), (10.0, 7.2)])
def test_floats_return_ints(cat_age: float, dog_age: float) -> None:
    res = get_human_age(cat_age, dog_age)
    assert isinstance(res, list)
    assert len(res) == 2
    assert all(isinstance(x, int) for x in res)


@pytest.mark.parametrize(("cat_age", "dog_age"),
                         [(-1, -5), (-100, 0), (0, -100)])
def test_negatives_not_below_zero(cat_age: int, dog_age: int) -> None:
    res = get_human_age(cat_age, dog_age)
    assert res[0] >= 0 and res[1] >= 0
