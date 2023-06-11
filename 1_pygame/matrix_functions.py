import pygame
import math
import numpy

def translate(pos):
    tx, ty, tz = pos
    return numpy.array([
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [tx,ty,tz,1]
    ])

def rotate_x(a):
    return numpy.array([
        [1,0,0,0],
        [0,math.cos(a),math.sin(a),0],
        [0,-math.sin(a),math.cos(a),0],
        [0,0,0,1]
    ])

def rotate_y(a):
    return numpy.array([
        [math.cos(a),0,-math.sin(a),a],
        [0,1,0,0],
        [math.sin(a),0,math.cos(a),0],
        [0,0,0,1]
    ])

def rotate_z(a):
    return numpy.array([
        [math.cos(a),math.sin(a),0,0],
        [-math.sin(a),math.cos(a),0,0],
        [0,0,1,0],
        [0,0,0,1]
    ])

def scale(n):
    return numpy.array([
        [n,0,0,0],
        [0,n,0,0],
        [0,0,n,0],
        [0,0,0,1]
    ])