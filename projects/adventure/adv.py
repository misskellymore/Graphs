from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# DFS
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

# DFS pseudo code
# DFS(graph):
#     for v of graph.verts:
#         v.color = white
#         v.parent = null

#     for v of graph.verts:
#         if v.color == white:
#             DFS_visit(v)

# DFS_visit(v):
#     v.color = gray

#     for neighbor of v.adjacent_nodes:
#         if neighbor.color == white:
#             neighbor.parent = v
#             DFS_visit(neighbor)

#     v.color = black


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
# visited_rooms.add(player.current_room)
traversal_path = []
traversal_graph = dict()

s = Stack()
s.push([player.current_room])

# while there are nodes/vertcies
while s.size() > 0:
    # pop the first vertex on the path/stack
    path = s.pop()
    # Grab the last vertex from the PATH
    cur = path[-1]
    # if it isnt in the visited room
    if cur not in visited_rooms:
        # add it
        visited_rooms.add(cur)        
        traversal_graph[cur.id] = {"n": "?", "s": "?", "e": "?", "w": "?", }

        # loop over exited rooms w/player
        for ex in player.current_room.get_exits():
            # if the last vertex in the path
            # of room directions isnt None
            if cur.get_room_in_direction(ex) != None:
                # append the list
                traversal_path.append(ex)
                # set the key in the dic as the
                # key in the list
                traversal_graph[cur.id][ex] = cur.get_room_in_direction(ex).id
                # set the last vertex in the path
                # of room directions to next
                nxt = cur.get_room_in_direction(ex)
                # create a new path by
                # creating a variable number
                # of pops followed by the next vertex
                new_path = [*path, nxt]
                # and push a new one onto the stack
                s.push(new_path)

            else:
                # set it as None
                traversal_graph[cur.id][ex] = None


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
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
