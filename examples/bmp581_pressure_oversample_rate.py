# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bmp581

i2c = board.I2C()
bmp = bmp581.BMP581(i2c)

bmp.pressure_oversample_rate = bmp581.OSR16

while True:
    for pressure_oversample_rate in bmp581.pressure_oversample_rate_values:
        print(
            "Current Pressure oversample rate setting: ", bmp.pressure_oversample_rate
        )
        for _ in range(10):
            print(f"Pressure: {bmp.pressure:.2f}kPa")
            print()
            time.sleep(0.5)
        bmp.pressure_oversample_rate = pressure_oversample_rate
