# conversor-de-imagem-python
O código gera uma interface amigável ao usuário que possibilita a compressão e conversão de imagens dos formatos PNG e JPG. As principais bibliotecas utilizadas foram a Pillow, para o tratamento de imagem, e Tkinter, para construção da interface. A versão do Python utilizada no desenvolvimento foi a 3.9.4.

<img src="preview.jpg" width=390px>

## Organização do programa
### Classe Interface

O programa possui uma classe chamada Interface que possui os seguintes métodos:
1. __init__: chamada os outros métodos da classe numa ordem lógica para o funcionamento do programa.
2. __configureWindow__: responsável por definir as características da janela do programa, tais como largura e altura.
3. __configureTemplate__: faz a configuração da interface em si, exibindo os botões e labels.
4. __configureModeFrames__: encarregado de configurar os Frames que contém os widgets necessários para a compressão e a conversão de imagens.
5. __changeMode__: está ligado a um botão e alterna entre os Frames (que contém os widgets necessários para compressão e conversão de imagens) que serão exibidos na janela.
6. __start__: responsável por identificar se o usuário escolheu o modo de conversão ou compressão de imagens e chamar as respectivas funções.
7. __setInputPath__: abre uma janela para seleção do diretório das imagens.
8. __setOutputpath__: abre uma janela para seleção do diretório de saída das imagens processadas.

### Funções externas da classe
__getFileFormat:__ helper que retorna a extensão da imagem identificada no parâmetro passado.<br>
__compress:__ responsável por fazer a compressão das imagens de fato.<br>
__convert:__ encarregado de fazer a conversão das imagens para outro formato.
