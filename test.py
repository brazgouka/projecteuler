input_file = "english2.txt"

from time import sleep

import csv
import requests
import json

# FreeDictionaryAPI base URL
API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def fetch_noun_definition(word):
    """Fetch the noun definition of a word from FreeDictionaryAPI."""
    try:
        response = requests.get(API_URL + word)
        if response.status_code == 429:
            sleep(10)
            response = requests.get(API_URL + word)
        if response.status_code == 200:
            data = response.json()
            meanings = data[0].get("meanings", [])
            for meaning in meanings:
                if meaning.get("partOfSpeech") == "noun":
                    definitions = meaning.get("definitions", [])
                    if definitions:
                        return definitions[0]["definition"]
            return None
        else:
            return None
    except Exception:
        return None

def process_english_txt():
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    updated_lines = []
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) < 2:
            continue  # skip malformed lines
        word = parts[0]
        freq = parts[1]
        definition = fetch_noun_definition(word)
        if definition:
            updated_lines.append(f"{word},{freq},{definition}\n")
        # else: skip line (remove)

    with open(input_file, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

# Run the script
process_english_txt()
