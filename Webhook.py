from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from DialogAgent import ChatAgent

flask_app = Flask(__name__)
chat_agent = ChatAgent('agent name')

@flask_app.route('/sms', methods = ['POST'])
def sms_reply(self):
    """Respond to incoming calls with a simple text message."""
    # Fetching the message from the chat
    msg = request.form.get('Body')
    # Creating a reply with twilio
    resp = MessagingResponse()
    resp.message(f"You said: {msg}")
    return str(resp)

flask_app.run(debug = True)