lr=0.0000001
iteration=1500000
w1=1
b=1;
a=[ [1,890],
    [2,-1411],
    [2,-1560],
    [3,-2220],
    [3,-2091],
    [4,-2878],
    [5,-3537],
    [6,-3268], [6,-3920], [6,-4163]
    ,[8,-5471], [10,-5157]]
m=len(a)
for i in range(0,iteration):
    b_grad=0
    w1_grad=0
    for j in range(0,m-1):
        b_grad=b_grad-2*(a[j][1]-(b+w1*a[j][0]))
        w1_grad=w1_grad-2*a[j][0]*(a[j][1]-(b+w1*a[j][0]))
    b=b-lr*b_grad
    w1=w1-lr*w1_grad
    if(abs(w1_grad)<10e-5 and abs(b_grad)<10e-5):
        break



print (w1,b)