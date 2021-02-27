import time
import serial
import pyguetzli

from rockblock import RockBlock


def chunks(lst):
    """
    Chunk a block of data into 340 blocks
    """
    for i in range(0, len(lst), 340):
        yield lst[i:i + 340]


def main(file='./fish.jpg', uart='/dev/ttyUSB0'):
    """
    Main code to send a jpg image to the Iridium network
    """

    input_jpeg = open(file, "rb").read()
    uart = serial.Serial('/dev/serial0', 19200)
    rb = RockBlock(uart)



    # Reduce the size of the jpeg as much as possible. This takes time
    optimized_jpeg = pyguetzli.process_jpeg_bytes(input_jpeg)
    with open('fish_small.jpg','wb') as save:
        for cnt, chunk in enumerate(chunks(optimized_jpeg)):
            rb.data = chunk
            status = rb.satellite_transfer()

            retry = 0
            while status[0] > 8:
                time.sleep(10)
                status = rb.satellite_transfer()
                print(retry, status)
                retry += 1
        
            print(f"\nDONE with {cnt.")

if __name__ == "__main__":
    main()
