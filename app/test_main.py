from app.main import get_human_age
import math


def test_get_human_age() -> None:
    assert math.isclose(
        get_human_age(0, 0)[0], 0.0, rel_tol=1e-9
    )
    assert math.isclose(
        get_human_age(0, 0)[1], 0.0, rel_tol=1e-9
    )
    assert math.isclose(
        get_human_age(10, 10)[0], 0.6666666666666666, rel_tol=1e-9
    )
    assert math.isclose(
        get_human_age(10, 10)[1], 0.6666666666666666, rel_tol=1e-9
    )
    assert math.isclose(
        get_human_age(14, 14)[0], 0.9333333333333333, rel_tol=1e-9
    )
    assert math.isclose(
        get_human_age(14, 14)[1], 0.9333333333333333, rel_tol=1e-9
    )
    assert math.isclose(
        get_human_age(15, 15)[0], 1.0, rel_tol=1e-9
    )
    assert math.isclose(
        get_human_age(15, 15)[1], 1.0, rel_tol=1e-9
    )
    assert math.isclose(
        get_human_age(23, 23)[0], 1.0, rel_tol=1e-9
    )
    assert math.isclose(
        get_human_age(23, 23)[1], 1.0, rel_tol=1e-9
    )
    assert math.isclose(
        get_human_age(24, 24)[0], 2.0, rel_tol=1e-9
    )
    assert math.isclose(
        get_human_age(24, 24)[1], 2.0, rel_tol=1e-9
    )
    assert math.isclose(
        get_human_age(27, 27)[0], 2.75, rel_tol=1e-9
    )
    assert math.isclose(
        get_human_age(27, 27)[1], 2.6, rel_tol=1e-9
    )
    assert math.isclose(
        get_human_age(28, 28)[0], 3.0, rel_tol=1e-9
    )
    assert math.isclose(
        get_human_age(28, 28)[1], 2.8, rel_tol=1e-9
    )
    assert math.isclose(
        get_human_age(100, 100)[0], 21.0, rel_tol=1e-9
    )
    assert math.isclose(
        get_human_age(100, 100)[1], 17.2, rel_tol=1e-9
    )


# Запуск тестов

if __name__ == "__main__":
    test_get_human_age()
    print("Все тесты пройдены успешно!")
