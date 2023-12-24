from app.main import get_human_age
import pytest


class TestExpectedHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, human_age",
        [
            pytest.param(0, 0, [0, 0]),
            pytest.param(14, 14, [0, 0]),
            pytest.param(15, 15, [1, 1]),
            pytest.param(23, 23, [1, 1]),
            pytest.param(24, 24, [2, 2]),
            pytest.param(27, 27, [2, 2]),
            pytest.param(28, 28, [3, 2]),
            pytest.param(100, 100, [21, 17])
        ]
    )
    def test_human_age_with_correct_positive_ages(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list
    ) -> None:
        assert (
            get_human_age(cat_age, dog_age) == human_age
        )

    @staticmethod
    def test_human_age_with_negative_ages() -> None:
        assert (
            get_human_age(-1, -15) == [0, 0]
        )

    @staticmethod
    def test_human_age_with_incorrect_types() -> None:
        with pytest.raises(TypeError):
            get_human_age(2, "28")
