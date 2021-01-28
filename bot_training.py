import json
import os
from pprint import pprint

import dialogflow_v2
from dotenv import load_dotenv


def create_intents(file_path, project_id):
    with open(file_path, 'r', encoding='UTF-8') as my_file:
        questions = json.load(my_file)

    client = dialogflow_v2.IntentsClient()
    parent = client.project_agent_path(project_id)

    for intent_name, texts in questions.items():
        intent = {}
        intent['display_name'] = intent_name
        intent['messages'] = [
            {
                'text': {'text': [texts['answer']]}
            }
        ]
        intent['training_phrases'] = []
        for phrase in texts['questions']:
            intent['training_phrases'].append({'parts': [{'text': phrase}]})

        response = client.create_intent(parent, intent)
        pprint(response)


def main():
    load_dotenv()
    project_id = os.environ['GOOGLE_PROJECT_ID']
    create_intents('questions.json', project_id)


if __name__ == '__main__':
    main()
