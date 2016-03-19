#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 - Piotr Skonieczka
#

from kivy.core.image import Image as CoreImage


class TrackImage:

    def __init__(self, source_file):
        self.texture = CoreImage.load(source_file).texture

        # Angle to pixels converters
        self.spherical_ratio_x = self.texture.width / 360.0
        self.spherical_ratio_y = self.texture.height / 180.0

    def get_subimage(self, center_x, center_y, radius_x, radius_y):
        pix_x_radius = radius_x * self.spherical_ratio_x
        pix_y_radius = radius_y * self.spherical_ratio_y

        pix_x_center = ((center_x + 180) % 360) * self.spherical_ratio_x
        pix_y_center = ((center_y + 90) % 180) * self.spherical_ratio_y

        return self.texture.get_region(int(pix_x_center), it(pix_y_center), int(pix_x_radius), int(pix_y_radius))