import strutils, sequtils, math, algorithm


proc solve() =
    var
        N = stdin.readLine.parseInt
        M = mapIt(1..N, stdin.readLine.parseInt)
        dp: array[2^16, int]
    const INF = 10000 * 15
    
    dp.fill(INF)
    dp[0] = 0
    
    for S in 0..<1 shl N:
        var m_sum = 0
        for i in 0..<N:
            if ((S shr i) and 1) == 1:
                m_sum += M[i]
        let d = m_sum mod 1000
        for i in 0..<N:
            if ((S shr i) and 1) == 0:
                dp[S or (1 shl i)] = min(dp[S or (1 shl i)], dp[S] + max(0, M[i] - d))
    echo dp[2^N - 1]


when is_main_module:
    solve()
