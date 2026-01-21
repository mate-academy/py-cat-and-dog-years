import pytest


from app.main import get_human_age


class TestAgesClasses:

    @pytest.mark.parametrize(
        "dog_age, cat_age, result",
        [pytest.param(0, 0, [0, 0]),
         pytest.param(14, 14, [0, 0]),
         pytest.param(28, 29, [3, 3]),
         pytest.param(15.1, 14.2, [4, 5]),
         pytest.param(14, 16, [0, 1]),
         pytest.param(16, 14, [1, 0])
         ]
    )
    def test_should_good_result(
            self,
            dog_age: int,
            cat_age: int,
            result: int
    ) -> None:
        wyn = get_human_age(dog_age, cat_age)
        assert wyn == result
