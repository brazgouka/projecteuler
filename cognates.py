import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

target_word = "ascending"
sentence = "An ascent"

tokens = word_tokenize(sentence)

# Stem of target
target_stem = ps.stem(target_word)

# Stem of sentence tokens
sentence_stems = [ps.stem(word) for word in tokens]

print(f"Target Stem: {target_stem}")
print(f"Sentence Stems: {sentence_stems}")

# Check
if target_stem in sentence_stems:
    print("Cognate Detected by Stem!")
else:
    print("No cognate found.")