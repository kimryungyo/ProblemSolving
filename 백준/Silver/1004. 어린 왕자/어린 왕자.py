def main():
  import sys
  input = sys.stdin.readline

  T = int(input())
  for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())

    N = int(input())
    count = 0

    for _ in range(N):
      x, y, r = map(int, input().split())
      circle = r ** 2

      in_count = 0

      dist_1 = (x1 - x) ** 2 + (y1 - y) ** 2
      if dist_1 < circle: in_count += 1

      dist_2 = (x2 - x) ** 2 + (y2 - y) ** 2
      if dist_2 < circle: in_count += 1

      if in_count == 1: count += 1

    print(count)

main()