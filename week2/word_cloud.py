
import re

# Word cloud dictionary
dict = dict()
# Regex expression for letters
regex = re.compile('[^a-zA-Z]')

# Open the stop words not to be included in the word count
f = open('stopwords.txt', 'r')
stop_words = f.readlines()
f.close()

# Open the file containing charles dickens novel and split into individual words
with open('98-0.txt', 'r') as f:
    for line in f:
        for word in line.split():
            #Strip words of punctuation
            word = word.strip()    
            word = regex.sub('', word)

            if word not in stop_words:
                if word in dict:
                    dict[word] = dict[word] + 1
                else:
                    dict.update({word:1}) 


key_max = max(dict.keys(), key=(lambda k: dict[k]))
key_min = min(dict.keys(), key=(lambda k: dict[k]))

print('Maximum Value: ',dict[key_max])
print('Minimum Value: ',dict[key_min])
