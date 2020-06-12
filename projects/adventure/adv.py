from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
traveral_graph = dict()



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

s = Stack()
s.push()([player.current_room])

while s.size() > 0:
    path = s.pop()
    cur = path[-1]

    if cur not in visited_rooms:
        visited_rooms.add(cur)
        traversal_graph[cur.id] = {"n": "?", "s": "?", "e": "?", "w": "?", }

        for ex in player.current_room.get_exits():

            if cur.get_room_in_direction(ex) != None:
                traversal_path.append(ex)
                traversal_graph[cur.id][ex] = cur.get_room_in_direction(ex).id
                nxt = cur.get_room_in_direction(ex)
                new_path = [*path, nxt]
                s.push(new_path)

            else:
                traversal_graph[cur.id][ex] = None


print("traversal", traversal_path)
print("traversal graph", traversal_graph)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
