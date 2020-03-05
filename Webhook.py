from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

def sms_reply(self):
    """Respond to incoming calls with a simple text message."""
    # Fetching the message from the chat
    msg = request.form.get('Body')
    # Creating a reply with twilio
    resp = MessagingResponse()
    resp.message(f"You said: {msg}")
    return str(resp)
