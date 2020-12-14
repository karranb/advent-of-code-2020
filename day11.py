from functools import reduce

input = """LLLLLLLLL.L.LLL.L.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL
LLLLLLLLLLLLL.LLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLL.LLLLLL.LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLL.LLL.LLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL
L..LL.L.L....L..L.L....L.....L.L.L......L..L..L....L.LL.......L.....L....L..L................L....
LLLLLLLLLLLLLLL.LLL.LLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL..LLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLL.LLLLLLLLL.LLL.LLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLL.LLL.LLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLL
LL.LLLLLLLLLLLL.LLL.LLL.LLLLLLLL.LLLLLLLL.LLLLLLL..LLLL.LLLLLLL.LLLL.LLLLLL.LLLLL.LLLL.LL.LLLLLLLL
LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLL.L.LLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLLLLLLLLLL.LLLL.LLL.LLLLLLLL.LLLLLLLLL.LLLLLLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLL.LLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLL.LL.LLLLLLLLLLLLLLLL
.LLLL..L.L..L....L.LLL...LLL..L.L....L.L.L...L.....L...L.....L...L..L...LL...L..LLL..L...L....L..L
LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLL
LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLL.LLLL..LLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLL..LLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL
.....LL...LL..L...L..L..LL.L..LLL...L..L.LLL...LLL..L.....L...L.....L........LLLL..LLL.....L....L.
LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLL.LLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLLLLLLLL.LL
LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLL.LL.LLLLLLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLL.L
LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLL.LLLLLLLLL.LLLLLLL.LLLL.LLL.LL.LLLLL.LLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.L.LLLLL.LLLLLLLL
....L..LL.L.L......L..LL.......LL......L..L...L..L.........LL....LL.LLL..LLLL..L..L.......L....L..
LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL
LLLLLLLLL.LLL.L.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLL.LLLLLLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL
.LL..LLLLL.LL.L...L...L...L....LLLL...LLLL.LL...LL...L.LL...LL..LL.L..L......L....L.L.L.L...LL...L
LLLLLLLLL.LLLLLLLLLLLLL..LLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLLLLL.LL.LLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLL.L.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLL.LLLL..LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLL.LL.LL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLLLL.LLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLL.LLLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLL.LLLLL.L.LLLLLLLL
....L.........LL...L.L..LL.L.L..L......L.L.L...L....L.......LL.LL....L.L...L....L...L....L...L....
L.LLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLL.LL..LLLL
LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLL..LLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLL.L.LLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL
LLLLLL.LL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL
LLL..L.L........L...L..L.LLLLLLL..LLLL..L...L..L.L..LLL....L..L.LLL..L...L..L.......L.LLLLLL.LL.L.
LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LL.LLLL.LLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LL.LL.LLLLLLL.LLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLL.LLL.LLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL
L...L.....LL....L.L.LLLLL.....L....LL..L.....L...L.L.LL.......LL...LL............L.L..L..LLL..LL..
LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLL.LLLLL.LLLLLLL.LLLLL.LL
LL.LLLLLLLLLLLL.L.LLL.LLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLL.LL.LLLL.LLLLLL.LLLLL.LLLLLLL.L.LLLLLL
LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLL.LLLL
LLLLLLLLL.LLLLL.L.LLLLL.LLLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLL.LLLLLLLLLLLLLL
LLLL.LLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLL..LLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL
LL...L.........L..LLL........L.L..L....L.L.L....LLLL.LL.L....LL....L.LL.LLL..L..L....LL.L......LLL
LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLL.L.LLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL
...L........L....L.L.LL.LL.L.L.....L.L..L.....LL....L..L.L.L..L..L.L...L.........L.LL.LLLLL..L....
LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL..LLLL.LLLLLLL.LLLLLLLLLLL.LLL.L.LLLLLLLLLLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLL.L.LLLLLLLL
LLLLLLLLL.LLLLLLLLLLLLL.LL.LLLLLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLL..LLLLLLL
LLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL
..LLLL.L..LL.L......LL.L...L.L..L....LLL.........L....L.......LL.LLL.L.L.....LL.L...L.LLL....L....
LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.L.LLL.LLLLLLL.LLLL.LLLLLL.LLLL..LLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLL.LLLLLLLLL.L.LLLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLLLLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLLLLLLL.LL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL
LLLL.LLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLL.LLLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLL
LL...LLLLL.....LL..L.....L....L......L.L........LL......LL.LL..L..LLL.L...L..L..L.L.....LLLL...LLL
LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLL.LL.LLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLL.LLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLL.LLLLLLLLLLLL.LLLLLL.LLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLL.LLLLL.LLL.LLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL
.LL..L.....LLLL.LL..L.LL....L.LL...L..LL......L..LL...LL..L.L.LLLL...LL.L..L..LLL.L.L.....L.LL.LL.
LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLLLLLLL.LLLLL.LLLLLLLLL.LL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLL.LLLL.LLLLLLLLLLLL.LLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLL.LLLLLLLL.LLLLLLLLLLL.LLLL.LLLLL.LLLLLLL.LLLL.LLLLLLLLLLLLLLLLLLLL.LLLLL.LL
LLLLLLLLL.LLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLLLLLL.LLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLL.LLLLLL.LLLLL.LLLLLLLLLLLLLLLL
LLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLLL.LLLLLLL.LLLL..LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL.LLLLLLLL
LLLLLLLLL.LLLLL.LLLLLLLLLLLLLLLL.LLLLLLLL.LLLLLLL.LLL.L.LLLLLLLLLLLL.LLLLLLLLLLLLLLLLLLLL.LLLLLLLL"""


