def distance(strand_a, strand_b):
  hamming = 0
  if len(strand_a) == 0 and len(strand_b) == 0:
    return 0
  elif len(strand_a) == len(strand_b):
    for i, lett in enumerate(strand_a):
      if lett != strand_b[i]:
        hamming += 1
  elif len(strand_a) > len(strand_b):
    raise ValueError('Strand A is too long!')
  elif len(strand_a) < len(strand_b):
    raise ValueError('Strand B is too long!')
  return hamming


