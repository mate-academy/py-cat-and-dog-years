import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_output",
    [
        (-1000, -1000, [0, 0]),
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
        (10000, 10000, [2496, 1997])
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_output: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_output


@pytest.mark.parametrize(
    "animal,boundary_age,old_human,new_human",
    [
        ("cat", 15, [0, 0], [1, 0]),
        ("cat", 24, [1, 0], [2, 0]),
        ("cat", 28, [2, 0], [3, 0]),
        ("dog", 15, [0, 0] , [0, 1]),
        ("dog", 24, [0, 1], [0, 2]),
        ("dog", 29, [0, 2], [0, 3])
    ]
)
def test_get_human_age_boundary_thresholds(
        animal: str,
        boundary_age: int,
        old_human: list,
        new_human: list
) -> None:
    if animal == "cat":
        assert get_human_age(boundary_age - 1, 0) == old_human
        assert get_human_age(boundary_age, 0) == new_human
    elif animal == "dog":
        assert get_human_age(0, boundary_age - 1) == old_human
        assert get_human_age(0, boundary_age) == new_human


def test_get_human_age_should_raise_type_error_for_invalid_types() -> None:
    invalid_inputs = [
        ("15", 15),
        (15, "15"),
        (15.5, 15),
        (15, 15.5),
        (None, 15),
        (15, None)
    ]

    for cat, dog in invalid_inputs:
        with pytest.raises(TypeError):
            get_human_age(cat, dog)
