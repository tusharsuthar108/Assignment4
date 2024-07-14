def unshuffle_sentence(s):
  words = s.split()
  sorted_words = sorted(words, key=lambda word: int(word[-1]))
  return ' '.join(word[:-1] for word in sorted_words)

s = "sentence4 a3 is2 This1"
print(unshuffle_sentence(s))
