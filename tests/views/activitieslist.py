# Copyright (C) 2013, Daniel Narvaez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

from gi.repository import Gtk
from dbus.mainloop.glib import DBusGMainLoop
DBusGMainLoop(set_as_default=True)

from jarabe.desktop.activitieslist import ActivityListPalette


tests_dir = os.getcwd()
base_dir = os.path.dirname(tests_dir)
data_dir = os.path.join(tests_dir, "data")


class MockActivityInfo:
    @staticmethod
    def get_bundle_id():
        return "mock"

    @staticmethod
    def get_activity_version():
        return 1

    @staticmethod
    def get_is_favorite():
        return False

    @staticmethod
    def get_icon():
        return os.path.join(data_dir, "activity.svg")

    @staticmethod
    def get_name():
        return "mock"

    @staticmethod
    def get_path():
        return "mock"

    @staticmethod
    def is_user_activity():
        return True


os.environ["SUGAR_MIME_DEFAULTS"] = \
    os.path.join(base_dir, "data", "mime.defaults")

palette = ActivityListPalette(MockActivityInfo())
palette.popup()

Gtk.main()