initial_state = list(map(lambda row: [char for char in row], input.split('\n')))

EMPTY = 'L'
FLOOR = '.'
BUSY = "#"

def get_busy_adjacents(state, i, j):
  total = 0
  if i > 0 and state[i-1][j] == BUSY:
    total = total + 1
  if i < len(state) - 1 and state[i+1][j] == BUSY:
    total = total + 1
  if j > 0 and state[i][j-1] == BUSY:
    total = total + 1
  if j < len(state[i]) - 1 and state[i][j+1] == BUSY:
    total = total + 1
  if i > 0 and j > 0 and state[i-1][j-1] == BUSY:
    total = total + 1
  if i > 0 and j < len(state[i]) - 1 and state[i-1][j+1] == BUSY:
    total = total + 1
  if i < len(state) - 1 and j > 0 and state[i+1][j-1] == BUSY:
    total = total + 1
  if i < len(state) - 1 and j < len(state[i]) - 1 and state[i+1][j+1] == BUSY:
    total = total + 1
  return total


def process_free(state, tolerance=4):
  new_state = []
  for i in range(len(state)):
    row = state[i]
    new_row = []
    for j in range(len(row)):
      seat_state = state[i][j]
      new_row += [EMPTY] if seat_state == BUSY and get_busy_adjacents(state, i, j) >= tolerance else [seat_state]
    new_state += [new_row]
  return new_state

def process_occupy(state):
  new_state = []
  for i in range(len(state)):
    row = state[i]
    new_row = []
    for j in range(len(row)):
      seat_state = state[i][j]
      new_row += [BUSY] if seat_state == EMPTY and not get_busy_adjacents(state, i, j) else [seat_state]
    new_state += [new_row]
  return new_state

def sum_row_occ(row):
  return len(list(filter(lambda char: char == BUSY, row)))

def sum_occ(state):
  return reduce(lambda acc, row: acc + sum_row_occ(row), state, 0)

def part1(_initial_state):
  states = [_initial_state]
  while len(states) < 2 or states[-2] != states[-1]:
    current_state = states[-1]
    if len(states) % 2 == 1:
      states += [process_occupy(current_state)]
    else:
      states += [process_free(current_state)]
  return sum_occ(states[-1])

def get_adjancent_state(state, i, j, i_factor=0, j_factor=0):
  default_state = FLOOR
  current_i = i + i_factor
  current_j = j + j_factor
  if current_i < 0 or current_i == len(state) or current_j < 0 or current_j ==len(state[current_i]):
    return default_state
  seat_state = state[current_i][current_j]
  if seat_state == FLOOR:
    return get_adjancent_state(state, current_i, current_j, i_factor, j_factor)
  return seat_state

def get_busy_adjacents2(state, i, j):
  total = 0
  if get_adjancent_state(state, i, j, -1, 0) == BUSY:
    total = total + 1
  if get_adjancent_state(state, i, j, 1, 0) == BUSY:
    total = total + 1
  if get_adjancent_state(state, i, j, 0, -1) == BUSY:
    total = total + 1
  if get_adjancent_state(state, i, j, 0, 1) == BUSY:
    total = total + 1
  if get_adjancent_state(state, i, j, -1, -1) == BUSY:
    total = total + 1
  if get_adjancent_state(state, i, j, -1, 1) == BUSY:
    total = total + 1
  if get_adjancent_state(state, i, j, 1, -1) == BUSY:
    total = total + 1
  if get_adjancent_state(state, i, j, 1, 1) == BUSY:
    total = total + 1
  return total


def process_free2(state, tolerance=4):
  new_state = []
  for i in range(len(state)):
    row = state[i]
    new_row = []
    for j in range(len(row)):
      seat_state = state[i][j]
      new_row += [EMPTY] if seat_state == BUSY and get_busy_adjacents2(state, i, j) >= tolerance else [seat_state]
    new_state += [new_row]
  return new_state

def process_occupy2(state):
  new_state = []
  for i in range(len(state)):
    row = state[i]
    new_row = []
    for j in range(len(row)):
      seat_state = state[i][j]
      new_row += [BUSY] if seat_state == EMPTY and not get_busy_adjacents2(state, i, j) else [seat_state]
    new_state += [new_row]
  return new_state

def part2(_initial_state):
  states = [_initial_state]
  while len(states) < 2 or states[-2] != states[-1]:
    current_state = states[-1]
    if len(states) % 2 == 1:
      states += [process_occupy2(current_state)]
    else:
      states += [process_free2(current_state, 5)]
  return sum_occ(states[-1])

print('part1', part1(initial_state))
print('part2', part2(initial_state))