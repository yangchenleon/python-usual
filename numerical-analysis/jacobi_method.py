def checkit(loads,oldlds,tol):
#检查多个未知数的收敛
  neq=loads.shape[0]
  big=0.0
  converged=True
  for i in range(1,neq+1):
    if abs(loads[i-1,0])>big:
      big=abs(loads[i-1,0])
  for i in range(1,neq+1):
    if abs(loads[i-1,0]-oldlds[i-1,0])/big>tol:
      converged=False
  checkit=converged
  return  checkit

def eliminate(a,b):
  n=a.shape[0]
##确定主对角线最大值
  for i in range(1,n):
    big=abs(a[i-1,i-1]);ihold=i
    for j in range(i+1,n+1):
      if abs(a[j-1,i-1])>big:
        big=abs(a[j-1,i-1]); ihold=j
    if ihold!=i:
      for j in range(i,n+1):
        hold=a[i-1,j-1]; a[i-1,j-1]=a[ihold-1,j-1]; a[ihold-1,j-1]=hold
      hold=b[i-1,0]; b[i-1,0]=b[ihold-1,0]; b[ihold-1,0]=hold
##消元阶段
    for j in range(i+1,n+1):
      fac=a[j-1,i-1]/a[i-1,i-1]
      for l in range(i,n+1):
        a[j-1,l-1]=a[j-1,l-1]-a[i-1,l-1]*fac
      b[j-1]=b[j-1]-b[i-1]*fac
##从后迭代
  for i in range(n,0,-1):
    hold=0.0
    for l in range(i+1,n+1):
      hold=hold+a[i-1,l-1]*b[l-1]
    b[i-1]=(b[i-1]-hold)/a[i-1,i-1]
  return b

#雅可比主对角线化求对称矩阵的特征值
import numpy as np
import math
n=3;tol=1.0e-5;limit=100
enew=np.zeros((n,1))
eold=np.zeros((n,1))
p=np.zeros((n,n))
a1=np.zeros((n,n))
# a=np.array([[10,5,6],[5,20,4],[6,4,30]],dtype=np.float)
a=np.array([[1,2,0],[2, -1, 1], [0, 1, 3]],dtype=np.float)
a2=a
pi=math.acos(-1)
x=np.zeros((n,1))
x=np.ones((3,1),dtype=np.float)
print('雅可比主对角线化求对称矩阵的特征值')
print('矩阵A')
print(a[:])
print('前几次迭代值')
iters=0;eold[:]=0
while(True):
    iters=iters+1
    big=0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if abs(a[i-1,j-1]>big):
                big=abs(a[i-1,j-1]);hold=a[i-1,j-1];nr=i;nc=j
    if abs(big)<1.0e-20:
        break
    den=a[nr-1,nr-1]-a[nc-1,nc-1]
    if abs(den)<1.0e-20:
        alpha=pi/4.0
        if hold<0:
            alpha=-alpha
    else:
        alpha=math.atan(2.0*hold/den)/2.0
    ct=math.cos(alpha);st=math.sin(alpha);p[:]=0
    for i in range(1,n+1):
        p[i-1,i-1]=1.0
    p[nr-1,nr-1]=ct;p[nc-1,nc-1]=ct;p[nr-1,nc-1]=-st;p[nc-1,nr-1]=st
    a=np.dot(np.dot(np.transpose(p),a),p)
    if iters<5:
        for i in range(1,n+1):
            for j in range(1,n+1):
                print('{:13.4e}'.format(a[i-1,j-1]),end='')
            print(end='\n')
        print(end='\n')
    for i in range(1,n+1):
        enew[i-1,0]=a[i-1,i-1]
    if checkit(enew,eold,tol) or iters==limit:
        break
    eold[:,0]=enew[:,0]
print('迭代到收敛次数',iters)
print('最后的转化矩阵A')
for i in range(1,n+1):
    for j in range(1,n+1):
        print('{:13.4e}'.format(a[i-1,j-1]),end='')
    print(end='\n')
for i in range(1,n+1):
    a1[:]=a2[:]
    for j in range(1,n+1):
        a1[j-1,j-1]=a1[j-1,j-1]-a[i-1,i-1]
    x[:]=0;a1[i-1,i-1]=1.0e20;x[i-1]=1.0e20;x[:]=eliminate(a1,x)
    l2=np.linalg.norm(x)
    print('特征值','{:13.4e}'.format(a[i-1,i-1]))
    print('特征向量')
    for i in range(1,n+1):
        print('{:13.4e}'.format(x[i-1,0]/l2),end=' ')
    print()
    
    

