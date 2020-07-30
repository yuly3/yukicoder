import strutils, sequtils, math, algorithm

const MOD = 10 ^ 9 + 7
var
    graph: seq[seq[int]]
    parents, depth, dp: array[1000010, int]
    stack0, stack1: seq[int]


proc solve() =
    let N = stdin.readLine.parseInt
    graph = newSeqWith(N, newSeq[int]())
    parents.fill(-1)
    var a, b: int
    for _ in 0..<N - 1:
        (a, b) = stdin.readLine.split.map(parseInt)
        a -= 1; b -= 1
        graph[a].add(b)
        parents[b] = a

    let root = find(parents, -1)
    stack0 = newSeq[int]()
    stack0.add(root)
    var cur: int
    while stack0.len != 0:
        cur = stack0.pop()
        for child in graph[cur]:
            depth[child] = depth[cur] + 1
            stack0.add(child)
            stack1.add(child)
    
    for cur in stack1.reversed():
        dp[parents[cur]] += dp[cur] + 1
    
    var ans = 0
    for n in 0..<N:
        ans = (ans + depth[n] * (dp[n] + 1)) mod MOD
    echo ans


when is_main_module:
    solve()
