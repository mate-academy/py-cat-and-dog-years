import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,human_age",
        [
            pytest.param(
                15,
                1,
                id="human age should be equal to 1 when cat age == 15"
            ),
            pytest.param(
                24,
                2,
                id="after 15 years every 9 cat years equal to 1 human"
            ),
            pytest.param(
                28,
                3,
                id="after 24 years next 4 cats years equal to 1 human"
            )
        ]
    )
    def test_cat_years(self, cat_age: int, human_age: int) -> None:
        assert get_human_age(cat_age, 0) == [human_age, 0]

    @pytest.mark.parametrize(
        "dog_age,human_age",
        [
            pytest.param(
                15,
                1,
                id="human age should be equal to 1 when dog age == 15"
            ),
            pytest.param(
                24,
                2,
                id="after 15 years every 9 dog years equal to 1 human"
            ),
            pytest.param(
                29,
                3,
                id="after 24 years next 5 dog years equal to 1 human"
            ),
            pytest.param(
                28,
                2,
                id="dog years don't count as cat"
            )
        ]
    )
    def test_dog_years(self, dog_age: int, human_age: int) -> None:
        assert get_human_age(0, dog_age) == [0, human_age]

    def test_cat_and_dog_years(self) -> None:
        assert get_human_age(100, 100) == [21, 17]
