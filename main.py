input = ['ab', 'bc', 'cd', 'de', 'ef']
input2 = ['ab', 'bc', 'ab', 'de', 'ef']
target = 'abab'
outputEx = ['ab', 'cd']
output = []

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
