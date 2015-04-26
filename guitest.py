from gi.repository import Gtk


class MyApp (object):

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("guitest.glade")
        signals = {'load_info': self.load_info}
        self.builder.connect_signals(signals)

    def run(self):
        self.builder.get_object("window1").show_all()
        Gtk.main()

    def on_window1_destroy(self, *args):
        Gtk.main_quit()

    def load_info(self):
        print "Hello world"


MyApp().run()