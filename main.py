import PySimpleGUI as sg

from ciphers.vigenere import VigenereCipher, FullVigenereCipher, AutoVigenereCipher, ExtendedVigenereCipher
from ciphers.affine import AffineCipher
from ciphers.hill import HillCipher
from ciphers.enigma import EnigmaCipher
from ciphers.playfair import PlayfairCipher


class Config:
    APP_NAME = "Kripto"


def group(msg: str, n: int = 5) -> str:
    # TODO
    return msg


ciphers = {
    "Vigenere Cipher": VigenereCipher,
    "Full Vigenere Cipher": FullVigenereCipher,
    "Auto Vigenere Cipher": AutoVigenereCipher,
    "Extended Vigenere Cipher": ExtendedVigenereCipher,
    "Affine Cipher": AffineCipher,
    "Hill Cipher": HillCipher,
    "Enigma Cipher": EnigmaCipher,
    "Playfair Cipher": PlayfairCipher,
}

sg.theme("Reddit")
layout = [
    [sg.T("Tucil 1 Kriptografi", font="Any 20")],
    [sg.TabGroup([[
        sg.Tab("Input", [
            [sg.TabGroup([[
                sg.Tab("From Text", [
                    [sg.Multiline(key="in_text", size=(70, 7))]
                ]),
                sg.Tab("From File", [
                    [sg.T("Select File", size=(10, 1)), sg.FileBrowse("Choose a file", key="in_file", target=(sg.ThisRow, 2)), sg.T("", size=(40, 2))]
                ]),
            ]])],
            [sg.T("Select Cipher", size=(10, 1)), sg.DropDown(list(ciphers.keys()), key="method", default_value=list(ciphers.keys())[0])],
            [sg.T("Cipher Key", size=(10, 1)), sg.In(key="cipher_key", size=(60, 1))],
            [sg.T("Action", size=(10, 1)), sg.DropDown(["Encrypt", "Decrypt"], key="action", default_value="Encrypt", size=(10, 1))],
            [sg.Button("Run", pad=(5, 10))],
        ]),
        sg.Tab("Output", [
            [sg.TabGroup([[
                sg.Tab("Without Space", [
                    [sg.Multiline(key="out_preview_no_space", write_only=True, size=(70, 10))]
                ]),
                sg.Tab("Spaced", [
                    [sg.Multiline(key="out_preview_spaced", write_only=True, size=(70, 10))]
                ]),
            ]])],
            [sg.T("Output File", size=(10, 1)), sg.In(key="out_filename", size=(60, 1))],
            [sg.Button("Export", pad=(5, 10))],
        ]),
        sg.Tab("About", [
            [sg.T("Created by:")],
            [sg.T("- Jonathan Yudi Gunawan / 13518084")],
            [sg.T("- Cisco Zulfikar / 13518073")],
        ]),
    ]])],
]

window = sg.Window(Config.APP_NAME, layout)
event, values = window.read()

is_ran = False
is_exported = False
while event not in (sg.WIN_CLOSED, "Exit"):
    event = event.lower()
    print(event, values)
    in_text = values["in_text"]

    from_file = False
    # TODO load in_file to replace in_text kalau method = extended vigenere, set from_file True
    selected_cipher = ciphers[values["method"]]
    if event == "run":
        out_text = getattr(selected_cipher, values["action"].lower())(in_text)
        if not from_file:
            window["out_preview_no_space"].update(out_text)
            window["out_preview_spaced"].update(group(out_text, 5))
        window["Output"].select()
    elif event == "export":
        if not is_ran and not is_exported:
            # TODO write to file
            is_exported = True
    event, values = window.read()
window.close()
