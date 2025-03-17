from prompt.messages_generator import generate_prompt_messages

import pandas
import json

DATASET_PATH = 'output/prompts.csv'
OUTPUT_PATH = 'output/llama.json'

data = pandas.read_csv(DATASET_PATH)
roles = data['CHARACTER'].unique().tolist()
roles.remove('<END>')
print(roles)

ROLE_IDS = [0]
LANG_ID = 1

selected_roles = [roles[i] for i in ROLE_IDS]
lang = data.keys()[LANG_ID]

msg_list = generate_prompt_messages(data, selected_roles, lang)

with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    json.dump(msg_list, f, ensure_ascii=False, indent=4)
