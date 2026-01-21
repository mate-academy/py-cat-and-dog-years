import pytest


from app.main import get_human_age


class TestCatsDogsClass:
    @pytest.mark.parametrize("cat,dog,expected", [
        (-1, -1, [0, 0]),
        (0, 0, [0, 0]),
        (5, 5, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (17, 17, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (25, 25, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17])
    ])
    def test_age_must_be_equal_to_expected(self,
                                           cat: int,
                                           dog: int,
                                           expected: list) -> None:
        assert get_human_age(cat, dog) == expected

    @pytest.mark.parametrize("cat,dog", [
        ("10", "10"),
        ([10], [10]),
        ({"10": 10}, {"10": 10}),
        ((10, ), (10, ))
    ])
    def test_receive_errors_when_type_incorrect(self,
                                                cat: int,
                                                dog: int) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat, dog)
