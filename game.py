import random
import time

"""
Using: 
    # print(self.board.getBoard())
    # print(f"{self.identity} is currently merged: {self.merge} and {whoInMySpot.identity} is currently merged: {whoInMySpot.merge}")
after every if within the direction check in the canMove() function will tell you the board, and information about the self merging and
the whoInMySpot merging. This will shed light on possible bugs, because it depicts every actual move the algorithm makes when moving each tile.


############################
# Task 1: 
#     Create a Tile object and a Board object.
#
# Task 2: 
#     Define initial values for both objects
#
# Task 3: 
#     Make function that allows Tile object to understand where it is
#     also make it capable of finding other tiles to get relations and merges
#
# Task 4: 
#     Define function for Board object to understand the order of Tiles needing to be moved first.

This gets tricky because of the use of a dictionary. To use a dictionary means we either have to read
left to right or right to left. Both options will allow for us to check for up and right movement(reading left to right)
or down and left movement(reading right to left). Thinking about it in this fasion allows us to scale the app, but we'd have
to account for the size, i.e. *lengOfUpDown = math.sqrt(dict.len()+1)* and from their change our sub and addition values for the W, and S keys. 
#
# Task 5: 
#     Understand the issue with using a dictionary and the extra code we have to write to check for where we compress and merge our tiles.
#
############################

"""

class Tile:
    tile_count = 0
    dict_of_tiles = {}
    def __init__(self, pos, data, get_board, start_val=2):
        self.currentPos = pos
        self.value = start_val
        self.data = data
        self.identity = Tile.tile_count
        self.remove = False
        self.merge = False
        self.board = get_board

        Tile.dict_of_tiles[Tile.tile_count] = self
        Tile.tile_count += 1;

        self.data[self.currentPos] = self.value

    def updateValue(self, val):
        self.value = val
        self.data[self.currentPos] = self.value
        self.merge = True

    def getTileByPos(pos):
        for tile in Tile.dict_of_tiles:
            if (Tile.dict_of_tiles[tile].currentPos == pos):
                return Tile.dict_of_tiles[tile]

    def canMove(self, direction):
        if (direction == 'w'):
            try:
                whoInMySpot = Tile.getTileByPos(self.currentPos-4)
                
                if (self.data[self.currentPos - 4] == ''):
                    self.data[self.currentPos] = ''
                    self.currentPos -= 4
                    self.data[self.currentPos] = self.value
                    return True

                elif (whoInMySpot.value == self.value):
                    if whoInMySpot.merge == True: return False;

                    whoInMySpot.updateValue(whoInMySpot.value*2)
                    self.remove = True
                    self.data[self.currentPos] = ''
                    self.currentPos = whoInMySpot.currentPos
                    self.merge = True

                elif (self.merge == True):
                    pass;

                else:
                    pass;

                return False
            except Exception:
                return False
                
        elif (direction == 's'):
            try:
                whoInMySpot = Tile.getTileByPos(self.currentPos+4)
                
                if (self.data[self.currentPos + 4] == ''):
                    self.data[self.currentPos] = ''
                    self.currentPos += 4
                    self.data[self.currentPos] = self.value
                    return True

                elif (whoInMySpot.value == self.value):
                    if whoInMySpot.merge == True: return False;

                    whoInMySpot.updateValue(whoInMySpot.value*2)
                    self.remove = True
                    self.data[self.currentPos] = ''
                    self.currentPos = whoInMySpot.currentPos
                    self.merge = True

                elif (self.merge == True):
                    pass;

                else:
                    pass;

                return False
            except Exception:
                return False
                
        elif (direction == 'a'):
            if (self.currentPos in [5,9,13]): 
                return False

            try:
                whoInMySpot = Tile.getTileByPos(self.currentPos-1)
                
                if (self.data[self.currentPos - 1] == ''):
                    self.data[self.currentPos] = ''
                    self.currentPos -= 1
                    self.data[self.currentPos] = self.value
                    return True

                elif (whoInMySpot.value == self.value):
                    if whoInMySpot.merge == True: return False;

                    whoInMySpot.updateValue(whoInMySpot.value*2)
                    self.remove = True
                    self.data[self.currentPos] = ''
                    self.currentPos = whoInMySpot.currentPos
                    self.merge = True

                elif (self.merge == True):
                    pass;

                else:
                    pass;

                return False
            except Exception:
                return False
                
        elif (direction == 'd'):
            if (self.currentPos in [4,8,12]): 
                return False

            try:
                whoInMySpot = Tile.getTileByPos(self.currentPos+1)
                
                if (self.data[self.currentPos + 1] == ''):
                    self.data[self.currentPos] = ''
                    self.currentPos += 1
                    self.data[self.currentPos] = self.value
                    return True

                elif (whoInMySpot.value == self.value):
                    if whoInMySpot.merge == True: return False;

                    whoInMySpot.updateValue(whoInMySpot.value*2)
                    self.remove = True
                    self.data[self.currentPos] = ''
                    self.currentPos = whoInMySpot.currentPos
                    self.merge = True

                elif (self.merge == True):
                    pass;

                else:
                    pass;

                return False
            except Exception:
                return False

    def move(self, direction):
        canIMove = self.canMove(direction)
        if (canIMove):
            self.move(direction)
        else:
            return self.remove

