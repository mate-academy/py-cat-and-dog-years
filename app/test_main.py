import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            pytest.param(
                14, 14, [0, 0],
                id="should calculate human age when "
                   "(`cat_age`, `dog_age`) = (14, 14)"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="should calculate human age when "
                   "(`cat_age`, `dog_age`) = (15, 15)"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="should calculate human age when "
                   "(`cat_age`, `dog_age`) = (23, 23)"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="should calculate human age when "
                   "(`cat_age`, `dog_age`) = (24, 24)"
            ),
            pytest.param(
                27, 28, [2, 2],
                id="should calculate human age when "
                   "(`cat_age`, `dog_age`) = (27, 28)"
            ),
            pytest.param(
                28, 29, [3, 3],
                id="should calculate human age when "
                   "(`cat_age`, `dog_age`) = (28, 29)"
            ),
            pytest.param(
                0, 0, [0, 0],
                id="should calculate human age when "
                   "`cat_age`, `dog_age` are zero"
            ),
            pytest.param(
                -5, -40, [0, 0],
                id="should calculate human age when "
                   "`cat_age`, `dog_age` are negative"
            ),
            pytest.param(
                219, 268, [50, 50],
                id="should calculate human age when "
                   "`cat_age`, `dog_age` are `really large numbers`"
            )
        ]
    )
    def test_calculate_human_age_correctly(
            self, cat_age, dog_age, human_age
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    @pytest.mark.parametrize(
        "args,expected_error",
        [
            pytest.param(
                ("test", "test"),
                TypeError,
                id="should raise `TypeError` when `cat_age` or `dog_age` "
                   "is not `int`"
            ),
            pytest.param(
                (5,),
                TypeError,
                id="should raise `TypeError` when only one parameter is given"
            ),
            pytest.param(
                tuple(),
                TypeError,
                id="should raise `TypeError` when no parameters given"
            )
        ]
    )
    def test_raising_errors_correctly(self, args, expected_error) -> None:
        with pytest.raises(expected_error):
            get_human_age(*args)
