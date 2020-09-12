import algorithm, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
    return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
    num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
    num0 = min(num0, num1)


proc bit_length(n: Natural): Natural =
    if n == 0:
      return 0
    let s = toBin(n, 60)
    return 60 - s.find('1')


type
    DuelSegmentTree*[T] = ref object
        LV: Natural
        N0: Positive
        lazy_ide_ele: T
        lazy_data: seq[T]

proc initDuelSegmentTree*[T](size: Positive, lazy_ide_ele: T): DuelSegmentTree[T] =
    var
        LV = bit_length(size - 1)
        N0 = 1 shl LV
    return DuelSegmentTree[T](LV: LV, N0: N0, lazy_ide_ele: lazy_ide_ele, lazy_data: newSeqWith(2 * N0, lazy_ide_ele))

iterator gindex*[T](self: var DuelSegmentTree[T], left, right: Natural): Natural =
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

proc propagates*[T](self: var DuelSegmentTree[T], ids: seq[Natural]) =
    var
        idx: Natural
        v: T
    for id in reversed(ids):
        idx = id - 1
        v = self.lazy_data[idx]
        if v == self.lazy_ide_ele:
            continue
        self.lazy_data[2*idx + 1] = v
        self.lazy_data[2*idx + 2] = v
        self.lazy_data[idx] = self.lazy_ide_ele

proc update*[T](self: var DuelSegmentTree[T], left, right: Natural, x: T) =
    self.propagates(toSeq(self.gindex(left, right)))
    var
        L = left + self.N0
        R = right + self.N0
    
    while L < R:
        if (L and 1) == 1:
            self.lazy_data[L - 1] = x
            inc L
        if (R and 1) == 1:
            dec R
            self.lazy_data[R - 1] = x
        L = L shr 1
        R = R shr 1

proc query*[T](self: var DuelSegmentTree[T], k: Natural): T =
    var ids = self.gindex(k, k + 1)
    self.propagates(toSeq(self.gindex(k, k + 1)))
    return self.lazy_data[k + self.N0 - 1]


var
    a, sorted_a, a_left, a_right, ans: seq[int]
    a_set: HashSet[int]
    compress: Table[int, int]
    duel_seg_tree: DuelSegmentTree[int]


proc solve() =
    let n = input().parseInt
    a = input().split.map(parseInt)

    a_set = toHashSet(a)
    sorted_a = sorted(toSeq(a_set.items))
    compress = initTable[int, int]()
    for idx, val in sorted_a:
        compress[val] = idx
    
    (a_left, a_right) = (newSeqWith(compress.len, -1), newSeqWith(compress.len, -1))
    for i, ai in a:
        if a_left[compress[ai]] == -1:
            a_left[compress[ai]] = i
        else:
            a_right[compress[ai]] = i
    
    duel_seg_tree = initDuelSegmentTree(n, 0)
    for i, ai in sorted_a:
        if a_right[i] != -1:
            duel_seg_tree.update(a_left[i], a_right[i] + 1, ai)
        else:
            duel_seg_tree.update(a_left[i], a_left[i] + 1, ai)
    
    ans = newSeq[int](n)
    for i in 0..<n:
        ans[i] = duel_seg_tree.query(i)
    echo ans.join(" ")


when is_main_module:
    solve()
