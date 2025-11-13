import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            pytest.param(
                -1,
                -1,
                [0, 0],
                id="Test should 0 zeros if ages equal -1"
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id="Test should 0 zeros if ages equal 0"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="Test should return 0 if ages less than first year"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="Test should return 1 if ages equal first year"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="Test should return 1 if ages between first and second year"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="Test should return 2 if ages between equal second year"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="Test should return 2 if ages over second year"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="Test should return 2 if ages over second year"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="Test should return 21 and 17 if ages equal 100 year"
            ),
        ]
    )
    def test_get_human_age_correct(self,
                                   cat_age: int,
                                   dog_age: int,
                                   result: list) -> None:
        if isinstance(result, type) and issubclass(result, Exception):
            with pytest.raises(result):
                get_human_age(cat_age, dog_age)
        else:
            assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            pytest.param(
                "ten",
                5,
                TypeError,
                id="Should raise TypeError"
            ),
            pytest.param(
                "a",
                "b",
                TypeError,
                id="Should raise TypeError"
            ),
            pytest.param(
                [],
                {},
                TypeError,
                id="Should raise TypeError"
            ),
            pytest.param(
                None,
                10,
                TypeError,
                id="Should raise TypeError"
            ),
        ]
    )
    def test_invalid_data_types_should_raise_typeerror(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:

        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
