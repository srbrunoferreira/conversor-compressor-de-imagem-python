from tkinter import Tk, Frame, Label, Button, TOP, X, LEFT, BOTH, RIGHT, BOTTOM, FLAT, SW, NW
from tkinter.ttk import Combobox, Style
from os.path import dirname
from converter_interface import ConverterInterface
from compress_interface import CompressInterface

WINDOW_BG = '#25242A'
SECUNDARY_BG = '#151418'
TERTIARY_BG = '#353438'
QUATERNARY_BG = '#515055'
FONT_FG = '#FFFFFF'
FONTF = {
    'title': ('Segoe UI', 15),
    'big': ('Segoe UI', 13.8),
    'normal': ('Segoe UI', 11),
    'small': ('Segoe UI Semibold', 11)
}


class Interface(Tk):
    def __init__(self):
        self.window = Tk()
        self.configureWindow()
        self.configureTemplate()
        self.window.mainloop()

    def configureWindow(self):
        self.window.geometry('640x330+363+150')
        self.window.configure(bg=WINDOW_BG)
        self.window.iconbitmap(dirname(__file__) + '\icon.ico')
        self.window.title('Image Converter & Compressor')
        self.window.resizable(False, False)

    def configureTemplate(self):
        comboboxStyle = Style()
        comboboxStyle.theme_create('comboboxstyle', parent='alt', settings={'TCombobox': {'configure': { 'selectbackground':  SECUNDARY_BG, 'fieldbackground':  SECUNDARY_BG, 'background': SECUNDARY_BG, 'bordercolor': QUATERNARY_BG, 'padding': 5, 'arrowsize': 18, 'arrowcolor': 'white', 'foreground': 'white'}}})
        comboboxStyle.theme_use('comboboxstyle')

        # CONTAINERS
        header = Frame(self.window, bg=WINDOW_BG)
        middle = Frame(self.window, bg=QUATERNARY_BG)
        bottom = Frame(self.window, bg=WINDOW_BG)

        # HEADER WIDGETS
        self.title = Label(header, text='Comprimir imagem', bg=WINDOW_BG, fg=FONT_FG, font=FONTF['title'])
        self.mode = Combobox(header, values=['Converter', 'Comprimir'], state='readonly', font=FONTF['normal'])
        self.mode.current(0)
        # BOTTOM WIDGETS
        selectInputContainer = Frame(bottom, bg=SECUNDARY_BG, width=300)
        selectInput = Button(selectInputContainer, text='Selecionar entrada...', bg=SECUNDARY_BG, fg=FONT_FG, relief=FLAT, font=FONTF['small'])
        selectInputLabel = Label(selectInputContainer, text='Atual: por favor, selecione um diretório.', bg=TERTIARY_BG, fg=FONT_FG)

        selectOutputContainer = Frame(bottom, bg=SECUNDARY_BG, width=300)
        selectOutput = Button(selectOutputContainer, text='Selecionar saída...', bg=SECUNDARY_BG, fg=FONT_FG, relief=FLAT, font=FONTF['small'])
        selectOutPutLabel = Label(selectOutputContainer, text='Atual: Área de Trabalho/output', bg=TERTIARY_BG, fg=FONT_FG)

        # PACKING HEADER
        self.title.pack(side=LEFT)
        self.mode.pack(side=RIGHT)
        header.pack(side=TOP, fill=X, padx=20, pady=10)
        # PACKING MIDDLE
        middle.pack(side=TOP, fill=BOTH)
        # PACKING BOTTOM
        bottom.pack(side=BOTTOM, fill=X, padx=20, pady=10)
        selectInputContainer.pack(side=TOP, anchor=NW, ipadx=5, ipady=4, pady=10)
        selectInput.pack(side=LEFT, padx=5)
        selectInputLabel.pack(side=RIGHT, padx=5, ipadx=5, ipady=5)

        selectOutputContainer.pack(side=BOTTOM, anchor=SW, ipadx=5, ipady=4)
        selectOutput.pack(side=LEFT, padx=5)
        selectOutPutLabel.pack(side=RIGHT, padx=5, ipadx=5, ipady=5)
    
    def setInputDir(self):
        pass

    def setOutputdir(self):
        pass



Interface()
