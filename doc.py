from cuesdk import CueSdk
from cuesdk.structs import CorsairLedColor

def get_available_leds():
    leds = list()
    device_count = sdk.get_device_count()

    for device_index in range(device_count):
        led_positions = sdk.get_led_positions_by_device_index(device_index)
        led_colors = list(
            [CorsairLedColor(led, 0, 0, 0) for led in led_positions.keys()])
        leds.append(led_colors)

    return leds

def getpos(tupl):
    return (int(((tupl[0] - 30) - (tupl[0] % 10)) / 10), int((((tupl[1] - 30) - (tupl[1] % 10)) / 10)))

def main():
    global sdk

    sdk = CueSdk()

    connected = sdk.connect()
    if not connected:
        err = sdk.get_last_error()
        print("Handshake failed: %s" % err)
        return


    # Make human readable log.txt
    qf = open("log.txt", "a")
    for di in range(len(get_available_leds())):
        bigdict = sdk.get_led_positions_by_device_index(di)
        for i in bigdict:
            qf.write(f"Name: {i}\nPosition Value: {getpos(bigdict[i])}\nActual Value: {int(i)}\nIndex: {[i.led_id for i in get_available_leds()[di]].index(i)}\n----------\n")
    qf.close()

    # Make machine readable transformations.txt
    mf = open("transformations.txt", "a")
    for di in range(len(get_available_leds())):
        bigdict = sdk.get_led_positions_by_device_index(di)
        for i in bigdict:
            mf.write(f"{getpos(bigdict[i])[0]} {getpos(bigdict[i])[1]} {[i.led_id for i in get_available_leds()[di]].index(i)}\n") # POSX POSY INDEX
    mf.close()

if __name__ == "__main__":
    main()