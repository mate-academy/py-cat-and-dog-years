import pytest

from app.main import get_human_age


class TestGetAge:
    @pytest.mark.parametrize(
        "dog_age, cat_age, excepted_age",
        [
            (-1, -1, [0, 0]),
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ],
        ids=[
            "test negative value",
            "test zero value",
            "test excepted_age is zero",
            "test first year",
            "test almost second year",
            "test second year",
            "test almost third year",
            "test each year",
            "test large year",
        ]
    )
    def test_correctly_age(
            self,
            dog_age: int,
            cat_age: int,
            excepted_age: list
    ) -> None:
        assert get_human_age(dog_age, cat_age) == excepted_age

@pytest.mark.parametrize(
    "dog_age, cat_age",
    [
        ("", ""),
        ([],[]),
    ],
    ids=[
        "if input is string",
        "if input is list",
    ]
)
def test_should_raise_error(
        cat_age: int,
        dog_age: int,
) -> None:
    with pytest.raises(TypeError):
        get_human_age(dog_age, cat_age)
