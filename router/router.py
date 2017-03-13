from router.route import Route
from utils.constants import *


class Router:
    def __init__(self, editor):
        self.routes = [
            Route(HELP, editor.help),
            Route(SHOW_CURRENT_LINE, editor.print_current_line),
            Route(NEW_FILE, editor.new_file),
            Route(LOAD_FILE, editor.load_file),
            Route(SAVE_FILE, editor.save_file),
            Route(MOVE_UP, editor.move_up),
            Route(MOVE_DOWN, editor.move_down),
            Route(PAGE_UP, editor.page_up),
            Route(PAGE_DOWN, editor.page_down),
            Route(HEAD, editor.head),
            Route(TAIL, editor.tail),
            Route(INSERT_BEFORE, editor.insert_before),
            Route(INSERT_AFTER, editor.insert_after),
            Route(DELETE, editor.delete),
            Route(REPLACE, editor.replace),
            Route(SHOW, editor.show),
            Route(EXIT, editor.exit)
        ]

    def get_route(self, command):
        for route in self.routes:
            if command == route.command:
                route.method()
                return
        print(INVALID_COMMAND_MESSAGE)
