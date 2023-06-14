import pytest


from app.main import get_human_age


class TestCatsDogsClass:
    @pytest.mark.parametrize("cat,dog,expected", [
        (0, 0, [0, 0]),
        (5, 5, [0, 0]),
        (14, 14, [0, 0])
    ])
    def test_zero_when_age_less_14(self, cat: int, dog: int, expected: list) -> None:
        assert get_human_age(cat, dog) == expected

    @pytest.mark.parametrize("cat,dog,expected", [
        (15, 15, [1, 1]),
        (17, 17, [1, 1]),
        (23, 23, [1, 1])
    ])
    def test_age_more_than_15(self, cat: int, dog: int, expected: list) -> None:
        assert get_human_age(cat, dog) == expected

    @pytest.mark.parametrize("cat,dog,expected", [
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (27, 27, [2, 2])
    ])
    def test_age_more_24(self, cat: int, dog: int, expected: list) -> None:
        assert get_human_age(cat, dog) == expected

    @pytest.mark.parametrize("cat,dog,expected", [
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ])
    def test_age_dog_and_cat_should_be_different(self, cat: int, dog: int, expected: list) -> None:
        assert get_human_age(cat, dog) == expected
