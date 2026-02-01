from function import convertor
import FreeSimpleGUI as Fgui
Fgui.theme('black')

textboxf = Fgui.Text("Enter feet:")
inputfeet = Fgui.Input(key="feet")
textboxi = Fgui.Text("Enter inches:")
inputinch = Fgui.Input(key="inch")
convert = Fgui.Button('Convert')
aexit = Fgui.Button('Exit')
answer = Fgui.Text(key="answer")

box = Fgui.Window("Convertor",
                  layout=[[textboxf, inputfeet],
                          [textboxi, inputinch],
                          [convert, aexit, answer]])

while True:
    event, value = box.read()
    results = convertor(value['feet'], value['inch'])

    if event == 'Convert':
        box["answer"].update(value=f'{results}m', text_color="red")
    elif event == 'Exit':
        break
box.close()
