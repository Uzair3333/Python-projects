def main():
    # Open and read the file
    try:
        filename = input("Enter path to the .txt file: ")
        with open(f'{filename}', 'r', encoding='utf-8') as file:
            content = file.readlines()
    except FileNotFoundError:
        print(f"File {filename} not found. Make sure the file exists in the correct folder.")
        exit()

    # Count number of lines
    def count_lines(content):
        return len(content)

    # Count number of words
    def count_words(content):
        num_of_words = 0
        for line in content:
            num_of_words += len(line.split())
        return num_of_words

    # Count number of characters
    def count_characters(content):
        num_of_characters = 0
        for line in content:
            num_of_characters += len(line)
        return num_of_characters

    # Count frequency of each word (case-insensitive, efficient)
    def count_each_word(content):
        word_freq = {}
        for line in content:
            words = line.strip().split()
            for word in words:
                word = word.casefold().strip(".,!?\"'()[]{}:;")  # Clean punctuation
                if word:
                    word_freq[word] = word_freq.get(word, 0) + 1
        return word_freq

    # Collect data
    lines = count_lines(content)
    words = count_words(content)
    characters = count_characters(content)
    word_frequencies = count_each_word(content)

    # Print results
    print(f"\nTotal number of lines: {lines}")
    print(f"Total number of words: {words}")
    print(f"Total number of characters: {characters}\n")

    print("🔍 Word Frequency:")
    for word, freq in sorted(word_frequencies.items()):
        print(f"'{word}' appears '{freq}' time(s)")

    with open("report.txt", 'w') as file:
        file.write(f"Total number of lines: {lines}")
        file.write(f"\nTotal number of words: {words}")
        file.write(f"\nTotal number of characters: {characters}\n")
        file.write("\nWord Frequency:\n")
        for word, freq in sorted(word_frequencies.items()):
            file.write(f"\n'{word}' appears '{freq}' time(s)")
        file.write('\n')

if __name__ == "__main__":
    main()