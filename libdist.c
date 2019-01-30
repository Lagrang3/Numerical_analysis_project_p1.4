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


	for(size_t i=1;i<N;++i)
		for(size_t j=1;j<N;++j){
			double vx,vy;
			vx = (A[i*N+j]-A[(i-1)*N+j])*inA 
				- (B[i*N+j]-B[(i-1)*N+j])*inB;
			vy = (A[i*N+j]-A[i*N+(j-1)])*inA 
				- (B[i*N+j]-B[i*N+(j-1)])*inB;
			I += vx*vx + vy*vy;
		}
	for(size_t i=1;i<N;++i){
		double vx,vy;
		vx=(A[i*N]-A[(i-1)*N])*inA-(B[i*N]-B[(i-1)*N])*inB;
		vy=(A[i]-A[i-1])*inA-(B[i]-B[i-1])*inB;
		I+= vx*vx+vy*vy;
	}
	
	return sqrt(I);
}

double dist_MA(const double* A,const double* B,const size_t N){
	const size_t N2=N*N,T= 100,Npad=N+2;
	double nA=0,nB=0;
	double *phi = (double*)malloc(Npad*Npad*sizeof(double)),
			*At = (double*)malloc(Npad*Npad*sizeof(double)),
			*Bt = (double*)malloc(Npad*Npad*sizeof(double));
	for(size_t i=0;i<N2;++i){ // compute the normalization
		nA+=A[i],
		nB+=B[i];
	}
	double inA=1./nA,inB=1./nB;

	for(size_t i=1;i<=N;++i)//boundaries set to zero
		phi[i*Npad+0]=phi[i*Npad+(N+1)]=phi[0*Npad+i]=phi[(N+1)*Npad+i]=0;
	
	for(size_t i=1;i<=N;++i)
		for(size_t j=1;j<=N;++j){
			At[i*Npad+j] = A[(i-1)*N+(j-1)]*inA;
			Bt[i*Npad+j] = B[(i-1)*N+(j-1)]*inB;
			phi[i*Npad+j] = (At[i*Npad+j]-Bt[i*Npad+j])*0.25;
		}
	
	for(int t=0;t<T;++t)
		for(size_t i=1;i<=N;++i)
			for(size_t j=1;j<=N;++j){
				phi[i*Npad+j] = 0.25*(
					At[i*Npad+j]-Bt[i*Npad+j] 
					+ phi[i*Npad+j-1]+phi[i*Npad+j+1]
					+ phi[(i+1)*Npad+j] + phi[(i-1)*Npad+j]);
			}
	
	double I=0;
	for(size_t i=1;i<=N;++i)
		for(size_t j=1;j<=N;++j){
			double vx = phi[(i+1)*Npad+j]-phi[(i-1)*Npad+j],
				vy = phi[i*Npad+j+1]-phi[i*Npad+j-1];
//				s = A[(i-1)*N+(j-1)]-B[(i-1)*N+(j-1)];
			I += ( vx*vx+vy*vy);
		}
		
	
	free(At);	
	free(Bt);	
	free(phi);
	return sqrt(I);
}
