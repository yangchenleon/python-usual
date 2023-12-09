# def ldlt(a,d):
#   n=a.shape[0]
#   for k in range(1,n):
#     d[0]=a[0,0]
#     if abs(a[k-1,k-1])>1.0e-10:
#       for i in range(k+1,n+1):
#         x=a[i-1,k-1]/a[k-1,k-1]
#         for j in range(k+1,n+1):
#           a[i-1,j-1]=a[i-1,j-1]-a[k-1,j-1]*x
#         d[i-1]=a[i-1,i-1]
#     else:
#       print('有0向量在第',k,'行')

# def ldlfor(a,b):
#   n=a.shape[0]
#   for i in range(1,n+1):
#     total=b[i-1]
#     if i>1:
#       for j in range(1,i):
#         total=total-a[j-1,i-1]*b[j-1]
#     b[i-1]=total/a[i-1,i-1]

# def subbac(a,b):
#   n=a.shape[0]
#   for i in range(n,0,-1):
#     total=b[i-1]
#     if i<n:
#       for j in range(i+1,n+1):
#         total=total-a[i-1,j-1]*b[j-1]
#     b[i-1]=total/a[i-1,i-1]

# #使用LDLT分解的高斯消元法
# import numpy as np
# import math
# n=3
# d=np.zeros((n,1))
# a=np.array([[3,-2,1],[-2,3,2],[1,2,2]],dtype=np.float)
# b=np.array([[3],[-3],[2]],dtype=np.float)
# print('系数矩阵')
# for i in range(1,n+1):
#     print(a[i-1,:])
# print('右手边向量',b)
# ldlt(a,d)
# print('下三角')
# for i in range(1,n+1):
#     print(a[i-1,0:i]/d[0:i])
# print('主对角项')
# print(d)
# ldlfor(a,b)
# for i in range(1,n+1):
#     a[i-1,:]=a[i-1,:]/d[i-1]
# subbac(a,b)
# print('解向量',b)   

import numpy as np
 
def LDLT(amatrix):
 
    if len(np.shape(amatrix)) != 2 or np.shape(amatrix)[0]!=np.shape(amatrix)[1]:
        print("error shape")
        return
    
    for i in range(np.shape(amatrix)[0]):
        for j in range(np.shape(amatrix)[1]):
            if amatrix[i][j] != amatrix[j][i]:
                print("The input matrix should be symmetric")
                return 
        
    n = np.shape(amatrix)[0] #dimension of matrix
 
    l = np.eye(n)
 
    d = np.zeros((n,n))
 
    for k in range(n):
 
        if k == 0:
 
            d[k][k] = amatrix[k][k]
 
            if d[k][k] == 0:
    
                print('error matrix type with 0 sequential principal minor determinant')
    
                return
            
            for m in range(n):
 
                l[m][k] = amatrix[m][k]/d[k][k]
        else:
 
            temp_sum1 = 0
 
            for m in range(k):
 
                temp_sum1 += amatrix[k][m]*l[k][m]
 
            d[k][k] = amatrix[k][k] - temp_sum1
 
            for j in range(k+1,n):
 
                temp_sum2 = 0
 
                for m in range(k):
 
                    temp_sum2 += amatrix[j][m]*l[k][m]
 
 
                amatrix[j][k] = amatrix[j][k] - temp_sum2
 
 
                l[j][k] = amatrix[j][k]/d[k][k]
 
    print("l")
    print(l)
    print('d')
    print(d)
 
    return l,d
 
 
 
a=[[5,-4,1],[-4,6,-4],[1,-4,-6]]
a=[[3, 3, 5], [3, 5, 9], [5, 9, 17]]
# a=[[6, 1, 0], [1, 4, 1], [0, 1, 14]]
# a = np.array([[3, 3, 5], [3, 3, 9], [5, 9, 17]],dtype=np.float)
# b = np.array([[10], [16], [30]],dtype=np.float)
# a = np.array([[6, 1, 0], [1, 4, 1], [0, 1, 14]])
# b = np.array([6, 24, 322])
 
l,d = LDLT(a)
 
print(np.dot(np.dot(l,d),l.T))
#print(np.shape(a))