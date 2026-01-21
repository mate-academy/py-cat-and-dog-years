from app.main import get_human_age
import pytest


class TestsGetHumanAge:
    @pytest.mark.parametrize(
        "initial_cat_age,initial_dog_age,expected_age",
        [
            pytest.param(
                0, 0, [0, 0],
                id="converted dog and cat \
                    should be equal 0 when animal age is 0"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="converted dog and cat age should \
                    be equal 0 when animal age less than 15"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="converted dog and cat age should be equal 1 \
                    when animal age more than 14 and less than 24"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="converted dog and cat age should be equal  2 when \
                    animal age more than 23 and less than \
                    (cat age 27), (dog age 28)"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="converted dog and cat age should be equal 3 \
                    when (cat age 28), (dog age 29)"
            ),
            pytest.param(
                50, 50, [8, 7],
                id="converted cat age should increase by one every 4 years \
                if cat age more than 27, converted dog age every 5 years \
                if dog age more than 28"
            ),
            pytest.param(
                -1, -10, [0, 0],
                id="converted animal age should be 0 when \
                    animal age less than 0"
            )
        ]
    )
    def test_translates_age_correctly(
        self,
        initial_cat_age: int,
        initial_dog_age: int,
        expected_age: list
    ) -> None:
        assert get_human_age(initial_cat_age, initial_dog_age) == expected_age


class TestsRaisesGetHumanAge:

    @pytest.mark.parametrize(
        "initial_cat_age,initial_dog_age",
        [
            pytest.param(
                "1", 2,
                id="should raises 'TypeError' when type \
                    of attribute not int and not float"
            ),
            pytest.param(
                2, [],
                id="should raises 'TypeError' when type of \
                    attribute not int and not float"
            ),
            pytest.param(
                "1", [],
                id="should raises 'TypeError' when type of \
                    attribute not int and not float"
            ),

        ]
    )
    def tests_type_error(
        self,
        initial_cat_age: int,
        initial_dog_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(initial_cat_age, initial_dog_age)
