# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bmp581

i2c = board.I2C()  # uses board.SCL and board.SDA
bmp = bmp581.BMP581(i2c)

while True:
    print(f"Temperature {bmp.temperature:.2f}°C")
    print()
    time.sleep(1)
