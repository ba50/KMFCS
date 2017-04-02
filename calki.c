#include "calki.h"

double get_S(int i, int j, int k, int l, double alpha)
{
 double a,A,B,C,D;
 double S=0.0;
 a=a0;
 A=alpha/(i*i*i);
 B=alpha/(j*j*j);
 C=alpha/(k*k*k);
 D=alpha/(l*l*l);
 S=pow(Pi,(3./2.))/(pow((A+B+C+D),(3./2.)));
 S=S*exp(-4.*a*a*(A+C)*(B+D)/(A+B+C+D));
 return S;
}

double get_T(int i, int j, int k, int l, double alpha)
{
 double a,A,B,C,D;
 double aux1,aux2;
 double T=0.;
 a=a0;
 A=alpha/(i*i*i);
 B=alpha/(j*j*j);
 C=alpha/(k*k*k);
 D=alpha/(l*l*l);
 aux1=(3.*(A+B)*(C+D))/(pow((A+B+C+D),(5./2.)));
 aux2=(8.*a*a*(B*C-A*D)*(B*C-A*D))/(pow((A+B+C+D),(7./2.)));
 T=pow(Pi,(3./2.))*(aux1-aux2);
 T=T*exp(-4.*a*a*(A+C)*(B+D)/(A+B+C+D));
 return T;
}

double get_V(int i, int j, int k, int l, int part, double alpha)
{
 double a,A,B,C,D;
 double aux1,aux2;
 aux1 = 0.0;
 aux2 = 0.0;
 double V=0.;
 a=a0;
 A=alpha/(i*i*i);
 B=alpha/(j*j*j);
 C=alpha/(k*k*k);
 D=alpha/(l*l*l);
 if(part==1) aux1=B+D;
 if(part==2) aux1=A+C;
 aux2=2.*(a*aux1)/(sqrt(A+B+C+D));
 V=(-1.)*pow(Pi,(3./2.))*(1./(2.*a*aux1*sqrt(A+B+C+D)));
 V=V*erf(aux2);
 V=V*exp(-4.*a*a*(A+C)*(B+D)/(A+B+C+D));
 return V;
}

