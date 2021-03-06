import os
import PySimpleGUI as sg

from ciphers.vigenere import VigenereCipher, FullVigenereCipher, AutoVigenereCipher, ExtendedVigenereCipher
from ciphers.affine import AffineCipher
from ciphers.hill import HillCipher
from ciphers.enigma import EnigmaCipher
from ciphers.playfair import PlayfairCipher


class Config:
    APP_NAME = "Kripto"
    SUCCESS_COLOR = "#90EE90"
    FAIL_COLOR = "#d9534f"


def group(msg: str, n: int = 5) -> str:
    out = [(msg[i:i + n]) for i in range(0, len(msg), n)]
    return " ".join(out)


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
    [sg.T("", key="debug")],
    [sg.TabGroup([[
        sg.Tab("Input", [
            [sg.TabGroup([[
                sg.Tab("From Text", [
                    [sg.Multiline(key="in_text", size=(70, 7))]
                ], key="text"),
                sg.Tab("From File", [
                    [sg.T("Select File", size=(10, 1)), sg.FileBrowse("Choose a file", key="in_file", target=(sg.ThisRow, 2)), sg.T("", size=(40, 2))]
                ], key="file"),
            ]], key="source")],
            [sg.T("Select Cipher", size=(10, 1)), sg.DropDown(list(ciphers.keys()), key="method", default_value=list(ciphers.keys())[-1])],
            [sg.T("Cipher Key", size=(10, 1)), sg.In(key="cipher_key", size=(60, 1))],
            [sg.T("Action", size=(10, 1)), sg.DropDown(["Encrypt", "Decrypt"], key="action", default_value="Encrypt", size=(10, 1))],
            [sg.Button("Run", pad=(5, 10))],
        ], key="input"),
        sg.Tab("Output", [
            [sg.TabGroup([[
                sg.Tab("Without Space", [
                    [sg.Multiline(key="out_preview_no_space", write_only=True, size=(70, 10))]
                ], key="no_space"),
                sg.Tab("Spaced", [
                    [sg.Multiline(key="out_preview_spaced", write_only=True, size=(70, 10))]
                ], key="spaced"),
            ]], key="out_type")],
            [sg.T("Output File", size=(10, 1)), sg.In(key="filename", size=(60, 1))],
            [sg.Button("Export", pad=(5, 10))],
        ], key="output"),
        sg.Tab("About", [
            [sg.T("Pada affine dan hill cipher, pisahkan angka dengan koma, contoh:")],
            [sg.T("Affine: 7,10 -> m: 7, b: 10")],
            [sg.T("Hill: 17, 17, 5, 21, 18, 21, 2, 2, 19 -> terbentuk matriks 3x3, yaitu")],
            [sg.T("| 17  17   5 |")],
            [sg.T("| 21  18  21 |")],
            [sg.T("|  2   2  19 |")],
            [sg.T("Created by:")],
            [sg.T("- Jonathan Yudi Gunawan / 13518084")],
            [sg.T("- Cisco Zulfikar / 13518073")],
        ], key="about"),
    ]], key="current_tab")],
]


def load_file(filepath: str, read_byte: bool):
    # return list of bytes if read_byte True, else return string
    try:
        file_text = []
        mode = "rb" if read_byte else "r"
        with open(filepath, mode) as f:
            for line in f.readlines():
                file_text += line
        if not read_byte:
            file_text = "".join(file_text)
        return [True, file_text]
    except Exception as e:
        return [False, str(e)]


def write_file(filepath: str, content: str, write_byte: bool) -> bool:
    try:
        mode = "wb" if write_byte else "w"
        content = bytes(content) if write_byte else content
        with open(filepath, mode) as f:
            f.write(content)
        return True
    except Exception as e:
        print(e)
        return False


window = sg.Window(Config.APP_NAME, layout)
event, values = window.read()

out_text = ""
while event not in (sg.WIN_CLOSED, "Exit"):
    event = event.lower()
    debug_text, debug_color = "", None
    print(event, values)

    selected_cipher = ciphers[values["method"]]

    if event == "run":
        # Read input
        in_text = values["in_text"]
        action = values["action"].lower()
        if values["source"] == "file":
            success, in_text = load_file(values["in_file"], read_byte=selected_cipher.allow_byte)
            window["filename"].update(os.path.basename(values["in_file"]) + "." + action[:3])
            out_text = ""
            if not success:
                debug_text, debug_color = in_text, Config.FAIL_COLOR

        # Procedd (decrypt / encrypt)
        raw_out_text = getattr(selected_cipher(in_text, values["cipher_key"]), action)()
        out_text = raw_out_text
        if type(raw_out_text) == list:
            try:
                out_text = "".join([chr(x) for x in out_text])
            except Exception:
                out_text = ""
        debug_text, debug_color = f"Succesfully {action}ed!", Config.SUCCESS_COLOR

    elif event == "export":
        filename = "out/" + values["filename"]
        if values["filename"]:
            to_write = out_text if values["out_type"] == "spaced" else group(out_text, 5)
            if not selected_cipher.allow_byte:
                filename += '.txt'
            else:
                to_write = raw_out_text
            success = write_file(filename, to_write, selected_cipher.allow_byte)
            if not success:
                debug_text, debug_color = f"Failed to save as {filename}", Config.FAIL_COLOR
            else:
                debug_text, debug_color = f"Succesfully saved as {filename}", Config.SUCCESS_COLOR
        else:
            debug_text, debug_color = "Output filename cannot be empty", Config.FAIL_COLOR

    # Output
    if event == "run" and debug_color == Config.SUCCESS_COLOR:
        window["out_preview_no_space"].update(out_text)
        window["out_preview_spaced"].update(group(out_text, 5))
        window["output"].select()
    window["debug"].update(debug_text)
    window["debug"].update(background_color=debug_color)

    # Get next value
    event, values = window.read()
window.close()
