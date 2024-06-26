import tkinter as tk
import tkinter.colorchooser as cc
from tkinter import filedialog
from PIL import Image

# Erstellt eine leere 16x16-Matrix
matrix = [[(0, 0, 0) for _ in range(16)] for _ in range(16)]

# Funktion, die aufgerufen wird, wenn eine Farbe ausgewählt wird
# Speichert die letzte ausgewählte Farbe
last_color = (0, 0, 0)

# Funktion, die aufgerufen wird, wenn eine Farbe ausgewählt wird
def set_color(row, col):
    global last_color  # Zugriff auf die globale Variable last_color
    color = cc.askcolor(initialcolor=last_color)[0]  # Verwendet die letzte ausgewählte Farbe als Voreinstellung
    matrix[row][col] = tuple(int(c) for c in color)
    last_color = tuple(int(c) for c in color)  # Speichert die ausgewählte Farbe als die letzte ausgewählte Farbe
    update_canvas()
    update_matrix()

# Funktion, die das 16x16-Gitter mit den Farben in der Matrix füllt
def update_canvas():
    for row in range(16):
        for col in range(16):
            canvas.itemconfig(f"rect_{row}_{col}", fill=f"#{matrix[row][col][0]:02x}{matrix[row][col][1]:02x}{matrix[row][col][2]:02x}")

# Funktion, die die Matrix in den API-Befehl konvertiert und ausgibt
def update_matrix():
    api_command = ""
    current_color = matrix[0][0]
    current_range = [0, 0]
    
    def rgb_to_hex(color):
        return f"{color[0]:02x}{color[1]:02x}{color[2]:02x}"
    
    for row in range(16):
        for col in range(16):
            if matrix[row][col] != current_color:
                if current_range[0] == current_range[1]:
                    api_command += f"{row*16+col-1},\"{rgb_to_hex(current_color)}\","
                else:
                    api_command += f"{row*16+current_range[0]},{row*16+current_range[1]},\"{rgb_to_hex(current_color)}\","
                current_range = [col, col]
                current_color = matrix[row][col]
        # Fügt den aktuellen Farbbereich am Ende der Zeile hinzu
        if current_range[0] == current_range[1]:
            api_command += f"{row*16+col},\"{rgb_to_hex(current_color)}\","
        else:
            api_command += f"{row*16+current_range[0]},{row*16+current_range[1]},\"{rgb_to_hex(current_color)}\","
        current_range = [0, 0]  # Setzt den aktuellen Farbbereich für die nächste Zeile zurück

    # Gibt den vollständigen API-Befehl aus
    print('{"on":true,"bri":100,"seg":{"i":[' + api_command[:-1] + ']}}')
    api_command = api_command[:-1]
    api_command_text.delete('1.0', 'end')
    api_command_text.insert('1.0', api_command)


def copy_api_command():
    api_command = '{"on":true,"bri":100,"seg":{"i":[' + api_command_text.get('1.0', 'end-1c') + ']}}'
    root.clipboard_clear()
    root.clipboard_append(api_command)
    print("API command copied to clipboard.")

# Erstellt das Farbrad und das 16x16-Gitter
def choose_image():

    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img = img.resize((16, 16))
    pixels = img.load()

    for row in range(16):
        for col in range(16):
            matrix[row][col] = tuple(pixels[col, row])
    update_canvas()
    update_matrix()


root = tk.Tk()
root.title("Pixelart creator")

choose_image_button = tk.Button(root, text="Choose Image", command=choose_image)
choose_image_button.pack(side=tk.LEFT)
copy_button = tk.Button(root, text="Copy API command", command=copy_api_command)
copy_button.pack()

canvas = tk.Canvas(root, width=260, height=260)
canvas.pack(side=tk.LEFT)
api_command_text = tk.Text(root, height=1)
api_command_text.pack()

for row in range(16):
    for col in range(16):
        canvas.create_rectangle(col*16, row*16, col*16+16, row*16+16, fill="#000000", outline="#555", tags=f"rect_{row}_{col}")
        canvas.tag_bind(f"rect_{row}_{col}", "<Button-1>", lambda e, r=row, c=col: set_color(r, c))

root.mainloop()
