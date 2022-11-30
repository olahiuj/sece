import tkinter


class UI:
    def __init__(self):
        self.__main_window__ = tkinter.Tk()
        self.__main_window__.title('sece diff')
        self.__main_window__.rowconfigure(0, weight=0)
        self.__main_window__.rowconfigure(1, weight=1)
        self.__main_window__.rowconfigure(2, weight=0)
        self.__main_window__.columnconfigure(0, weight=1)
        self.__main_window__.columnconfigure(1, weight=1)
        self.__main_window__.columnconfigure(2, weight=0)

        # File Name Label
        self.__left_file_name__ = tkinter.Label(self.__main_window__)
        self.__left_file_name__.grid(row=0, column=0, sticky=tkinter.NSEW)

        self.__right_file_name__ = tkinter.Label(self.__main_window__)
        self.__right_file_name__.grid(row=0, column=1, sticky=tkinter.NSEW)

        # Left Text Frame Initialization
        self.__left_text__ = tkinter.Text(self.__main_window__)
        self.__left_text__.grid(row=1, column=0, sticky=tkinter.NSEW)
        self.__left_text__.config(state=tkinter.DISABLED)
        self.__left_text__.config(yscrollcommand=self.text_on_scroll)
        self.__left_text__ = TextFrame(self.__left_text__)

        # Left Text Frame Initialization
        self.__right_text__ = tkinter.Text(self.__main_window__)
        self.__right_text__.grid(row=1, column=1, sticky=tkinter.NSEW)
        self.__right_text__.config(state=tkinter.DISABLED)
        self.__right_text__.config(yscrollcommand=self.text_on_scroll)
        self.__right_text__ = TextFrame(self.__right_text__)

        # Scroll Bar Initialization
        self.__vertical_scroll_bar__ = tkinter.Scrollbar(self.__main_window__)
        self.__vertical_scroll_bar__.grid(row=0, column=2, rowspan=3, sticky=tkinter.NS)
        self.__vertical_scroll_bar__.config(command=self.bar_on_scroll)

        self.__eq_button__ = tkinter.Button(
            self.__main_window__,
            text="EQ",
            justify=tkinter.CENTER,
            takefocus=0
        )
        self.__eq_button__.grid(row=2, column=0, sticky=tkinter.NSEW)

        self.__neq_button__ = tkinter.Button(
            self.__main_window__,
            text="NEQ",
            justify=tkinter.CENTER,
            takefocus=0
        )
        self.__neq_button__.grid(row=2, column=1, sticky=tkinter.NSEW)

    def bar_on_scroll(self, _, position, type=None):
        self.__left_text__.scroll_to(position)
        self.__right_text__.scroll_to(position)

    def text_on_scroll(self, first, last, type=None):
        self.bar_on_scroll(None, first)
        self.__vertical_scroll_bar__.set(first, last)

    def update_text(self, diff_result, filename1, filename2):
        self.__left_file_name__.config(text=filename1)
        self.__right_file_name__.config(text=filename2)
        for d in diff_result:
            cont = d['cont']
            match d['type']:
                case 'L':
                    self.__left_text__.append_line(cont, 'red')
                    self.__right_text__.new_line('gray')
                case 'R':
                    self.__right_text__.append_line(cont, 'green')
                    self.__left_text__.new_line('gray')
                case 'S':
                    self.__left_text__.append_line(cont, 'white')
                    self.__right_text__.append_line(cont, 'white')
                case 'D':
                    # TODO: lines with internal differences
                    pass

    def eq_action(self, func):
        self.__eq_button__.config(command=func)

    def neq_action(self, func):
        self.__neq_button__.config(command=func)

    def main_loop(self):
        self.__main_window__.mainloop()


def modifies_text(func):
    def wrapped_func(*args, **kwargs):
        self = args[0]
        self.__text_frame__.config(state=tkinter.NORMAL)
        func(*args, **kwargs)
        self.__text_frame__.config(state=tkinter.DISABLED)

    return wrapped_func


class TextFrame:
    def __init__(self, text_frame):
        self.__text_frame__ = text_frame
        self.__text_frame__.tag_configure('red', background='#ffc4c4')
        self.__text_frame__.tag_configure('darkred', background='#ff8282')
        self.__text_frame__.tag_configure('green', background='#c9fcd6')
        self.__text_frame__.tag_configure('darkgreen', background='#50c96e')
        self.__text_frame__.tag_configure('gray', background='#dddddd')
        self.__text_frame__.tag_configure('white', background='#ffffff')

    def scroll_to(self, position):
        self.__text_frame__.yview_moveto(position)

    @modifies_text
    def new_line(self, color):
        self.__text_frame__.insert(tkinter.END, '\n', color)

    @modifies_text
    def append(self, cont, color):
        self.__text_frame__.insert(
            tkinter.END,
            cont,
            color
        )

    def append_line(self, cont, color):
        self.append(cont, color)
        self.new_line(color)
