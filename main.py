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


# Driver code
if __name__ == "__main__":

  input = ['ab', 'bc', 'cd']  # input4 = ['ab', 'ba', 'ab']
  target = 'abcd'  # target2 = 'cdab' # target3 = 'abab' # target4 = 'abab'
  print(process(input, target))
  print('done')
