from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()
    
    def peek(self) -> T:
        if len(self._container) > 0:
            return self._container[-1]
        return None
    
    def size(self) -> int:
        return len(self._container)
    
    def get_items(self) -> List[T]:
        return self._container.copy()

    def __repr__(self):
        return repr(self._container)

def solve_hanoi(towers, begin, end, n, t, move_function=None):
    def hanoi(begin, end, n, t):
        count = n//(t-2)
        
        for i in range(2, t-1):
            hanoi3(towers[0], towers[t-i], towers[1], count)
        
        hanoi3(towers[0], towers[t-1], towers[1], n-(count*(t-3)))
        
        for i in range(t-2, 1, -1):
            hanoi3(towers[t-i], towers[t-1], towers[1], count)

    def hanoi3(begin, end, temp, n):
        if n == 0:
            return
        
        if n == 1:
            if move_function:
                move_function(begin, end)
            else:
                end.push(begin.pop())
        else:
            hanoi3(begin, temp, end, n - 1)
            hanoi3(begin, end, temp, 1)
            hanoi3(temp, end, begin, n - 1)

    hanoi(begin, end, n, t)