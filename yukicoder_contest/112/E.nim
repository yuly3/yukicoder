import algorithm, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
    return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
    num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
    num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) =
    num0 = num0 mod num1

const MOD = 10^9 + 7


type
    HeavyLightDecomposition* = ref object
        graph: seq[seq[Natural]]
        path_root, path_parent, left, right: seq[Natural]

proc initHeavyLightdecomposition*(size: Positive): HeavyLightDecomposition =
    var
        graph = newSeqWith(size, newSeq[Natural]())
        empty_seq = newSeq[Natural]()
    return HeavyLightDecomposition(graph: graph, path_root: empty_seq, path_parent: empty_seq, left: empty_seq, right: empty_seq)

proc add_edge*(self: var HeavyLightDecomposition, a, b: Natural) =
    self.graph[a].add(b)
    self.graph[b].add(a)

proc build*(self: var HeavyLightDecomposition, root: Natural) =
    var
        stack = @[(root, root)]
        q = newSeq[Natural]()
        v, p: Natural
    
    while stack.len != 0:
        (v, p) = stack.pop()
        q.add(v)
        for i, to in self.graph[v]:
            if to == p:
                self.graph[v][i] = self.graph[v][^1]
                let _ = self.graph[v].pop()
                break
        for to in self.graph[v]:
            stack.add((to, v))
    
    let n = self.graph.len
    var size = newSeqWith(n, 1)
    for v in reversed(q):
        for i, to in self.graph[v]:
            size[v] += size[to]
            if size[self.graph[v][0]] < size[to]:
                (self.graph[v][0], self.graph[v][i]) = (self.graph[v][i], self.graph[v][0])
    
    self.path_root = newSeqWith(n, root)
    self.path_parent = newSeqWith(n, root)
    self.left = newSeq[Natural](n)
    self.right = newSeq[Natural](n)
    var
        k = 0
        stack1 = @[(root, 0)]
        op: int
        to: Natural
    while stack1.len != 0:
        (v, op) = stack1.pop()
        if op == 1:
            self.right[v] = k
            continue
        self.left[v] = k
        inc k
        stack1.add((v, 1))
        if 1 < self.graph[v].len:
            for i, to in self.graph[v][1..^1]:
                self.path_root[to] = to
                self.path_parent[to] = v
                stack1.add((to, 0))
        if self.graph[v].len != 0:
            to = self.graph[v][0]
            self.path_root[to] = self.path_root[v]
            self.path_parent[to] = self.path_parent[v]
            stack1.add((to, 0))

proc sub_tree*(self: var HeavyLightDecomposition, v: Natural): (Natural, Natural) =
    return (self.left[v], self.right[v])

proc path*(self: var HeavyLightDecomposition, v, u: Natural): seq[(Natural, int)] =
    var
        x = v
        y = u
        res = newSeq[(Natural, int)]()
        p: Natural
    while self.path_root[x] != self.path_root[y]:
        if self.left[x] < self.left[y]:
            p = self.path_root[y]
            res.add((self.left[p], self.left[y] + 1))
            y = self.path_parent[y]
        else:
            p = self.path_root[x]
            res.add((self.left[p], self.left[x] + 1))
            x = self.path_parent[x]
    res.add((min(self.left[x], self.left[y]), max(self.left[x], self.left[y]) + 1))
    return res


proc bit_length(n: Natural): Natural =
    const BIT_SIZE = 24
    if n == 0:
      return 0
    let s = toBin(n, BIT_SIZE)
    return BIT_SIZE - s.find('1')


type
    LazySegmentTree*[T, K] = ref object
        LV: Natural
        N0: Positive
        ide_ele: T
        lazy_ide_ele: K
        data: seq[T]
        lazy_data: seq[K]
        fold: proc (a, b: T): T
        eval: proc (a: T, b: K): T
        merge: proc (a, b: K): K

proc initLazySegmentTree*[T, K](size: Positive, ide_ele: T, lazy_ide_ele: K, fold: proc (a, b: T): T, eval: proc (a: T, b: K): T, merge: proc (a, b: K): K): LazySegmentTree[T, K] =
    var
        LV = bit_length(size - 1)
        N0 = 1 shl LV
        data = newSeqWith(2*N0, ide_ele)
        lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    return LazySegmentTree[T, K](LV: LV, N0: N0, ide_ele: ide_ele, lazy_ide_ele: lazy_ide_ele, data: data, lazy_data: lazy_data, fold: fold, eval: eval, merge: merge)

