def getChessSquareColor(column, row):
    # If the column and row is out of bounds, return a blank string: 
    if column < 1 or column > 8 or row < 1 or row >8: 
        return '' 

    # If the even/oddness of the column and row match, return 'white': 
    if column % 2 == row % 2: 
        return 'white' 

    # If they don't match, then return 'black': 
    else: 
        return 'black' 
    
def checkfunc():
    assert getChessSquareColor(1, 1) == 'white' 
    assert getChessSquareColor(2, 1) == 'black' 
    assert getChessSquareColor(1, 2) == 'black' 
    assert getChessSquareColor(8, 8) == 'white' 
    assert getChessSquareColor(0, 8) == '' 
    assert getChessSquareColor(2, 9) == '' 
    print("The Functions are Working!")
    
def main():
    checkfunc()
    
if __name__ == '__main__' :
    main()