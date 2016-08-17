from gi.repository import Gtk
from functools import wraps
from compatibility import CompatibleScrolledWindow as GtkScrolledWindow


def scrollable(width=-1, height=-1, overlay_scrolling=False):
    """A function that takes optinal width and height and returns
    the scrollable decorator. -1 is the default GTK option for both
    width and height."""

    def scrollable_decorator(func):
        """Takes a function and returns the scroll_object_wrapper."""

        @wraps(func)
        def scroll_object_wrapper(*args, **kwargs):
            """Takes arguments and obtains the original object from
            func(*args, **kwargs). Creates a box and puts the original
            inside that box. Creates a scrolled window and puts the
            box inside it.
            """

            original = func(*args, **kwargs)
            scrolled_box = GtkScrolledWindow(None, None)
            scrolled_box.set_min_content_width(width)
            scrolled_box.set_min_content_height(height)
            scrolled_box.set_overlay_scrolling(overlay_scrolling)
            scrolled_box.add(original)
            return scrolled_box

        return scroll_object_wrapper

    return scrollable_decorator
