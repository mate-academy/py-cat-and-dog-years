import pytest

from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected",
                         [
                             pytest.param(0,
                                          0,
                                          [0, 0],
                                          id="test_bottom_boundary_zero_age"),
                             pytest.param(14,
                                          14,
                                          [0, 0],
                                          id="test_top_boundary_zero_age"),
                             pytest.param(15,
                                          15,
                                          [1, 1],
                                          id="test_bottom_boundary_first_age"),
                             pytest.param(23,
                                          23,
                                          [1, 1],
                                          id="test_top_boundary_first_age"),
                             pytest.param(24,
                                          24,
                                          [2, 2],
                                          id="test_boundary_second_age"),
                             pytest.param(27,
                                          27,
                                          [2, 2],
                                          id="test_top_boundary_second_age"),
                             pytest.param(28,
                                          28,
                                          [3, 2],
                                          id="test cat age less dog age"),
                             pytest.param(100,
                                          100,
                                          [21, 17],
                                          id="test cat age more dog age"),
                             pytest.param(-5,
                                          -10,
                                          [0, 0],
                                          id="data outside the normal age")
                         ]
                         )
def test_function(cat_age: int, dog_age: int, expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
