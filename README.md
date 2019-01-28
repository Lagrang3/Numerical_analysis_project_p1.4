# Numerical analysis project p1.4
Final exam of Numerical Analysis for the Master in High Performance Computing

author: Myself

### Assignment 1.
See file `methods.py`. Here below the performance of
the distance functions implemented, running on an array size of *NxN*
with *N=1000*. The complexity is *O(N^2)*.

```
dist_oo at 1000: 	0.00952 seconds
dist_1 at 1000: 	0.00592 seconds
dist_2 at 1000: 	0.00905 seconds
```

### Assignment 2.
See file `init.py`. Here below the performance of the
computation of matrix distances for *N* images of size 
*SxS* with *S=28* and *N=100*. The complexity is *O(N^2 S^2)*.

```
dist_oo at 100: 0.14429 seconds
dist_1 at 100: 	0.14468 seconds
dist_2 at 100: 	0.14166 seconds
```

### Assignment 3.

Distance table for the first *N=100* images using the function `dist_oo`.
<img src="./dist_oo.png" alt="Drawing" style="width: 800px;"/>

Distance table for the first *N=100* images using the function `dist_1`.
<img src="./dist_1.png" alt="Drawing" style="width: 800px;"/>

Distance table for the first *N=100* images using the function `dist_2`.
<img src="./dist_2.png" alt="Drawing" style="width: 800px;"/>

### Assignment 4.
See file `init.py`

### Assignment 5.

Distance table error for three different distance functions.
<img src="./all_dist_err.png" alt="Drawing" style="width: 800px;"/>
