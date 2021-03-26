from main import main

def test_a():
  r = main(5, 0, 3); assert len(r) == 5
  ans = ['A', 'D', 'E', 'B', 'C'];  assert r == ans

def test_b():
  r = main(5, 3, 3); assert len(r) == 5
  ans = ['D', 'B', 'C', 'E', 'A'];  assert r == ans

def test_c():
  r = main(7, 2, 3); assert len(r) == 7
  ans = ['F', 'E', 'D', 'C', 'B', 'G', 'A'];  assert r == ans

def test_d():
  r = main(7, 0, 9); assert len(r) == 7
  ans = ['D', 'E', 'B', 'A', 'G', 'C', 'F'];  assert r == ans
