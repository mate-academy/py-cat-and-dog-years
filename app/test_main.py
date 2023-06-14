import pytest


from app.main import get_human_age


class TestCatAndDogYears:
    @pytest.mark.parametrize(
        "cat_age, dog_age, exp_result",
        [
            pytest.param(-1, -1, [0, 0],
                         id="Should return zero when input is negative"),
            pytest.param(0, 0, [0, 0],
                         id="Should return zero values"),
            pytest.param(14, 14, [0, 0],
                         id="Values less when cat/gog one year"),
            pytest.param(23, 23, [1, 1],
                         id="Values less when cat/gog two year"),
            pytest.param(27, 27, [2, 2],
                         id="Values less when cat/gog three year"),
            pytest.param(28, 28, [3, 2],
                         id="Values cat has three year and dog four"),
            pytest.param(28, 28, [3, 2],
                         id="Values cat has three year and dog four"),
            pytest.param(100, 100, [21, 17],
                         id="Cat and dog have more than three year"),
        ]
    )
    def test_get_human_age(self,
                           cat_age: int,
                           dog_age: int,
                           exp_result: list) -> None:
        assert (
            get_human_age(cat_age, dog_age) == exp_result
        ), f"Cat:{cat_age} and dog:{cat_age} should return {exp_result}"

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            pytest.param("",
                         17,
                         TypeError,
                         id="Should return error when type is incorrect")
        ]
    )
    def test_raising_error(self,
                           cat_age: int,
                           dog_age: int,
                           expected_error: type[Exception]) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
