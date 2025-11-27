import unittest
from numbers import isprime, isperfect


class TestIsPrime(unittest.TestCase):
    """Test cases for the isprime function."""

    def test_isprime_with_small_primes(self):
        """Test isprime with small prime numbers."""
        self.assertTrue(isprime(2))
        self.assertTrue(isprime(3))
        self.assertTrue(isprime(5))
        self.assertTrue(isprime(7))
        self.assertTrue(isprime(11))

    def test_isprime_with_large_primes(self):
        """Test isprime with larger prime numbers."""
        self.assertTrue(isprime(97))
        self.assertTrue(isprime(101))
        self.assertTrue(isprime(307))

    def test_isprime_with_non_primes(self):
        """Test isprime with non-prime numbers."""
        self.assertFalse(isprime(4))
        self.assertFalse(isprime(6))
        self.assertFalse(isprime(8))
        self.assertFalse(isprime(9))
        self.assertFalse(isprime(10))

    def test_isprime_with_composite_numbers(self):
        """Test isprime with composite numbers."""
        self.assertFalse(isprime(100))
        self.assertFalse(isprime(144))
        self.assertFalse(isprime(200))

    def test_isprime_with_one(self):
        """Test isprime with 1 (not a prime)."""
        self.assertFalse(isprime(1))

    def test_isprime_with_zero(self):
        """Test isprime with 0 (not a prime)."""
        self.assertFalse(isprime(0))

    def test_isprime_with_negative_numbers(self):
        """Test isprime with negative numbers."""
        self.assertFalse(isprime(-1))
        self.assertFalse(isprime(-5))
        self.assertFalse(isprime(-10))


class TestIsPerfect(unittest.TestCase):
    """Test cases for the isperfect function."""

    def test_isperfect_with_perfect_numbers(self):
        """Test isperfect with known perfect numbers."""
        self.assertTrue(isperfect(6))   # 6 = 1 + 2 + 3
        self.assertTrue(isperfect(28))  # 28 = 1 + 2 + 4 + 7 + 14

    def test_isperfect_with_non_perfect_numbers(self):
        """Test isperfect with non-perfect numbers."""
        self.assertFalse(isperfect(2))
        self.assertFalse(isperfect(4))
        self.assertFalse(isperfect(5))
        self.assertFalse(isperfect(10))
        self.assertFalse(isperfect(12))
        self.assertFalse(isperfect(20))
        self.assertFalse(isperfect(27))

    def test_isperfect_with_one(self):
        """Test isperfect with 1 (not a perfect number)."""
        self.assertFalse(isperfect(1))

    def test_isperfect_with_zero(self):
        """Test isperfect with 0 (not a perfect number)."""
        self.assertFalse(isperfect(0))

    def test_isperfect_with_negative_numbers(self):
        """Test isperfect with negative numbers."""
        self.assertFalse(isperfect(-1))
        self.assertFalse(isperfect(-6))
        self.assertFalse(isperfect(-28))

    def test_isperfect_with_abundant_numbers(self):
        """Test isperfect with abundant numbers (sum of divisors > number)."""
        self.assertFalse(isperfect(12))  # divisors: 1, 2, 3, 4, 6 = 16 > 12
        self.assertFalse(isperfect(18))  # divisors: 1, 2, 3, 6, 9 = 21 > 18
        # divisors: 1, 2, 3, 4, 6, 8, 12 = 36 > 24
        self.assertFalse(isperfect(24))

    def test_isperfect_with_deficient_numbers(self):
        """Test isperfect with deficient numbers (sum of divisors < number)."""
        self.assertFalse(isperfect(7))   # divisors: 1 = 1 < 7
        self.assertFalse(isperfect(15))  # divisors: 1, 3, 5 = 9 < 15
        self.assertFalse(isperfect(25))  # divisors: 1, 5 = 6 < 25


if __name__ == '__main__':
    unittest.main()
