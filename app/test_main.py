import pytest

from app.main import get_human_age


class TestMainClass:
    @pytest.mark.parametrize(
        "initial_cat_age,"
        "initial_dog_age,"
        "expected_cat_to_human,"
        "expected_dog_to_human",
        [
            pytest.param(
                0,
                0,
                0,
                0,
                id="should return 0 if animal_age < 15"),
            pytest.param(
                14,
                14,
                0,
                0,
                id="should return 0 if animal_age < 15"),
            pytest.param(
                15,
                15,
                1,
                1,
                id="should return 1 if 15 <= animal_age < 24"),
            pytest.param(
                23,
                23,
                1,
                1,
                id="should return 1 if 15 <= animal_age < 24"),
            pytest.param(
                28,
                28,
                3,
                2,
                id="should return >= 2 if animal_age > 24"),
            pytest.param(
                100,
                100,
                21,
                17,
                id="should return 0 if animal_age > 24")
        ]
    )
    def test_get_human_age(
            self,
            initial_cat_age: int,
            initial_dog_age: int,
            expected_cat_to_human: int,
            expected_dog_to_human: int
    ) -> None:
        assert (get_human_age(initial_cat_age, initial_dog_age)
                == [expected_cat_to_human, expected_dog_to_human])
