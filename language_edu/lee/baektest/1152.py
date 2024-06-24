def count_words(s):
    words = s.split()
    return len(words)
s = input()
words_count = count_words(s)
print(words_count)
