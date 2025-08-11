import pytest
from app.main import get_human_age


class TestBoundaryCatDogAge:
    @pytest.mark.parametrize("cat_age, dog_age, expected_array",
                             [
                                 pytest.param(
                                     0, 0, [0, 0],
                                     id="cat and dog age equal 0 when human age 0"),
                                 pytest.param(
                                     14, 14, [0, 0],
                                     id="cat and dog age equal 0 when human age 14"),
                                 pytest.param(
                                     15, 15, [1, 1],
                                     id="cat and dog age equal 1 when human age 15"),
                                 pytest.param(
                                     23, 23, [1, 1],
                                     id="cat and dog age equal 1 when human age 23"),
                                 pytest.param(
                                     24, 24, [2, 2],
                                     id="cat and dog age equal 2 when human age 24"),
                                 pytest.param(
                                     27, 27, [2, 2],
                                     id="cat and dog age equal 2 when human age 27"),
                                 pytest.param(
                                     28, 28, [3, 2],
                                     id="cat age equal 3, dog age equal 2  when human age 28"),
                                 pytest.param(
                                     29, 29, [3, 3],
                                     id="cat and dog age equal 3 when human age 29"),

                             ]
                             )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_array: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_array
