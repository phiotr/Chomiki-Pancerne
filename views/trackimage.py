#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 - Piotr Skonieczka
#

from kivy.core.image import Image as CoreImage


class TrackImage:

    def __init__(self, source_file):
        self.source_file = source_file
        self.texture = CoreImage.load(source_file).texture
        # Angle to pixels converters
        self.spherical_ratio_x = self.texture.width / 360.0
        self.spherical_ratio_y = self.texture.height / 180.0

    def __str__(self):
        print self.source_file

    def get_texture_size(self):
        return self.texture.size

    def get_subimage(self, center_x, center_y, radius_x, radius_y):

        if center_x < radius_x:
            center_x = radius_x
        if center_x + radius_x > 360:
            center_x = 360 - radius_x

        pix_x_center = int(center_x * self.spherical_ratio_x)
        pix_y_center = int(center_y * self.spherical_ratio_y)

        pix_x_radius = int(radius_x * self.spherical_ratio_x)
        pix_y_radius = int(radius_y * self.spherical_ratio_y)

        return self.texture.get_region(int(pix_x_center), int(pix_y_center), int(pix_x_radius), int(pix_y_radius))