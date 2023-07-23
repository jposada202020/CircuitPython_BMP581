# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bmp581

i2c = board.I2C()
bmp = bmp581.BMP581(i2c)

bmp.output_data_rate = bmp581.ODR240

while True:
    for output_data_rate in range(0, 32, 1):
        print("Current Output data rate setting: ", bmp.output_data_rate)
        for _ in range(10):
            print(f"Pressure: {bmp.pressure:.2f}kPa")
            print()
            time.sleep(0.5)
        bmp.output_data_rate = output_data_rate
