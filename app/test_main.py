import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            pytest.param(0, 0, [0, 0],
                         id="O numbers of years should return [0, 0]"),
            pytest.param(14, 14, [0, 0],
                         id="Up to 15 numbers of years given 0 human year"),
            pytest.param(27, 28, [2, 2],
                         id="27 cat 28 dog years should equal 2 human age"),
            pytest.param(24, 24, [2, 2],
                         id="24 cat/dog years should be equal 2 human years"),
            pytest.param(28, 29, [3, 3],
                         id="Every 4/5 cat/dog years give 1 extra human year"),
            pytest.param(-20, -34, [0, 0],
                         id="Negative numbers of years should be equal [0,0]"),
            pytest.param(1000, 10000, [246, 1997],
                         id="larges numbers of ages should be equal not real"),
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
        "cat_age,dog_age",
        [
            pytest.param("14", "14",
                         id="The function receives an incorrect type of data"),
        ]
    )
    def test_should_error_parameters_not_int(self,
                                             cat_age: int,
                                             dog_age: int
                                             ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
