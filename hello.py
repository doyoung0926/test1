import sys

A, B, N = map(int, sys.stdin.readline().split())

result = A / B
end = result - int(result)
print(str(end)[N+1])

