import algorithm, deques, heapqueue, math, sets, sequtils, strutils, sugar, tables

proc input*(): string =
    return stdin.readLine
proc chmax*[T: SomeNumber](num0: var T, num1: T) =
    num0 = max(num0, num1)
proc chmin*[T: SomeNumber](num0: var T, num1: T) =
    num0 = min(num0, num1)
proc `%=`*[T: SomeInteger](num0: var T, num1: T) =
    num0 = num0 mod num1

proc solve() =
    var P, Q, R: float
    (P, Q, R) = input().split.map(parseFloat)

    echo 1.0 - min([P, Q, R]) / (P + Q + R)

when is_main_module:
    solve()
