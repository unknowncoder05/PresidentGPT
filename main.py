import json
from openai import OpenAI
import logging

DEFAULT_COUNTRY = "USA"
PESEIDENT_DATA_JSON_FILE = 'presidents.json'
TEMP_DATA_FILE = '.data/temp.json'
AMOUNT_OF_PRESIDENTS = 2

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
client = OpenAI()

# Load presidents data from JSON file
def load_presidents_data(filename):
    logging.info(f"Loading presidents data from {filename}")
    with open(filename, 'r') as file:
        data = json.load(file)
    logging.info(f"Loaded data for {len(data)} presidents")
    return data

presidents = load_presidents_data(PESEIDENT_DATA_JSON_FILE)[-AMOUNT_OF_PRESIDENTS:]

def get_presidents_opinions(prompt, country=DEFAULT_COUNTRY, save_file=True):
    responses = []
    for president in presidents:
        logging.info(f"Asking {president['name']} for their opinion")
        system_message = f"""you are {president['name']}, president from the {country},
return a json list of opinion objects with the keys name, description
EX:
[
    "name": "do something",
    "description": "beacause of reasons",
]
output JSON
"""
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": [
                        {
                        "type": "text",
                        "text": system_message
                        }
                    ]
                },
                {
                    "role": "user",
                    "content": [
                        {
                        "type": "text",
                        "text": prompt
                        }
                    ]
                }
            ],
            response_format={ "type": "json_object" },
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        opinion = response.choices[0].message.content.strip()
        logging.info(f"{president['name']} says: {opinion}")
        responses.append({
            "president": president["name"],
            "opinion": opinion
        })
    
    if save_file:
        with open(TEMP_DATA_FILE, 'w') as file:
            json.dump(responses, file)
    return responses

def summarize_opinions(opinions, country=DEFAULT_COUNTRY):
    logging.info("Summarizing opinions")
    summary_prompt = f"""Given the following opinions from various {country} presidents,
return a summarized list of the core opinions and which presidents support them
keys name, description, supporters
EX:
[
    "name": "do something",
    "description": "beacause of reasons",
    "supporters": ["president a"]
]
output JSON 
"""
    for opinion in opinions:
        summary_prompt += f"{opinion['president']} says: {opinion['opinion']}\n\n"
    
    summary_response = client.chat.completions.create(
        model="gpt-4o",
        response_format={ "type": "json_object" },
        messages=[
                {
                    "role": "system",
                    "content": [
                        {
                        "type": "text",
                        "text": summary_prompt
                        }
                    ]
                },
            ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    summary = summary_response.choices[0].message.content.strip()
    logging.info(f"Summary: {summary}")
    return summary

prompt = "Inflation is high, what should we do?"
logging.info("Starting the process to gather and summarize opinions")
opinions = get_presidents_opinions(prompt)
summary = summarize_opinions(opinions)

logging.info("Finished gathering and summarizing opinions")

print("Individual Opinions:")
for opinion in opinions:
    print(f"{opinion['president']} says: {opinion['opinion']}")

print("\nSummary of Core Opinions:")
print(summary)
