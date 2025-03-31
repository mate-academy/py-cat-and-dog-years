import pytest
from app.main import get_human_age


class TestGetHumanAgeClass:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                -12,
                -12,
                [0, 0],
                id="Negative amount of years should convert into 0 human age"
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id="0 cat/dog years should convert into 0 human age."
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="14 cat/dog years should convert into 0 human age."
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="15 cat/dog years should convert into 1 human age."
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="23 cat/dog years should convert into 1 human age."
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="24 cat/dog years should convert into 2 human age."
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="27/28 cat/dog years should convert into 2 human age."
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="28/29 cat/dog years should convert into 3 human age."
            ),



        ]
    )
    def test_get_human_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: [int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                "Foo",
                "Foo",
                TypeError,
                id="Should raise TypeError "
                   "if cat's or dog's years are not integers"
            ),
        ]
    )
    def test_raising_errors_correctly(
        self,
        cat_age: int,
        dog_age: int,
        expected_error: TypeError
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
