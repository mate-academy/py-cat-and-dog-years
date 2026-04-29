import pytest
from app.main import get_human_age


class TestGetHumanAge:

    @pytest.mark.parametrize("cat_age, dog_age, expected_human_age",
                             [
                                 (0, 0, [0, 0]),
                                 (14, 14, [0, 0]),
                                 (15, 15, [1, 1]),
                                 (18, 19, [1, 1]),
                                 (18, 25, [1, 2]),
                                 (24, 24, [2, 2]),
                                 (27, 28, [2, 2]),
                                 (28, 28, [3, 2]),
                                 (29, 29, [3, 3]),
                                 (32, 32, [4, 3]),
                                 (32, 34, [4, 4]),
                                 (34, 34, [4, 4]),
                                 (32, 5, [4, 0]),
                                 (22, 34, [1, 4]),
                                 (10, 24, [0, 2])
                             ])
    def test_cat_and_dog_age_equal_to_expected_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_human_age: int
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_human_age

    @pytest.mark.parametrize("cat_age, dog_age, expected_human_age",
                             [
                                 (-1, -1, [0, 0]),
                                 (-15, -15, [0, 0])
                             ])
    def test_cat_and_dog_age_is_lower_than_zero(
            self,
            cat_age: int,
            dog_age: int,
            expected_human_age: int
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_human_age

    @pytest.mark.parametrize("cat_age, dog_age",
                             [
                                 (None, 15),
                                 ("5", 2),
                                 (25.3, None)
                             ])
    def test_age_is_not_a_number(
            self,
            cat_age: int,
            dog_age: int,
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
