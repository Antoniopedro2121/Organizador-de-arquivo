import os
from pathlib import Path
from tkinter import *
from tkinter import filedialog

import magic


def Organizar():
    texto_resposta['text'] = f"Em execução"
    dir = filedialog.askdirectory()
    res = os.listdir(dir)
    total = 0

    for arq in res:
        texto_resposta['text'] = f"Em execução: arquivos organizados Total = {total}"
        tipo = magic.detect_from_filename(f"{dir}/{arq}").name[:14]
        diretorio = f"{dir}/{arq}"

        try:
            Path(f'{dir}/Tipo {tipo}').mkdir(exist_ok=True)
            if not arq == f'Tipo {tipo}':
                os.replace(diretorio, f'{dir}/Tipo {tipo}/{arq}')
                total = total + 1
        except OSError:
            num = 1
            repitido = True
            while(repitido):
                try:
                    repitido = False
                    os.replace(diretorio, f'{dir}/Tipo {tipo}/{arq}{num}')
                    total = total + 1
                except OSError:
                    repitido = True
                    num = num + 1
    
    texto_resposta['text'] = f"Seus arquivos foram organizados total de arquivos {total}"

janela = Tk()
janela.title("Organizador de pastas")
texto = Label(janela, text='Selecione sua pasta para ser organizada')
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Organizar", command=Organizar)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()