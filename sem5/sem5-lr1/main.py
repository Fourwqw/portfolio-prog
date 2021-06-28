def squareSequenceDigit(n):
  sum = 0
  pos = 0
  while (sum < n):
    pos = pos + 1
    quadOfNmb = pos * pos
    nmb = 1
    den = 10
    while ((quadOfNmb // den) != 0): 
      den = den * 10
      nmb = nmb + 1
    sum = sum + nmb  
    if (quadOfNmb == n):
      break

  sum = sum - nmb 
  den = den // 10

  while (sum != n):
    findNmb = quadOfNmb // den
    findNmb %= 10
    den = den // 10
    sum = sum + 1
    
  result = findNmb

  return result

      
     
if __name__ == "__main__":
    squareSequenceDigit(1)
    squareSequenceDigit(2)
    squareSequenceDigit(7)
    squareSequenceDigit(12)
    squareSequenceDigit(17)
    squareSequenceDigit(27)