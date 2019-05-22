from XoXo_code import *

def test_is_it_good_move():
  global Board
  Board = [
      ['o', 'x', 'o'],
      ['x', ' ', 'x'],
      ['x', 'o', 'o'],
  ]
  assert Is_it_good_move(1,1) == True

  Board = [
      ['o', 'x', 'o'],
      ['x', 'o', 'x'],
      ['x', 'o', 'o'],
  ]
  assert Is_it_good_move(1,1) == False


if __name__ == "__main__":
    test_is_it_good_move()
    print("Everything passed")