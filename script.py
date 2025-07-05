import csv
import requests
import json
import re
import inflect
import nltk
from time import sleep
from wordfreq import word_frequency
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
ps = PorterStemmer()
p = inflect.engine()
input_file = "english.txt"
API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def remove_unused_words():
    updated_lines = []
    pattern = re.compile(r'^[a-zA-Z]+$')
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        filtered = [
            line for line in lines
            if pattern.match(line.strip().split(',')[0])  # only letters allowed
               and len(line.strip()) >= 3
               and not p.singular_noun(line.strip())
               and line.strip().split(',')[0]  # skip if word is empty
        ]
        for line in filtered:
            updated_lines.append(line.strip() + "\n")
    with open(input_file, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

def add_frequency():
    updated_lines = []
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            word = line.strip().split(',')[0]
            if not word:
                continue  # skip empty word
            freq = word_frequency(word, 'en')
            updated_lines.append(f"{word},{freq:.15f}\n")
    with open(input_file, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

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
                    if definitions and not contains_cognate(word, definitions[0]["definition"]):
                        return definitions[0]["definition"]
            return None
        else:
            return None
    except Exception:
        return None

def process_english_txt(file):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    updated_lines = []
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) < 2 or not parts[0]:
            continue  # skip malformed or empty word lines
        word = parts[0]
        freq = parts[1]
        definition = fetch_noun_definition(word)
        if definition:
            updated_lines.append(f"{word},{freq},{definition}\n")

    with open(file, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

def count_words_with_min_frequency(min_freq):
    count = 0
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) < 2 or not parts[0]:
                continue
            try:
                freq = float(parts[1])
                if freq > min_freq:
                    count += 1
            except ValueError:
                continue
    return count

def split_words_by_frequency(threshold, high_freq_file, low_freq_file):
    high_freq_lines = []
    low_freq_lines = []
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) < 2 or not parts[0]:
                continue
            try:
                freq = float(parts[1])
                if freq > threshold:
                    high_freq_lines.append(line)
                else:
                    low_freq_lines.append(line)
            except ValueError:
                continue
    with open(high_freq_file, "w", encoding="utf-8") as f:
        f.writelines(high_freq_lines)
    with open(low_freq_file, "w", encoding="utf-8") as f:
        f.writelines(low_freq_lines)

def sort_words_by_frequency(file):
    with open(file, "r", encoding="utf-8") as f:
        lines = [line for line in f if line.strip() and line.strip().split(',')[0]]
    def get_freq(line):
        parts = line.strip().split(",")
        try:
            return float(parts[1])
        except (IndexError, ValueError):
            return float('-inf')
    sorted_lines = sorted(lines, key=get_freq, reverse=True)
    with open(file, "w", encoding="utf-8") as f:
        f.writelines(sorted_lines)

def replace_cognates(file):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    updated_lines = []
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) < 3 or not parts[0]:
            continue  # skip malformed or empty word lines
        word = parts[0]
        freq = parts[1]
        definition = parts[2]
        if contains_cognate(word, definition):
            definition = fetch_noun_definition(word)
        if definition:
            updated_lines.append(f"{word},{freq},{definition}\n")
    with open(file, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

def contains_cognate(word, sentence):
    tokens = word_tokenize(sentence)
    target_stem = ps.stem(word)
    sentence_stems = [ps.stem(word) for word in tokens]

    return target_stem in sentence_stems

# remove_unused_words()
# add_frequency()
# split_words_by_frequency(0.000002, "high_freq.txt", "low_freq.txt")
#
# sort_words_by_frequency("high_freq.txt")
# sort_words_by_frequency("low_freq.txt")
#
# process_english_txt("high_freq.txt")

replace_cognates("high_freq.txt")
