import PySimpleGUI as sq
from zip_creator import make_arhive


label1 = sq.Text("Select files to compress:")
input1 = sq.Input()
choose_button1 = sq.FilesBrowse("Choose", key="files")

label2 = sq.Text("Select destination folder:")
input2 = sq.Input()
choose_button2 = sq.FolderBrowse("Choose", key="folder")

compress_button = sq.Button("Compress")
output_label = sq.Text(key="output", text_color="green")


window = sq.Window("FIle Compressor",
                   layout=[
                        [label1, input1, choose_button1],
                        [label2, input2, choose_button2],
                        [compress_button, output_label]
                        ]
                   )
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(";")
    folder = values['folder']
    make_arhive(filepaths, folder)
    window["output"].update(value="Compression Completed!")

window.close()