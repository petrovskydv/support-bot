import json
import os

import dialogflow_v2
import dialogflow_v2beta1
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

        client.create_intent(parent, intent)


def train_intents(project_id):
    client = dialogflow_v2beta1.AgentsClient()
    parent = client.project_path(project_id)
    client.train_agent(parent)


def main():
    load_dotenv()
    project_id = os.environ['GOOGLE_PROJECT_ID']
    create_intents('questions.json', project_id)
    train_intents(project_id)


if __name__ == '__main__':
    main()
