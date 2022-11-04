import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            pytest.param(14, 14, [0, 0],
                         id="Up to 15 cat/dog years give 0 human year"),
            pytest.param(15, 15, [1, 1],

                         id="First 15 cat/dog years give 1 human year"),
            pytest.param(23, 23, [1, 1],
                         id="24 cat/dog years should be equal 1 human years"),
            pytest.param(27, 27, [2, 2],
                         id="Every 4 next cat years give 1 extra human year"),
            pytest.param(27, 28, [2, 2],
                         id="Every 5 next dog years give 1 extra human year"),
            pytest.param(28, 28, [3, 2],
                         id="28 cat years should be equal 3 human years"),
            pytest.param(28, 29, [3, 3],
                         id="29 dog years should be equal 3 human years"),
        ],
    )
    def test_get_human_age(self,
                           cat_age: int,
                           dog_age: int,
                           human_age: list) -> None:
        assert (
            get_human_age(cat_age, dog_age) == human_age
        ), f"Cat years: {cat_age} " \
           f"and Dog years: {dog_age} " \
           f"should be equal to human years: {human_age}"

    @pytest.mark.parametrize(
        "cat_age,dog_age,key_error",
        [
            pytest.param("14", 14, TypeError,
                         id="The function receives an incorrect type of data"),
        ]
    )
    def test_should_raise_error_when_input_not_int(self,
                                                   cat_age: int,
                                                   dog_age: int,
                                                   key_error: Exception)\
            -> None:
        with pytest.raises(key_error):
            get_human_age(cat_age, dog_age)
