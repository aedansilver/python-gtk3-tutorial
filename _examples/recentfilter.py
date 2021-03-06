#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class RecentFilter(Gtk.RecentChooserDialog):
    def __init__(self):
        Gtk.RecentChooserDialog.__init__(self)
        self.set_title('RecentFilter')
        self.set_default_size(300, 200)

        recentfilter = Gtk.RecentFilter()
        recentfilter.set_name('All Items')
        recentfilter.add_pattern('*')
        self.add_filter(recentfilter)

        recentfilter = Gtk.RecentFilter()
        recentfilter.set_name('Within last 3 days')
        recentfilter.add_age(3)
        self.add_filter(recentfilter)

        recentfilter = Gtk.RecentFilter()
        recentfilter.set_name('Image Files')
        recentfilter.add_pattern('*.png')
        recentfilter.add_pattern('*.jpg')
        recentfilter.add_pattern('*.svg')
        self.add_filter(recentfilter)

dialog = RecentFilter()
dialog.run()
dialog.destroy()
