from app.main import get_human_age
import pytest


class TestEdge:
    @pytest.mark.parametrize(
        "init_data_cat, init_data_dog, expected_cat, expected_dog",
        [
            # Test 1
            pytest.param(0,

                         0,
                         0,
                         0,
                         id="Return 0 test"
                         ),

            # Test 2
            pytest.param(100,
                         100,
                         21,
                         17,
                         id="Return big data test"
                         ),

            # Test 3
            pytest.param(
                14,
                14,
                0,
                0,
                id="Return 0, 0 in edge 14, 14"
            ),

            # Test 4
            pytest.param(
                15,
                15,
                1,
                1,
                id="Return 1, 1 in edge 15, 15"

            ),

            # Test 5
            pytest.param(
                23,
                23,
                1,
                1,
                id="Return 1, 1 in edge 23, 23"

            ),

            # Test 6
            pytest.param(
                24,
                24,
                2,
                2,
                id="Return 2, 2 in edge 24, 24"

            ),

            # Test 7
            pytest.param(
                27,
                27,
                2,
                2,
                id="Return 2, 2 in edge 27, 27"

            ),

            # Test 8
            pytest.param(
                28,
                28,
                3,
                2,
                id="Return 3, 2 in edge 28, 28"

            ),

        ]
    )
    def test_data(self,
                  init_data_cat: int,
                  init_data_dog: int,
                  expected_cat: int,
                  expected_dog: int) -> None:
        assert get_human_age(
            init_data_cat,
            init_data_dog) == [expected_cat, expected_dog]

    @pytest.mark.parametrize(
        "init_cat, init_dog, expect_error",
        [
            pytest.param(
                [],
                "",
                TypeError,
                id="Value test 1 "

            ),
            pytest.param(
                "",
                [],
                TypeError,
                id="Value test 2"

            ),

        ]
    )
    def test_raising_error(self,
                           init_cat,
                           init_dog,
                           expect_error) -> None:
        with pytest.raises(expect_error):
            get_human_age(init_cat, init_dog)
