import json
import random

# Load words from JSON file
def load_words(filename="words.json"):
    with open(filename, "r", encoding="utf-8") as file:
        word_dict = json.load(file)
    return word_dict  # Extract only words

# Select random words that fit within the matrix
def select_words(word_dict, size):
    selected_words = []
    used_letters = list()
    words = list(word_dict.keys())

    while len(used_letters) < size * size:
        word = random.choice(words)
        if word not in selected_words and (len(word) + len(used_letters) == size * size or len(word) + len(used_letters) < size * size - 4):
            print(word + " - " + word_dict.get(word))
            selected_words.append(word)
            used_letters += list(word)

        # Stop if we have enough letters to fill the matrix
        if len(used_letters) >= size * size:
            break

    return selected_words

# Generate NxN matrix using letters from selected words
def generate_matrix(size, words):
    letters = list("".join(words))  # Flatten selected words into a list of characters
    random.shuffle(letters)  # Shuffle for randomness

    # Fill the matrix row by row
    matrix = [[letters.pop() for _ in range(size)] for _ in range(size)]

    return matrix, words

# Print the matrix
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))

# Main function
def main():
    try:
        size = int(input("Enter matrix size (N): "))
        if size <= 0:
            print("Size must be greater than 0!")
            return

        word_dict = load_words()
        if not word_dict:
            print("No words found in words.json!")
            return

        selected_words = select_words(word_dict, size)
        matrix, final_words = generate_matrix(size, selected_words)

        print("\nGenerated Word Matrix:")
        print_matrix(matrix)

        print("\nWords included in the matrix:", ", ".join(final_words))

    except ValueError:
        print("Please enter a valid number.")

# Run the script
if __name__ == "__main__":
    main()