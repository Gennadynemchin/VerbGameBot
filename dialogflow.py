from google.cloud import dialogflow


def detect_intent_texts(text: str, session_id, project_id='verbgamebot', language_code='ru-RU'):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    answer = response.query_result.fulfillment_text
    no_answer = response.query_result.intent.is_fallback
    return answer, no_answer
