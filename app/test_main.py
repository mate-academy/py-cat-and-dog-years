import pytest
from app.main import get_human_age


class TestMain:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (28, 29, [3, 3]),
            (100, 100, [21, 17]),
            (1000, 1000, [246, 197]),
            (5000, 3000, [1246, 597]),
        ],
        ids=[
            "human age must be 0 because animal age is less than 15 years old",
            "human age must be 0 because animal age is less than 15 years old",
            "human age must be 1 because animal age is 15 years old",
            "human age must be 1 because animal age is less than 24 years old",
            "human age must be 2 because animal age 25 years old",
            "human age must be 2 because animal age is less than 29 years old",
            "human age must be 3 and 2  because cat and dog age == 28",
            "human age must be 3 and 3 because cat and dog age == 29",
            "human age must be 21 and 17 because cat and dog age == 100",
            "It is very large number",
            "It is too very large number",

        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",

        [
            pytest.param(
                -2,
                15,
                [0, 1],
                id="cat_age is negative!!!!"
            ),
            pytest.param(
                25,
                -4,
                [2, 0],
                id="dog_age is negative!!!!"
            ),
            pytest.param(
                -3,
                -7,
                [0, 0],
                id="dog_age and cat_age is negative!!!!"
            ),

        ]
    )
    def test_should_return_zero(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                (1,),
                0,
                TypeError,
                id="should raise exception because cat_age is tuple"
            ),
            pytest.param(
                "1",
                0,
                TypeError,
                id="should raise exception because cat_age is str"
            ),
            pytest.param(
                None,
                0,
                TypeError,
                id="should raise exception because cat_age is None"
            ),
            pytest.param(
                0,
                [1, 1, 1],
                TypeError,
                id="should raise exception because dog_age is list"
            ),
            pytest.param(
                0,
                {"1": 1},
                TypeError,
                id="should raise exception because dog_age is dict"
            ),

            pytest.param(
                0,
                {1, 1, 1, 1},
                TypeError,
                id="should raise exception because dog_age is set"
            ),
        ]
    )
    def test_should_raise_exception(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: type
    ) -> None:
        with pytest.raises(expected_result):
            get_human_age(cat_age, dog_age)
