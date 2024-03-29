"""
The MIT License (MIT)

Copyright (c) 2019 Dave Astels for Adafruit Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

# pylint: disable=invalid-name

# Wait for a falling transition on the clock (signal 1)
# When it's seen, display the values of signal 2-5
# Denmonstrates debouncing a lambda predicate

import time
from adafruit_crickit import crickit
from adafruit_debouncer import Debouncer

ss = crickit.seesaw

def make_criket_signal_debouncer(pin):
    """Return a lambda to read the specified pin"""
    ss.pin_mode(pin, ss.INPUT_PULLUP)
    return Debouncer(lambda: ss.digital_read(pin))

# Two buttons are pullups, connect to ground to activate
clock = make_criket_signal_debouncer(crickit.SIGNAL1)
signal_2 = make_criket_signal_debouncer(crickit.SIGNAL2)
signal_3 = make_criket_signal_debouncer(crickit.SIGNAL3)
signal_4 = make_criket_signal_debouncer(crickit.SIGNAL4)
signal_5 = make_criket_signal_debouncer(crickit.SIGNAL5)

while True:
    clock.update()
    signal_2.update()
    signal_3.update()
    signal_4.update()
    signal_5.update()

    if clock.fell:
        print('%u %u %u %u' % (signal_2.value, signal_3.value, signal_4.value, signal_5.value))

    time.sleep(0.1)
