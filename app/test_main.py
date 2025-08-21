import pytest
from app.main import get_human_age  # ajuste o import conforme seu projeto

def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]

def test_before_first_threshold() -> None:
    # menos que 15 anos de gato/cachorro
    assert get_human_age(14, 14) == [0, 0]

def test_first_threshold() -> None:
    # exatamente 15 anos
    assert get_human_age(15, 15) == [1, 1]

def test_after_first_threshold() -> None:
    # entre 15 e 24 anos
    assert get_human_age(23, 23) == [1, 1]
    assert get_human_age(24, 24) == [2, 2]

def test_middle_values() -> None:
    assert get_human_age(27, 27) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]

def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]

def test_varied_values() -> None:
    # valores diferentes de gato e cachorro
    assert get_human_age(15, 24) == [1, 2]
    assert get_human_age(24, 15) == [2, 1]
    assert get_human_age(0, 20) == [0, 2]
    assert get_human_age(20, 0) == [2, 0]
