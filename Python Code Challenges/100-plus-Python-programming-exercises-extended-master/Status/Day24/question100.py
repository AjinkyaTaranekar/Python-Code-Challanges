from collections import OrderedDict

list_of_words = OrderedDict()
num_of_words = int(input())
for _ in range(num_of_words):
    word = ''.join(input().lstrip().rstrip().split(' '))
    list_of_words[word] = list_of_words.get(word, 0) + 1
print(len(list_of_words))
result = []
for item in list_of_words.values():
    print(item, end=' ')
