import tkinter as tk
from tkinter import filedialog

# Create the main window
window = tk.Tk()

# Create a menu bar
menu_bar = tk.Menu(window)

# Create a File menu and add it to the menu bar
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create an Open... menu item and add it to the File menu
def open_image():
  # Open a file dialog and get the selected file's path
  file_path = filedialog.askopenfilename()

  # Create a PhotoImage object from the image file
  image = tk.PhotoImage(file=file_path)

  # Create a label widget and set the image as its image
  label = tk.Label(window, image=image)
  label.pack()

file_menu.add_command(label="Open...", command=open_image)

# Add the menu bar to the window
window.config(menu=menu_bar)

# Run the Tkinter event loop
window.mainloop()
