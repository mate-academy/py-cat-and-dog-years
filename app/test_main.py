import pytest

from app.main import get_human_age


class TestDogAndCat:
    @pytest.mark.parametrize(
        "cat_age,dog_age,correct_answer",
        [
            pytest.param(
                14,
                0,
                [0, 0],
                id="0 dog years should into 0 human age"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="First 15 years animal should into 1 human age",
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="Animal years should convert into 2 human age",
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="Animal years should into 3 human age",
            )
        ]
    )
    def test_correct_get_human_age(self,
                                   cat_age: int,
                                   dog_age: int,
                                   correct_answer: list) -> None:
        assert get_human_age(cat_age, dog_age) == correct_answer
