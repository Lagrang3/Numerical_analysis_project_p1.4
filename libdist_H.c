#include <stdlib.h>
#include <math.h>
#include <stdio.h>

double dist_H(const double* A,const double *B,const size_t N){
	const size_t N2=N*N;
	double nA=0,nB=0;

	for(size_t i=0;i<N2;++i){
		nA += fabs(A[i]),
		nB += fabs(B[i]);
	}
	double inA = 1./nA, inB = 1./nB, I=0.;
	
	for(size_t i=0;i<N2;++i){
		double v = A[i]*inA - B[i]*inB;
		I += v*v;
	}
	
	for(size_t i=0;i<N;++i)
		for(size_t j=0;j<N;++j){
			double nextAx=0.,nextAy=0.,nextBx=0.,nextBy=0.;
			if(i<(N-1)){
				nextAx = A[(i+1)*N+j];
				nextBx = B[(i+1)*N+j];
			}
			if(j<(N-1)){
				nextAy = A[i*N+j+1];
				nextBy = B[i*N+j+1];
			}
			double vx = (nextAx-A[i*N+j])*inA - (nextBx-B[i*N+j])*inB;
			double vy = (nextAy-A[i*N+j])*inA - (nextBy-B[i*N+j])*inB;
			I += vx*vx + vy*vy;
		}
	
	return sqrt(I);
}
