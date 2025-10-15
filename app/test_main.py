from __future__ import annotations

import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    ("cat_age", "dog_age", "expected"),
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
def test_examples(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    ("cat_age", "expected_cat"),
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (16, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 3),
    ],
)
def test_cat_boundaries(cat_age: int, expected_cat: int) -> None:
    cat_h, dog_h = get_human_age(cat_age, 0)
    assert dog_h == 0
    assert cat_h == expected_cat


@pytest.mark.parametrize(
    ("dog_age", "expected_dog"),
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (16, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 2),
        (30, 3),
    ],
)
def test_dog_boundaries(dog_age: int, expected_dog: int) -> None:
    cat_h, dog_h = get_human_age(0, dog_age)
    assert cat_h == 0
    assert dog_h == expected_dog


@pytest.mark.parametrize(("cat_age", "dog_age"),
                         [(0, 0), (10, 7), (15, 15), (40, 33)])
def test_result_shape_and_types(cat_age: int, dog_age: int) -> None:
    res = get_human_age(cat_age, dog_age)
    assert isinstance(res, list)
    assert len(res) == 2
    assert all(isinstance(x, int) for x in res)


def test_monotonicity() -> None:
    for aa in range(0, 60):
        cat_prev, _ = get_human_age(aa, 0)
        cat_next, _ = get_human_age(aa + 1, 0)
        assert cat_next >= cat_prev

        _, dog_prev = get_human_age(0, aa)
        _, dog_next = get_human_age(0, aa + 1)
        assert dog_next >= dog_prev
