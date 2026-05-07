import pytest
from typing import Any

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,cat_human_age,dog_human_age",
    [
        (0, 0, 0, 0),
        (14, 14, 0, 0),
        (15, 15, 1, 1),
        (23, 23, 1, 1),
        (24, 24, 2, 2),
        (27, 28, 2, 2),
        (28, 29, 3, 3),
        (31, 33, 3, 3),
        (32, 34, 4, 4),
        (35, 38, 4, 4),
        (36, 39, 5, 5),
        (39, 43, 5, 5),
        (40, 44, 6, 6),
        (43, 48, 6, 6),
        (44, 49, 7, 7),
        (47, 53, 7, 7),
        (48, 54, 8, 8),
        (51, 58, 8, 8),
        (52, 59, 9, 9),
        (55, 63, 9, 9),
        (56, 64, 10, 10),
        (59, 68, 10, 10),
        (60, 69, 11, 11),
        (63, 73, 11, 11),
        (64, 74, 12, 12),
        (67, 78, 12, 12),
        (68, 79, 13, 13),
        (71, 83, 13, 13),
        (72, 84, 14, 14),
        (75, 88, 14, 14),
        (76, 89, 15, 15),
        (79, 93, 15, 15),
        (80, 94, 16, 16),
        (83, 98, 16, 16),
        (84, 27, 17, 2),
        (87, 31, 17, 3),
        (88, 32, 18, 3),
        (91, 35, 18, 4),
        (92, 36, 19, 4),
        (95, 40, 19, 5),
        (96, 47, 20, 6),
        (99, 51, 20, 7),
        (100, 100, 21, 17),
        (14.8, 14.8, 0, 0),
        (23.8, 23.8, 1, 1),
        (27.8, 28.8, 2, 2),
        (31.8, 33.8, 3, 3),
        (35.8, 38.8, 4, 4),
        (39.8, 43.8, 5, 5),
        (43.8, 48.8, 6, 6),
        (47.8, 53.8, 7, 7),
        (51.8, 58.8, 8, 8),
        (55.8, 63.8, 9, 9),
        (59.8, 68.8, 10, 10),
        (63.8, 73.8, 11, 11),
        (67.8, 78.8, 12, 12),
        (71.8, 83.8, 13, 13),
        (75.8, 88.8, 14, 14),
        (79.8, 93.8, 15, 15),
        (83.8, 98.8, 16, 16),
        (87.8, 31.2, 17, 3),
        (91.8, 35.5, 18, 4),
        (95.8, 40.7, 19, 5),
        (99.8, 51.9, 20, 7),
        (100.8, 100.8, 21, 17)
    ]
)
def test_can_properly_covert_animal_age_to_human_age(
        cat_age: int | float,
        dog_age: int | float,
        cat_human_age: int,
        dog_human_age: int
) -> None:
    assert get_human_age(
        cat_age=cat_age,
        dog_age=dog_age
    ) == [cat_human_age, dog_human_age]


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        (-36.7, 36.7),
        (-2, 2),
        (101, 27),
        (36.7, -36.7),
        (2, -2),
        (27, 101),
        (-36.7, -36.7),
        (-2, -2),
        (101, 101)
    ]
)
def test_raises_an_error_for_data_out_of_range(
        cat_age: int | float,
        dog_age: int | float
) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age=cat_age, dog_age=dog_age)


@pytest.mark.parametrize(
    "cat_age,dog_age",
    [
        ("32", "32"),
        ([32], [32]),
        ({32}, {32}),
        ((32, 53), (32, 53)),
        (True, True),
        (32, "32"),
        (32, [32]),
        (32, {32}),
        (32, (32, 53)),
        (1, True),
        ("32", 32),
        ([32], 32),
        ({32}, 32),
        ((32, 53), 32),
        (True, 1)
    ]
)
def test_values_are_not_numbers(cat_age: Any, dog_age: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age=cat_age, dog_age=dog_age)
