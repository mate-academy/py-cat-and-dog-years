import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, -50, [0, 0]),
            (28, 29, [3, 3]),
            (103, 103, [21, 17]),
            (
                9832475923845729347,
                92343459304593498493,
                [2458118980961432332, 18468691860918699695]
            )
        ],
        ids=[
            "for zero and below argument(s)",
            "if age is divisible without remainder",
            "if age is divisible with remainder",
            "when a very high age is indicated"
        ]
    )
    def test_should_return_correct_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("123", 10),
            (15, [1, 2, 3])
        ],
        ids=[
            "if `cat_age` argument is wrong type",
            "if `dog_age` argument is wrong type"
        ]
    )
    def test_should_raise_type_error(
        self,
        cat_age: int,
        dog_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

    def test_result_should_not_be_changed_by_previous_value(self) -> None:
        assert (
            get_human_age(28, 29)
            is not get_human_age(103, 103)
        )
