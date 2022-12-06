from colorama import Fore

def sum(a,b,c):
    return a + b + c

def printBord(xState, yState):
    one   = 'x' if xState[1] else ('O' if yState[1] else 1)
    two   = 'x' if xState[2] else ('O' if yState[2] else 2)
    three = 'x' if xState[3] else ('O' if yState[3] else 3)
    four  = 'x' if xState[4] else ('O' if yState[4] else 4)
    five  = 'x' if xState[5] else ('O' if yState[5] else 5)
    six   = 'x' if xState[6] else ('O' if yState[6] else 6)
    seven = 'x' if xState[7] else ('O' if yState[7] else 7)
    eight = 'x' if xState[8] else ('O' if yState[8] else 8)
    nine  = 'x' if xState[9] else ('O' if yState[9] else 9)
    print(Fore.LIGHTCYAN_EX + f"╔═══╦═══╦═══╗")
    print(Fore.LIGHTCYAN_EX + f"║ {one} ║ {two} ║ {three} ║")
    print(Fore.LIGHTCYAN_EX + f"╠═══╬═══╬═══╣")
    print(Fore.LIGHTCYAN_EX + f"║ {four} ║ {five} ║ {six} ║")
    print(Fore.LIGHTCYAN_EX + f"╠═══╬═══╬═══╣")
    print(Fore.LIGHTCYAN_EX + f"║ {seven} ║ {eight} ║ {nine} ║")
    print(Fore.LIGHTCYAN_EX + f"╚═══╩═══╩═══╝")

def checkWin(xState, yState):
    wins = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print(Fore.LIGHTWHITE_EX,"x won the match")
            return 1
        if(sum(yState[win[0]], yState[win[1]], yState[win[2]]) == 3):
            print(Fore.LIGHTWHITE_EX,"o won the match")
            return 0
    return - 1

if __name__ == "__main__":
    xState = [0,0,0,0,0,0,0,0,0,0]
    yState = [0,0,0,0,0,0,0,0,0,0]
    turn = 1
    print("Welcome to Tic Tac Toe")
    while(True):
        try:
            printBord(xState, yState)
            if(turn == 1):
                print(Fore.LIGHTGREEN_EX,"x's chance")
                value = int(input("Enter a value :"))
                xState[value] = 1 
            else:
                print(Fore.LIGHTYELLOW_EX,"o's chance")
                value = int(input("Enter a value :"))
                yState[value] = 1 
            cwin = checkWin(xState, yState)
            if(cwin != -1):
                print(Fore.LIGHTBLUE_EX,"Match over")
                exit()
            turn = 1- turn
        except Exception as e:
            print(Fore.LIGHTRED_EX + f"Your input resulted in an error: {e}")
