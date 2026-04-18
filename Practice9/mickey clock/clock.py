import pygame
import datetime

def get_time():
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second
    return minutes, seconds


def calculate_angles(minutes, seconds):
    minute_angle = minutes * 6
    second_angle = seconds * 6
    return minute_angle, second_angle