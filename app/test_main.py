from app.main import get_human_age, convert_to_human


class TestGetHumanAge:
    def test_should_also_take_float_as_argumen(self):
        result = get_human_age(15.3, 15)
        assert result == [1, 1]

    def test_should_be_equal_to_zero_when_age_less_then_15(self):
        result = get_human_age(14, 14)
        assert result == [0, 0]

    def test_should_be_equal_to_1_when_age_less_then_24(self):
        result = get_human_age(23, 23)
        assert result == [1, 1]

    def test_should_return_different_values_when_age_28(self):
        result = get_human_age(28, 28)
        assert result == [3, 2]


class TestConvertToHuman:
    def test_should_also_take_float_as_argumen(self):
        result = convert_to_human(17, 15, 9.4, 4.2)
        assert result == 1
