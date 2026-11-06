class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkCompartment(n):
            print("***********" + str(n) + "**********")
            checker3 = [False] * 9
            startj = (n % 3) * 3
            endj = ((n % 3) * 3) + 3 
            starti = (n // 3)*3
            endi = starti + 3
            for i in range(starti , endi):
                for j in range(startj, endj):
                    print(board[i][j], i, j)
                    if (board[i][j] != "."):
                        currentBoxNum = int(board[i][j])
                        if (not checker3[currentBoxNum - 1]):
                            checker3[currentBoxNum - 1] = True
                        else:
                            return False
            return True

            print("*************************************")
        def outputBoard():
            for i in range(9):
                for j in range(9):
                    print(board[i][j] + " ", end="")
                print()

        outputBoard()
        for i in range(len(board)):
            checker1 = [False] * 9
            checker2 = [False] * 9
            for j in range(len(board[0])):
                if (board[i][j] != "."):
                    currentRowNum = int(board[i][j])
                    if (not checker1[currentRowNum - 1]):
                        checker1[currentRowNum - 1] = True
                    else:
                        return False
                if (board[j][i] != "."):
                    currentColNum = int(board[j][i])
                    if (not checker2[currentColNum - 1]):
                        checker2[currentColNum - 1] = True
                    else:
                        return False

            if(not checkCompartment(i)):
                return False
        

        return True
