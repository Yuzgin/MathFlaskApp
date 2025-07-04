import unittest
from flask_math.calculation import bode

class TestBodeFunction(unittest.TestCase):
    """Unit tests for bode() function that generates Bode plots and calculates margins."""

    def test_basic_lowpass(self):
        """Test a standard 2nd-order low-pass transfer function."""
        formula = "1 / (s**2 + 2*s + 1)"
        lower_end, upper_end = 0, 2  # 1 to 100 rad/s
        # Should not throw error, should return a Flask response with image content.
        response = bode.bode(formula, lower_end, upper_end)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'image/png')
        self.assertGreater(int(response.headers['Content-Length']), 0)

    def test_highpass(self):
        """Test a high-pass transfer function for correct response."""
        formula = "s / (s + 1)"
        response = bode.bode(formula, 0, 2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'image/png')

    def test_gain_margin_and_phase_margin(self):
        """Test that Bode plot for a lead compensator calculates margins without error."""
        formula = "(s + 2)/(s + 1)"
        response = bode.bode(formula, -1, 2)
        self.assertEqual(response.status_code, 200)
        # (Visual check for margin lines should be done manually or via image diff tools.)

    def test_invalid_formula(self):
        """Test that an invalid formula input returns an error or valid response."""
        with self.assertRaises(Exception):
            bode.bode("1 / (", 0, 2)
        with self.assertRaises(Exception):
            bode.bode("not_a_formula", 0, 2)

    def test_extremely_small_range(self):
        """Test Bode plot for a very small frequency range."""
        formula = "1 / (s + 1)"
        response = bode.bode(formula, 0, 0.01)  # ~1 to 1.023 rad/s
        self.assertEqual(response.status_code, 200)

    def test_extremely_large_range(self):
        """Test Bode plot for a very large frequency range."""
        formula = "1 / (s + 1)"
        response = bode.bode(formula, 0, 6)  # 1 to 1,000,000 rad/s
        self.assertEqual(response.status_code, 200)

    def test_non_causal_transfer_function(self):
        """Test transfer function where numerator degree > denominator."""
        formula = "(s**3 + 1) / (s + 1)"
        response = bode.bode(formula, 0, 2)
        self.assertEqual(response.status_code, 200)

    def test_constant_transfer_function(self):
        """Test transfer function with no s (constant system)."""
        formula = "5"
        response = bode.bode(formula, 0, 2)
        self.assertEqual(response.status_code, 200)

    def test_zero_transfer_function(self):
        """Test edge case with zero transfer function."""
        formula = "0"
        response = bode.bode(formula, 0, 2)
        self.assertEqual(response.status_code, 200)

    def test_improper_input_types(self):
        """Test non-string formula and non-numeric bounds."""
        with self.assertRaises(Exception):
            bode.bode(None, 0, 2)
        with self.assertRaises(Exception):
            bode.bode("1 / (s + 1)", "low", "up")

if __name__ == '__main__':
    unittest.main()