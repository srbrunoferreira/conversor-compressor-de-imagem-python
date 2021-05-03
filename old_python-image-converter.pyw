# Esta é uma versão antiga do programa.
# Com base nela, elaborei a nova versão.

from tkinter import Tk, Frame, Label, Button, PhotoImage, TOP, BOTH, LEFT, RIGHT, NW, SE, RIDGE
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showwarning, showinfo
from tkinter.ttk import Combobox, Style
from os import environ, listdir
from os.path import isfile, isdir, join
from pathlib import Path
from ntpath import normpath
from datetime import datetime
from PIL import Image

TRY_TRANSPARENT_BG = False

QUALITY_LEVEL = {
    'PNG': 90,
    'JPEG': 90,
    'JPG': 90,
    'ICO': 90
}

DEFAULT_SAVE_DIR = join(
    join(environ['USERPROFILE']), 'Desktop') + '\\converted_images\\'

COLOR = {
    'darkBlack': '#2f3640',
    'darkBlack2': '#1e272e',
    'lightBlack': '#353b48',
    'lightBlack2': '#485460',
    'lightBlue': '#273c75',
    'white': '#f5f6fa',
}

COMPATIBLE_IMG_FORMATS = ['png', 'jpg', 'jpeg', 'ico']
COMPATIBLE_IMG_FORMATS_UPPER = ['PNG', 'JPG', 'JPEG', 'ICO']

FONT = {
    'title': ('Tahoma', 15),
    'normal': ('Tahoma', 13),
    'small': ('Tahoma', 11)
}


class Interface():
    inputDir = ''
    outputDir = ''
    def __init__(self):
        print('[INICIANDO INTERFACE]')
        print('[CONFIGURANDO INTERFACE]')

        self.root = Tk()
        self.configureWindow()
        self.insertElementsInWindow()

        print('[INTERFACE CONFIGURADA]')

        self.root.mainloop()

    def setInputDir(self):
        directory = askdirectory()
        if isdir(directory):
            self.inputDir = directory
            print('[DIRETÓRIO DE ENTRADA DEFINIDO PARA]: ' + self.inputDir)
        else:
            showwarning(title='Diretório inválido', message='O diretório que você informou é inválido.\nTente novamente.')

    def setOutPutDir(self):
        directory = askdirectory()
        if isdir(directory):
            self.outputDir = directory
            print('[DIRETÓRIO DE SAÍDA DEFINIDO PARA]: ' + self.outputDir)
        else:
            showwarning(title='Diretório inválido', message='O diretório que você informou é inválido.\nTente novamente.')

    def checkInputs(self):
        if len(self.inputDir) > 0 and len(self.selectOutputFormat.get()) > 0:
            if len(self.outputDir) > 0:
                outputDir = self.outputDir
            else:
                outputDir = DEFAULT_SAVE_DIR

            self.outputFormat = self.selectOutputFormat.get()
            self.converter = Converter(self.inputDir, outputDir, self.outputFormat)

            print('[OBJETO CONVERTER CRIADO]')

            numerOfImages = self.converter.getNumberOfImages()

            self.info.configure(text=f'Nº. de imagens: {numerOfImages}')
            self.converterButton.pack(side=RIGHT, padx=10, pady=10, anchor=SE)

            showinfo(title='Informações', message=f'Serão convertidas {numerOfImages} imagens\n\ndo diretório {self.inputDir}\n\npara o formato .{self.outputFormat}')
        else:
            showwarning(title='Diretório inválido', message='Selecione ao menos o diretório das imagens.')

    def goConverter(self):
        self.converter.converter()

    def configureWindow(self):
        self.root.title('Image Converter & Compressor by github.com/brunoferreiracoder')
        self.root.geometry('640x360+640+360')
        self.root.configure(background=COLOR['lightBlack'])
        self.root.resizable(False, False)

        # Para definir o ícone da janela
        # if (isfile('icon.png')):
            # self.root.iconphoto(False, PhotoImage(file='icon.png'))

    def insertElementsInWindow(self):
        comboboxStyle = Style()
        comboboxStyle.theme_create('comboboxstyle', parent='alt',
                                   settings={'TCombobox':
                                             {'configure':
                                              {'selectbackground':  COLOR['darkBlack2'],
                                               'fieldbackground':  COLOR['darkBlack2'],
                                               'background': COLOR['darkBlack2'],
                                               'bordercolor': 'gray'
                                               }}}
                                   )
        comboboxStyle.theme_use('comboboxstyle')

        self.title = Label(self.root, bg=COLOR['darkBlack'], fg=COLOR['white'], font=FONT['title'], text='Image Converter & Compressor by github.com/brunoferreiracoder')

        self.topContainer = Frame(self.root, bg=COLOR['lightBlack'], height=100, width=640)
        self.middleContainer = Frame(self.root, bg=COLOR['lightBlack'], height=100, width=640)
        self.bottomContainer = Frame(self.root, bg=COLOR['lightBlack'], height=100, width=640)

        self.selectInputDirLabel = Label(self.topContainer, text='Diretório das imagens: ', bg=COLOR['darkBlack'], font=FONT['normal'], fg=COLOR['white'], width=30)
        self.selectInputDir = Button(self.topContainer, text='Selecionar...', command=self.setInputDir, bg=COLOR['darkBlack2'], font=FONT['normal'], fg=COLOR['white'], cursor='hand2', relief=RIDGE)

        self.selectOutputFormatLabel = Label(self.middleContainer, text='Converter para: ', bg=COLOR['darkBlack'], font=FONT['normal'], fg=COLOR['white'])
        self.selectOutputFormat = Combobox(self.middleContainer, values=COMPATIBLE_IMG_FORMATS, state='readonly', font=FONT['normal'], foreground=['white'])
        self.selectOutputFormat.current(0)

        self.selectOutputDirLabel = Label(self.middleContainer, text='Diretório\nde saida:\n(opcional)', bg=COLOR['darkBlack'], font=FONT['small'], fg=COLOR['white'])
        self.selectOutputDir = Button(self.middleContainer, text='Selecionar...\n(Padrão:\nDesktop/output)', command=self.setOutPutDir, bg=COLOR['darkBlack2'], font=FONT['small'], fg=COLOR['white'], cursor='hand2', relief=RIDGE)

        self.verifyButton = Button(self.bottomContainer, text='Verificar', command=self.checkInputs, bg=COLOR['lightBlack2'], font=FONT['normal'], fg=COLOR['white'], cursor='hand2', width=10)
        self.converterButton = Button(self.bottomContainer, text='Converter', command=self.goConverter, bg=COLOR['lightBlue'], font=['normal'], fg=COLOR['white'], cursor='hand2', width=10)

        self.info = Label(self.bottomContainer, bg=COLOR['lightBlack2'], font=FONT['normal'], fg=COLOR['white'], cursor='hand2')

        # Packing:
        self.title.pack(side=TOP, fill=BOTH, ipadx=10, ipady=10)

        self.selectInputDirLabel.pack(side=LEFT, padx=10, pady=10, expand=True, fill=BOTH)
        self.selectInputDir.pack(side=LEFT, padx=10, pady=10, expand=True, fill=BOTH)

        self.selectOutputFormatLabel.pack(side=LEFT, padx=10, pady=10, expand=True, fill=BOTH)
        self.selectOutputFormat.pack(side=LEFT, padx=10, pady=10, expand=True, fill=BOTH)
        self.selectOutputDirLabel.pack(side=LEFT, padx=10, pady=10, expand=True, fill=BOTH)
        self.selectOutputDir.pack(side=LEFT, padx=10, pady=10, expand=True, fill=BOTH)

        self.verifyButton.pack(side=RIGHT, padx=10, pady=10, anchor=SE)
        self.info.pack(side=LEFT, padx=10, pady=10, anchor=NW, expand=True, fill=BOTH)

        self.topContainer.pack(side=TOP, expand=True, fill=BOTH)
        self.middleContainer.pack(side=TOP, expand=True, fill=BOTH)
        self.bottomContainer.pack(side=TOP, expand=True, fill=BOTH)

