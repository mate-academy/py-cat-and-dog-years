import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_human_age",
        [
            pytest.param(
                28, 28, [3, 2],
                id="cat and dog years must be calculated in different ways"),
            pytest.param(
                0, 0, [0, 0],
                id="should return array with zeros when input is zeros"),
            pytest.param(
                8, 14, [0, 0],
                id="should return array with zeros when years less then 15"),
            pytest.param(
                15, 15, [1, 1],
                id="first 15 animal years must give 1 human year"),
            pytest.param(
                24, 24, [2, 2],
                id="next 9 animal years after 15 must give 1 human year"),
            pytest.param(
                27, 27, [2, 2],
                id="less then 9 animal years after 15 not give human years"),
            pytest.param(
                78, 15, [15, 1],
                id="should use cat and dog years separately"),
            pytest.param(
                -10, -20, [0, 0],
                id="should return array with zeros when input is negative"),
            pytest.param(
                True, False, [0, 0],
                id="should return array with zeros when input type is 'bool'"),
            pytest.param(
                123456789, 987654321, [30864193, 197530861],
                id="should work without errors when animal age is too huge"),
            pytest.param(
                28.0, 28.0, [3, 2],
                id="must return correct value when animal age type is 'float'")
        ]
    )
    def test_get_human_age_correctly(
        self,
        cat_age: int,
        dog_age: int,
        expected_human_age: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_human_age

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            pytest.param(
                "28", "28",
                id="must raise 'TypeError' when animal age type is 'string'"),
            pytest.param(
                [28], [28],
                id="must raise 'TypeError' when animal age type is 'list'"),
            pytest.param(
                None, None,
                id="must raise 'TypeError' when animal age type is 'None'"),
        ]
    )
    def test_raising_errors_correctly(
            self,
            cat_age: int,
            dog_age: int,
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
