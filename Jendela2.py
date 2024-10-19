import PySimpleGUI as sg
sg.theme("Black2")
sg.theme_text_color("#00FFFF")
window = sg.Window(title="Latihan 2",
layout=[[sg.Text("NPM : 2210010063 ")],
[sg.Text("Nama : M. Sendhy Eko Maulana ")],
[sg.Text("Kelas: 5A Non-Reguler Banjarmasin ")]
],
size=(400,200),
font=("Times", 18))
window()
window.close()