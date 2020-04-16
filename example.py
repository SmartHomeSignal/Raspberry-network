import time

from network import Network


def callback(is_signal_on):
    if is_signal_on:
        print("Enable signal")
    else:
        print("Disable signal")


if __name__ == '__main__':
    network = Network()

    network.connect(callback)

    time.sleep(3)

    network.enable_signal()

    time.sleep(3)

    network.disable_signal()

    time.sleep(3)

    network.disconnect()
