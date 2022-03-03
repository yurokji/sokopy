from constant import *
import levels
import copy

class Sokopy:
    curr_map = []
    curr_map = []
    man_y = 0
    man_x = 0
    def __init__(self):
        self.all_levels = levels.soko_all_levels

    def print(self):
        for y in self.curr_map:
            print("      ", end="")
            for x in y:
                print(x, end=" ")
            print()

    
    def prepare(self, curr_level=0):
        self.level = curr_level
        current_data = self.all_levels[self.level]
        self.map_size = current_data['map_size']
        self.curr_map = []
        for i in range(self.map_size[0]):
            row = []
            for j in range(self.map_size[1]):
                row.append(ROAD)
            self.curr_map.append(row)

        for pos in current_data['wall_pos']:
            y = pos[0]
            x = pos[1]
            self.curr_map[y][x] = WALL

        for pos in current_data['target_pos']:
            y = pos[0]
            x = pos[1]
            self.curr_map[y][x] = TARGET

        for pos in current_data['box_pos']:
            y = pos[0]
            x = pos[1]
            if self.curr_map[y][x] == TARGET:
                self.curr_map[y][x] = BOX_TARGET
            else: 
                self.curr_map[y][x] = BOX

        y = current_data['man_pos'][0]
        x = current_data['man_pos'][1]
        if self.curr_map[y][x] == TARGET:
            self.curr_map[y][x] = MAN_TARGET
        else: 
            self.curr_map[y][x] = MAN

        self.man_y = y
        self.man_x = x
        # 원본 맵 기억
        self.curr_map = copy.deepcopy(self.curr_map)


    def reset(self):
        self.prepare(self.level)

    def is_cleared(self):
        targets = self.all_levels[self.level]['target_pos']
        size_targets = len(targets)
        count = 0
        for pos in targets:
            y = pos[0]
            x = pos[1]
            if self.curr_map[y][x] == BOX_TARGET:
                count += 1
        if count == size_targets:
            return True
        else:
            return False


    def move(self, k):
        if k == 'w':
            if self.curr_map[self.man_y - 1][self.man_x] == ROAD:
                if self.curr_map[self.man_y][self.man_x] == MAN:
                    self.curr_map[self.man_y][self.man_x] = ROAD
                    self.curr_map[self.man_y - 1][self.man_x] = MAN
                    self.man_y -= 1 
                    return True
                elif self.curr_map[self.man_y][self.man_x] == MAN_TARGET:
                    self.curr_map[self.man_y][self.man_x] = TARGET
                    self.curr_map[self.man_y - 1][self.man_x] = MAN 
                    self.man_y -= 1 
                    return True          
            elif self.curr_map[self.man_y - 1][self.man_x] == TARGET:
                if self.curr_map[self.man_y][self.man_x] == MAN:
                    self.curr_map[self.man_y][self.man_x] = ROAD
                    self.curr_map[self.man_y - 1][self.man_x] = MAN_TARGET
                    self.man_y -= 1 
                    return True
                elif self.curr_map[self.man_y][self.man_x] == MAN_TARGET:
                    self.curr_map[self.man_y][self.man_x] = TARGET
                    self.curr_map[self.man_y - 1][self.man_x] = MAN_TARGET 
                    self.man_y -= 1 
                    return True

        elif k == 's':
            if self.curr_map[self.man_y + 1][self.man_x] == ROAD:
                if self.curr_map[self.man_y][self.man_x] == MAN:
                    self.curr_map[self.man_y][self.man_x] = ROAD
                    self.curr_map[self.man_y + 1][self.man_x] = MAN
                    self.man_y += 1
                    return True 
                elif self.curr_map[self.man_y][self.man_x] == MAN_TARGET:
                    self.curr_map[self.man_y][self.man_x] = TARGET
                    self.curr_map[self.man_y + 1][self.man_x] = MAN 
                    self.man_y += 1
                    return True                  
            elif self.curr_map[self.man_y + 1][self.man_x] == TARGET:
                if self.curr_map[self.man_y][self.man_x] == MAN:
                    self.curr_map[self.man_y][self.man_x] = ROAD
                    self.curr_map[self.man_y + 1][self.man_x] = MAN_TARGET
                    self.man_y += 1
                    return True 
                elif self.curr_map[self.man_y][self.man_x] == MAN_TARGET:
                    self.curr_map[self.man_y][self.man_x] = TARGET
                    self.curr_map[self.man_y + 1][self.man_x] = MAN_TARGET 
                    self.man_y += 1
                    return True 

        elif k == 'a':
            if self.curr_map[self.man_y][self.man_x - 1] == ROAD:
                if self.curr_map[self.man_y][self.man_x] == MAN:
                    self.curr_map[self.man_y][self.man_x] = ROAD
                    self.curr_map[self.man_y][self.man_x - 1] = MAN
                    self.man_x -= 1 
                    return True     
                elif self.curr_map[self.man_y][self.man_x] == MAN_TARGET:
                    self.curr_map[self.man_y][self.man_x] = TARGET
                    self.curr_map[self.man_y][self.man_x - 1] = MAN 
                    self.man_x -= 1 
                    return True                   
            elif self.curr_map[self.man_y][self.man_x - 1] == TARGET:
                 if self.curr_map[self.man_y][self.man_x] == MAN:
                    self.curr_map[self.man_y][self.man_x] = ROAD
                    self.curr_map[self.man_y][self.man_x - 1] = MAN_TARGET
                    self.man_x -= 1 
                    return True
                 elif self.curr_map[self.man_y][self.man_x] == MAN_TARGET:
                    self.curr_map[self.man_y][self.man_x] = TARGET
                    self.curr_map[self.man_y][self.man_x - 1] = MAN_TARGET 
                    self.man_x -= 1 
                    return True

        elif k == 'd':
            if self.curr_map[self.man_y][self.man_x + 1] == ROAD:
                 if self.curr_map[self.man_y][self.man_x] == MAN:
                    self.curr_map[self.man_y][self.man_x] = ROAD
                    self.curr_map[self.man_y][self.man_x + 1] = MAN
                    self.man_x += 1  
                    return True   
                 elif self.curr_map[self.man_y][self.man_x] == MAN_TARGET:
                    self.curr_map[self.man_y][self.man_x] = TARGET
                    self.curr_map[self.man_y][self.man_x + 1] = MAN    
                    self.man_x += 1  
                    return True                
            elif self.curr_map[self.man_y][self.man_x + 1] == TARGET:
                 if self.curr_map[self.man_y][self.man_x] == MAN:
                    self.curr_map[self.man_y][self.man_x] = ROAD
                    self.curr_map[self.man_y][self.man_x + 1] = MAN_TARGET
                    self.man_x += 1  
                    return True   
                 elif self.curr_map[self.man_y][self.man_x] == MAN_TARGET:
                    self.curr_map[self.man_y][self.man_x] = TARGET
                    self.curr_map[self.man_y][self.man_x + 1] = MAN_TARGET 
                    self.man_x += 1  
                    return True
        return False
    
    def push(self, k):
        if k == 'w':
            if self.curr_map[self.man_y - 1][self.man_x] == BOX:
                if self.man_y - 2 >= 0:
                    if self.curr_map[self.man_y - 2][self.man_x] != WALL and\
                    self.curr_map[self.man_y - 2][self.man_x] != BOX and\
                    self.curr_map[self.man_y - 2][self.man_x] != BOX_TARGET:
                        if self.curr_map[self.man_y - 2][self.man_x] == TARGET:
                            self.curr_map[self.man_y - 2][self.man_x] = BOX_TARGET
                            self.curr_map[self.man_y - 1][self.man_x] = ROAD
                        else:
                            self.curr_map[self.man_y - 2][self.man_x] = BOX
                            self.curr_map[self.man_y - 1][self.man_x] = ROAD
                        return True
            elif self.curr_map[self.man_y - 1][self.man_x] == BOX_TARGET:
                if self.man_y - 2 >= 0:
                    if self.curr_map[self.man_y - 2][self.man_x] != WALL and\
                    self.curr_map[self.man_y - 2][self.man_x] != BOX and\
                    self.curr_map[self.man_y - 2][self.man_x] != BOX_TARGET:
                        if self.curr_map[self.man_y - 2][self.man_x] == TARGET:
                            self.curr_map[self.man_y - 2][self.man_x] = BOX_TARGET
                            self.curr_map[self.man_y - 1][self.man_x] = TARGET
                        else:
                            self.curr_map[self.man_y - 2][self.man_x] = BOX
                            self.curr_map[self.man_y - 1][self.man_x] = TARGET
                        return True
        elif k == 's':
            if self.curr_map[self.man_y + 1][self.man_x] == BOX:
                if self.man_y + 2 < self.map_size[0]:
                    if self.curr_map[self.man_y + 2][self.man_x] != WALL and\
                    self.curr_map[self.man_y + 2][self.man_x] != BOX and\
                    self.curr_map[self.man_y + 2][self.man_x] != BOX_TARGET:
                        if self.curr_map[self.man_y + 2][self.man_x] == TARGET:
                            self.curr_map[self.man_y + 2][self.man_x] = BOX_TARGET
                            self.curr_map[self.man_y + 1][self.man_x] = ROAD
                        else:
                            self.curr_map[self.man_y + 2][self.man_x] = BOX
                            self.curr_map[self.man_y + 1][self.man_x] = ROAD
                        return True
            elif self.curr_map[self.man_y + 1][self.man_x] == BOX_TARGET:
                if self.man_y + 2 < self.map_size[0]:
                    if self.curr_map[self.man_y + 2][self.man_x] != WALL and\
                    self.curr_map[self.man_y + 2][self.man_x] != BOX and\
                    self.curr_map[self.man_y + 2][self.man_x] != BOX_TARGET:
                        if self.curr_map[self.man_y + 2][self.man_x] == TARGET:
                            self.curr_map[self.man_y + 2][self.man_x] = BOX_TARGET
                            self.curr_map[self.man_y + 1][self.man_x] = TARGET
                        else:
                            self.curr_map[self.man_y + 2][self.man_x] = BOX
                            self.curr_map[self.man_y + 1][self.man_x] = TARGET
                        return True
        elif k == 'a':
            if self.curr_map[self.man_y][self.man_x - 1] == BOX:
                if self.man_x - 2 >= 0:
                    if self.curr_map[self.man_y][self.man_x - 2] != WALL and\
                    self.curr_map[self.man_y][self.man_x - 2] != BOX and\
                    self.curr_map[self.man_y][self.man_x - 2] != BOX_TARGET:
                        if self.curr_map[self.man_y][self.man_x - 2] == TARGET:
                            self.curr_map[self.man_y][self.man_x - 2] = BOX_TARGET
                            self.curr_map[self.man_y][self.man_x - 1] = ROAD
                        else:
                            self.curr_map[self.man_y][self.man_x - 2] = BOX
                            self.curr_map[self.man_y][self.man_x - 1] = ROAD
                        return True
            elif self.curr_map[self.man_y][self.man_x - 1] == BOX_TARGET:
                if self.man_x - 2 >= 0:
                    if self.curr_map[self.man_y][self.man_x - 2] != WALL and\
                    self.curr_map[self.man_y][self.man_x - 2] != BOX and\
                    self.curr_map[self.man_y][self.man_x - 2] != BOX_TARGET:
                        if self.curr_map[self.man_y][self.man_x - 2] == TARGET:
                            self.curr_map[self.man_y][self.man_x - 2] = BOX_TARGET
                            self.curr_map[self.man_y][self.man_x - 1] = TARGET
                        else:
                            self.curr_map[self.man_y][self.man_x - 2] = BOX
                            self.curr_map[self.man_y][self.man_x - 1] = TARGET
                        return True
        if k == 'd':
            if self.curr_map[self.man_y][self.man_x + 1] == BOX:
                    if self.curr_map[self.man_y][self.man_x + 2] != WALL and\
                    self.curr_map[self.man_y][self.man_x + 2] != BOX and\
                    self.curr_map[self.man_y][self.man_x + 2] != BOX_TARGET:
                        if self.curr_map[self.man_y][self.man_x + 2] == TARGET:
                            self.curr_map[self.man_y][self.man_x + 2] = BOX_TARGET
                            self.curr_map[self.man_y][self.man_x + 1] = ROAD
                        else:
                            self.curr_map[self.man_y][self.man_x + 2] = BOX
                            self.curr_map[self.man_y][self.man_x + 1] = ROAD
                        return True
            elif self.curr_map[self.man_y][self.man_x + 1] == BOX_TARGET:
                if self.man_x + 2 < self.map_size[1]:
                    if self.curr_map[self.man_y][self.man_x + 2] != WALL and\
                    self.curr_map[self.man_y][self.man_x + 2] != BOX and\
                    self.curr_map[self.man_y][self.man_x + 2] != BOX_TARGET:
                        if self.curr_map[self.man_y][self.man_x + 2] == TARGET:
                            self.curr_map[self.man_y][self.man_x + 2] = BOX_TARGET
                            self.curr_map[self.man_y][self.man_x + 1] = TARGET
                        else:
                            self.curr_map[self.man_y][self.man_x + 2] = BOX
                            self.curr_map[self.man_y][self.man_x + 1] = TARGET
                        return True
        return False







