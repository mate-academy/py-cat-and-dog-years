from app.main import get_human_age
import pytest


class TestDogAge:
    @pytest.mark.parametrize(
        "age,result",
        [
            pytest.param(0, 0),
            pytest.param(14, 0),
            pytest.param(15, 1),
            pytest.param(23, 1),
            pytest.param(24, 2),
            pytest.param(27, 2),
            pytest.param(29, 3),
            pytest.param(100, 17)
        ]
    )
    def test_for_dog(self, age, result):

        assert get_human_age(0, age)[1] == result


class TestCatAge:
    @pytest.mark.parametrize(
        "age,result",
        [
            pytest.param(0, 0),
            pytest.param(14, 0),
            pytest.param(15, 1),
            pytest.param(23, 1),
            pytest.param(24, 2),
            pytest.param(27, 2),
            pytest.param(28, 3),
            pytest.param(100, 21)
        ]
    )
    def test_for_dog(self, age, result):

        assert get_human_age(age, 0)[0] == result
