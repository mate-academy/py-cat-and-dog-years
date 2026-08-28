import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            (-1, 0, [0, 0]),
            (0, -1, [0, 0]),
            (-1, -1, [0, 0]),
        ],
        ids=[
            "cat/dog ages incorrect/correct, test should return [0, 0]",
            "cat/dog ages correct/incorrect, test should return [0, 0]",
            "cat/dog ages incorrect/incorrect, test should return [0, 0]"
        ]
    )
    def test_should_return_zeros_if_input_data_is_incorrect_or_border(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result, \
            (f"test should return {expected_result},"
             f"if cat age={cat_age} and dog age={dog_age} ")

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            (1, 14, [0, 0]),
            (15, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (29, 29, [3, 3]),
            (33, 35, [4, 4]),
            (100, 100, [21, 17])
        ],
        ids=[
            "test should return [0, 0]",
            "test should return [1, 1]",
            "test should return [2, 2]",
            "test should return [2, 2]",
            "test should return [3, 2]",
            "test should return [3, 3]",
            "test should return [4, 4]",
            "test should return [21, 17]",
        ]
    )
    def test_should_return_correct_result_if_pets_age_are_correct(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result, \
            (f"test should return {expected_result}"
             f" if cat/dog ages are {cat_age}/{dog_age}")

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            ({}, 5, TypeError),
            ((), 4, TypeError),
            ([], 5, TypeError),
            (set(), 5, TypeError),
            ("some_text", 5, TypeError),
            (5, {}, TypeError),
            (4, (), TypeError),
            (5, [], TypeError),
            (5, set(), TypeError),
            (5, "some_text", TypeError),
            ({}, "some_text", TypeError),
        ]
    )
    def test_should_raise_error_if_any_of_arguments_is_incorrect(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: Exception,
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age), \
                (f"test should return {expected_error}"
                 f"if input data cat/dog {type(cat_age)}/{type(dog_age)}")
