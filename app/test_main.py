import pytest

from app.main import get_human_age


class TestHumanAgeCalculate:

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            pytest.param(0, 0, [0, 0],
                         id="should add zeros when cat_dog just born"),
            pytest.param(15, 15, [1, 1], id="should add one year young"),
            pytest.param(23, 23, [1, 1], id="should add one year elderly"),
            pytest.param(24, 24, [2, 2], id="should add two year"),
            pytest.param(28, 28, [3, 2], id="should add three year"),
            pytest.param(100, 100, [21, 17], id="should add many years"),
        ]
    )
    def test_modify(self, cat_age: int, dog_age: int, expected: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected


class TestRaisingErrors:

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            pytest.param("12", 12, ValueError,
                         id="should raise error if arguments Not integer"),
            pytest.param(-12, 12, ValueError,
                         id="should raise error if arguments Negative"),
            pytest.param(112, 12, ValueError,
                         id="should raise error if arguments Very big"),
        ]
    )
    def test_raising_errors_correctly(self, cat_age: int, dog_age: int,
                                      expected_error:
                                      type[ValueError]) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
