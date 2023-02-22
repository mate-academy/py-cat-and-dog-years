import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(0,
                         0,
                         [0, 0],
                         id="0/0 animal age  should equal 0/0 human age"),
            pytest.param(14,
                         14,
                         [0, 0],
                         id="14/14 animal age should equal 0/0 human age"),
            pytest.param(15,
                         15,
                         [1, 1],
                         id="15/15 animal age should equal 1/1 human age"),
            pytest.param(23,
                         23,
                         [1, 1],
                         id="23/23 animal age should equal 1/1 human age"),
            pytest.param(27,
                         27,
                         [2, 2],
                         id="27/27 animal age should equal 2/2 human age"),
            pytest.param(28,
                         28,
                         [3, 2],
                         id="28/28 animal age should equal 3/2 human age"),
            pytest.param(100,
                         100,
                         [21, 17],
                         id="100/100 animal age should equal 21/17 human age"),
            pytest.param(-1,
                         -1,
                         [0, 0],
                         id="Negative animal age should equal 0 human age")
        ]
    )
    def test_years_counting_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cate_age,dog_age,expected_error",
        [
            pytest.param(5,
                         "5",
                         TypeError,
                         id="should raise error when param's aren't numbers")
        ]
    )
    def test_raising_errors_correctly(
            self,
            cate_age: int,
            dog_age: int,
            expected_error: TypeError
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cate_age, dog_age)