class Board:
    def __init__(self):
        self.data = {1: '', 2: '', 3: '', 4: '',
                    5: '', 6: '', 7: '', 8: '',
                    9: '', 10: '', 11: '', 12: '',
                    13: '', 14: '', 15: '', 16: ''}

    def checkForEmpty(self):
        for key in self.data:
            if (self.data[key] == ''):
                return True
        return False

    def checkForWin(self):
        for key in self.data:
            if (self.data[key] == 2048):
                return None
        return True

    def removeOld(self):
        removeList = []
        for tile in Tile.dict_of_tiles:
            this = Tile.dict_of_tiles[tile]
            if (this.remove):
                removeList.append(this.identity)
        for num in removeList:
            Tile.dict_of_tiles.pop(num, None)

    def getBoard(self):
        board_str = ""
        for key in self.data:
            data_str = str(self.data[key])

            if (key == 4) or (key == 8) or (key == 12) or (key == 16):
                board_str += "|" + f"{data_str : ^5}" + "|\n"
                continue
            board_str += "|" + f"{data_str : ^5}"

        return board_str

    def changeBoard(self, dir):
        if (dir in ['w', 's', 'd', 'a']):
            for tile in Tile.dict_of_tiles:
                Tile.dict_of_tiles[tile].merge = False

            
            if (dir == 'w') or (dir == 'a'):
                for key in self.data:
                    for tile in Tile.dict_of_tiles:
                        if (Tile.dict_of_tiles[tile].currentPos == key):
                            Tile.dict_of_tiles[tile].move(dir)
            elif (dir == 's') or (dir == 'd'):
                for key in self.data:
                    for tile in Tile.dict_of_tiles:
                        if (Tile.dict_of_tiles[tile].currentPos == (17-key)):
                            Tile.dict_of_tiles[tile].move(dir)

    def findSpot(self):
        spot = random.randrange(16)+1
        if (self.data[spot] == ''):
            return spot
        else:
            return self.findSpot()

    def addTile(self):
        newSpot = self.findSpot()
        Tile(newSpot, self.data, self);

    def getInput(self):
        value = input()
        if (value in ['w', 'a', 's', 'd']):
            return value
        else:
            return self.getInput()
            
    def start(self):
        start = time.time()
        while (self.checkForEmpty() and self.checkForWin()):
            print(self.getBoard())
            dir = self.getInput()
            self.changeBoard(dir)
            self.removeOld()

            self.addTile()

        amount = str(round((time.time() - start), 2))
        if not(self.checkForWin()):
            print("|" + f'{"WIN" :^23}' + "|\n|" + f'{amount+" sec" :^23}' + "|")
        else:
            print("|" + f'{"LOS" :^23}' + "|\n|" + f'{amount+" sec" :^23}' + "|")
        
        cont = input("PLAY AGAIN [y/N]:")
        if (cont == 'y'):
            obj = Board()
            obj.start()
        
            


if __name__ == '__main__':
    obj = Board()
    t0, t1 = Tile(1, obj.data, obj), Tile(4, obj.data, obj)
    obj.start()