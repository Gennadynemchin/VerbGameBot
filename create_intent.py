import json
from google.cloud import dialogflow


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print(f'Intent created: {response}')


def get_questions_answers(file):
    with open(file, 'r') as my_file:
        questions_json = json.loads(my_file.read())
        for intent_name, questions_answers in questions_json.items():
            display_name = intent_name
            training_phrases_parts = questions_answers['questions']
            message_text = [questions_answers['answer']]

            create_intent('verbgamebot', display_name, training_phrases_parts, message_text)


def main():
    get_questions_answers('questions.json')


if __name__ == '__main__':
    main()
