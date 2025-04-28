'''
8 3
1 3 -1 -3 5 3 6 7
'''

import sys
from collections import deque

def sliding_window(n, k, arr):
    min_result = []
    max_result = []
    
    min_q = deque()
    for i in range(n):
        # 移除超出窗口范围的元素
        while min_q and min_q[0] <= i - k:
            min_q.popleft()
        
        # 维护单调递增队列
        while min_q and arr[min_q[-1]] >= arr[i]:
            min_q.pop()
        
        min_q.append(i)
        
        # 当窗口形成后开始记录结果
        if i >= k - 1:
            min_result.append(str(arr[min_q[0]]))
    
    max_q = deque()
    for i in range(n):
        while max_q and max_q[0] <= i - k:
            max_q.popleft()
        
        while max_q and arr[max_q[-1]] <= arr[i]:
            max_q.pop()
        
        max_q.append(i)
        
        if i >= k - 1:
            max_result.append(str(arr[max_q[0]]))
    
    print(' '.join(min_result))
    print(' '.join(max_result))

n,k = map(int, input().split())
arr = list(map(int, input().split()))
sliding_window(n, k, arr)
