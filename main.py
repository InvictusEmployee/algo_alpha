input1 = ['ab', 'bc', 'cd']
input4 = ['ab', 'ba', 'ab']
target1 = 'abcd'
target2  = 'cdab'
target3 = 'abab'
target4 = 'abab'

# limitation
# this function can not find if the 2 words in the array can be a permutated to the target word.
# this function can only return 2 combined words (or None) in the array, not more or less.
# this function doesn't check if the words in the  array has a duplicate one.
def process(input: list, target: str):
  output = []
  for i in input:
    if target.startswith(i):
      input.remove(i)
      output.append(i)
      target = target[len(i):]
      for e in input:
        if target.startswith(e):
          output.append(e)
          return output
  return None


print(process(input4, target4))
