import numpy as np
def eig_power(A,v0,eps):
    uk = v0
    flag = 1
    val_old = 0
    n = 0
    while flag:
        n = n+1
        vk = A*uk        
        val = vk[np.argmax(np.abs(vk))]        
        uk = vk/val              
        if (np.abs(val-val_old)<eps):
            flag = 0
        val_old = val
        print(np.asarray(uk).flatten(),val)
    print('max eigenvalue:',val)
    print('eigenvector:',np.asarray(uk).flatten())
    print('iteration:',n)
    return val, uk  
    
if __name__ == '__main__':
    A = np.matrix([[1,   1,      0.5],
                   [1,   1,      0.25],
                   [0.5,   0.25,   2.0]], dtype='float')
    v0 = np.matrix([[1],[1],[1]], dtype='float')
    eps = 1e-10
    val,uk = eig_power(A,v0,eps)