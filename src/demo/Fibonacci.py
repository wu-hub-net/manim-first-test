def Fibnacci(n: int)->int:
  #终止条件
  if(n <= 0): return 0
  if(n == 1): return 1
  #递归公式
  return Fibnacci(n - 1) + Fibnacci(n - 2)

# def Fibnacci_combo(n: int)->int:
#   if(n <= 0): return 0
#   #从1走到n层，相当于从0走到n - 1层
#   m = n - 1
#   res = 0
#   mid = m // 2 + 1
#   c = 1
#   10 
#   5
  
#   for k in range(mid):
#     res =