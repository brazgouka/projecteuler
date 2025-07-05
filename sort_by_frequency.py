from wordfreq import word_frequency


def add_frequency(input_file):
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

add_frequency("nounlist.csv")
sort_words_by_frequency("nounlist.csv")