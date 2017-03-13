import os.path
from router.router import Router
from utils.constants import *


class TextEditor:
    def __init__(self):
        self.file_lines = [EMPTY_LINE]
        self.current_line_index = FIRST_LINE_INDEX
        self.router = Router(self)
        self.end = False

    def start(self):
        print(WELCOME_TEXT_MESSAGE)
        while not self.end:
            command = input()
            self.router.get_route(command)

    @staticmethod
    def help():
        for command in ALL_POSSIBLE_COMMANDS:
            print(command)

    def new_file(self):
        self.file_lines = [EMPTY_LINE]

    def load_file(self):
        file_name = input()
        try:
            file = open(os.path.dirname(__file__) + PATH_TO_FILE % file_name, READ_FILE)
            self.file_lines = file.read().split(NEW_LINE)
            file.close()
        except FileNotFoundError:
            print(FILE_ERROR_MESSAGE)

    def save_file(self):
        file_name = input()
        file = open(os.path.dirname(__file__) + PATH_TO_FILE % file_name, WRITE_FILE)
        file.write(NEW_LINE.join(self.file_lines))
        file.close()

    def move_up(self):
        if not self.is_first_line():
            self.decrement_line_index()
            self.print_current_line()

    def move_down(self):
        if not self.is_last_line():
            self.increment_line_index()
            self.print_current_line()

    def page_up(self):
        start_index = self.current_line_index - PAGE_UP_DOWN_RANGE if self.current_line_index > PAGE_UP_DOWN_RANGE else 0
        for i in range(start_index, self.current_line_index):
            self.current_line_index = i
            self.print_current_line()

    def page_down(self):
        end_index = self.current_line_index + PAGE_UP_DOWN_RANGE \
            if self.get_count_lines_before_end() > PAGE_UP_DOWN_RANGE else len(self.file_lines)
        while self.current_line_index != end_index:
            self.move_down()

    def head(self):
        self.current_line_index = FIRST_LINE_INDEX
        self.print_current_line()

    def tail(self):
        self.current_line_index = self.get_last_line_index()
        self.print_current_line()

    def insert_before(self):
        self.decrement_line_index() if not self.is_first_line() else None
        self.insert_empty_line()
        self.print_current_line()

    def insert_after(self):
        self.increment_line_index()
        self.insert_empty_line()
        self.print_current_line()

    def delete(self):
        self.remove_current_line() if not self.is_first_line() else self.set_current_line(EMPTY_LINE)

    def replace(self):
        self.set_current_line(input())

    def show(self):
        start_index = self.current_line_index - SHOW_UP_DOWN_RANGE \
            if self.current_line_index > SHOW_UP_DOWN_RANGE else FIRST_LINE_INDEX
        end_index = self.current_line_index + SHOW_UP_DOWN_RANGE + 1 \
            if self.get_count_lines_before_end() > SHOW_UP_DOWN_RANGE else len(self.file_lines)
        [self.print_line(i) for i in range(start_index, self.current_line_index)]
        self.print_current_line()
        [self.print_line(i) for i in range(self.current_line_index + 1, end_index)]

    def exit(self):
        print(EXIT_TEXT_MESSAGE)
        self.end = True

    def get_count_lines_before_end(self):
        return self.get_last_line_index() - self.current_line_index

    def is_first_line(self):
        return self.current_line_index == FIRST_LINE_INDEX

    def is_last_line(self):
        return self.current_line_index == self.get_last_line_index()

    def insert_empty_line(self):
        self.file_lines.insert(self.current_line_index, EMPTY_LINE)

    def get_last_line_index(self):
        return len(self.file_lines) - 1

    def increment_line_index(self):
        self.current_line_index += 1

    def decrement_line_index(self):
        self.current_line_index -= 1

    def print_current_line(self):
        print(PRINT_LINE_FORMAT % (self.current_line_index + 1, self.file_lines[self.current_line_index]))

    def print_line(self, index):
        print(PRINT_LINE_FORMAT % (index + 1, self.file_lines[index]))

    def set_current_line(self, value):
        self.file_lines[self.current_line_index] = value

    def remove_current_line(self):
        if self.is_last_line():
            self.current_line_index -= 1
        self.file_lines.pop(self.current_line_index + 1)
