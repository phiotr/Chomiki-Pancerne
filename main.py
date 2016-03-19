# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from views.trackviewer import TrackViewer


class SomeApp(App):

    track_viewer = ObjectProperty(None)

    # def __init__(self, **kwargs):
    #     super(SomeApp, self).__init__(**kwargs)

    def build(self):
        Builder.load_file("kv/trackviewer.kv")

        track_impaths = ["tracks/R0010260.JPG" ]

        self.track_viewer = TrackViewer(list_of_track_images=track_impaths)
        return self.track_viewer

    def on_pause(self):
        return True

    def on_resume(self):
        return True

    def on_motion(self, motion_type, motion_event):
        #if motion_event.p
        print motion_event.profile


if __name__ == '__main__':
    SomeApp().run()
