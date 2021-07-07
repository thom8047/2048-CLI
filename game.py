import random

class Tile:
    tile_count = 0
    dict_of_tiles = {}
    def __init__(self, pos, data, get_board, start_val=2):
        self.currentPos = pos
        self.value = start_val
        self.data = data
        self.identity = Tile.tile_count
        self.remove = False
        self.merge = 0
        self.board = get_board

        Tile.dict_of_tiles[Tile.tile_count] = self
        Tile.tile_count += 1;

        self.data[self.currentPos] = self.value

    def updateValue(self, val):
        self.value = val
        self.data[self.currentPos] = self.value
        self.merge = 1

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
                    
                    # print(self.identity, ' : Value -> ', self.value, ' : Pos ->', self.currentPos)
                    # print(self.board.getBoard())

                    return True
                elif (whoInMySpot.value == self.value):
                    if whoInMySpot.merge == 1: return False;

                    whoInMySpot.updateValue(whoInMySpot.value*2)
                    self.remove = True
                    self.data[self.currentPos] = ''
                elif (self.merge == 1):
                    pass;

                return False
            except Exception as err:
                #print(err)
                return False
        elif (direction == 's'):
            try:
                whoInMySpot = Tile.getTileByPos(self.currentPos+4)
                
                if (self.data[self.currentPos + 4] == ''):
                    self.data[self.currentPos] = ''
                    self.currentPos += 4
                    self.data[self.currentPos] = self.value
                    
                    # print(self.identity, ' : Value -> ', self.value, ' : Pos ->', self.currentPos)
                    # print(self.board.getBoard())

                    return True
                elif (whoInMySpot.value == self.value):
                    if whoInMySpot.merge == 1: return False;

                    whoInMySpot.updateValue(whoInMySpot.value*2)
                    self.remove = True
                    self.data[self.currentPos] = ''
                elif (self.merge == 1):
                    pass;

                return False
            except Exception as err:
                #print(err)
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
                    
                    # print(self.identity, ' : Value -> ', self.value, ' : Pos ->', self.currentPos)
                    # print(self.board.getBoard())

                    return True
                elif (whoInMySpot.value == self.value):
                    if whoInMySpot.merge == 1: return False;

                    whoInMySpot.updateValue(whoInMySpot.value*2)
                    self.remove = True
                    self.data[self.currentPos] = ''
                elif (self.merge == 1):
                    pass;

                return False
            except Exception as err:
                #print(err)
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
                    
                    #print(self.identity, ' : Value -> ', self.value, ' : Pos ->', self.currentPos)
                    #print(self.board.getBoard())

                    return True
                elif (whoInMySpot.value == self.value):
                    if whoInMySpot.merge == 1: return False;

                    whoInMySpot.updateValue(whoInMySpot.value*2)
                    self.remove = True
                    self.data[self.currentPos] = ''
                elif (self.merge == 1):
                    pass;

                return False
            except Exception as err:
                #print(err)
                return False

    def move(self, direction):
        canIMove = self.canMove(direction)
        if (canIMove):
            self.move(direction)
        else:
            return self.remove
            # check to see if we're at the end of the board
            # if not then we need to check if the tile that's in our direction is the same, then we can double
    

class Board:
    def __init__(self):
        self.data = {1: '', 2: '', 3: '', 4: '',
                    5: '', 6: '', 7: '', 8: '',
                    9: '', 10: '', 11: '', 12: '',
                    13: '', 14: '', 15: '', 16: ''}

        t0 = Tile(4, self.data, self);
        t1 = Tile(12, self.data, self);
        t1 = Tile(16, self.data, self, 4);

    def organizeBoard(self, dir):
        pass


    def checkForEmpty(self):
        for key in self.data:
            if (self.data[key] == ''):
                return True
        return False

    def checkForWin(self):
        for key in self.data:
            if (self.data[key] == 2048):
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
        for tile in Tile.dict_of_tiles:
            Tile.dict_of_tiles[tile].merge = 0
            Tile.dict_of_tiles[tile].move(dir)

    def findSpot(self):
        spot = random.randrange(16)+1
        if (self.data[spot] == ''):
            return spot
        else:
            return self.findSpot()

    def addTile(self):
        newSpot = self.findSpot()
        newTile = Tile(newSpot, self.data, self);
            
    def start(self):
        while (self.checkForEmpty()):
            print(self.getBoard())
            dir = input()
            self.changeBoard(dir)
            self.removeOld()

            self.addTile()

        if (self.checkForWin):
            print("-------------- YOU WON --------------");
        else:
            print("-------------- YOU LOST --------------");

        
            


if __name__ == '__main__':
    obj = Board()
    obj.start()
        