import random
import string

# A simple dictionary-based approach to classify sentences into English or German
language_classifier = {
    'en': ['the', 'a', 'an', 'is', 'are', 'am', 'be', 'was', 'were', 'be', 'has', 'have', 'had'],
    'de': ['ist', 'sind', 'bin', 'bin', 'war', 'waren', 'sei', 'seien', 'sei', 'hat', 'haben', 'hat']
}

def predict_language(sentence: str) -> str:
    """
    Predict the language of a given sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: 'English' if the sentence is in English, 'German' if it is in German.
    """
    # Convert the sentence to lowercase
    sentence = sentence.lower()
    
    # Split the sentence into words
    words = sentence.split()
    
    # Initialize a counter for English and German words
    en_count = 0
    de_count = 0
    
    # Check each word in the sentence
    for word in words:
        # Remove punctuation from the word
        word = word.strip(string.punctuation)
        
        # Check if the word is in the English or German dictionary
        if word in language_classifier['en']:
            en_count += 1
        elif word in language_classifier['de']:
            de_count += 1
    
    # Return 'English' if there are more English words, 'German' otherwise
    return 'English' if en_count > de_count else 'German'

# Test the function