import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    left_acc = [0]
    right_acc = [0]
    for i in range(N):
        left_acc.append(left_acc[-1] + A[2 * i])
        right_acc.append(right_acc[-1] + A[2 * i + 1])
    
    ans = right_acc[-1] - left_acc[-1]
    for i in range(N):
        homu = left_acc[i + 1] + right_acc[-1] - right_acc[i + 1]
        ten = right_acc[i + 1] + left_acc[-1] - left_acc[i + 1]
        ans = max(ans, homu - ten)
    print(ans)


if __name__ == '__main__':
    solve()
