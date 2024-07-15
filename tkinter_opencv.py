import cv2

import os
from os import walk

import tkinter as tk       
from tkinter import *
from tkinter import filedialog, font, ttk
from tkinter.ttk import Notebook, Style

from PIL import Image, ImageTk


def select_folder():
    global fol_dir
    fol_dir = filedialog.askdirectory()
    update_listbox(fol_dir)


def update_listbox(fol_dir):
    filenames = os.listdir(fol_dir)
    extensions = [".bmp", ".jpg", ".jpeg", ".png"]
    filenames = [fi for fi in filenames if fi.endswith(tuple(extensions))]
    list_box.delete(0, tk.END)
    for item in filenames:
        list_box.insert(tk.END, item)


def show_image():
    if list_box.curselection() == ():
        return
    elif list_box.curselection() != ():
        img_name = list_box.get(list_box.curselection())
        
    img_name = os.path.join(fol_dir, img_name)
    
    # Read image with PIL library
    img = Image.open(img_name)
    
    # Resize image to fit with Tk Label widget
    height, width = img.size
    ratio = width / height
    
    if ratio >= 1:
        new_height = 215
        new_width = int(ratio * new_height)
    else:
        new_width = 215
        new_height = int(ratio * new_width)
        
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    img_label.configure(image = img)
    img_label.image = img


def show_result():
    if list_box.curselection() == ():
        return
    elif list_box.curselection() != ():
        img_name = list_box.get(list_box.curselection())
        
    img_name = os.path.join(fol_dir, img_name)
    rgb_image = cv2.imread(img_name)

    # [IMAGE PROCESSING] Perform RGB to Grayscale conversion
    gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY) 

    # We cannot directly display image from OpenCV to Tk Label
    # --> However, we can convert OpenCV image to PIL image for displaying
    img = Image.fromarray(gray_image)

    # Resize image to fit with Tk Label widget
    height, width = img.size
    ratio = width / height
    
    if ratio >= 1:
        new_height = 215
        new_width = int(ratio * new_height)
    else:
        new_width = 215
        new_height = int(ratio * new_width)
        
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    img_label_2.configure(image = img)
    img_label_2.image = img


if __name__ == "__main__":
    root = tk.Tk()
    # root.iconbitmap('icon.ico')
    root.title(' Simple Image Processing application - RGB2GRAY ')
    root.geometry("800x600")

    # Configure columns and rows to expand and fill the available space
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    
    file_label_frame = tk.LabelFrame(root, 
                                     text=' List of images ',
                                     font='Helvetica 9 bold',
                                     labelanchor='nw', 
                                     padx=5, pady=5)
    file_label_frame.grid(row=0, column=0, rowspan=1, padx=5, pady=5)
    
    file_frame_buttons = tk.Frame(root)
    file_frame_buttons.grid(row=1, column=0, rowspan=1, padx=5, pady=5)

    # [FILE] listbox
    CWD = os.getcwd()
    
    global fol_dir
    fol_dir = CWD

    extensions = [".bmp", ".jpg", ".jpeg", ".png"]

    filenames = next(walk(CWD), (None, None, []))[2] 
    filenames = [fi for fi in filenames if fi.endswith(tuple(extensions))]

    file_list = tk.StringVar()
    file_list.set(tuple(filenames))
    list_box = tk.Listbox(file_label_frame, listvariable=file_list, width=40)
    list_box.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    choose_file_button = tk.Button(file_frame_buttons, text='Browse', command=lambda:[select_folder()])
    choose_file_button.grid(row=0, column=0, padx=5, pady=10)
    view_file_button = tk.Button(file_frame_buttons, text='Display', command=lambda:[show_image(), show_result()])
    view_file_button.grid(row=0, column=1, padx=5, pady=10)

    # [IMAGE] Display Input
    image_frame = tk.Frame(root)
    image_frame.grid(row=0, column=1, rowspan=2, padx=5, pady=5)
    image_label_frame = tk.LabelFrame(image_frame, 
                                     text=' Display image ',
                                     font='Helvetica 9 bold',
                                     labelanchor='nw', 
                                     padx=5, pady=5)
    image_label_frame.grid(row=0, column=0)
    image_label_frame.grid_columnconfigure(1, weight=1, minsize=220)
    image_label_frame.grid_rowconfigure(1, weight=1, minsize=220)
    
    img_label = tk.Label(image_label_frame)
    img_label.grid(row=0, column=1, rowspan=2, sticky="nsew")

    # [IMAGE] Display Output
    image_frame_2 = tk.Frame(root)
    image_frame_2.grid(row=0, column=3, rowspan=2, sticky="nsew", padx=5, pady=5)
    image_label_frame_2 = tk.LabelFrame(image_frame_2, 
                                     text=' Display output ',
                                     font='Helvetica 9 bold',
                                     labelanchor='nw', 
                                     padx=5, pady=5)
    image_label_frame_2.grid(row=0, column=0)
    image_label_frame_2.grid_columnconfigure(1, minsize=220)
    image_label_frame_2.grid_rowconfigure(1, minsize=220)
    
    img_label_2 = tk.Label(image_label_frame_2)
    img_label_2.grid(row=0, column=1, rowspan=2, sticky="nsew")

    root.mainloop()