import PySimpleGUI as sg
from zip_creator  import make_archive

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_btn1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_btn2 = sg.FolderBrowse("Choose", key="folder")

compress_btn = sg.Button("Compress")
window = sg.Window("File Compressor", layout=[[label1, input1, choose_btn1],
                                              [label2, input2, choose_btn2],
                                              [compress_btn]])
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed!")

window.close()