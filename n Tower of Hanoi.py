from typing import TypeVar, Generic, List
T = TypeVar('T')
class Stack(Generic[T]):
    def __init__(self):
        self._container: List[T] = []
    def push(self, item:T) -> None:
        self._container.append(item)
    def pop(self) -> T:
        return self._container.pop()
    def __repr__(self):
        return repr(self._container)

def hanoi(begin: int, end: int, n: int, t: int):
    for i in range(2, t-1):
        towers[i].push(towers[begin].pop())
    hanoi3(towers[0], towers[t-1], towers[1], n-t+3)
    for i in range(t-2, 1, -1):
        towers[end].push(towers[i].pop())

def hanoi3(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi3(begin, temp, end, n - 1)
        hanoi3(begin, end, temp, 1)
        hanoi3(temp, end, begin, n - 1)

if __name__ == '__main__':
    num_discs: int = int(input())
    num_towers: int = int(input('Number of Towers: '))
    towers = []
    for i in range(num_towers):
        temp: Stack[int] = Stack()
        towers.append(temp)
        del temp
    for i in range(1, num_discs+1):
        towers[0].push(i)
    hanoi(0, num_towers-1, num_discs, num_towers)
    print(towers)