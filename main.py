"""
  Автор: Анисимов Дмитрий, группа №p42552
  Ссылка на сайт-портфолио: https://alterson95.github.io/itmo-4155/
  
  Дополнительные комментарии по решению: -

"""
import random

class SumOfTwo():
  def randNum():
    return random.randint(0, 99)

  def find_sum(data, targetSum):
    """'find_sum' function returns indexes of two numbers whose sum is equal to the number in the 'targetSum' variable"""
    targetListOfIndexes = []
    i = 0
    while (i < len(data)-1):
      if data[i] + data[i+1] == targetSum:
        coupleOfIndex = (i, i+1)
        targetListOfIndexes.append(coupleOfIndex)
      i += 2  
    if not targetListOfIndexes:
      return 'coupleOfIndex is not found'
    return targetListOfIndexes   


if __name__ == '__main__': 
  cortegePi = (3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,7,6,7,4,4,5,9,2,9,9,8,0,6,7,9,8,2,2,6,5,3,5,4,1,5,3,5,8,9,0,6,5,3,5,3,2,3,8,4,7)
  
  """ Test #1 """
  targetSum = 5
  res1 = SumOfTwo.find_sum(cortegePi, targetSum)
  print('targetSum=',targetSum)
  print('res1',res1)
  assert res1 == [(2, 3), (16, 17), (42, 43), (54, 55)], 'test #1 passed'

  """ Test #2 """
  targetSum = 9
  res2 = SumOfTwo.find_sum(cortegePi, targetSum)
  print('\ntargetSum=',targetSum)
  print('res2',res2)
  assert res2 == [(24, 25), (48, 49)], 'test #2 passed'

  """ Test #3 """
  targetSum = 27
  res3 = SumOfTwo.find_sum(cortegePi, targetSum)
  print('\ntargetSum=',targetSum)
  print('res3',res3)
  assert res3 == 'coupleOfIndex is not found', 'test #3 passed'

  """ Test #4 """
  targetSum = 7
  res4 = SumOfTwo.find_sum(cortegePi, targetSum)
  print('\ntargetSum=',targetSum)
  print('res4',res4)
  assert res4 == [(2, 3), (42, 43), (54, 55)], 'test #4 failed'





  
    

