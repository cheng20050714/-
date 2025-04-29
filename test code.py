from collections import deque

def solve():
    min_width = float('inf')
    max_q = deque()
    min_q = deque()
    left = 0
    
    for right in range(N):
        x_right_value, y_right_value = drops[right]
        
        # 维护单调队列（右边界）
        while max_q and drops[max_q[-1]][1] <= y_right_value:
            max_q.pop()
        max_q.append(right)
        
        while min_q and drops[min_q[-1]][1] >= y_right_value:
            min_q.pop()
        min_q.append(right)
        
        # 单调队列构建完成后
        # 开始改变窗口大小
        # 寻找符合条件的花盆长度D
        while left <= right and drops[max_q[0]][1] - drops[min_q[0]][1] >= D:
            current_width = x_right_value - drops[left][0]
            if current_width < min_width:
                min_width = current_width
            # 维护单调队列（左边届）
            if max_q[0] == left:
                max_q.popleft()
            if min_q[0] == left:
                min_q.popleft()
            left += 1
    
    print(min_width if min_width != float('inf') else -1)

N, D = map(int, input().split())
drops = []
for _ in range(N):
    x, y = map(int, input().split())
    drops.append((x, y))
drops.sort()

solve()