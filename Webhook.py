from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from DialogAgent import ChatAgent

flask_app = Flask(__name__)
chat_agent = ChatAgent('agent name')

@flask_app.route('/sms', methods = ['POST'])
def smsReply():
    """Respond to incoming calls with a simple text message."""
    # Fetching the message from the chat
    msg = request.form.get('Body')
    # Creating a reply with twilio
    resp = MessagingResponse()
    resp.message(chat_agent.detect_intent_from_text(msg, 12314).fulfillment_text)
    return str(resp)

flask_app.run(debug = True)
# print(" ")
# print(f'Fulfillment Text: {response.fulfillment_text}')
# print(" ")
# response = chat_agent.detect_intent_from_text("John", 12314) ## Try to use the phone number of a person here
# print(f'Fulfillment Text: {response.fulfillment_text}')
# print(' ')
# print(f'Display Name: {response.intent.display_name}')
# print(f'Detection Confidence: {response.intent_detection_confidence}')