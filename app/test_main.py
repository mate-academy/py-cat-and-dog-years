import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return list of 0 when ages are zeros"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="pet's age is less than 1 human's year"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="pet's age should convert in 1 human's year"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id=("pet's age should convert in 1 human's year "
                    "when less than 24")
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="pet's age should convert in 2 human's year"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id=("pet's age should convert in 2 human's year "
                    "when less than 28(29) for cat(dog)")
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="pet's age should convert into 3 for cat and 2 for dog "
                   "when ages are 28"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="pet's age should correct convert into 3 human years "
                   "when more or equal 28(29) for cat(dog)"
            ),
            pytest.param(
                1000,
                1000,
                [246, 197],
                id=("cat/dog years should correct convert into human age "
                    "when used large pet's ages")
            ),
            pytest.param(
                -15,
                -15,
                [0, 0],
                id="should return 0 when ages are negative numbers"
            )
        ]
    )
    def test_age_conversion(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    def test_incorrect_data(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("15", 15)
