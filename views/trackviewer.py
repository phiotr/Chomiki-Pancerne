#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 - Piotr Skonieczka
#

from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

from views.trackimage import TrackImage


class TrackViewer(Screen):
    left_eye_image = ObjectProperty(None)
    right_eye_image = ObjectProperty(None)

    def __init__(self, list_of_track_images, **kwargs):
        Screen.__init__(self, **kwargs)
        self._read_images(list_of_track_images)

        self.looking_direction_x = 0
        self.looking_direction_y = 0
        self.eye_range_x = 120
        self.eye_range_y = 80
        self.eye_offset = 3

        self._display_texture()


    def _read_images(self, list_of_files):
        self.list_of_track_images = [TrackImage(image_path) for image_path in list_of_files]
        self.current_image_number = 0
        self.last_image_number = len(list_of_files) - 1

    def _display_texture(self):
        # print "Going to display textrue"
        photo = self.list_of_track_images[self.current_image_number]

        self.left_eye_image.texture = \
            photo.get_subimage(self.looking_direction_x, self.looking_direction_y, self.eye_range_x, self.eye_range_y)
        self.right_eye_image.texture = \
            photo.get_subimage(self.looking_direction_x + self.eye_offset, self.looking_direction_y, self.eye_range_x, self.eye_range_y)

    def on_touch_move(self, touch):
        self.looking_direction_x = (touch.x / 2) % 360
        self.looking_direction_y = (touch.y / 2) % 180

        self._display_texture()

    def go_to_the_next_image(self):
        if self.current_image_number < self.last_image_number:
            self.current_image_number += 1
            self._display_texture()

    def go_to_the_previous_image(self):
        if self.current_image_number > 0:
            self.current_image_number -= 1
            self._display_texture()

    def on_scroll_motion(self):
        print "scroll"