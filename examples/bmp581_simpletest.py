# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bmp581

i2c = board.I2C()
bmp = bmp581.BMP581(i2c)

while True:
    print(f"Pressure: {bmp.pressure:.2f}kPa")
    print()
    time.sleep(0.5)
