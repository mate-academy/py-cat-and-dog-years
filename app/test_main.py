import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_list",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="test zero cat and dog age"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="test borderline case zero and one human year"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="test for one human year"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="test for two human years"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="test for the borderline case between two and three years"
            ),
            pytest.param(
                30,
                30,
                [3, 3],
                id="test for three human years"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="test for twenty eight cat and dog years"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="test for hundred cat and dog years"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="test for twenty three cat and dog years"
            ),
            pytest.param(
                29,
                29,
                [3, 3],
                id="test for twenty nine cat and dog years"
            ),
            pytest.param(
                31,
                31,
                [3, 3],
                id="test for thirty one cat and dog years"
            ),
            pytest.param(
                32,
                32,
                [4, 3],
                id="test for thirty two cat and dog years"
            ),
        ]
    )
    def test_human_age_correctly(
        self,
        cat_age: int,
        dog_age: int,
        expected_list: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_list

    @pytest.mark.parametrize(
        "cat_age, dog_age, error",
        [
            pytest.param(
                None,
                None,
                TypeError,
                id="test should raise error if none values"
            ),
            pytest.param(
                "23",
                "25",
                TypeError,
                id="test for incorrect type input"
            ),
            pytest.param(
                "23",
                25,
                TypeError,
                id="test for cat age incorrect type input"
            ),
            pytest.param(
                23,
                "25",
                TypeError,
                id="test for dog age incorrect type input"
            ),
            pytest.param(
                -23,
                -25,
                ValueError,
                id="test for negative age"
            ),
            pytest.param(
                -23,
                25,
                ValueError,
                id="test for cat negative age"
            ),
            pytest.param(
                23,
                -25,
                ValueError,
                id="test for dog negative age"
            ),
        ]
    )
    def test_human_age_error(
        self,
        cat_age: object,
        dog_age: object,
        error: type[Exception]
    ) -> None:
        with pytest.raises(error):
            get_human_age(cat_age, dog_age)
