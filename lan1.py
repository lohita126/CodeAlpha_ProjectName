import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def translate_text():
    src = src_lang_combo.get()
    dest = dest_lang_combo.get()
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input needed", "Please enter text to translate.")
        return
    try:
        translator = Translator()
        # googletrans expects language codes like 'en', 'fr', etc.
        src_code = lang_code_map.get(src)
        dest_code = lang_code_map.get(dest)
        # If user chooses "Auto", set src='auto'
        if src == "Auto":
            src_code = "auto"
        translated = translator.translate(text, src=src_code, dest=dest_code)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed:\n{e}")

# Map display names to language codes
lang_code_map = {name.capitalize(): code for code, name in LANGUAGES.items()}
# Add an “Auto” option
lang_code_map["Auto"] = "auto"

root = tk.Tk()
root.title("Language Translator")

# Layout
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Source language combo
ttk.Label(frame, text="Source language:").grid(row=0, column=0, sticky=tk.W)
src_lang_combo = ttk.Combobox(frame, values=sorted(lang_code_map.keys()), state="readonly")
src_lang_combo.set("Auto")
src_lang_combo.grid(row=0, column=1, sticky=(tk.W, tk.E))

# Target language combo
ttk.Label(frame, text="Target language:").grid(row=1, column=0, sticky=tk.W)
dest_lang_combo = ttk.Combobox(frame, values=sorted(lang_code_map.keys()), state="readonly")
dest_lang_combo.set("English")
dest_lang_combo.grid(row=1, column=1, sticky=(tk.W, tk.E))

# Input text
ttk.Label(frame, text="Input text:").grid(row=2, column=0, sticky=tk.NW)
input_text = tk.Text(frame, height=10, width=50)
input_text.grid(row=2, column=1, sticky=(tk.W, tk.E))

# Translate button
translate_button = ttk.Button(frame, text="Translate", command=translate_text)
translate_button.grid(row=3, column=1, sticky=tk.E, pady=10)

# Output text
ttk.Label(frame, text="Translated text:").grid(row=4, column=0, sticky=tk.NW)
output_text = tk.Text(frame, height=10, width=50)
output_text.grid(row=4, column=1, sticky=(tk.W, tk.E))

# Configure resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

root.mainloop()
