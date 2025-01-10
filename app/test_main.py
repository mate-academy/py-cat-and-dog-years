import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (0, 0),
            (14, 14),
            (15, 17)
        ]
    )
    def test_get_human_age_should_return_a_list(
        self,
        cat_age: int,
        dog_age: int
    ) -> None:
        assert type(get_human_age(cat_age, dog_age)) == list

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (0, 0),
            (14, 14),
            (15, 17)
        ]
    )
    def test_get_human_age_should_return_len_equals_two(
        self,
        cat_age: int,
        dog_age: int
    ) -> None:
        assert len(get_human_age(cat_age, dog_age)) == 2

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (0, 0),
            (14, 14),
        ]
    )
    def test_get_human_age_should_return_zeroes_list(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        assert get_human_age(cat_age, dog_age) == [0, 0]

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ]
    )
    def test_get_human_age_check_with_different_input_values(
            self,
            cat_age: int,
            dog_age: int,
            expected: int
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected
