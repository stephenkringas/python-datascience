
import re
from collections import Counter

# Word cloud dictionary
dict = dict()

# Regex expression for letters
regex = re.compile('[^a-zA-Z]')

# Open the file containing charles dickens novel and split into individual words
with open('98-0.txt', 'r') as f:
    for line in f:
        for word in line.split():
            
            #Strip words of punctuation
            word = word.strip()    
            word = regex.sub('', word)
            word = word.lower()

            if word in dict:
                dict[word] = dict[word] + 1
            else:
                dict.update({word:1})

# Find the top 10 words and print the number of occurances
for key, value in Counter(dict).most_common(10):
    print(key, value)