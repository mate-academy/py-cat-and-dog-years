import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            (0, 0, [0, 0]),
            (3, 12, [0, 0]),
            (12, 4, [0, 0]),
            (14, 14, [0, 0]),
            (-20, -15, [0, 0]),
        ]
    )
    def test_should_be_equal_zero(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            (17, 17, [1, 1]),
            (18, 2, [1, 0]),
            (19, 23, [1, 1]),
            (2, 23, [0, 1]),
        ]
    )
    def test_should_be_equal_one(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            (35, 30, [4, 3]),
            (60, 60, [11, 9]),
            (70, 65, [13, 10]),
            (105, 105, [22, 18]),
            (120, 120, [26, 21]),
        ]
    )
    def test_should_be_result_function(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    def test_should_type_error(self) -> None:
        with pytest.raises(TypeError):
            get_human_age(5, "5")
