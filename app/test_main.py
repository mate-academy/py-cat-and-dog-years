import pytest

from app.main import get_human_age


class TestAnimalToHumanAge:
    @pytest.mark.parametrize(
        "dog_age, cat_age, result",
        [
            pytest.param(
                100,
                100,
                [21, 17],
                id="try big amount"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="try less than 15"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="try 15"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="try between 15 and 24"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="try 15"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="difference output for cat and dog"
            ),
            pytest.param(
                -100,
                -100,
                [0, 0],
                id="try negative amount"
            )
        ]
    )
    def test_get_human_age(
            self,
            dog_age: int,
            cat_age: int,
            result: list[int]
    ) -> None:
        assert get_human_age(dog_age, cat_age) == result

    def test_raise_error_when_incorrect_value(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("idx", None)
