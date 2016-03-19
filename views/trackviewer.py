#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 - Piotr Skonieczka
#

from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen



class TrackViewer(Screen):
    left_eye_image = ObjectProperty(None)
    right_eye_image = ObjectProperty(None)

    def __init__(self, list_of_track_images, **kwargs):
        Screen.__init__(self, **kwargs)

        self.list_of_track_images = list_of_track_images
        self.current_image = 0

        self.looking_direction_x = 0
        self.looking_direction_y = 0
        self.eye_range_x = 120
        self.eye_range_y = 80
        self.eye_offset = 3

        self.track_image = TrackImage("tracks/R0010260.JPG")
        self.display_texture()

    def display_texture(self):
        photo = self.list_of_track_images[self.current_image]

        self.left_eye_image.texture = \
            photo.get_subimage(self.looking_direction_x, self.looking_direction_y, self.eye_range_x, self.eye_range_y)
        self.right_eye_image.texture = \
            photo.get_subimage(self.looking_direction_x + self.eye_offset, self.looking_direction_y, self.eye_range_x, self.eye_range_y)



    def on_touch_move(self, touch):
        self.looking_direction_x = (touch.x / 2) % 360
        self.looking_direction_y = (touch.y / 2) % 180

        self.display_texture()


