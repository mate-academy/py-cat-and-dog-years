from app.main import get_human_age
import pytest

# write your code here


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "age_cat, age_dog, expected_list",
        [
            pytest.param(14, 14, [0, 0],
                         id="14/14 cat/dog years should "
                         "convert into 3 human age."),
            pytest.param(23, 23, [1, 1],
                         id="23/23 cat/dog years should "
                         "convert into 1 human age."),
            pytest.param(27, 28, [2, 2],
                         id="27/28 cat/dog years should "
                            "convert into 2 human age."),
            pytest.param(28, 29, [3, 3],
                         id="28/29 cat/dog years should "
                         "convert into 3 human age."),
        ]
    )
    def test_get_human_age(self,
                           age_cat: int,
                           age_dog: int,
                           expected_list: list[int]) -> None:
        assert get_human_age(age_cat, age_dog) == expected_list
