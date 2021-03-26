
# O(n^2) time | O(1) space
def twoNubers(array, targetSum):
  for in range(len(array)-1):
    firstNum = array[i]
    for j in range(i+1, len(array)):
      secondNum = array[j]
      if firstNum + secondNum == targetSum:
        return [firstNum, secondNum]
  return []
# O(n) time | O(n) space

def twoNumberSum(array, targetSum):
  nums = {}
  for num in array:
    potensialMatch = targetSum - num
    if potensialMatch in nums:
      return [potensialMatch, num]
    else:
      nums[num] = True
  return []


