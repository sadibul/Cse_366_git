
import pygame
from collections import deque

class Agent(pygame.sprite.Sprite):
    def __init__(self, environment, grid_size):
        super().__init__()
        self.image = pygame.Surface((grid_size, grid_size))
        self.image.fill((0, 0, 255)) 
        self.rect = self.image.get_rect()
        self.grid_size = grid_size
        self.environment = environment
        self.position = [0, 0]  
        self.rect.topleft = (0, 0)
        self.task_completed = 0
        self.completed_tasks = []
        self.path = [] 
        self.moving = False 

    def move(self):
        """Move the agent along the path."""
        if self.path:
            next_position = self.path.pop(0)
            self.position = list(next_position)
            self.rect.topleft = (self.position[0] * self.grid_size, self.position[1] * self.grid_size)
            self.check_task_completion()
        else:
            self.moving = False 

    def check_task_completion(self):
        """Check if the agent has reached a task location."""
        position_tuple = tuple(self.position)
        if position_tuple in self.environment.task_locations:
            task_number = self.environment.task_locations.pop(position_tuple)
            self.task_completed += 1
            self.completed_tasks.append(task_number)

    def find_nearest_task(self):
        """Find the nearest task based on the shortest path length using IDA_star."""
        nearest_task = None
        shortest_path = None
        for task_position in self.environment.task_locations.keys():
            path = self. IDA_star(task_position)
            if path:
                if not shortest_path or len(path) < len(shortest_path):
                    shortest_path = path
                    nearest_task = task_position
        if shortest_path:
            self.path = shortest_path[1:]
            self.moving = True

    def  IDA_star(self, target):
        """Find a path to the target position using IDA* algorithm."""
        def search(path, g, threshold):
            """Recursive search function for IDA*."""
            current = path[-1]
            f = g + self.heuristic(current, target)
            if f > threshold: 
                return f
            if current == target:
                return path
            min_threshold = float('inf') 
            for neighbor in self.get_neighbors(current):
                if neighbor not in path:  
                    path.append(neighbor) 
                    result = search(path, g + 1, threshold) 
                    if isinstance(result, list):  
                        return result
                    if result < min_threshold: 
                        min_threshold = result
                    path.pop() 
            return min_threshold

        start = tuple(self.position)
        threshold = self.heuristic(start, target) 
        path = [start]  #

        while True: 
            result = search(path, 0, threshold) 
            if isinstance(result, list):  
                return result
            if result == float('inf'):  
                return None
            threshold = result

    def get_neighbors(self, position):
        """Get walkable neighboring positions."""
        x, y = position
        neighbors = []
        directions = [("up", (0, -1)), ("down", (0, 1)), ("left", (-1, 0)), ("right", (1, 0))]
        for _, (dx, dy) in directions:
            nx, ny = x + dx, y + dy
            if self.environment.is_within_bounds(nx, ny) and not self.environment.is_barrier(nx, ny):
                neighbors.append((nx, ny))
        return neighbors

    def heuristic(self, a, b):
        """Calculate the Manhattan distance heuristic between two points."""
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)
