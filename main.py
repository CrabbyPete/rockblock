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


def main(file='./fish.jpg', uart='/dev/serial0'):
    """
    Main code to send a jpg image to the Iridium network
    """
    jpeg = open(file, "rb").read()
    uart = serial.Serial('/dev/serial0', 19200)
    rb = RockBlock(uart)

    # Reduce the size of the jpeg as much as possible. This takes time
    #jpeg = pyguetzli.process_jpeg_bytes(jpeg)

    # Let the server know you will start transmitting
    rb.text_out = "BEGIN"
    status = rb.satellite_transfer()
    retry = 0
    while status[0] > 8:
        time.sleep(10)
        status = rb.satellite_transfer()
        print(retry, status)
        retry += 1
    print("DONE with BEGIN")

    # Send the file in chunks of 340 ( the permitted maximum)
    for cnt, chunk in enumerate(chunks(jpeg)):
        print(chunk)
        rb.data_out = chunk
        status = rb.satellite_transfer()

        retry = 0
        while status[0] > 8:
            time.sleep(10)
            status = rb.satellite_transfer()
            print(retry, status)
            retry += 1
        
        print("DONE {}".format(cnt))

    # Let the server know you are done
    rb.text_out = "END"
    status = rb.satellite_transfer()
    retry = 0
    while status[0] > 8:
        time.sleep(10)
        status = rb.satellite_transfer()
        print(retry, status)
        retry += 1
        
    print("DONE with END")
    return


if __name__ == "__main__":
    main()
