from app.main import get_human_age


def test_output_type():
    assert type(get_human_age(1, 1)) == list

    is_int = True
    if type(get_human_age(1, 1)) == list:
        for i in get_human_age(30, 31):
            if not type(i) == int:
                is_int = False
                break

    assert is_int


def test_zero_age():
    assert get_human_age(0, 0) == [0, 0]


def test_age_less_than_15():
    expected = {
        (2, 2): [0, 0],
        (10, 10): [0, 0],
        (14, 14): [0, 0]
    }
    values = [(2, 2), (10, 10), (14, 14)]

    actual = {item[1]: get_human_age(values[item[0]][0], values[item[0]][1])
              for item in enumerate(values)}

    assert actual == expected


def test_age_less_than_24():
    expected = {
        (15, 15): [1, 1],
        (20, 20): [1, 1],
        (23, 23): [1, 1]
    }
    values = [(15, 15), (20, 20), (23, 23)]

    actual = {item[1]: get_human_age(values[item[0]][0], values[item[0]][1])
              for item in enumerate(values)}

    assert actual == expected


def test_age_more_than_24_for_cat():
    expected = {
        (24, 0): [2, 0],
        (28, 0): [3, 0],
        (108, 0): [23, 0]
    }
    values = [(24, 0), (28, 0), (108, 0)]

    actual = {item[1]: get_human_age(values[item[0]][0], values[item[0]][1])
              for item in enumerate(values)}

    assert actual == expected


def test_age_more_than_24_for_dog():
    expected = {
        (0, 24): [0, 2],
        (0, 29): [0, 3],
        (0, 114): [0, 20]
    }
    values = [(0, 24), (0, 29), (0, 114)]

    actual = {item[1]: get_human_age(values[item[0]][0], values[item[0]][1])
              for item in enumerate(values)}

    assert actual == expected


def test_random_age():
    expected = {
        (2, 1022): [0, 201],
        (2023, 3): [501, 0],
        (1000, 1000): [246, 197]
    }
    values = [(2, 1022), (2023, 3), (1000, 1000)]

    actual = {item[1]: get_human_age(values[item[0]][0], values[item[0]][1])
              for item in enumerate(values)}

    assert actual == expected
