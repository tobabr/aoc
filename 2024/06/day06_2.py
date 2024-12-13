#!/usr/bin/env python3

from copy import deepcopy
from enum import Enum
from textwrap import wrap

class Pos:
    def __init__(self, row, col):
        self._row = row
        self._col = col

    def __repr__(self) -> str:
        return f"({self._row},{self._col})"
    def up(self):
        self._row += 1

    def down(self):
        self._row -= 1

    def right(self):
        self._col += 1

    def left(self):
        self._col -= 1

    @property
    def x(self):
        return self._col

    @property
    def y(self):
        return self._row

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

def next_pos(current: Pos, direction: Direction) -> Pos:
    if direction == Direction.UP:
        return Pos(current.y-1, current.x)
    if direction == Direction.RIGHT:
        return Pos(current.y, current.x+1)
    if direction == Direction.DOWN:
        return Pos(current.y+1, current.x)
    if direction == Direction.LEFT:
        return Pos(current.y, current.x-1)

def find_start(text_map: list[list]) -> Pos:
    for row in range(len(text_map)):
        for col in range(len(text_map[0])):
            if text_map[row][col] == '^':
                return Pos(row, col)

class Guard:

    def __init__(self, start: Pos) -> None:
        self._pos: Pos = start
        self._direction: Direction = Direction.UP

    def __repr__(self) -> str:
        if self._direction == Direction.UP:
            return '^'
        if self._direction == Direction.RIGHT:
            return '>'
        if self._direction == Direction.LEFT:
            return '<'
        if self._direction == Direction.DOWN:
            return 'V'

    @property
    def pos(self):
        return self._pos

    @property
    def direction(self) -> Direction:
        return self._direction

    def turn_right(self) -> None:
        self._direction = Direction((self._direction.value + Direction.RIGHT.value)%4)

    def move(self, direction: Direction = None) -> None:
        direction = direction or self._direction
        self._pos = next_pos(self._pos, direction)


class Map:

    def __init__(self, text_map):
        self._map = text_map
        self._guard: Guard = Guard(find_start(self._map))
        self._visited = self.mark_visited(self._guard.pos)
        self._loops = 0

    def mark_visited(self, pos: Pos) -> int:
        if self._map[pos.y][pos.x] == '.':
            self._map[pos.y][pos.x] = self._guard.direction.name
            return 1
        else:
            return 0

    def _next_is_loop_candidate(self, next_possition: Pos) -> bool:
        if self._position_outside_map(next_possition):
            return False
        cur_pos = self._guard.pos
        if self._map[next_possition.y][next_possition.x] == '.' and self._map[cur_pos.y][cur_pos.x] == Direction.RIGHT.name:
            return True

    def _get_direction(self) -> None:
        #print(f"current: {self._guard.pos}")
        next = next_pos(self._guard.pos, self._guard.direction)
       # print(f"next: {next}")

        if self._next_is_loop_candidate(next):
            self._guard.turn_right()
            self._loops += 1
            return

        while not self._position_outside_map(next) and self._map[next.y][next.x] == '#':
            self._guard.turn_right()
            next = next_pos(self._guard.pos, self._guard.direction)
            #print(f"next: {next}")

    def _position_outside_map(self, position: Pos) -> bool:
        if (len(self._map) <= position.y  or position.y < 0) or (len(self._map[0]) <= position.x or position.x < 0):
            return True
        else:
            return False

    def step(self) -> bool:
        self._get_direction()
        self._guard.move()
       # print(self._guard, end=" ")
        if self._position_outside_map(self._guard.pos):
            return False
        else:
            self._visited += self.mark_visited(self._guard.pos)
            return True

    def get_num_visited(self):
        return self._visited

    def get_num_loops(self):
        return self._loops


class Game:

    def __init__(self, file_input):
        text_map: list[list] = []
        with open(file_input, 'r') as f:
            for line in f.readlines():
                text_map.append(wrap(line, 1))

        self._world_map = Map(text_map)

    def start(self):
        while self._world_map.step():
            pass

    def visited(self):
        return self._world_map.get_num_visited()

    def loops(self):
        return self._world_map.get_num_loops()

def main():

    game = Game('test_data.txt')
    game.start()

    print(f"Number of loops: {game.loops()}")



    return 0

if __name__ == '__main__':
    main()