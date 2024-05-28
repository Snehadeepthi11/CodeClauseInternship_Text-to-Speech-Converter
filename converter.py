import os
from gtts import gTTS
import tkinter as tk
from tkinter import ttk, messagebox
from playsound import playsound

def convert_text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Input Error", "Please enter the text to convert.")
        return
    
    language = lang_var.get()
    slow = speed_var.get() == "Slow"
    
    try:
        tts = gTTS(text=text, lang=language, slow=slow)
        filename = "output.mp3"
        tts.save(filename)
        playsound(filename)
        os.remove(filename)  # Remove the file after playing
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Set up the main application window
app = tk.Tk()
app.title("Text to Speech Converter")

# Text entry
text_label = tk.Label(app, text="Enter text:")
text_label.pack()
text_entry = tk.Text(app, height=10, width=25)
text_entry.pack(padx=5,pady=5)

# Language selection
lang_label = tk.Label(app, text="Select language/voice:")
lang_label.pack()
lang_var = tk.StringVar(value='en')
languages = {'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de', 'Italian': 'it'}
lang_menu = ttk.Combobox(app, textvariable=lang_var, values=list(languages.values()))
lang_menu.pack()

# Speech speed selection
speed_label = tk.Label(app, text="Select speech speed:")
speed_label.pack()
speed_var = tk.StringVar(value='Normal')
speed_menu = ttk.Combobox(app, textvariable=speed_var, values=['Normal', 'Slow'])
speed_menu.pack()

# Convert button
convert_button = tk.Button(app, text="Convert to Speech", command=convert_text_to_speech)
convert_button.pack()

# Run the application
app.mainloop()
