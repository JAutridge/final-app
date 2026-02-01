from function2 import convertor2
import FreeSimpleGUI as WindowConvertor

qbox = WindowConvertor.Text("Enter ounces:")
ounces = WindowConvertor.Input(key="ounces")
convert = WindowConvertor.Button("Convert")
answer = WindowConvertor.Text(key="answer")

box = WindowConvertor.Window("Convertor",
                             layout=[[qbox, ounces],
                                     [convert, answer]])

while True:
    text, values = box.read()
    result = convertor2(values['ounces'])
#   print(values)
#   print(result)
    box['answer'].update(value=f'{result}mm', text_color='red')
box.close()
