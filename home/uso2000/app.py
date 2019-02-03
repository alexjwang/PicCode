import requests
import sys
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import subprocess

reload(sys)
sys.setdefaultencoding('utf8')

DOWNLOAD_DIRECTORY = '/home/alexwang3150'
app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming with a simple text message."""
    resp = MessagingResponse()
    if request.values['NumMedia'] != '0':
        # Use the message SID as a filename.
        #filename = request.values['MessageSid'] + '.jpg'
        filename = 'img.jpg'
        with open('{}/{}'.format(DOWNLOAD_DIRECTORY, filename), 'wb') as f:
           image_url = request.values['MediaUrl0']
           f.write(requests.get(image_url).content)
       
        subprocess.call(['/home/joheen_c/backend.sh'])
        textout = "e"
        output = open('/home/joheen_c/error.txt', 'r')
        textout = output.read()
        output.close()
        print(textout)
        if "error" not in textout:
            output = open('/home/joheen_c/out.txt', 'r')
            textout = output.read()
            output.close()
        resp.message(textout)
    else:
        resp.message("Try sending a picture message.")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
