#Has 1 child classes for each block
from block import Block
from position import Position

class LBlock(Block):
    def __init__(self):
        super().__init__(id=1)
        self.cells = {
            0:[Position(0,2),Position(1,0),Position(1,1),Position(1,2)],
            1:[Position(0,1),Position(1,1),Position(2,1),Position(2,2)],
            2:[Position(1,0),Position(1,1),Position(1,2),Position(2,0)],
            3:[Position(0,0),Position(0,1),Position(1,1),Position(2,1)]
        }       ##Has the cell positions for each rotation state
        self.move(0,3)


class JBlock(Block):
    def __init__(self):
        super().__init__(id=2)
        self.cells={
            0:[Position(0,0),Position(1,0),Position(1,1),Position(1,2)],
            1:[Position(0,1),Position(0,2),Position(1,1),Position(2,1)],
            2:[Position(1,0),Position(1,1),Position(1,2),Position(2,2)],
            3:[Position(0,1),Position(1,1),Position(2,0),Position(2,1)]
        }
        self.move(0,3)  #make the block appear from the center of grid (not top left -- origin)

class IBlock(Block):
    def __init__(self):
        super().__init__(id=3)
        self.cells={
            0:[Position(1,0),Position(1,1),Position(1,2),Position(1,3)],
            1:[Position(0,2),Position(1,2),Position(2,2),Position(3,2)],
            2:[Position(2,0),Position(2,1),Position(2,2),Position(2,3)],
            3:[Position(0,1),Position(1,1),Position(2,1),Position(3,1)]
        }
        self.move(-1,3)     # Different starting position adjusted

class OBlock(Block):
    def __init__(self):
        super().__init__(id=4)
        self.cells={
            0:[Position(0,0),Position(0,1),Position(1,0),Position(1,1)]
        }
        self.move(0,4)      # Has different center 

class TBlock(Block):
    def __init__(self):
        super().__init__(id=5)
        self.cells={
            0:[Position(0,1),Position(1,0),Position(1,1),Position(1,2)],
            1:[Position(0,1),Position(1,1),Position(1,2),Position(2,1)],
            2:[Position(1,0),Position(1,1),Position(1,2),Position(2,1)],
            3:[Position(0,1),Position(1,0),Position(1,1),Position(2,1)]
        }
        self.move(0,3) 

class ZBlock(Block):
    def __init__(self):
        super().__init__(id=6)
        self.cells={
            0:[Position(0,0),Position(0,1),Position(1,1),Position(1,2)],
            1:[Position(0,2),Position(1,1),Position(1,2),Position(2,1)],
            2:[Position(1,0),Position(1,1),Position(2,1),Position(2,2)],
            3:[Position(0,1),Position(1,0),Position(1,1),Position(2,0)]
        }
        self.move(0,3) 

class SBlock(Block):
    def __init__(self):
        super().__init__(id=7)
        self.cells={
            0:[Position(0,1),Position(0,2),Position(1,0),Position(1,1)],
            1:[Position(0,1),Position(1,1),Position(1,2),Position(2,2)],
            2:[Position(1,1),Position(1,2),Position(2,0),Position(2,1)],
            3:[Position(0,0),Position(1,0),Position(1,1),Position(2,1)]
        }
        self.move(0,3) 
