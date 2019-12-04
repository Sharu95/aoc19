def main(modules):
  
  # Part 1
  fuel = lambda mass: int(mass / 3) - 2
  required_fuel = list(map(fuel, modules))
  total_fuel = sum(required_fuel)
  print('Part 1:', total_fuel)

  # Part 2
  fuel_need = lambda n: n + fuel_need(fuel(n)) if n >= 0 else 0
  required_fuel = list(map(fuel_need, required_fuel))
  total_fuel = sum(required_fuel)
  print('Part 2:', total_fuel)

if __name__ == '__main__':
  with open('input.txt', 'r') as f:
    modules = list(map(int, f.read().split('\n')))
    main(modules)