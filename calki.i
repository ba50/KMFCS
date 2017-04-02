%module calki

%{
#define SWIG_FILE_WITH_INIT
#include "calki.h"
%}

double get_S(int i, int j, int k, int l, double alpha);
double get_T(int i, int j, int k, int l, double alpha);
double get_V(int i, int j, int k, int l, int part, double alpha);
