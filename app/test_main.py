from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(0, 0, [0, 0],
                     id="checking value = 0"),
        pytest.param(14, 14, [0, 0],
                     id="checking limit value = 14, "
                        "equivalence class 0 - 14"),
        pytest.param(15, 15, [1, 1],
                     id="checking limit value = 15, "
                        "equivalence class 15 - 23"),
        pytest.param(23, 23, [1, 1],
                     id="checking limit value = 23, "
                        "equivalence class 15 - 23"),
        pytest.param(24, 24, [2, 2],
                     id="checking limit value = 24, "
                        "equivalence class 24 - 27"),
        pytest.param(27, 27, [2, 2],
                     id="checking limit value = 27, "
                        "equivalence class 24 - 27"),
        pytest.param(28, 28, [3, 2],
                     id="checking limit value = 28, "
                        "equivalence class 28 - 31"),
        pytest.param(100, 100, [21, 17],
                     id="checking value = 100")
    ]
)
def test_get_human_age_for_different_equivalence_class(
        cat_age: int,
        dog_age: int,
        result: list[int]) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), (f"Cat age: {cat_age} "
        f"and Dog age: {dog_age} "
        f"should be equal to next list {result}")
