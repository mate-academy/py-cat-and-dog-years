import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_human_ages",
        [
            pytest.param(
                0, 0, [0, 0],
                id="should return 0 human years if animal age is 0"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="should return 0 human years if animal age is 1-14"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="should return 1 human year if animal age is 15-23"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="should return 2 human years if cat age is 24-27"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="should return 2 human years if dog age is 24-28"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="should add 1 human year per each 4 cat years "
                   "if cat age is 24+"
            ),
            pytest.param(
                28, 29, [3, 3],
                id="should add 1 human year per each 5 dog years "
                   "if dog age is 24+"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="add 1 human year per 4 cat years and 5 dog years "
                   "if animal age is 24+"
            ),
            pytest.param(
                -1, -1, [0, 0],
                id="should return 0 if animal age is a negative integer"
            )
        ]
    )
    def test_give_correct_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_human_ages: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_human_ages

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            pytest.param(
                {"age": 3}, {"age": 12},
                id="should raise error "
                   "if data type doesn't support arithmetic "
                   "or comparison operators"
            )
        ]
    )
    def test_raise_error(
            self,
            cat_age: dict | set | str | list | tuple,
            dog_age: dict | set | str | list | tuple,
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
