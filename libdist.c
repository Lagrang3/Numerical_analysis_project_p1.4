#include <stdlib.h>
#include <math.h>

void csolve_poisson(const double* rho,double* phi,const size_t N){
	const size_t N2=N*N,T=56;
	for(size_t i=0;i<N2;++i)
		phi[i]=rho[i]*0.25;
		
	for(size_t t=0;t<T;++t)
		for(size_t i=0;i<N;++i)
			for(size_t j=0;j<N;++j){
				double left,right,top,down;
				
				if(i)
					top=phi[(i-1)*N+j];
				else
					top=0;
				
				if(j)
					left=phi[i*N+j-1];
				else 
					left=0;
				
				if(i<(N-1))
					down=phi[(i+1)*N+j];
				else
					down=0;
				
				if(j<(N-1))
					right=phi[i*N+j+1];
				else
					right=0;
			
				phi[i*N+j] = 0.25*(
					rho[i*N+j]
					+ left+right+top+down);
			}
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
