import heapq


class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, start_node, end_node, cost):
        if start_node not in self.edges:
            self.edges[start_node] = []
        self.edges[start_node].append((end_node, cost))

    def get_neighbors(self, node):
        if node in self.edges:
            return self.edges[node]
        return []

    def __str__(self):
        return str(self.edges)

    def heuristic(self, node, goal):
        dict_h = {
            "Arad": 366,
            "Buccharesr": 0,
            "Craioya": 160,
            "Dobreta": 242,
            "Eforie": 161,
            "Fagaras": 178,
            "Giurgiu": 77,
            "Hirsova": 151,
            "Iasi": 226,
            "Lugoj": 244,
            "Mehadia": 241,
            "Neamt": 234,
            "Oradea": 380,
            "Pitesti": 98,
            "Rimnicu Vilcea": 193,
            "Sibiu": 253,
            "Timisoara": 329,
            "Urziceni": 80,
            "Vaslui": 190,
            "Zerind": 374
        }
        return dict_h[node]

    def a_star_search(self, graph, start, goal):
        frontier = []
        heapq.heappush(frontier, (0, start))
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while frontier:
            current = heapq.heappop(frontier)[1]

            if current == goal:
                break

            for neighbor, cost in graph.get_neighbors(current):
                new_cost = cost_so_far[current] + cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self.heuristic(neighbor, goal)
                    heapq.heappush(frontier, (priority, neighbor))
                    came_from[neighbor] = current

        path = []
        current = goal
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()

        return path, cost_so_far[goal]


graph = Graph()
graph.add_edge("Arad", "Zerind", 75)
graph.add_edge("Arad", "Sibiu", 140)
graph.add_edge("Arad", "Timisoara", 118)
graph.add_edge("Sibiu", "Oradea", 151)
graph.add_edge("Sibiu", "Fagaras", 99)
graph.add_edge("Sibiu", "Rimnicu Vilcea", 80)
graph.add_edge("Zerind", "Oradea", 71)
graph.add_edge("Timisoara", "Lugoj", 111)
graph.add_edge("Lugoj", "Mehadia", 70)
graph.add_edge("Mehadia", "Dobreta", 75)
graph.add_edge("Dobreta", "Craioya", 120)
graph.add_edge("Craioya", "Rimnicu Vilcea", 146)
graph.add_edge("Rimnicu Vilcea", "Pitesti", 97)
graph.add_edge("Craioya", "Pitesti", 138)
graph.add_edge("Pitesti", "Buccharesr", 101)
graph.add_edge("Fagaras", "Buccharesr", 211)
graph.add_edge("Buccharesr", "Giurgiu", 90)
graph.add_edge("Buccharesr", "Urziceni", 85)
graph.add_edge("Urziceni", "Hirsova", 98)
graph.add_edge("Hirsova", "Eforie", 86)
graph.add_edge("Urziceni", "Vaslui", 142)
graph.add_edge("Vaslui", "Iasi", 92)
graph.add_edge("Iasi", "Neamt", 87)

# __Taohid = 2019831073

path, cost = graph.a_star_search(graph, "Arad", "Buccharesr")
print("Shortest path:", path)
print("Total cost:", cost)