def solve(self, A, B):
        for i in range(0,len(A)):
              for j in range(i+1, len(A)):
                  if (A[i]+A[j]) == B :
                      return 1
        return 0