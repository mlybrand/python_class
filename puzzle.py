import re, random

def clean_phrase(phrase):
    phrase = phrase.lower()
    phrase = re.sub(r'[^a-z0-9]','', phrase)
    return phrase

def is_palindrome(phrase):
    phrase = clean_phrase(phrase)
    return phrase == phrase[::-1]

def generate_anagram(phrase):
    phrase = clean_phrase(phrase)
    letter_list = list(phrase)
    random.shuffle(letter_list)
    no_of_spaces = random.randrange(0,len(letter_list)//2)
    for x in range(1,no_of_spaces):
        index = random.randrange(1,len(letter_list)-1)
        letter_list.insert(index," ")
    new_phrase = "".join(letter_list)
    new_phrase = re.sub(r' +',' ',new_phrase)
    new_phrase = new_phrase.strip()
    return new_phrase
