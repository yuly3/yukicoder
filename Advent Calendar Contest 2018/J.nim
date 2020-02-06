import strutils, sequtils, math

var
    N = stdin.readLine.parseInt
    graph = newSeqWith(N+1, newSeq[int]())
    dp: array[10^5 + 1, array[2, int]]


proc dfs(cur, parent: int) =
    dp[cur][0] = 1
    
    for child in graph[cur]:
        if child != parent:
            dfs(child, cur)
            dp[cur][0] += max(dp[child][0] - 1, dp[child][1])
            dp[cur][1] += max(dp[child][0], dp[child][1])


proc solve() =
    var u, v: int
    for _ in 0..<N-1:
        (u, v) = stdin.readLine.split.map(parseInt)
        graph[u].add(v)
        graph[v].add(u)
    
    dfs(1, -1)
    echo max(dp[1])


when is_main_module:
    solve()
