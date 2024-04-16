import tkinter
import customtkinter
from PIL import Image

import os

DATA_PATH = os.path.dirname(__file__) + "/data/{path}"

#-----------#
# UTILITIES #
#-----------#

def load_recipe():
    print('loading recipe')

def save_recipe():
    print('saving recipe')

def generate_cooking_help():
    print('generating cooking help')

#-----#
# HUD #
#-----#

def get_cookbook_widget(root):
    frame = customtkinter.CTkFrame(root)
    frame.configure(fg_color = 'lavender')
    frame.pack(fill = "both", expand = True, padx = 10, pady = 10)

    cookbook_cover = customtkinter.CTkFrame(frame)
    cookbook_cover.configure(fg_color = 'plum4')
    cookbook_cover.pack(fill = "both", expand = True, padx = 10, pady = 10)

    cookbook_left_page = customtkinter.CTkFrame(cookbook_cover)
    cookbook_left_page.configure(fg_color = 'blanchedalmond')
    cookbook_left_page.pack(fill= "both", side = "left", expand = True, padx = (10,0), pady = 10)

    cookbook_title = customtkinter.CTkLabel(cookbook_left_page, text="Title", font = ("",50), fg_color="transparent")
    cookbook_title.pack(side = "top", pady = 20)

    cookbook_right_page = customtkinter.CTkFrame(cookbook_cover)
    cookbook_right_page.configure(fg_color = 'blanchedalmond')
    cookbook_right_page.pack(fill= "both", side = "right", expand = True, padx = (0,10), pady = 10)

    return frame

def get_cookbook_window_menu(root):
    menu_file = tkinter.Menu(root, tearoff = 0)
    menu_file.add_command(label = "Charger recette", command = load_recipe, font = ("", 12))
    menu_file.add_command(label = "Sauvegarder recette", command = save_recipe, font = ("", 12))
    menu_file.add_command(label = "Générer aide de cuisine", command = generate_cooking_help, font = ("", 12))
    return menu_file