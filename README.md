# rockbock
Write code to send an image from a Raspberry Pi Zero to a server with a RockBlock modem

# Setup Instructions.

**Raspberry Pi**

1. Connect the RockBlock modem and insure there is a signal using screen /dev/serial0 19200  
   and issuing an AT command, which should reply OK and an AT-CSQ which should return a number > 0

2. Create a virtualenv with python -venv rockblock Once complete, cd into the rockblock directory  
   and issue the command . /bin/activate

3. Clone the repo with a the command

    > git clone https://github.com/CrabbyPete/rockblock.git`

    This will create new rockblock directy. cd to that directory and issue the following command

    `pip install -r requirements.txt`

    To upload a file issue the command

    > python main.py < name of the file>

    but before doing this make sure the code server.py is running on a server.

**Server**

The code was tested using pagekite. On the admin page of the device in the Rock7 page  
https://rockblock.rock7.com/Operations# Select Deliver Groups. Select the name of the modem  
to send the data, select Delivery Address. Enter the address to send it to ( in the test case it was qa.pagekite.me ) and   
select HTTP_JSON.

Run the server code with python server.py. If you use this code on a local PC or Mac and use pagekite  
make sure the kites are up. (See https://pagekite.net/ for instructions)

Currently the server will create a file called jpeg.jpg. The is the resulting file.

This code can be modified to put the file anywhere or send it to an email address. It can be   
converted to an AWS lambda function as well.


