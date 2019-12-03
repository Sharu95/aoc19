def main(seq, i=0):
  if seq[i] in [1, 2]:
    ix, iy, iz = seq[i + 1:i + 4]
    seq[iz] = seq[ix] + seq[iy] if seq[i] == 1 else seq[ix] * seq[iy]
    return main(seq, i + 4)
  elif seq[i] == 99:
    return seq
  else:
    return main(seq, i + 1)


if __name__ == '__main__':
  with open('input.txt', 'r') as f:
    seq = list(map(int, f.read().split(','))) 
    seq_copy = seq.copy()

    # Part 1: noun = 12, verb = 2
    noun, verb = 12, 2
    seq_copy[1:3] = [noun, verb]
    print('Part 1:\t', main(seq_copy)[0])

    # Part 2: noun = 31, verb = 46
    # Exploit multiplicative growth, finetune additive growth
    # Sub-optimal, no need to check all combinations
    noun, verb = 12, 2
    while True:
      seq_copy = seq.copy()
      seq_copy[1:3] = [noun, verb]
      res = main(seq_copy)[0]

      if res > 19690720:
        noun -= 1
      elif res < 19690720:
        noun += 1
        verb += 1
      else:
        break
      
    print('== Part 2 ==')
    print(f'Target:\t\t\t{19690720}', )
    print(f'Found:\t\t\t{res}')
    print(f'100 * noun + verb\t{100 * noun + verb} ({noun} x {verb})')