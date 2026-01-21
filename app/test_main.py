from app.main import get_human_age


function_calls = [
            get_human_age(0, 0),
            get_human_age(14, 14),
            get_human_age(15, 15),
            get_human_age(23, 23),
            get_human_age(24, 24),
            get_human_age(27, 27),
            get_human_age(28, 28),
            get_human_age(100, 100)
        ]


class TestGetHumanAgeClass:
    def test_len_should_be_equal_to_2(self):
        for call in function_calls:
            assert len(call) == 2

    def test_1(self):
        assert get_human_age(0, 0) == [0, 0]

    def test_2(self):
        assert get_human_age(14, 14) == [0, 0]

    def test_3(self):
        assert get_human_age(15, 15) == [1, 1]

    def test_4(self):
        assert get_human_age(23, 23) == [1, 1]

    def test_5(self):
        assert get_human_age(24, 24) == [2, 2]

    def test_6(self):
        assert get_human_age(27, 27) == [2, 2]

    def test_7(self):
        assert get_human_age(28, 28) == [3, 2]

    def test_8(self):
        assert get_human_age(100, 100) == [21, 17]
