import PySimpleGUI as sg
sg.theme("Black2")
sg.theme_text_color("#00FFFF")
window = sg.Window(title="Profile",
layout=[[sg.Text("SELAMAT DATANG DI KELAS",
font=("Arial",25))],
[sg.Text("NPM : 22100100063 ")],
[sg.Text("Nama : M.Sendhy Eko Maulana ")],
[sg.Text("Kelas: 5A Non - Regular Banjarmasin ")]
],
size=(500,200),
font=("Times", 18))
window()
window.close()