class Converter:
    def __init__(self, inputDir, outputDir, outputFormat):
        self.inputDir = normpath(inputDir)
        self.outputDir = normpath(outputDir) + '\\'
        self.outputFormat = outputFormat

        self.imagesNumber = 0

    def converter(self):
        print('\n[INICIANDO CONVERSÃO]')
        print('[DIRETÓRIO DE ENTRADA]: ' + self.inputDir)
        print('[DIRETÓRIO DE SAÍDA]: ' + self.outputDir, end='\n')

        if (self.outputDir == DEFAULT_SAVE_DIR):
            Path(DEFAULT_SAVE_DIR).mkdir(parents=True, exist_ok=True)
        else:
            Path(self.outputDir).mkdir(parents=True, exist_ok=True)

        for filename in listdir(self.inputDir):
            fileFormat = filename.split('.')[-1].upper()
            if fileFormat in COMPATIBLE_IMG_FORMATS or fileFormat.upper() in COMPATIBLE_IMG_FORMATS_UPPER:
                newImgName = f'{datetime.today()}'.split(' ')
                newImgName = newImgName[0] + '_' + newImgName[1].replace(':', '-').replace('.', '-') + '.' + self.outputFormat

                print (f'[PROCESSANDO] [{datetime.today()}] [DE] {filename} [PARA] {newImgName}')

                savePath = join(self.outputDir, newImgName)
                currentPath = join(self.inputDir, filename)

                image = Image.open(currentPath)

                if self.outputFormat == 'ico':
                    image.save(savePath, optimize=True,quality=QUALITY_LEVEL['ICO'], sizes=[(255, 255)])
                elif self.outputFormat == 'jpg' or self.outputFormat == 'jpeg':
                    convertedImage = image.convert('RGB')
                    convertedImage.save(savePath, optimize=True, quality=QUALITY_LEVEL['JPG'])
                else:
                    image = image.convert("RGBA")
                    if (TRY_TRANSPARENT_BG):
                        pixels = image.getdata()
                        newPixels = []
                        for pixel in pixels:
                            if pixel[0] > 180 and pixel[1] > 180 and pixel[2] > 180:
                                newPixels.append((255, 255, 255, 0))
                            else:
                                newPixels.append(pixel)
                        image.putdata(newPixels)
                    image.save(savePath, optimize=True,quality=QUALITY_LEVEL['PNG'], compress_level=6)
                image.close()

        print('[OPERAÇÃO FINALIZADA]')
        showinfo('Operação finalizada', 'Todas as imagens foram convertidas.\nCheque sua Área de Trabalho.')

    def getNumberOfImages(self):
        for filename in listdir(self.inputDir):
            fileFormat = filename.split('.')[-1]
            if fileFormat in COMPATIBLE_IMG_FORMATS or fileFormat.upper() in COMPATIBLE_IMG_FORMATS_UPPER:
                self.imagesNumber += 1

        print(f'[IMAGENS COMPATÍVEIS ENCONTRADAS]: {self.imagesNumber}')

        return self.imagesNumber


Interface()
