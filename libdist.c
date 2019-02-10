#include <stdlib.h>
#include <math.h>

void csolve_poisson(const double* rho,double* phi,const size_t N){
	const size_t Np2=N+2,T=56;
	double *buff = (double*)malloc(Np2*Np2*sizeof(double));
	
	// boundaries to zero
	for(size_t i=0;i<Np2;++i)
		buff[i*Np2+(0)]=buff[i*Np2+(N+1)]=buff[(0)*Np2+i]=buff[(N+1)*Np2+i]=0;
	
	// estimate for starting values
	for(size_t i=1;i<=N;++i)
		for(size_t j=1;j<=N;++j)
			buff[ i*Np2 +j ] = 0.25*rho[(i-1)*N+(j-1)] ;
	
	// iterate to solution
	for(size_t t=0;t<T;++t)
		for(size_t i=1;i<=N;++i)
			for(size_t j=1;j<=N;++j){
				buff[i*Np2+j] = 0.25*(
					rho[(i-1)*N+(j-1)]
					+ buff[(i-1)*Np2+j] + buff[(i+1)*Np2+j] 
					+ buff[i*Np2+(j-1)] + buff[i*Np2+(j+1)]);
			}
	
	// copy data to output buffer
	for(size_t i=1;i<=N;++i)
		for(size_t j=1;j<=N;++j)
			phi[(i-1)*N+(j-1)] = buff[ i*Np2 +j  ];
	
	free(buff);
}

double cdist_MA(const double* A,const double* B,const size_t N){
	const size_t N2=N*N,T=56,Npad=N+2;
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
	
	for(size_t t=0;t<T;++t)
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
