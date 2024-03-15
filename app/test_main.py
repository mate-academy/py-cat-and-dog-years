import traceback
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
            ),
            pytest.param(
                120,
                129,
                [26, 23],
                id="Animal years (big value) should into 26(23) human age",
            )
            ,
            pytest.param(
                -10,
                -6,
                [0, 0],
                id="Animal years (all negative value) should into 0 human age",
            )
        ]
    )
    def test_correct_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            correct_answer: list) -> None:
        assert get_human_age(cat_age, dog_age) == correct_answer

    @pytest.mark.parametrize(
        "cat_age,dog_age,type_errors",
        [
            pytest.param(
                "cat",
                "dog",
                TypeError,
                id="String type error"
            ),
            pytest.param(
                None,
                None,
                TypeError,
                id="None type error"
            )
        ]
    )
    def test_incorrect_type_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            type_errors: traceback) -> None:
        with pytest.raises(type_errors):
            get_human_age(cat_age, dog_age)
