import algorithm, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
    return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
    num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
    num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) =
    num0 = num0 mod num1

proc bit_length(n: Natural): Natural =
    const BIT_SIZE = 24
    if n == 0:
      return 0
    let s = toBin(n, BIT_SIZE)
    return BIT_SIZE - s.find('1')


type
    LowestCommonAncestor* = ref object
        size: Positive
        LV: Natural
        depth: seq[int]
        tree, parent: seq[seq[int]]

proc initLowestCommonAncestor*(tree: seq[seq[int]]): LowestCommonAncestor =
    let
        size = tree.len
        LV = bit_length(size)
        depth = newSeq[int](size)
        parent = newSeqWith(LV, newSeqWith(size, -1))
    return LowestCommonAncestor(size: size, LV: LV, depth: depth, tree: tree, parent: parent)

proc build*(self: var LowestCommonAncestor, root: Natural) =
    var que = initDeque[(int, int, int)]()
    que.addLast((root, -1, 0))

    var cur, par, dist: int
    while que.len != 0:
        (cur, par, dist) = que.popFirst()
        self.parent[0][cur] = par
        self.depth[cur] = dist
        for child in self.tree[cur]:
            if child != par:
                self.depth[child] = dist + 1
                que.addLast((child, cur, dist + 1))
    
    for i in 1..<self.LV:
        for j in 0..<self.size:
            let k = self.parent[i - 1][j]
            if k != -1:
                self.parent[i][j] = self.parent[i - 1][k]

proc query*(self: var LowestCommonAncestor, u, v: Natural): int =
    var (u, v) = (u, v)
    if self.depth[v] < self.depth[u]:
        (u, v) = (v, u)
    for i in 0..<self.LV:
        if (((self.depth[v] - self.depth[u]) shr i) and 1) == 1:
            v = self.parent[i][v]
    if u == v:
        return u
    
    for i in countdown(self.LV - 1, 0):
        if self.parent[i][u] != self.parent[i][v]:
            u = self.parent[i][u]
            v = self.parent[i][v]
    return self.parent[0][v]

proc dist*(self: var LowestCommonAncestor, u, v: Natural): int =
    let ancestor = self.query(u, v)
    return self.depth[u] + self.depth[v] - 2*self.depth[ancestor]


type
    SegmentTree*[T, K] = ref object
        N0: Positive
        ide_ele: T
        data: seq[T]
        fold: proc (a, b: T): T
        eval: proc (a: T, b: K): T

proc initSegmentTree*[T, K](size: Positive, ide_ele: T, fold: proc (a, b: T): T, eval: proc (a: T, b: K): T): SegmentTree[T, K] =
    var
        N0 = 1 shl bit_length(size - 1)
        data = newSeqWith(2*N0, ide_ele)
    return SegmentTree[T, K](N0: N0, ide_ele: ide_ele, data: data, fold: fold, eval: eval)

proc toSegmentTree*[T, K](init_value: openArray[T], ide_ele: T, fold: proc (a, b: T): T, eval: proc (a: T, b: K): T): SegmentTree[T, K] =
    var
        N0 = 1 shl bit_length(init_value.len - 1)
        data = newSeqWith(2*N0, ide_ele)
    for i, x in init_value:
        data[i + N0 - 1] = x
    for i in countdown(N0 - 2, 0):
        data[i] = fold(data[2*i + 1], data[2*i + 2])
    return SegmentTree[T, K](N0: N0, ide_ele: ide_ele, data: data, fold: fold, eval: eval)

proc update*[T, K](self: var SegmentTree[T, K], idx: Natural, x: K) =
    var k = self.N0 - 1 + idx
    self.data[k] = self.eval(self.data[k], x)
    while k != 0:
        k = (k - 1) div 2
        self.data[k] = self.fold(self.data[2*k + 1], self.data[2*k + 2])

proc query*[T, K](self: var SegmentTree[T, K], left, right: Natural): T =
    var
        L = left + self.N0
        R = right + self.N0
        res = self.ide_ele
    
    while L < R:
        if (L and 1) == 1:
            res = self.fold(res, self.data[L - 1])
            inc L
        if (R and 1) == 1:
            dec R
            res = self.fold(res, self.data[R - 1])
        L = L shr 1
        R = R shr 1
    return res


var
    C, A, max_c, ans: seq[int]
    graph: seq[seq[int]]
    lca: LowestCommonAncestor
    seg_tree: SegmentTree[int, int]

proc solve() =
    var N, K, Q, u, v: int
    (N, K, Q) = input().split.map(parseInt)
    C = input().split.map(parseInt)
    A = input().split.mapIt(it.parseInt - 1)
    graph = newSeqWith(N, newSeq[int]())
    for _ in 0..<N - 1:
        (u, v) = input().split.mapIt(it.parseInt - 1)
        graph[v].add(u)
    
    max_c = newSeq[int](N)
    proc dfs(cur, c: int) =
        max_c[cur] = c
        for child in graph[cur]:
            dfs(child, max(c, C[child]))
    dfs(0, C[0])

    lca = initLowestCommonAncestor(graph)
    lca.build(0)

    proc fold(a, b: int): int =
        if a == -1:
            return b
        if b == -1:
            return a
        return lca.query(a, b)
    seg_tree = toSegmentTree(A, -1, fold, (a, b: int) => b)
    
    var xi, yi, li, ri: int
    for _ in 0..<Q:
        let query = input().split.map(parseInt)
        if query[0] == 1:
            (xi, yi) = query[1..^1].mapIt(it - 1)
            seg_tree.update(xi, yi)
        else:
            (li, ri) = query[1..^1]
            dec li
            ans.add(max_c[seg_tree.query(li, ri)])
    echo ans.join("\n")

when is_main_module:
    solve()
