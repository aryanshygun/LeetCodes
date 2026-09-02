n = 124651

stack = []
check = (-1, -1)
n = reversed(list(str(n)))
n = [int(i) for i in n]
# nlist = [n[i] for i in range(len(str(n)))]

xmin = (0, 0)
xmax = (0, 0)

print(n)
# value = val 

for i in range(len(n)):
    if n[i] < xmin[1]:
        xmin = (i, n[i])
        break
    else:
        xmin = (i, n[i])
    


# for idx, val in enumerate(n):
#     print(idx, val)
    
#     # while stack and val < stack[-1]:
#     #     pass
#     # stack.append(i)
