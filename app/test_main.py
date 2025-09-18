import pytest
from app.main import get_human_age


class TestGetHumanAge:

    @pytest.mark.parametrize("cat_age,dog_age,expected", [
        (0, 0, [0, 0]),
        (1, 1, [0, 0]),
        (10, 5, [0, 0]),
        (14, 14, [0, 0]),
    ])
    def test_ages_below_first_threshold(
            self, cat_age: int, dog_age: int, expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize("cat_age,dog_age,expected", [
        (15, 15, [1, 1]),
        (16, 16, [1, 1]),
        (20, 20, [1, 1]),
        (23, 23, [1, 1]),
    ])
    def test_ages_between_first_and_second_threshold(
            self, cat_age: int, dog_age: int, expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize("cat_age,dog_age,expected", [
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
    ])
    def test_ages_at_and_after_second_threshold(
            self, cat_age: int, dog_age: int, expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize("cat_age,dog_age,expected", [
        (15, 20, [1, 1]),
        (20, 15, [1, 1]),
        (30, 25, [3, 2]),
        (25, 30, [2, 3]),
        (28, 29, [3, 3]),
        (29, 28, [3, 2]),
    ])
    def test_different_cat_dog_ages(
            self, cat_age: int, dog_age: int, expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize("cat_age,dog_age,expected", [
        (50, 50, [8, 7]),
        (100, 100, [21, 17]),
        (200, 200, [46, 37]),
        (1000, 1000, [246, 197]),
    ])
    def test_large_ages(
            self, cat_age: int, dog_age: int, expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize("cat_age,expected_cat", [
        (15, 1),
        (24, 2),
        (28, 3),
        (32, 4),
    ])
    def test_cat_specific_calculation(
            self, cat_age: int, expected_cat: int
    ) -> None:
        result = get_human_age(cat_age, 0)
        assert result[0] == expected_cat

    @pytest.mark.parametrize("dog_age,expected_dog", [
        (15, 1),
        (24, 2),
        (29, 3),
        (34, 4),
    ])
    def test_dog_specific_calculation(
            self, dog_age: int, expected_dog: int
    ) -> None:
        result = get_human_age(0, dog_age)
        assert result[1] == expected_dog

    def test_negative_ages_behavior(self) -> None:
        assert get_human_age(-1, 0) == [0, 0]
        assert get_human_age(0, -1) == [0, 0]
        assert get_human_age(-5, -10) == [0, 0]

    def test_incorrect_data_types_raise_exception(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("15", 20)
        with pytest.raises(TypeError):
            get_human_age(15, "20")
        with pytest.raises(TypeError):
            get_human_age(None, 20)
        with pytest.raises(TypeError):
            get_human_age(15, None)

    def test_float_inputs_work(self) -> None:
        assert get_human_age(15.5, 20.5) == [1, 1]
        assert get_human_age(15.0, 20.0) == [1, 1]

    def test_very_large_numbers(self) -> None:
        assert get_human_age(10000, 10000) == [2496, 1997]
        assert get_human_age(100000, 100000) == [24996, 19997]
