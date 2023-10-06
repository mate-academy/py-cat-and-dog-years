import pytest
from app.main import get_human_age


class TestGetHumanAgeClass:
    @pytest.mark.parametrize(
        "cat_age, dog_age, value",
        [
            (-1, 1, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 28, [2, 2]),
            (28, 29, [3, 3]),
            (1000, 1000, [246, 197])
        ]
    )
    def test_values_get_human_age_tester(
            self,
            cat_age: int,
            dog_age: int,
            value: list
    ) -> None:

        assert get_human_age(cat_age, dog_age) == value

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("k", 12),
            (12, "k"),
            ("k", "k"),
            ({"k"}, {"k"}),
            (["k"], ["k"])
        ]
    )
    def test_correct_types_value_get_human_age(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:

        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
