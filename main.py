input = ['ab', 'bc', 'cd', 'de', 'ef']
input2 = ['ab', 'bc', 'ab', 'de', 'ef']
target = 'abab'
outputEx = ['ab', 'cd']
output = []


# def process(input: list, target: str, output: list):
#   # output = []
#   currentTarget = target
#   for i in input:
#     # word = input[i]
#     if target.startswith(i):
#       output.append(i)
#       input.remove(i)
#       currentTarget = currentTarget[len(i):]
#       return process(input, currentTarget, output)
#       # if i[0] == target[0] and i[-1] == target[-1]:
#       #     output.append(i)
#   return output

def process(input: list, target: str):
  output = []
  for i in input:
    # word = input[i]
    if target.startswith(i):
      input.remove(i)
      output.append(i)
      target = target[len(i):]
      # print('i', i)
      # print('input', input)
      # print('output', output)
      # print('target', target)
      for e in input:
        if target.startswith(e):
          output.append(e)
          # print('e', e)
          return output
  return None


print(process(input, target))
