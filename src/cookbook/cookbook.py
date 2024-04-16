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

    recipe_title = customtkinter.CTkLabel(cookbook_left_page, text="Title", font = ("",50), fg_color="transparent")
    recipe_title.pack(side = "top", pady = 20)

    recipe_info = customtkinter.CTkFrame(cookbook_left_page)
    recipe_info.configure(fg_color = "transparent")
    recipe_info.pack(side = "top", fill = "x", padx = (50,0) , pady = 10)

    portion_logo = customtkinter.CTkImage(light_image=Image.open(DATA_PATH.format(path = 'img/bowl.png')),
                                  dark_image=Image.open(DATA_PATH.format(path = 'img/bowl.png')),
                                  size=(20, 20))
    portion_frame = customtkinter.CTkLabel(master = recipe_info, image=portion_logo, fg_color="transparent", text = '')
    portion_frame.pack(side = "left", padx = (20,0))

    portion_text = customtkinter.CTkLabel(master = recipe_info, text="4", fg_color="transparent", font = ("",30))
    portion_text.pack(side = "left", padx = 10)
    portion_text.pack(side = "left", padx = (20,0))

    time_logo = customtkinter.CTkImage(light_image=Image.open(DATA_PATH.format(path = 'img/hourglass.png')),
                                  dark_image=Image.open(DATA_PATH.format(path = 'img/hourglass.png')),
                                  size=(25, 25))
    time_frame = customtkinter.CTkLabel(master = recipe_info, image = time_logo, fg_color="transparent", text = '')
    time_frame.pack(side = "left", padx = (50,0))

    time_text = customtkinter.CTkLabel(master = recipe_info, text="30 min", fg_color="transparent", font = ("",30))
    time_text.pack(side = "left", padx = 10)
    time_text.pack(side = "left", padx = (20,0))

    #entry = customtkinter.CTkEntry(recipe_info, placeholder_text="4")
    #entry.pack(side = "left", padx = (20,0))

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