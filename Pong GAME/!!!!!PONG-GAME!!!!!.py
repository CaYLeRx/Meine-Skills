# War grossteil abgeschrieben,
# ich wollte die erfahrung machen wie es ist 
# in sollchen Codes nach Fehlern zu suchen
# und diesezu behebn und optisch anzupassen!!


import pygame
import numpy as np


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        self.p1_pos = np.array([10, 250])
        self.p2_pos = np.array([780, 250])
        self.ball_pos = np.array([385, 285])

        self.ball_acceleration = np.array([5, 6])
        self.player_acceleration = np.array([0, 5])

        self.game_loop()

    def reset(self):
        self.p1_pos = np.array([10, 250])
        self.p2_pos = np.array([780, 250])
        self.ball_pos = np.array([385, 285])

    def game_loop(self):
        while True:
            self.clock.tick(144)
            self.screen.fill((0, 0, 0))

            self.input()
            self.update()
            self.draw()

            pygame.display.flip()

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if pygame.key.get_pressed()[pygame.K_w]:
             self.p1_pos += self.player_acceleration * np.array([0, -1])

        if pygame.key.get_pressed()[pygame.K_s]:
             self.p1_pos += self.player_acceleration

        if pygame.key.get_pressed()[pygame.K_UP]:
             self.p2_pos += self.player_acceleration * np.array([0, -1])

        if pygame.key.get_pressed()[pygame.K_DOWN]:
             self.p2_pos += self.player_acceleration

    def update(self):
        if self.ball_collision_screen_left() or self.ball_collision_screen_right():
            self.reset()

        if self.ball_player_collision():
            self.ball_acceleration = self.ball_acceleration * np.array([-1, 1])

        if self.ball_collision_screen_top() or self.ball_collision_screen_bottom():
            self.ball_acceleration = self.ball_acceleration * np.array([1, -1])

        self.ball_pos += self.ball_acceleration

    def draw(self):
        pygame.draw.rect(self.screen, pygame.Color(255, 0, 0), (self.p1_pos[0], self.p1_pos[1], 10, 100))  # Farbe Player One & Position
        pygame.draw.rect(self.screen, pygame.Color(204, 255, 0), (self.p2_pos[0], self.p2_pos[1], 10, 100))  # Farbe Player Two & Position
        pygame.draw.rect(self.screen, pygame.Color(255, 255, 255), (self.ball_pos[0], self.ball_pos[1], 15, 15))  # Fabe Ball & Position

    def ball_player_collision(self):
        return self.ball_player1_collision() or self.ball_player2_collision()

    def ball_player1_collision(self):
        return self.aabb_collision(self.p1_pos[0], self.p1_pos[1], 10, 100, self.ball_pos[0], self.ball_pos[1], 15, 15)

    def ball_player2_collision(self):
        return self.aabb_collision(self.p2_pos[0], self.p2_pos[1], 10, 100, self.ball_pos[0], self.ball_pos[1], 15, 15)

    def aabb_collision(self, a_x, a_y,  a_width, a_height, b_x, b_y, b_width, b_height):
        collision_x = a_x + a_width >= b_x and b_x + b_width >= a_x
        collision_y = a_y + a_height >= b_y and b_y + b_height >= a_y

        return collision_y and collision_x

    def ball_collision_screen_left(self):
        return self.ball_pos[0] <= 0

    def ball_collision_screen_right(self):
        return self.ball_pos[0] + 15 >= 800

    def ball_collision_screen_top(self):
        return self.ball_pos[1] <= 0

    def ball_collision_screen_bottom(self):
        return self.ball_pos[1] + 15 >= 600



Game()

