# Numerical analysis project p1.4
Final exam of Numerical Analysis for the Master in High Performance Computing

author: Myself

## Instructions

Do `make` to compile the shared libraries,
and `make check` to run test.

### Assignment 1.
See file `methods.py`. 
Here below the performance of
the distance functions implemented, running on an array size of *NxN*
with *N=1000*. The complexity is *O(N^2)*.

```
dist_oo for images of size (1000, 1000): 0.00948 seconds
dist_1 for images of size (1000, 1000): 0.00583 seconds
dist_2 for images of size (1000, 1000): 0.00899 seconds
```

### Assignment 2.
See file `init.py`. 
Here below the performance of the
computation of matrix distances for *N* images of size 
*SxS* with *S=28* and *N=100*. The complexity is *O(N^2 S^2)*.

```
dist_matrix for 100 images of size (28, 28) using dist_oo: 0.15924 seconds
dist_matrix for 100 images of size (28, 28) using dist_1: 0.14767 seconds
dist_matrix for 100 images of size (28, 28) using dist_2: 0.14563 seconds
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

### Assignment 6.

Here below the performance of
the distance function `dist_H`, running on an array size of *NxN*
with *N=1000*. The complexity is *O(N^2)*.
```
dist_H for images of size (1000, 1000): 0.06248 seconds
```
Here below the performance of the
computation of matrix distances for *N* images of size 
*SxS* with *S=28* and *N=100*. The complexity is *O(N^2 S^2)*.
```
dist_matrix for 100 images of size (28, 28) using dist_H: 0.46454 seconds
```

The errors of the distance table for *N=100,200,400,800,1600* are
`[0.24, 0.19, 0.155, 0.14625, 0.1175]` respectively.

Distance table for the first *N=100* images using the function `dist_2`.
<img src="./dist_H.png" alt="Drawing" style="width: 800px;"/>
