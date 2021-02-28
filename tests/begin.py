import requests

URL = 'http://qa.pagekite.me'


def main(file='../fish.jpg'):
    iridium = {'imei': '300534061386680',
               'device_type': 'ROCKBLOCK',
               'serial': '203129',
               'momsn': '2',
               'transmit_time': '21-02-27 16:39:24',
               'iridium_latitude': '41.0392',
               'iridium_longitude': '-72.1520',
               'iridium_cep': '4.0',
               'iridium_session_status': '0',
               'data': '424547494e'
               }

    # Send the begin
    ok = requests.post(URL, json=iridium)
    if not ok:
        print( ok.text)


if __name__ == "__main__":
    main()