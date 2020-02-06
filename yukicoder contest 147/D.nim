import strutils, sequtils, algorithm

var
    N, M: int
    U: array[200, int]
    graph: seq[seq[(int, int)]]
    dp: array[200, array[1001, int]]


proc dfs(cur, parent: int) =
    dp[cur].fill(U[cur])

    for (child, ci) in graph[cur]:
        if child != parent:
            dfs(child, cur)
            
            for i in countdown(M, 0):
                for j in ci..i:
                    dp[cur][i] = max(dp[cur][i], dp[cur][i - j] + dp[child][j - ci])


proc solve() =
    (N, M) = stdin.readLine.split.map(parseInt)
    M = M div 2
    for i in 0..<N:
        U[i] = stdin.readLine.parseInt
    graph = newSeqWith(N, newSeq[(int, int)]())
    var a, b, c: int
    for _ in 0..<N-1:
        (a, b, c) = stdin.readLine.split.map(parseInt)
        graph[a].add((b, c))
        graph[b].add((a, c))
    
    dfs(0, -1)
    echo dp[0][M]


when is_main_module:
    solve()
