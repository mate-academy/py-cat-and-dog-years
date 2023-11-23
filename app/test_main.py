import pytest

from app.main import get_human_age


class TestCatAndDogYear:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            pytest.param(
                0, 0, [0, 0],
                id="should return list [0, 0] if cat and dog ages equal 0"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="should return list [0, 0] if cat and dog ages equal 14"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="should return list [1, 1] if cat and dog ages equal 15"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="should return list [1, 1] if cat and dog ages equal 23"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="should return list [2, 2] if cat and dog ages equal 24"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="should return list [2, 2] if cat and dog ages equal 27"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="should return list [3, 2] if cat and dog ages equal 28"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="should return list [21, 17] if cat and dog ages equal 100"
            ),
        ]
    )
    def test_get_human_age(
        self,
        cat_age: int,
        dog_age: int,
        expected: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age, excepted_error",
        [
            pytest.param(
                "15", 15,
                TypeError,
                id="should raise error when attribute type is str"
            ),
            pytest.param(
                15, "15",
                TypeError,
                id="should raise error when attribute type is str"
            ),
            pytest.param(
                None, 15,
                TypeError,
                id="should raise error when attribute type is None"
            ),
            pytest.param(
                15, None,
                TypeError,
                id="should raise error when attribute type is None"
            ),
            pytest.param(
                (15,), 15,
                TypeError,
                id="should raise error when attribute type is tuple"
            ),
            pytest.param(
                15, (15,),
                TypeError,
                id="should raise error when attribute type is tuple"
            ),
            pytest.param(
                15, [15],
                TypeError,
                id="should raise error when attribute type is list"
            ),
            pytest.param(
                [15], 15,
                TypeError,
                id="should raise error when attribute type is list"
            ),
            pytest.param(
                15, {15},
                TypeError,
                id="should raise error when attribute type is dict"
            ),
            pytest.param(
                {15}, 15,
                TypeError,
                id="should raise error when attribute type is dict"
            ),
        ]
    )
    def test_get_human_age_invalid_input(
            self,
            dog_age: int,
            cat_age: int,
            excepted_error: Exception
    ) -> None:
        with pytest.raises(excepted_error):
            get_human_age(cat_age, dog_age)
