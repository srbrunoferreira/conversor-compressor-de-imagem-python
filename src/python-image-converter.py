# https://pypi.org/project/auto-py-to-exe/

from tkinter import Tk, Frame, Label, Button, Entry, TOP, X, LEFT, RIGHT, BOTTOM, BOTH, FLAT, GROOVE, SW, NW, NE, CENTER, SE
from tkinter.ttk import Combobox, Style
from os.path import dirname
from os import environ
from tkinter.filedialog import askdirectory

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

def compress(rate, inputPath, outputPath):
    pass

def convert(convertTo, inputPath, outputPath):
    pass

class Interface:
    def __init__(self):
        self.inputPath = ''
        self.outputPath = environ['USERPROFILE'] + '\\Desktop\\output'

        self.window = Tk()
        self.configureWindow()
        self.configureTemplate()
        self.configureModeFrames()
        self.compressorFrame.pack(side=TOP, anchor=NE, pady=5) # The default mode
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
        self.bottom = Frame(self.window, bg=WINDOW_BG)

        # HEADER WIDGETS
        self.title = Label(header, text='Comprimir imagem', bg=WINDOW_BG, fg=FONT_FG, font=FONTF['title'])
        self.mode = Combobox(header, values=['Comprimir', 'Converter'], state='readonly', font=FONTF['normal'])
        self.mode.current(0)
        self.mode.bind('<<ComboboxSelected>>', self.changeMode)
        # MIDDLE WIDGETS
        startBtn = Button(middle, command=self.start, text='Iniciar', bg=SECUNDARY_BG, font=FONTF['small'], fg=FONT_FG, relief=GROOVE)
        # BOTTOM WIDGETS
        selectContainer = Frame(self.bottom, bg=WINDOW_BG)
        selectInputContainer = Frame(selectContainer, bg=SECUNDARY_BG)
        selectInput = Button(selectInputContainer, command=self.setInputPath, text='Selecionar entrada...', bg=TERTIARY_BG, fg=FONT_FG, relief=FLAT, font=FONTF['small'])
        selectInputLabel = Label(selectInputContainer, text='Atual: por favor, selecione um diretório.', bg=SECUNDARY_BG, fg=FONT_FG)

        selectOutputContainer = Frame(selectContainer, bg=SECUNDARY_BG)
        selectOutput = Button(selectOutputContainer, command=self.setOutputPath, text='Selecionar saída...', bg=TERTIARY_BG, fg=FONT_FG, relief=FLAT, font=FONTF['small'])
        selectOutPutLabel = Label(selectOutputContainer, text='Atual: Área de Trabalho/output', bg=SECUNDARY_BG, fg=FONT_FG)

        # PACKING HEADER
        self.title.pack(side=LEFT)
        self.mode.pack(side=RIGHT)
        header.pack(side=TOP, fill=X, padx=20, pady=10)
        # PACKING MIDDLE
        middle.pack(side=TOP, anchor=SE, fill='both', expand=True, padx=5, pady=5)
        startBtn.pack(side=BOTTOM, anchor=SE, ipadx=14, ipady=2, padx=10, pady=10)
        # PACKING BOTTOM
        self.bottom.pack(side=BOTTOM, fill=X, padx=20, pady=10)
        selectContainer.pack(side=LEFT)
        selectInputContainer.pack(side=TOP, anchor=NW, pady=5)
        selectInput.pack(side=LEFT)
        selectInputLabel.pack(side=RIGHT)

        selectOutputContainer.pack(side=BOTTOM, anchor=SW, pady=5)
        selectOutput.pack(side=LEFT)
        selectOutPutLabel.pack(side=RIGHT)
    
    def configureModeFrames(self):
        # COMPRESS MODE
        self.compressorFrame = Frame(self.bottom, bg=WINDOW_BG)
        compressorLabel = Label(self.compressorFrame, width=20, text='Taxa (%)', bg=SECUNDARY_BG, fg=FONT_FG, font=FONTF['small'])
        compressorInput = Entry(self.compressorFrame, width=20, bg=TERTIARY_BG, fg=FONT_FG, font=FONTF['small'], relief=FLAT, justify=CENTER)

        # CONVERT MODE
        self.convertFrame = Frame(self.bottom, bg=WINDOW_BG)
        convertLabel = Label(self.convertFrame, width=20, text='Converter para', bg=SECUNDARY_BG, fg=FONT_FG, font=FONTF['small'])
        convertInput = Combobox(self.convertFrame, width=20, values=['png', 'jpg'], state='readonly', font=FONTF['small'])
        convertInput.current(0)
        convertInput.bind('<<ComboboxSelected>>', self.changeMode)

        # PACKING COMPRESS MODE WIDGETS
        compressorLabel.pack(side=TOP, pady=1, ipady=2)
        compressorInput.pack(side=BOTTOM, ipady=4, ipadx=11)
        compressorInput.insert(0, '75')

        # PACKING CONVERT MODE WIDGETS
        convertLabel.pack(side=TOP, pady=1, ipady=2)
        convertInput.pack(side=BOTTOM, ipady=4)

    def changeMode(self, event):
        mode = self.mode.get()
        self.title.config(text=mode + ' imagem')
        if (mode == 'Comprimir'):
            self.convertFrame.pack_forget()
            self.compressorFrame.pack(side=TOP, anchor=NE, pady=5)
        else:
            self.compressorFrame.pack_forget()
            self.convertFrame.pack(side=TOP, anchor=NE, pady=5)

    def start(self):
        pass

    def setInputPath(self):
        self.inputPath = askdirectory()

    def setOutputPath(self):
        self.inputPath = askdirectory()



Interface()
