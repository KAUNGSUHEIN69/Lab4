# System imports
import time
from time import sleep

# Local imports
from hal import hal_input_switch as switch  # Import hal_input_switch with an alias
from hal import hal_led as led  # Import the LED module

# Function to blink the LED
def blink_led():
    led.init()  # Initialize the LED

    try:
        while True:
            if switch.read_slide_switch() == 1:  # If the switch is in the left position
                # Blink LED at 5 Hz
                led.set_output(0, 1)  # Turn on the LED
                sleep(0.1)  # 0.1 seconds on (5 Hz)
                led.set_output(0, 0)  # Turn off the LED
                sleep(0.1)  # 0.1 seconds off
            else:  # If the switch is in the right position
                # Blink LED at 10 Hz for 5 seconds
                start_time = time.time()  # Record the current time
                while (time.time() - start_time) < 5:  # Run for 5 seconds
                    led.set_output(0, 1)  # Turn on the LED
                    sleep(0.05)  # 0.05 seconds on (10 Hz)
                    led.set_output(0, 0)  # Turn off the LED
                    sleep(0.05)  # 0.05 seconds off
                led.set_output(0, 0)  # Turn off the LED after 5 second
                while True:
                    sleep(1)  # Sleep indefinitely
    except KeyboardInterrupt:
        led.set_output(0, 0)  # Ensure the LED is turned off when exiting

# Main function
def main():
    switch.init()  # Initialize the input switch
    blink_led()  # Call the blink LED function

# Main entry point
if __name__ == "__main__":
    main()
