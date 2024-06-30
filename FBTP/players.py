# coding=utf-8


class Player: # Represents a football player.

    def __init__(self, key):
        self.id = key  # player's ID
        # Dictionary that stores the players he is connected to
        # and the strength of this connection (similarity).
        self.connectedTo = {}
        # Dictionary that stores player skills (skill ID: value).
        self.abilities = {}
        self.position = None  # Player position on the field.
        self.salary = 0  # players' salary.

    def add_neighbor(self, nbr, weight=0): # Adds a neighbor (another player) to the connections list.
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo : ' + str([x.id for x in self.connectedTo])

    # Methods for accessing player attributes.
    def get_connection(self):  # get the neighbors
        return self.connectedTo.keys()

    def get_id(self):
        return self.id

    def get_abilities(self):
        return self.abilities

    def get_position(self):
        return self.position

    def get_salary(self):
        return self.salary

    def get_weight(self, nbr):  # get the weight of a neighbor
        return self.connectedTo[nbr]
	
class Goalkeeper:

    def __init__(self, g_id):
        self.id = g_id # Unique goalkeeper identifier.
        self.ability = [] # List of goalkeeper skills (probably specific to goalkeepers).
        self.rating = 0 # Overall goalkeeper rating.
        self.salary = 0 # Goalkeeper salary.

    #  Methods for accessing goalkeeper attributes.
    def get_id(self):
        return self.id

    def get_ability(self):
        return self.ability

    def get_rating(self):
        return self.rating

    def get_salary(self):
        return self.salary

class CutPlayer:
    """
    The player to be pruning
    """

    def __init__(self, key):
        self.id = key # Unique player identifier.
        self.cut_pos = None  # Indicates whether the player is attacking/midfield or defending
        self.cut_position = ""  # Specific position of the player to be removed.
        self.cut_salary = 0  # Player's salary to be removed.

    # Methods for accessing the attributes of the player to be removed.
    def get_id(self):
        return self.id

    def get_cut_pos(self):
        return self.cut_pos

    def get_cut_position(self):
        return self.cut_position

    def get_cut_salary(self):
        return self.cut_salary

class Graph:

    def __init__(self):
        self.vertexList = {} # Dictionary that stores players (graph vertices) and their connections.
        self.numVertices = 0 # Total number of vertices in the graph.

    def add_vertex(self, key): # Adds a player (vertex) to the graph.
        self.numVertices = self.numVertices + 1
        newVertex = Player(key)
        self.vertexList[key] = newVertex
        return newVertex

    def get_vertex(self, key): # Returns a player (vertex) of the graph, if it exists.
        if key in self.vertexList:
            return self.vertexList[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertexList

    def add_edge(self, f, t, cost=0): # Adds a connection (edge) between two players in the graph.
        # if f and t are not in the graph, add these two nodes
        if f not in self.vertexList:
            nv = self.add_vertex(f)

        if t not in self.vertexList:
            nv = self.add_vertex(t)

        self.vertexList[f].add_neighbor(self.vertexList[t], cost)

    def get_vertices(self):  # Returns a list of all players (vertices) in the graph.
        return self.vertexList.keys()

    def __iter__(self):
        return iter(self.vertexList.values())
