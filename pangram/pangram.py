def is_pangram(sentence):
  alph = 'abcdefghijklmnopqrstuvwxyz'
  count = 0
  for lett in alph:
    if lett in sentence.lower():
      count += 1
  if count == 26:
    return True
  else:
    return False
