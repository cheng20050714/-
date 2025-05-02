import sys
import math

MOD = 10**9 + 7

def solve():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    a = [0] + a

    # 计算前缀对数和
    prefix_log = [0.0] * (n + 1)
    for i in range(1, n + 1):
        prefix_log[i] = prefix_log[i - 1] + math.log2(a[i])
    
    max_log = -1.0
    max_prod = 0
    
    # 辅助函数：构造回文串并处理
    def update(l, r, center_val):
        nonlocal max_log, max_prod
        changes = 0
        cur_prod = center_val  
        
        while l >= 1 and r <= n:
            if a[l] != a[r]:
                changes += 1
            if changes > k:
                break
                
            cur_prod = (cur_prod * a[l] * a[r]) % MOD
            current_log = prefix_log[r] - prefix_log[l-1]
            
            if current_log > max_log or (current_log == max_log and cur_prod > max_prod):
                max_log = current_log
                max_prod = cur_prod
            
            l -= 1
            r += 1
    
    # 枚举每个可能的中心位置
    for i in range(1, n + 1):
        # 奇数长度回文串，中心是a[i]
        update(i - 1, i + 1, a[i])
        # 偶数长度回文串，中心是虚拟的1
        update(i, i + 1, 1)
    
    print(max_prod)

solve()