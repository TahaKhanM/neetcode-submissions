class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if (board[i][j] != "."):
                    num = int(board[i][j])
                    if not (num in rows[i]):
                        rows[i].add(num)
                    else:
                        print("row fail")
                        return False
                    
                    if not (num in cols[j]):
                        cols[j].add(num)
                    else:
                        print("col fail")
                        return False

                    box = ((i//3) * 3) + (j//3)
                    if not (num in boxes[box]):
                        boxes[box].add(num)
                    else:
                        return False
        return True