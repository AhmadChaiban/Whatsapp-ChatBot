import os
import dialogflow_v2 as dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Ahmad-1-5d7d63a5b8ca.json"

class ChatAgent:
    def __init__(self, projectID):
        self.dialogflow_session_client = dialogflow.SessionsClient()
        self.PROJECT_ID = projectID

    def detect_intent_from_text(self, text, session_id, language_code='en'):
        session = self.dialogflow_session_client.session_path(self.PROJECT_ID, session_id)
        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = self.dialogflow_session_client.detect_intent(session=session, query_input=query_input)
        return response.query_result