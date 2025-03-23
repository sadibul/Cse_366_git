import pygame
import heapq

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
        if self.path:
            next_position = self.path.pop(0)
            self.position = list(next_position)
            self.rect.topleft = (self.position[0] * self.grid_size, self.position[1] * self.grid_size)
            self.check_task_completion()
        else:
            self.moving = False

    def check_task_completion(self):
        position_tuple = tuple(self.position)
        if position_tuple in self.environment.task_locations:
            task_number = self.environment.task_locations.pop(position_tuple)
            self.task_completed += 1
            self.completed_tasks.append(task_number)

    def find_nearest_task(self):
        nearest_task = None
        shortest_path = None
        for task_position in self.environment.task_locations.keys():
            path = self.A_star(task_position)
            if path:
                if not shortest_path or len(path) < len(shortest_path):
                    shortest_path = path
                    nearest_task = task_position
        if shortest_path:
            self.path = shortest_path[1:]
            self.moving = True

    def heuristic(self, a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    def get_neighbors(self, position):
        x, y = position
        neighbors = []
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if self.environment.is_within_bounds(nx, ny) and not self.environment.is_barrier(nx, ny):
                neighbors.append((nx, ny))
        return neighbors

    def A_star(self, target):
        start = tuple(self.position)
        goal = target
        
        open_set = []
        heapq.heappush(open_set, (0, start, [start]))
        g_scores = {start: 0}
        f_scores = {start: self.heuristic(start, goal)}

        while open_set:
            (_, current, path) = heapq.heappop(open_set)
            if current == goal:
                return path

            neighbors = self.get_neighbors(current)
            for neighbor in neighbors:
                tentative_g_score = g_scores[current] + 1
                
                if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                    g_scores[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor, goal)
                    f_scores[neighbor] = f_score
                    heapq.heappush(open_set, (f_score, neighbor, path + [neighbor]))
        return None
