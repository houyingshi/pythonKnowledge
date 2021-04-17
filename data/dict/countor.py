from collections import Counter
char_countor = Counter('abracadabra')
print(char_countor)

char_countor.update('aaaaazzz')
print(char_countor)

most = char_countor.most_common(2)
print(most)