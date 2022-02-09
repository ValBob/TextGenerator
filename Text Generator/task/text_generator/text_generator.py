import re
import string
import random
from pprint import pprint
from nltk.tokenize import WhitespaceTokenizer

# path = r'C:\Users\gefes\PycharmProjects\Text Generator\Text Generator\task\test\corpus.txt'
path = input()
tokenizer = WhitespaceTokenizer()

with open(path, 'r', encoding='utf-8') as f:
    a = f.read()
    tokens_list = tokenizer.tokenize(a)

# print('Corpus statistics')
# print('All tokens:', len(tokens_list))
# print('Unique tokens:', len(set(tokens_list)))

# n_bigrams = len(tokens_list) - 1
# bigrams_list = [(tokens_list[i], tokens_list[i + 1]) for i in range(n_bigrams)]

trigrams_list = [(' '.join([tokens_list[i], tokens_list[i + 1]]), tokens_list[i + 2]) for i in range(len(tokens_list) - 2)]

# print('Number of bigrams:', n_bigrams)

# bigrams_frequency = {for head, tail in bigrams_list}
# bigrams_frequency = {}
trigrams_frequency = {}


# for bigram in bigrams_list:
#     head, tail = bigram
#     if not bigrams_frequency.get(head):
#         bigrams_frequency[head] = {}
#     if bigrams_frequency[head].get(tail):
#         bigrams_frequency[head][tail] += 1
#     else:
#         bigrams_frequency[head][tail] = 1

for trigram in trigrams_list:
    head, tail = trigram
    if not trigrams_frequency.get(head):
        trigrams_frequency[head] = {}
    if trigrams_frequency[head].get(tail):
        trigrams_frequency[head][tail] += 1
    else:
        trigrams_frequency[head][tail] = 1


# while True: Stage 2
#     number = input()
#     if number == 'exit':
#         break
#     else:
#         if not re.match('-?[0-9]+', number):  # not number.isnumeric():
#             print('Type Error. Please input an integer.')
#         elif int(number) > n_bigrams - 1 or int(number) < -n_bigrams:
#             print('Index Error. Please input a value that is not greater than the number of all bigrams.')
#         else:
#             head, tail = bigrams_list[int(number)]
#             print(f'Head: {head}    Tail: {tail}')

# while True:  # Stage 3
#     word = input()
#     if word == 'exit':
#         break
#     elif not bigrams_frequency.get(word):
#         print('Key Error. The requested word is not in the model. Please input another word.')
#     else:
#         print(f'Head: {word}')
#         top7_tails = sorted(bigrams_frequency[word].items(), key=lambda x: x[1], reverse=True)[:7]
#         for tail, count in top7_tails:
#             print(f'Tail: {tail} Count: {count}')

# next_word = random.choice(tokens_list)  # start word for entire text block

# words = [word for word in bigrams_frequency[next_word].keys()]
# probs = [prob for prob in bigrams_frequency[next_word].values()]
#
#
tokens_set = list(trigrams_frequency)
heads = [head for head in trigrams_frequency]
freqs = [len(trigrams_frequency[head]) for head in trigrams_frequency]

for _ in range(10):
    while True:
        head = random.choices(heads, freqs)[0]
        if re.match(r'^[A-Z].*[^.!?]$', head.split()[0]):
            break
    chain = head.split()
    next_word = chain[0]
    while len(chain) < 5 or re.match(r'.*[^.!?]$', next_word):
        words = [word for word in trigrams_frequency[head].keys()]
        probs = [prob for prob in trigrams_frequency[head].values()]
        next_word = random.choices(words, probs)[0]
        chain.append(next_word)
        head = ' '.join(chain[-2:])
    print(*chain)

