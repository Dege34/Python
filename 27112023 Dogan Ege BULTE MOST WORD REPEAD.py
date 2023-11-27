# Copyright © 2023 Dogan Ege BULTE
# https://github.com/Dege34
# doganege.bulte@studenti.polito.it
# www.thedege.com

import string
from collections import Counter

conjective = ['the', 'and', 'or', 'in', 'on', 'at', 'is', 'are', 'a', 'an','as',"é","und","ve"] # I was 


def clean_word(word):
    return word.lower().strip()


def common(word):
    return word in conjective


with open('input.txt', 'r') as file:

    content = file.read()


    words = content.split()


    words = [clean_word(word) for word in words if not common(clean_word(word))]

  
    word_counts = Counter(words)

    top_words = word_counts.most_common(5)

    print("The 5 most frequent words (excluding common words) are:")

    for word, count in top_words:
        print(f"{word}: {count} occurrences")