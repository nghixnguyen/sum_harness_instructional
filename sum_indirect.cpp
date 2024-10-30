#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>
#include <cstdio>



void 
setup(int64_t N, uint64_t A[])
{
   for (int64_t i = 0; i < N; ++i) {
      A[i] = rand() % N;
   }
   printf(" inside sum_indirect problem_setup, N=%lld \n", N);
}

int64_t
sum(int64_t N, uint64_t A[])
{
   int64_t sum = 0;
   int64_t indx = A[0];
   for (int64_t i = 0; i < N; ++i) {
      sum += A[indx];
      indx = A[indx];
   }
   printf(" inside sum_indirect perform_sum, N=%lld \n", N);
   return sum;
}

