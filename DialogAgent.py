import os
import dialogflow_v2 as dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "nikubuntu-1-5d7d63a5b8ca.json"

dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "nikubuntu-1"

def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

response = detect_intent_from_text("say joke", 12314)
response.fulfillment_text
response.intent.display_name
response.intent_detection_confidence