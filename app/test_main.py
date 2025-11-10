import pytest
from app.main import get_human_age


class TestCatAge:
    @pytest.mark.parametrize(
        "cat_age, expected",
        [
            (0, 0),
            (14, 0),
            (15, 1),
            (23, 1),
            (24, 2),
            (27, 2),
            (28, 3),
            (32, 4),
            (100, 21),
        ]
    )
    def test_cat_years_to_human(self, cat_age: int, expected: int) -> None:
        assert get_human_age(cat_age, 0)[0] == expected


class TestDogAge:
    @pytest.mark.parametrize(
        "dog_age, expected",
        [
            (0, 0),
            (14, 0),
            (15, 1),
            (23, 1),
            (24, 2),
            (28, 2),
            (29, 3),
            (34, 4),  # ✅ виправлено
            (35, 4),
            (100, 17),
        ]
    )
    def test_dog_years_to_human(self, dog_age: int, expected: int) -> None:
        assert get_human_age(0, dog_age)[1] == expected


class TestCombinedAges:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (28, 29, [3, 3]),
            (100, 100, [21, 17]),
        ]
    )
    def test_get_human_age_both(self,
                                cat_age: int,
                                dog_age: int,
                                expected: list[int]) -> None:
        assert get_human_age(cat_age, dog_age) == expected


class TestOutputFormat:
    def test_result_always_two_values(self) -> None:
        result = get_human_age(50, 50)
        assert isinstance(result, list)
        assert len(result) == 2

    def test_result_values_are_integers(self) -> None:
        result = get_human_age(50, 50)
        assert all(isinstance(age, int) for age in result)
