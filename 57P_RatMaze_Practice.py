class OmniCreate:

    def printmatrix(self, tria):

        for anim in tria:
            print(anim, end="\n")

    def isSafe(self, ekahs, current_M, current_N, N):
    
        if current_M >= 0 and current_M < N and current_N >= 0  and current_N < N and ekahs[current_M][current_N] == 1:
            return True

        return False


    def find_paths(self, ekahs, current_M, current_N, N, best_paths):

        """Base Condition to return best_paths"""
        if current_M == N - 1 and current_N == N - 1:
            best_paths[current_M][current_N] == 1
            print(best_paths[current_M][current_N])
            return True
        
        if self.isSafe(ekahs, current_M, current_N, N) == True:

            best_paths[current_M][current_N] == 1

            if self.find_paths(ekahs, current_M+1, current_N, N, best_paths) == True:
                return True
    
            if self.find_paths(ekahs, current_M, current_N+1, N, best_paths) == True:
                return True


            best_paths[current_M][current_N] == 0

            return False
  
    
    def ratMaze(self, ekahs, N):

        best_paths = [[0 for anim in range(N)] for anim in range(N)]

        if self.find_paths(ekahs, 0, 0, N, best_paths) == False:
            print('No Paths')
            return False
            
        print(self.printmatrix(best_paths))
        return True


create = OmniCreate()

print(create.ratMaze([[1, 0, 0, 0],
			          [1, 1, 0, 1],
			          [0, 1, 0, 0],
			          [1, 1, 1, 1]], 4))