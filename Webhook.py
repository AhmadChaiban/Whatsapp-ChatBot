from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

class Application:
    def __init__(self):
        ## initialize the flask app
        self.app = Flask(__name__)

    def sms_reply(self):
        """Respond to incoming calls with a simple text message."""
        # Fetching the message from the chat
        msg = request.form.get('Body')
        # Creating a reply with twilio
        resp = MessagingResponse()
        resp.message(f"You said: {msg}")
        return str(resp)

    def run_app(self):
        self.app.run(debug = True)

if __name__ == "__main__":
    application = Application()
    application.run_app(debug=True)
