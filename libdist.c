/*
	C shared library to solve Poisson equation	
	
	Written by myself sometime around three weeks ago.
	
	License is Copycenter.
*/

#include <stdlib.h>
#include <math.h>


/*
	Poisson equation solver.	
*/
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


