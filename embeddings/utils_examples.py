print('Hi')

import utils
from collections import Counter

file_path = 'mytext.txt'
with open(file_path) as f:
     text = f.read()
words = utils.preprocess(text)
words_counter = Counter(words)
sorted_words_counter = sorted(words_counter, key=words_counter.get, reverse=True)
#print(words_counter)
print("=============================Sorted Words Below==================================================")
print(sorted_words_counter)
print("Total no. of words: {}".format(len(words)))
print("No. of Unique words: {}".format(len(set(words))))
#print(words[:30])
vocab_to_int, int_to_vocab = utils.create_lookup_tables(words)

print(len(vocab_to_int))
print(vocab_to_int)
print(type(vocab_to_int))
print(type(int_to_vocab))
d_word = 'the'
print(words_counter.most_common(5))

freq = 39000
prob = 1 - (10000/freq)**0.5
print('Subsampling prob is: {}'.format(prob))


    