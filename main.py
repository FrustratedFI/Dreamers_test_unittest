def reverse_string(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text[::-1]

def count_vowels(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def count_words(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
        
    words = text.split()
    return len(words)