import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("2", "4"),
            ((2,), (4,)),
            ({2}, {4}),
            ([2], [4]),
            (None, None)
        ]
    )
    def test_correct_value_types_get_human_age(
            self, cat_age: int, dog_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_value",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 28, [2, 2]),
            (28, 29, [3, 3]),
            (100, 100, [21, 17]),
            (-3, -3, [0, 0])
        ]
    )
    def test_convert_ages_correctly(
        self, cat_age: int, dog_age: int, expected_value: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_value
