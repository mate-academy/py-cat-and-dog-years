import pytest

from app.main import get_human_age


class TestGetHumanAgeShouldReturnExpectedResult:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
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
            (5, 10, [0, 0]),
            (12, 3, [0, 0]),
        ]
    )
    def test_get_human_age_returns_correct_age_for_cat_and_dog(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("five", 10),
            (12, "ten"),
            ([5], [10]),
            ({"cat": 5}, {"dog": 10}),
            (None, 10),
            (5, None),
        ]
    )
    def test_get_human_age_invalid_inputs(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
