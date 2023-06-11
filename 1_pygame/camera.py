import pygame
import math
import numpy
from matrix_functions import *


class Camera:
    def __init__(self, render, position):
        self.render = render
        self.position = numpy.array([*position, 1.0])
        self.forward = numpy.array([0, 0, 1, 1])
        self.up = numpy.array([0, 1, 0, 1])
        self.right = numpy.array([1, 0, 0, 1])
        self.h_fov = math.pi / 3
        self.v_fov = self.h_fov * (render.HEIGHT / render.WIDTH)
        self.near_plane = 0.1
        self.far_plane = 100
        self.moving_speed = 0.1
        self.rotation_speed = 0.015

        self.anglePitch = 0
        self.angleYaw = 0
        self.angleRoll = 0

    def control(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.position -= self.right * self.moving_speed
        if key[pygame.K_d]:
            self.position += self.right * self.moving_speed
        if key[pygame.K_w]:
            self.position += self.forward * self.moving_speed
        if key[pygame.K_s]:
            self.position -= self.forward * self.moving_speed
        if key[pygame.K_q]:
            self.position += self.up * self.moving_speed
        if key[pygame.K_e]:
            self.position -= self.up * self.moving_speed

        if key[pygame.K_LEFT]:
            self.camera_yaw(-self.rotation_speed)
        if key[pygame.K_RIGHT]:
            self.camera_yaw(self.rotation_speed)
        if key[pygame.K_UP]:
            self.camera_pitch(-self.rotation_speed)
        if key[pygame.K_DOWN]:
            self.camera_pitch(self.rotation_speed)

    def camera_yaw(self, angle):
        self.angleYaw += angle

    def camera_pitch(self, angle):
        self.anglePitch += angle

    def axiiIdentity(self):
        self.forward = numpy.array([0, 0, 1, 1])
        self.up = numpy.array([0, 1, 0, 1])
        self.right = numpy.array([1, 0, 0, 1])

    def camera_update_axii(self):
        # rotate = rotate_y(self.angleYaw) @ rotate_x(self.anglePitch)
        rotate = rotate_x(self.anglePitch) @ rotate_y(self.angleYaw)  # this concatenation gives right visual
        self.axiiIdentity()
        self.forward = self.forward @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate

    def camera_matrix(self):
        self.camera_update_axii()
        return self.translate_matrix() @ self.rotate_matrix()

    def translate_matrix(self):
        x, y, z, w = self.position
        return numpy.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])

    def rotate_matrix(self):
        rx, ry, rz, w = self.right
        fx, fy, fz, w = self.forward
        ux, uy, uz, w = self.up
        return numpy.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])