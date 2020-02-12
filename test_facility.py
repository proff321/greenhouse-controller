# Test file for the facility module

import unittest
import facility
import gpiozero
from mock import patch, MagicMock

class FacilityTest(unittest.TestCase):
    
    def test_shouldReturnTemp(self):
        self.assertEquals(12, facility.getTemp())

    @patch("gpiozero.OutputDevice") 
    def test_shouldTurnFanOn(self, mock_class):
	facility.fanOn()

	mock_class.assert_called_once_with(facility.FAN_PIN)
	mock_class().on.assert_called_once()

    @patch("gpiozero.OutputDevice") 
    def test_shouldTurnFanOff(self, mock_class):
	facility.fanOff()

	mock_class.assert_called_once_with(facility.FAN_PIN)
	mock_class().off.assert_called_once()

    @patch("gpiozero.OutputDevice") 
    def test_shouldTurnLightOn(self, mock_class):
	facility.lightOn()

	mock_class.assert_called_once_with(facility.LIGHT_PIN)
	mock_class().on.assert_called_once()

    @patch("gpiozero.OutputDevice") 
    def test_shouldTurnLightOff(self, mock_class):
	facility.lightOff()

	mock_class.assert_called_once_with(facility.LIGHT_PIN)
	mock_class().off.assert_called_once()

    @patch("gpiozero.OutputDevice") 
    def test_shouldTurnHeaterOn(self, mock_class):
	facility.heaterOn()

	mock_class.assert_called_once_with(facility.HEATER_PIN)
	mock_class().on.assert_called_once()

    @patch("gpiozero.OutputDevice") 
    def test_shouldTurnHeaterOff(self, mock_class):
	facility.heaterOff()

	mock_class.assert_called_once_with(facility.HEATER_PIN)
	mock_class().off.assert_called_once()
