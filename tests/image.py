import requests
import binascii

from time import sleep

URL = 'http://qa.pagekite.me'


def chunks(lst):
    """
    Chunk a block of data into 340 blocks
    """
    for i in range(0, len(lst), 340):
        yield lst[i:i + 340]


def main(file='../fish.jpeg', uart='/dev/serial0'):
    """
    Main code to send a jpg image to the Iridium network
    """
    jpeg = open(file, "rb").read()
    headers = {"Content-Type":"application/binary"}
    iridium = {'imei': '300534061386680',
               'device_type': 'ROCKBLOCK',
               'serial': '203129',
               'momsn': None,
               'transmit_time': '21-02-27 16:39:24',
               'iridium_latitude': '41.0392',
               'iridium_longitude': '-72.1520',
               'iridium_cep': '4.0',
               'iridium_session_status': '0',
               'data': None
               }


    # Send the file in chunks of 340 ( the permitted maximum)
    for cnt, chunk in enumerate(chunks(jpeg)):
        iridium['momsn'] = str(cnt)
        iridium['data'] = binascii.hexlify(chunk).decode('utf-8')

        ok = requests.post(URL, json=iridium)
        if not ok:
            print(ok.text)
        sleep(1)

    return


if __name__ == "__main__":
    main()
