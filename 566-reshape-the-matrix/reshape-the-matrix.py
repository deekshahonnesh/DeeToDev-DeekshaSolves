class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        total=m*n
        if r*c!=total:
           return mat
        else:
        
            k=[[0]*c for i in range(r)]
            for i in range(total):
                k[i//c][i%c]=mat[i//n][i%n]
        return k



        