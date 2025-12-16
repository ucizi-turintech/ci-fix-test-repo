"""Unit tests for calculator module."""

import pytest
from ci_fix_test_repo.calculator import add, subtract, multiply, divide


class TestCalculator:
    """Test cases for calculator functions."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 4
        assert add(10, 5) == 15

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-2, -3) == -5
        assert add(-10, 5) == -5

    def test_add_zero(self):
        """Test adding with zero."""
        assert add(5, 0) == 5
        assert add(0, -3) == -3

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert subtract(5, 3) == 1
        assert subtract(10, 5) == 5

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert subtract(-2, -3) == 1
        assert subtract(5, -3) == 8

    def test_subtract_zero(self):
        """Test subtracting zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 3) == -3

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(3, 4) == 11
        assert multiply(5, 2) == 10

    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, -3) == 0

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-2, 3) == -6
        assert multiply(-2, -3) == 6

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        assert divide(-10, 2) == -5
        assert divide(-9, -3) == 3

    def test_divide_by_zero(self):
        """Test dividing by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(10, 0)
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(-5, 0)

    def test_divide_float_result(self):
        """Test division resulting in float."""
        assert divide(7, 2) == 3.5
        assert divide(1, 3) == pytest.approx(0.3333333, rel=1e-6)

