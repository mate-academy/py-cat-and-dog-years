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
            pytest.param(
                -1, -1, [0, 0],
                id="should return list [0, 0] if cat and dog ages less than 0"
            ),
            pytest.param(
                111, 123, [23, 21],
                id="should return list with different numbers "
                   "[23, 21] if cat and dog have different age"
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
        "cat_age,dog_age,expected",
        [
            pytest.param(
                "14", 15, None,
                id="should raise a TypeError if given parameters aren't int"
            )
        ]
    )
    def test_get_human_age_with_invalid_type(
            self,
            cat_age: int,
            dog_age: int,
            expected: list[int]
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
