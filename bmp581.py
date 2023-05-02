# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT
"""
`bmp581`
================================================================================

CircuitPython Driver for the Bosch BMP581 pressure sensor


* Author(s): Jose D. Montoya


"""

from micropython import const
from adafruit_bus_device import i2c_device
from adafruit_register.i2c_struct import ROUnaryStruct
from adafruit_register.i2c_bits import RWBits, ROBits

try:
    from busio import I2C
except ImportError:
    pass

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/jposada202020/CircuitPython_BMP581.git"

_REG_WHOAMI = const(0x01)
_OSR_CONF = const(0x36)
_ODR_CONFIG = const(0x37)


# Power Modes
STANDBY = const(0x00)
NORMAL = const(0x01)
FORCED = const(0x02)
NON_STOP = const(0x03)
power_mode_values = (STANDBY, NORMAL, FORCED, NON_STOP)


# Oversample Rate
OSR1 = const(0x00)
OSR2 = const(0x01)
OSR4 = const(0x02)
OSR8 = const(0x03)
OSR16 = const(0x04)
OSR32 = const(0x05)
OSR64 = const(0x06)
OSR128 = const(0x07)
pressure_oversample_rate_values = (OSR1, OSR2, OSR4, OSR8, OSR16, OSR32, OSR64, OSR128)


class BMP581:
    """Driver for the BMP581 Sensor connected over I2C.

    :param ~busio.I2C i2c_bus: The I2C bus the BMP581 is connected to.
    :param int address: The I2C device address. Defaults to :const:`0x47`

    :raises RuntimeError: if the sensor is not found

    **Quickstart: Importing and using the device**

    Here is an example of using the :class:`BMP581` class.
    First you will need to import the libraries to use the sensor

    .. code-block:: python

        import board
        import bmp581

    Once this is done you can define your `board.I2C` object and define your sensor object

    .. code-block:: python

        i2c = board.I2C()  # uses board.SCL and board.SDA
        bmp = bmp581.BMP581(i2c)

    Now you have access to the attributes

    .. code-block:: python

        press = bmp.pressure

    """

    _device_id = ROUnaryStruct(_REG_WHOAMI, "B")

    _power_mode = RWBits(2, _ODR_CONFIG, 0)
    _pressure_oversample_rate = RWBits(3, _OSR_CONF, 3)

    _temperature = ROBits(24, 0x1D, 0, 3)
    _pressure = ROBits(24, 0x20, 0, 3)

    def __init__(self, i2c_bus: I2C, address: int = 0x47) -> None:
        self.i2c_device = i2c_device.I2CDevice(i2c_bus, address)

        if self._device_id != 0x50:
            raise RuntimeError("Failed to find BMP581")

        self._power_mode = NORMAL

    @property
    def power_mode(self) -> str:
        """
        Sensor power_mode

        +-----------------------------+------------------+
        | Mode                        | Value            |
        +=============================+==================+
        | :py:const:`bmp581.STANDBY`  | :py:const:`0x00` |
        +-----------------------------+------------------+
        | :py:const:`bmp581.NORMAL`   | :py:const:`0x01` |
        +-----------------------------+------------------+
        | :py:const:`bmp581.FORCED`   | :py:const:`0x02` |
        +-----------------------------+------------------+
        | :py:const:`bmp581.NON_STOP` | :py:const:`0X03` |
        +-----------------------------+------------------+
        """
        values = (
            "STANDBY",
            "NORMAL",
            "FORCED",
            "NON_STOP",
        )
        return values[self._power_mode]

    @power_mode.setter
    def power_mode(self, value: int) -> None:
        if value not in power_mode_values:
            raise ValueError("Value must be a valid power_mode setting")
        self._power_mode = value

    @property
    def pressure_oversample_rate(self) -> str:
        """
        Sensor pressure_oversample_rate

        +---------------------------+------------------+
        | Mode                      | Value            |
        +===========================+==================+
        | :py:const:`bmp581.OSR1`   | :py:const:`0x00` |
        +---------------------------+------------------+
        | :py:const:`bmp581.OSR2`   | :py:const:`0x01` |
        +---------------------------+------------------+
        | :py:const:`bmp581.OSR4`   | :py:const:`0x02` |
        +---------------------------+------------------+
        | :py:const:`bmp581.OSR8`   | :py:const:`0x03` |
        +---------------------------+------------------+
        | :py:const:`bmp581.OSR16`  | :py:const:`0x04` |
        +---------------------------+------------------+
        | :py:const:`bmp581.OSR32`  | :py:const:`0x05` |
        +---------------------------+------------------+
        | :py:const:`bmp581.OSR64`  | :py:const:`0x06` |
        +---------------------------+------------------+
        | :py:const:`bmp581.OSR128` | :py:const:`0x07` |
        +---------------------------+------------------+
        """
        values = (
            "OSR1",
            "OSR2",
            "OSR4",
            "OSR8",
            "OSR16",
            "OSR32",
            "OSR64",
            "OSR128",
        )
        return values[self._pressure_oversample_rate]

    @pressure_oversample_rate.setter
    def pressure_oversample_rate(self, value: int) -> None:
        if value not in pressure_oversample_rate_values:
            raise ValueError("Value must be a valid pressure_oversample_rate setting")
        self._pressure_oversample_rate = value

    @property
    def temperature(self) -> float:
        """
        The temperature sensor in C
        :return: Temperature
        """
        raw_temp = self._temperature

        return self._twos_comp(raw_temp, 24) / 2**16

    @property
    def pressure(self) -> float:
        """
        The sensor pressure in kPa
        :return: Pressure in kPa
        """
        raw_pressure = self._pressure

        return self._twos_comp(raw_pressure, 24) / 2**6 / 1000

    @staticmethod
    def _twos_comp(val: int, bits: int) -> int:

        if val & (1 << (bits - 1)) != 0:
            return val - (1 << bits)
        return val
