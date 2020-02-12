# Test the main controller logic

import unittest
import facility
import gpiozero
import main
from mock import patch, MagicMock

class MainTest(unittest.TestCase):

    @patch("facility.getTemp")
    @patch("main.SET_POINT", 70)
    def test_tempDiff_shouldReturnPositiveValue(self, mock):
        mock.return_value = 72
        self.assertEqual(2, main.tempDiff())
        mock.assert_called_once()

    @patch("facility.getTemp")
    @patch("main.SET_POINT", 70)
    def test_tempDiff_shouldReturnNegativeValue(self, mock):
        mock.return_value = 68
        self.assertEqual(-2, main.tempDiff())
        mock.assert_called_once()

    @patch("facility.getTemp")
    @patch("main.SET_POINT", 70)
    def test_tempDiff_shouldReturnZero(self, mock):
        mock.return_value = 70
        self.assertEqual(0, main.tempDiff())
        mock.assert_called_once()

    @patch("facility.getTemp")
    @patch("main.SET_POINT", 73)
    @patch("main.DELTA", 5)
    def test_shouldEnableHeater_shouldReturnTrueWhenTooCold(self, mock):
        mock.return_value = 67
        self.assertTrue(main.shouldEnableHeater())
        mock.assert_called_once()

    @patch("facility.getTemp")
    @patch("main.SET_POINT", 73)
    @patch("main.DELTA", 5)
    def test_shouldEnableHeater_shouldReturnFalseWithinDelta(self, mock):
        mock.return_value = 68
        self.assertFalse(main.shouldEnableHeater())
        mock.assert_called_once()

    @patch("facility.getTemp")
    @patch("main.SET_POINT", 73)
    @patch("main.DELTA", 5)
    def test_shouldEnableHeater_shouldReturnFalseWhenTooWarm(self, mock):
        mock.return_value = 78
        self.assertFalse(main.shouldEnableHeater())
        mock.assert_called_once()
