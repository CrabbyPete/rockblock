import logging

from flask import Flask, abort, request, Response

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')
log = logging.getLogger("rockblock")

app = Flask(__name__)

class Image:
    """
    Class to hold the blocks
    """
    data_blocks = []
    def __init__(self):
        self.data_blocks = []

    def clear(self):
        self.data_blocks = []

    def stitch(self):
        """
        Stitch the images together
        :return:
        """
        # sorted(self.data_blocks, key=lambda kv: kv['momsn'])
        final_image =  b''.join(image.data_blocks)
        return final_image


image = Image()

"""
request.form comes back as:
[('imei', '300534061386680'), 
('device_type', 'ROCKBLOCK'), 
('serial', '203129'), 
('momsn', '2'), 
('transmit_time', '21-02-27 16:39:24'), 
('iridium_latitude', '41.0392'), 
('iridium_longitude', '-72.1520'), 
('iridium_cep', '4.0'), 
('iridium_session_status', '0'), 
('data', '454e44')])
"""

@app.route('/', methods=['POST'])
def respond():
    if not request.json:
        log.error("Message received with no data")
        return abort(400,"No data")
    try:
        command = bytes.fromhex(request.json['data']).decode('utf-8')
    except ValueError:
        pass
    else:
        # Clear the buffer and start collecting frames
        if command == "BEGIN":
            log.info("Received Begin")
            image.clear()

        # Transmission complete put the image together
        elif command == "END":
            log.info("Received End")
            jpg_image = image.stitch()
            with open('jpeg.jpg','wb') as f:
                f.write(jpg_image)

        return Response(status=200)

    # Collect all the messages and put them together when its done
    byte_data = request.json['data']
    data = bytes.fromhex(request.json['data'])
    jpeg = image.data_blocks.append(data)

    return Response(status=200)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)