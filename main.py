# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from views.trackviewer import TrackViewer


class SomeApp(App):
    track_viewer = ObjectProperty(None)

    use_kivy_settings = False

    def __init__(self, **kwargs):
        super(SomeApp, self).__init__(**kwargs)

    def build(self):
        Window.bind(on_motion=self.on_motion)
        Window.bind(mouse_pos=self.on_mouse_move)

        Builder.load_file("kv/trackviewer.kv")

        track_impaths = ["tracks/R00102%i.JPG" % idx for idx in range(60, 79)]
        #
        # track_impaths = ["tracks/R0010260.JPG", "tracks/R0010261.JPG", "tracks/R0010262.JPG", "tracks/R0010263.JPG",
        #                  "tracks/R0010264.JPG", "tracks/R0010264.JPG",]

        self.track_viewer = TrackViewer(list_of_track_images=track_impaths)
        return self.track_viewer

    def open_settings(self, *largs):
        return True

    def on_pause(self):
        return True

    def on_resume(self):
        return True

    def on_mouse_move(self, window, position):
        self.track_viewer.move_view_port(position)

    def on_motion(self, window, motion_type, motion_event):
        # print motion_event, dir(motion_event)

        if hasattr(motion_event, "button") and motion_type == "end" and motion_event.button == "left":
            self.track_viewer.go_to_the_next_image()


if __name__ == '__main__':
    SomeApp().run()