proc toLazySegmentTree*[T, K](init_value: openArray[T], ide_ele: T, lazy_ide_ele: K, fold: proc (a, b: T): T, eval: proc (a: T, b: K): T, merge: proc (a, b: K): K): LazySegmentTree[T, K] =
    var
        LV = bit_length(init_value.len - 1)
        N0 = 1 shl LV
        data = newSeqWith(2*N0, ide_ele)
        lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    for i, x in init_value:
        data[i + N0 - 1] = x
    for i in countdown(N0 - 2, 0):
        data[i] = fold(data[2*i + 1], data[2*i + 2])
    return LazySegmentTree[T, K](LV: LV, N0: N0, ide_ele: ide_ele, lazy_ide_ele: lazy_ide_ele, data: data, lazy_data: lazy_data, fold: fold, eval: eval, merge: merge)

iterator gindex*[T, K](self: var LazySegmentTree[T, K], left, right: Natural): Natural =
    var
        L = (left + self.N0) shr 1
        R = (right + self.N0) shr 1
        lc = if (left and 1) == 1: 0 else: bit_length(L and -L)
        rc = if (right and 1) == 1: 0 else: bit_length(R and -R)
    for i in 0..<self.LV:
        if rc <= i:
            yield R
        if L < R and lc <= i:
            yield L
        L = L shr 1
        R = R shr 1

proc propagates*[T, K](self: var LazySegmentTree[T, K], ids: seq[Natural]) =
    var
        idx: Natural
        v: K
    for id in reversed(ids):
        idx = id - 1
        v = self.lazy_data[idx]
        if v == self.lazy_ide_ele:
            continue
        # v = v shr 1
        self.data[2*idx + 1] = self.eval(self.data[2*idx + 1], v)
        self.data[2*idx + 2] = self.eval(self.data[2*idx + 2], v)
        self.lazy_data[2*idx + 1] = self.merge(self.lazy_data[2*idx + 1], v)
        self.lazy_data[2*idx + 2] = self.merge(self.lazy_data[2*idx + 2], v)
        self.lazy_data[idx] = self.lazy_ide_ele

proc update*[T, K](self: var LazySegmentTree[T, K], left, right: Natural, x: K) =
    let ids = toSeq(self.gindex(left, right))
    # self.propagates(ids)
    var
        L = left + self.N0
        R = right + self.N0
        # x = x
    
    while L < R:
        if (L and 1) == 1:
            self.lazy_data[L - 1] = self.merge(self.lazy_data[L - 1], x)
            self.data[L - 1] = self.eval(self.data[L - 1], x)
            inc L
        if (R and 1) == 1:
            dec R
            self.lazy_data[R - 1] = self.merge(self.lazy_data[R - 1], x)
            self.data[R - 1] = self.eval(self.data[R - 1], x)
        L = L shr 1
        R = R shr 1
        # x = x shl 1
    var idx: Natural
    for id in ids:
        idx = id - 1
        self.data[idx] = self.eval(self.fold(self.data[2*idx + 1], self.data[2*idx + 2]), self.lazy_data[idx])

proc query*[T, K](self: var LazySegmentTree[T, K], left, right: Natural): T =
    self.propagates(toSeq(self.gindex(left, right)))
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
    S, C, ans: seq[int]
    init_val: seq[(int, int)]
    hld: HeavyLightDecomposition
    lazy_seg_tree: LazySegmentTree[(int, int), int]

proc solve() =
    let N = input().parseInt
    S = input().split.map(parseInt)
    C = input().split.map(parseInt)

    hld = initHeavyLightdecomposition(N)
    var ai, bi: int
    for _ in 0..<N - 1:
        (ai, bi) = input().split.mapIt(it.parseInt - 1)
        hld.add_edge(ai, bi)
    hld.build(0)

    init_val = newSeqWith(N, (0, 0))
    for i, (si, ci) in zip(S, C):
        let idx = hld.sub_tree(i)[0]
        init_val[idx] = (si, ci)
    lazy_seg_tree = toLazySegmentTree(init_val, (0, 0), 0, (a, b) => ((a[0] + b[0]) mod MOD, (a[1] + b[1]) mod MOD),
                                      (a, b) => ((a[0] + a[1]*b) mod MOD, a[1]), (a, b) => (a + b) mod MOD)

    let Q = input().parseInt
    var xi, yi, zi, cost: int
    for _ in 0..<Q:
        let inputs = input().split.map(parseInt)
        if inputs[0] == 0:
            (xi, yi, zi) = inputs[1..^1]
            dec xi; dec yi
            for (left, right) in hld.path(xi, yi):
                lazy_seg_tree.update(left, right, zi)
        else:
            (xi, yi) = inputs[1..^1]
            dec xi; dec yi
            cost = 0
            for (left, right) in hld.path(xi, yi):
                cost += lazy_seg_tree.query(left, right)[0]
            cost %= MOD
            ans.add(cost)
    echo ans.join("\n")

when is_main_module:
    solve()
