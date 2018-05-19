参考blog：http://blog.csdn.net/u012323318/article/
details/78759142

不懂得地方：在更新b w1 w2的值得时候 是用的所有的数据 ？？？

自己对于梯度下降理解的还不是很到位

1、用csvread函数

注意：csvread函数只试用与用逗号分隔的纯数字文件

第一种：M = CSVREAD('FILENAME') ，直接读取csv文件的数据，并返回给M

第二种：M = CSVREAD('FILENAME',R,C) ，读取csv文件中从第R-1行，第C-1列的数据开始的数据，这对带有头文件说明的csv文件(如示波器等采集的文件)的读取是很重要的。

第三种：M = CSVREAD('FILENAME',R,C,RNG)，其中 RNG = [R1 C1 R2 C2]，读取左上角为索引为(R1,C1) ,右下角索引为(R2,C2)的矩阵中的数据。

注意：matlab认为CSV第1行第1列的单元格坐标为（0,0）

2、zeros函数

=zeros(n)：生成n×n全零阵。


B=zeros(m,n)：生成m×n全零阵。


B=zeros([m n])：生成m×n全零阵。


B=zeros(d1,d2,d3……)：生成d1×d2×d3×……全零阵或数组。


B=zeros([d1 d2 d3……])：生成d1×d2×d3×……全零阵或数组。


B=zeros(size(A))：生成与矩阵A相同大小的全零阵。