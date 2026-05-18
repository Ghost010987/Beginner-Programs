# Function for counting the word frequency in a text or paragraph.
import string

def count_word_freq(text):
# Function to count the number of words in a text as a parameter.
# Count is the dictionary to contain keys and values.
    count = {}

# Text should be converted to lowercase.
    text = text.lower()

# Need a translator table to remove any punctuations from the text.
    translator = str.maketrans(string.punctuation, " " * len(string.punctuation))
    text = text.translate(translator)

#Take the current count of this word (or 0 if it doesn’t exist yet), then add 1 and store it back.
    for word in text.split():
        count[word] = count.get(word, 0) + 1 
    return count

user_input = input("Write or past the text: ")
result = count_word_freq(user_input)

# Loop to set the format for the output. 
for word, freq in sorted(result.items()):
    print(f"{word}: {freq}")
