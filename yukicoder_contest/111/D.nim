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
    LazySegmentTree*[T] = ref object
        LV: Natural
        N0: Positive
        ide_ele, lazy_ide_ele: T
        data, lazy_data: seq[T]
        segfunc: proc (a, b: T): T

proc initLazySegmentTree*[T](size: Positive, ide_ele, lazy_ide_ele: T, f: proc (a, b: T): T): LazySegmentTree[T] =
    var
        LV = bit_length(size - 1)
        N0 = 1 shl LV
        data = newSeqWith(2*N0, ide_ele)
        lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    return LazySegmentTree[T](LV: LV, N0: N0, ide_ele: ide_ele, lazy_ide_ele: lazy_ide_ele, data: data, lazy_data: lazy_data, segfunc: f)

proc toLazySegmentTree*[T](init_value: openArray[T], ide_ele, lazy_ide_ele: T, f: proc (a, b: T): T): LazySegmentTree[T] =
    var
        LV = bit_length(init_value.len - 1)
        N0 = 1 shl LV
        data = newSeqWith(2*N0, ide_ele)
        lazy_data = newSeqWith(2*N0, lazy_ide_ele)
    for i, x in init_value:
        data[i + N0 - 1] = x
    for i in countdown(N0 - 2, 0):
        data[i] = f(data[2*i + 1], data[2*i + 2])
    return LazySegmentTree[T](LV: LV, N0: N0, ide_ele: ide_ele, lazy_ide_ele: lazy_ide_ele, data: data, lazy_data: lazy_data, segfunc: f)

iterator gindex*[T](self: var LazySegmentTree[T], left, right: Natural): Natural =
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

proc propagates*[T](self: var LazySegmentTree[T], ids: seq[Natural]) =
    var
        idx: Natural
        v: T
    for id in reversed(ids):
        idx = id - 1
        v = self.lazy_data[idx]
        if v == self.lazy_ide_ele:
            continue
        self.data[2*idx + 1] = v shr 1
        self.data[2*idx + 2] = v shr 1
        self.lazy_data[2*idx + 1] = v shr 1
        self.lazy_data[2*idx + 2] = v shr 1
        self.lazy_data[idx] = self.lazy_ide_ele

proc update*[T](self: var LazySegmentTree[T], left, right: Natural, x: T) =
    let ids = toSeq(self.gindex(left, right))
    self.propagates(ids)
    var
        L = left + self.N0
        R = right + self.N0
        x = x
    
    while L < R:
        if (L and 1) == 1:
            self.lazy_data[L - 1] = x
            self.data[L - 1] = x
            inc L
        if (R and 1) == 1:
            dec R
            self.lazy_data[R - 1] = x
            self.data[R - 1] = x
        L = L shr 1
        R = R shr 1
        x = x shl 1
    var idx: Natural
    for id in ids:
        idx = id - 1
        self.data[idx] = self.segfunc(self.data[2*idx + 1], self.data[2*idx + 2])# + self.lazy_data[idx]

proc query*[T](self: var LazySegmentTree[T], left, right: Natural): T =
    self.propagates(toSeq(self.gindex(left, right)))
    var
        L = left + self.N0
        R = right + self.N0
        res = self.ide_ele
    
    while L < R:
        if (L and 1) == 1:
            res = self.segfunc(res, self.data[L - 1])
            inc L
        if (R and 1) == 1:
            dec R
            res = self.segfunc(res, self.data[R - 1])
        L = L shr 1
        R = R shr 1
    return res


var lazy_seg_tree_a, lazy_seg_tree_b: LazySegmentTree[int]

proc solve() =
    let
        N = input().parseInt
        Q = input().parseInt
    
    lazy_seg_tree_a = initLazySegmentTree(N, 0, -1, (a, b) => a + b)
    lazy_seg_tree_b = initLazySegmentTree(N, 0, -1, (a, b) => a + b)
    var score_a, score_b, xi, li, ri, cnt_a, cnt_b: int
    for _ in 0..<Q:
        (xi, li, ri) = input().split.map(parseInt)
        if xi == 0:
            cnt_a = lazy_seg_tree_a.query(li, ri + 1)
            cnt_b = lazy_seg_tree_b.query(li, ri + 1)
            if cnt_a < cnt_b:
                score_b += cnt_b
            elif cnt_b < cnt_a:
                score_a += cnt_a
        elif xi == 1:
            lazy_seg_tree_a.update(li, ri + 1, 1)
            lazy_seg_tree_b.update(li, ri + 1, 0)
        else:
            lazy_seg_tree_a.update(li, ri + 1, 0)
            lazy_seg_tree_b.update(li, ri + 1, 1)
    
    score_a += lazy_seg_tree_a.query(0, N)
    score_b += lazy_seg_tree_b.query(0, N)
    echo score_a, " ", score_b

when is_main_module:
    solve()
