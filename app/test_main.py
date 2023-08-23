import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return zeros when ages are zeros"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="cat/dog years should convert into 0 human age "
                   "when less then 15"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="cat/dog years should convert into 1 human age "
                   "when more or equal 15"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="cat/dog years should convert into 1 human age "
                   "when less than 24"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="cat/dog years should convert into 2 human age "
                   "when more or equal 24"
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="cat/dog years should convert into 2 human age "
                   "when less than 28(29) for cat(dog)"
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="cat/dog years should correct convert into human age "
                   "when more or equal 28(29) for cat(dog)"
            ),
            pytest.param(
                1000,
                1000,
                [246, 197],
                id="cat/dog years should correct convert into human age "
                   "when ages are really!! large numbers"
            ),
            pytest.param(
                -15,
                -25,
                [0, 0],
                id="should return zeros when ages are negative numbers"
            )
        ]
    )
    def test_convert_ages_correctly(
        self,
        cat_age: int,
        dog_age: int,
        expected_result: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    def test_ages_type(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("10", 2)
