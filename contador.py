import PySimpleGUI as sg
import pdfplumber


contadortotal = 0
nrpag = 1
pdf = pdfplumber.open(r"C:\Users\dan\Desktop\genetica.pdf")
print(f'O documento contém {len(pdf.pages)} páginas no total.')
for pagina in pdf.pages:
    contadorpag = 0
    texto = pagina.extract_text()
    for letra in texto:
        if letra != ' ':
            contadorpag += 1
    contadortotal += contadorpag
    print(f'A pagina {nrpag} contém {contadorpag} caracteres.')
    nrpag += 1
print(f'No total, o texto tem {contadortotal} caracteres')

# layout = [
#     [sg.T('',size=10),sg.T('Contador de palavras',font='Arial 15'), sg.T('',size=10)],
#     [sg.T('',size=10),sg.T('Selecionar arquivos',font='Arial 12'), sg.FilesBrowse('Abrir')],
#     [sg.Button('Contar'),sg.Text('Resultado: ',font='Arial 10'),sg.T(f'{nr} palavras.',font='Arial 10')]
# ]
#
# window = sg.Window('contador',layout=layout)
#
# while True:
#     event, value = window.read()
#     if event == sg.WIN_CLOSED:
#         break
#
# window.close()