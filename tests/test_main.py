import pytest

from contextlib import nullcontext as does_not_raise
from src.main import Calculator


@pytest.mark.parametrize("x, y, res, expectation",
[
    (1, 2, 0.5, does_not_raise()),
    (4, 2, 2, does_not_raise()),
    (3, 2, 1.5, does_not_raise()),
    (3, '3', 1, pytest.raises(TypeError, match="^Both arguments should be numeric$")),
    (5, 0, 5, pytest.raises(ZeroDivisionError, match="^Cannot divide by zero$")),
    ('5', 2, 2.5, pytest.raises(TypeError, match="^Both arguments should be numeric$")),
    ('a', 3, 2, pytest.raises(TypeError, match="^Both arguments should be numeric$")),
    (10, "a", 2, pytest.raises(TypeError, match="^Both arguments should be numeric$"))
])
def test_divide(x, y, res, expectation):
    with expectation:
        assert Calculator().divide(x, y) == res


@pytest.mark.parametrize('x, y, res, expectation',
[
    (3, 2, 5, does_not_raise()),
    (9, 3, 12, does_not_raise()),
    (0.2, 0.3, 0.5, does_not_raise()),
    ('2', 3, 6, pytest.raises(TypeError, match="^Both arguments should be numeric$")),
    (4, '2', 2, pytest.raises(TypeError, match="^Both arguments should be numeric$")),
    ('a', 2, 2, pytest.raises(TypeError, match="^Both arguments should be numeric$")),
    (4, 'a', 4, pytest.raises(TypeError, match="^Both arguments should be numeric$"))
])
def test_add(x, y, res, expectation):
    with expectation:
        assert Calculator().add(x, y) == res


@pytest.mark.parametrize("x, y, res, expectation",
[
    (2, 0, 0, does_not_raise()),
    (10, 10, 100, does_not_raise()),
    (11, 11, 121, does_not_raise()),
    ('2', 3, 6, pytest.raises(TypeError, match="^Both arguments should be numeric$")),
    (4, '2', 8, pytest.raises(TypeError, match="^Both arguments should be numeric$")),
    ('a', 2, 2, pytest.raises(TypeError, match="^Both arguments should be numeric$")),
    (4, 'a', 4, pytest.raises(TypeError, match="^Both arguments should be numeric$"))
])
def test_mult(x, y, res, expectation):
    with expectation:
        assert Calculator().mult(x, y) == res


@pytest.mark.parametrize("x, y, res, expectation",
[
    (10, 0, 10, does_not_raise()),
    (111, 112, -1, does_not_raise()),
    (105, 2.5, 102.5, does_not_raise()),
    ('4', 2, 2, pytest.raises(TypeError, match="^Both arguments should be numeric$")),
    (4, '2', 2, pytest.raises(TypeError, match="^Both arguments should be numeric$")),
    ('a', 1, 2, pytest.raises(TypeError, match="^Both arguments should be numeric$")),
    (5, 'f', 2, pytest.raises(TypeError, match="^Both arguments should be numeric$"))
])
def test_subtract(x, y, res, expectation):
    with expectation:
        assert Calculator().subtract(x, y) == res
