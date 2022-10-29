from google.cloud import dialogflow


def detect_intent_texts(texts, project_id='verbgamebot', session_id='123456789', language_code='ru-RU'):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
        answer = response.query_result.fulfillment_text
        return answer
