# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder
from views.trackviewer import TrackViewer
from views.trackimage import TrackImage

class SomeApp(App):

    def build(self):
        Builder.load_file("kv/trackviewer.kv")

        track_impaths = ["R0010260.JPG", ]
        track_objects = [TrackImage("tracks/" + path) for path in track_impaths]

        return TrackViewer(list_of_track_images=track_objects)

    def on_pause(self):
        return True

    def on_resume(self):
        return True


if __name__ == '__main__':
    SomeApp().run()
