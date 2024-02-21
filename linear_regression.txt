y = m1*x1 + m2*x2 ... + b => fitting curve
x1,x2 ...=> Independent variables
y => Dependent varibles

Now, given dataset containing x and y values,
We need to find the the slopes and intercept of fitting curve, by which it fits best to the datas with minimizing cost function.
Where cost function gives us the idea of how far or closer the datas are to approximated curve.
Cost fucntion can be minimized using Least Square Method(Traditional), Gradient Descent Method(Iterative and better method).

From the picture: gd_algo,
J => cost function
a0,a1 => fucntion parameters which corresponds to m and b of fitting curve
alpha(α) => Learing factor should be in the range 0.01(Significance of alpha value in parameter convergence and oscillations) 
By following these iterative steps, we can successfully approximate m and b of the fitting curve.

