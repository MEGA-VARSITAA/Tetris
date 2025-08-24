from colors import Color
from position import Position
import pygame
class Block:
    def __init__(self,id):
        self.id=id
        self.cells={}
        self.row_offset=0
        self.column_offset=0
        self.cell_size = 30
        self.rotation_state = 0
        self.colors = Color.get_cell_colors()

    def draw(self,screen,offest_x,offest_y):
        tiles=self.get_cell_positions()
        for tile in tiles:
            tile_rect=pygame.Rect(tile.col*self.cell_size +offest_x ,tile.row*self.cell_size +offest_y, self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(screen,self.colors[self.id],tile_rect)
    
    def move(self,rows, columns):
        self.row_offset+=rows
        self.column_offset+=columns

    def rotate(self):
        self.rotation_state+=1
        if self.rotation_state==len(self.cells):
            self.rotation_state=0

    def undo_rotation(self):
        self.rotation_state-=1
        if self.rotation_state<0:
            self.rotation_state=len(self.cells)-1

    def get_cell_positions(self):
        # returns the position of occupied cells with offset applied
        tiles=self.cells[self.rotation_state]
        moved_tiles=[]
        for position in tiles:
            position = Position(position.row + self.row_offset, position.col + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles