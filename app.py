import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils import fetch_reply

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h4>Hi, I'm Daisy</h4>"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    #Fetch the message.
    msg = request.form.get('Body')
    phone = request.form.get('From')
    short = phone[9:]

    reply = fetch_reply(msg, short)

    #Create reply
    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)

if __name__ == "__main__":
    app.run(debug = True)
