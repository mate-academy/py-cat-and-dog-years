import pytest
from app.main import get_human_age


class TestBoundaryCatDogAge:
    @pytest.mark.parametrize("cat_age, dog_age, expected_array",
                             [
                                 pytest.param(
                                     0, 0, [0, 0],
                                     id="both 0 when human age 0"
                                 ),
                                 pytest.param(
                                     14, 14, [0, 0],
                                     id="both 0 when human age 14"
                                 ),
                                 pytest.param(
                                     15, 0, [1, 0],
                                     id="cat age 1 when human age 15"
                                 ),
                                 pytest.param(
                                     0, 15, [0, 1],
                                     id="dog age 1 when human age 15"
                                 ),
                                 pytest.param(
                                     23, 0, [1, 0],
                                     id="cat age 1 when human age 23"
                                 ),
                                 pytest.param(
                                     0, 23, [0, 1],
                                     id="dog age 1 when human age 23"
                                 ),
                                 pytest.param(
                                     24, 0, [2, 0],
                                     id="cat age 2 when human age 24"
                                 ),
                                 pytest.param(
                                     0, 24, [0, 2],
                                     id="dog age 2 when human age 24"
                                 ),
                                 pytest.param(
                                     27, 0, [2, 0],
                                     id="cat age 2 when human age 27"
                                 ),
                                 pytest.param(
                                     0, 27, [0, 2],
                                     id="dog age 2 when human age 27"
                                 ),
                                 pytest.param(
                                     28, 0, [3, 0],
                                     id="cat age 3 when human age 28"
                                 ),
                                 pytest.param(
                                     0, 28, [0, 2],
                                     id="dog age 2 when human age 28"
                                 ),
                                 pytest.param(
                                     29, 0, [3, 0],
                                     id="cat age 3 when human age 29"
                                 ),
                                 pytest.param(
                                     0, 29, [0, 3],
                                     id="dog age 3 when human age 29"
                                 ),
                                 pytest.param(
                                     100, 100, [21, 17],
                                     id="cat 21, dog 17  when human age 28"
                                 ),
                             ]
                             )
    def test_correct_conversion(
            self,
            cat_age: int,
            dog_age: int,
            expected_array: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_array


class TestValueErrorCatDogAge:
    @pytest.mark.parametrize("cat_age, dog_age", [
        pytest.param(
            -5, 5,
            id="cat age must be greater than 0"
        ),
        pytest.param(
            5, -5,
            id="dog age must be greater than 0"
        ),
    ])
    def test_negative_ages_raise_value_error(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        with pytest.raises(ValueError):
            get_human_age(cat_age, dog_age)


class TestTypeErrorCatDogAge:
    @pytest.mark.parametrize("cat_age, dog_age", [
        pytest.param(
            2.5, 5,
            id="cat age must be int not float"
        ),
        pytest.param(
            10, 3.7,
            id="dog age must be int not float"
        ),
        pytest.param(
            "15", 20,
            id="cat age must be int not str"
        ),
        pytest.param(
            20, "15",
            id="dog age must be int not str"
        ),
        pytest.param(
            None, 10,
            id="cat age must be int not None"
        ),
        pytest.param(
            10, None,
            id="dog age must be int not None"
        ),
    ])
    def test_invalid_type_raises_type_error(
            self,
            cat_age : int,
            dog_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
