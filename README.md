# Daisychaining-SN74HC595-MicroPython-Raspberry-Pi-Pico
3 different methods to daisy chain SN74HC595 shift bit registers using MicroPuthon on Raspberry Pi Pico

The file pico74hc595_3methods.py contains 3 different ways to raise outputs sequentially from 1 to 16. Once enabled, any given output remains high (until the reset pin disables all).

Method # 1 (mine) is a real hack, but it works.

Method # 2 (mine too) is very wordy, but easily understandable, and could easily be expanded to 3+ registers. All you need to do is some typing.

Method # 3 was generated by Microsoft Copilot. Very compact.

In order to daisychain n number of SN595's, wire up the first chip with the data pin (14) connected to the data output pin you chose to use on the Raspberry Pi Pico. Do the same for the latch pin (12), the clock pin (11) and the reset pin (10). VCC goes from pin(16) to the Pico's VBUS pin(40), Ground pin (8) to any GND pin on the Pico. To test whether or not working, connect 5mm or similar LEDs via 330 ohm resistors to pins 1 thru to 7 as well as pin 15. The other end of the LED goes to ground. Once that works, wire the second and subsequential chips to the very same output pins on the Pico, with the exception of the data pin (14). It gets wired to pin 9, sometimes labelled QH` of the preceding chip in the chain. Repeat for any other chip added to the chain.

If you get to probably 4+ chips, you might want to power the SN595's independently from a separate supply, with the ground tied to a Pico ground pin.
