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
        pix_x_radius = radius_x * self.spherical_ratio_x
        pix_y_radius = radius_y * self.spherical_ratio_y

        pix_x_center = int(center_x * self.spherical_ratio_x)
        pix_y_center = int(center_y * self.spherical_ratio_y)

        # print "X:", pix_x_center, pix_x_radius
        # print "Y:", pix_y_center, pix_y_radius

        # if pix_y_center + pix_y_radius > self.texture.height:
        #     pix_y_center = self.texture.height - pix_y_radius
        #     print "gorna krawedz"
        #
        # if pix_y_center - pix_y_radius < 0:
        #     pix_y_center = pix_y_radius
        #     print "dolna krawedz"

        if pix_x_center + pix_x_radius > self.texture.width:
            pix_x_center = self.texture.width - pix_x_radius
            # print "za bardzo na prawo"

        if pix_x_center - pix_x_radius < -60:
            pix_x_center = pix_x_radius
            # print "za bardzo na lewo"

        return self.texture.get_region(int(pix_x_center), int(pix_y_center), int(pix_x_radius), int(pix_y_radius))