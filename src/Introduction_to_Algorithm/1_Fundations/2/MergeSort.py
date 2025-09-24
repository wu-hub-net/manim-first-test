def merge_sort(arr,p,r):
  if(p >= r): return
  q = (p + r) // 2
  merge_sort(arr,p,q)
  merge_sort(arr,q + 1,r)
  merge(arr,p,q,r)

def merge(arr,p,q,r):
  length1 = q - p + 1
  length2 = r - q
  L = []
  R = []
  for i in range(length1):
    L.append(arr[p + i])
  for j in range(length2):
    R.append(arr[q + j + 1])
  i , j , k = 0, 0, p
  while(i < length1 and j < length2):
    if(L[i] <= R[j]):
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k += 1
  while(i < length1):
    arr[k] = L[i]
    i += 1
    k += 1
  while(j < length2):
    arr[k] = R[j]
    j += 1
    k += 1