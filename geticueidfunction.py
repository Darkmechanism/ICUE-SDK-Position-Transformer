from cuesdk import CueSdk
from cuesdk.structs import CorsairLedColor

global sdk
sdk = CueSdk()

def get_available_leds():
    leds = list()
    device_count = sdk.get_device_count()

    for device_index in range(device_count):
        led_positions = sdk.get_led_positions_by_device_index(device_index)
        led_colors = list(
            [CorsairLedColor(led, 0, 0, 0) for led in led_positions.keys()])
        leds.append(led_colors)

    return leds

def get_led_from_pos(x, y):
    coordindex = 0
    for i in open("transformations.txt", "r"):
        if i.startswith(f"0 0"):
            coordindex = int(i.split("\n")[0].split(" ")[2])
    cnt = len(get_available_leds())
    for di in range(cnt):
        device_leds = get_available_leds()[di]
        return device_leds[coordindex]