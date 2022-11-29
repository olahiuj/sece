import tkinter


class UI:
    def __init__(self):
        self.__main_window__ = tkinter.Tk()
        self.__main_window__.title('sece diff')

        self.__left_text__ = tkinter.Text(self.__main_window__)
        self.__left_text__.grid(row=0, column=0)
        self.__left_text__.insert(tkinter.END, ''.join(f"{i}\n" for i in range(100)))
        self.__left_text__.config(state=tkinter.DISABLED)
        self.__left_text__.config(yscrollcommand=self.text_on_scroll)

        self.__right_text__ = tkinter.Text(self.__main_window__)
        self.__right_text__.grid(row=0, column=1)
        self.__right_text__.insert(tkinter.END, ''.join(f"{i}\n" for i in range(100)))
        self.__right_text__.config(state=tkinter.DISABLED)
        self.__right_text__.config(yscrollcommand=self.text_on_scroll)

        self.__vertical_scroll_bar__ = tkinter.Scrollbar(self.__main_window__)
        self.__vertical_scroll_bar__.grid(row=0, column=2, sticky=tkinter.NS)
        self.__vertical_scroll_bar__.config(command=self.bar_on_scroll)

        self.__main_window__.mainloop()

    def bar_on_scroll(self, _, position):
        self.__left_text__.yview_moveto(position)
        self.__right_text__.yview_moveto(position)

    def text_on_scroll(self, first, last):
        self.bar_on_scroll(None, first)
        self.__vertical_scroll_bar__.set(first, last)
