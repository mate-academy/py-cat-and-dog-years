from app.main import get_human_age
import pytest


class Test:
    @pytest.mark.parametrize("cat_age, dog_age, expected_result", [
        (1, 1, [0, 0]),
        (7, 7, [0, 0]),
        (15, 15, [1, 1]),
    ])
    def test_get_human_age_first_15_years(
            self, cat_age: int, dog_age: int, expected_result: list
    ) -> list:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize("cat_age, dog_age, expected_result", [
        (16, 16, [1, 1]),
        (20, 27, [1, 2]),
        (24, 20, [2, 1]),
    ])
    def test_get_human_age_next_9_years(
            self, cat_age: int, dog_age: int, expected_result: list
    ) -> list:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize("cat_age, dog_age, expected_result", [
        (25, 25, [2, 2]),
        (30, 35, [3, 4]),
        (35, 45, [4, 6]),
    ])
    def test_get_human_age_after_24_years(
            self, cat_age: int, dog_age: int, expected_result: list
    ) -> list:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize("cat_age, dog_age, expected_result", [
        (36, 36, [5, 4]),
        (40, 45, [6, 6]),
        (43, 43, [6, 5]),
    ])
    def test_get_human_age_extra_years(
            self, cat_age: int, dog_age: int, expected_result: list
    ) -> list:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize("cat_age, dog_age, expected_result", [
        (7, 6, [0, 0]),
        (22, 15, [1, 1]),
        (30, 24, [3, 2]),
        (50, 35, [8, 4]),
        (60, 45, [11, 6]),
    ])
    def test_get_human_age_dog_ages(
            self, cat_age: int, dog_age: int, expected_result: list
    ) -> list:
        assert get_human_age(cat_age, dog_age) == expected_result
