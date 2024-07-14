from cookbook import cookbook_api

import tkinter
import tkinter.filedialog as tkFileDialog
import customtkinter
from PIL import Image

import os

DATA_PATH = os.path.dirname(__file__) + "/data/{path}"

#------------------#
# GLOBAL VARIABLES #
#------------------#

cookbook_widget = None
title_widget = None
portion_widget = None
cooking_time_widget = None
ingredients_widget = None
steps_widget = None

#-----------#
# UTILITIES #
#-----------#

def load_recipe():
    recipe_path = DATA_PATH.format(path = "recipes/")
    recipe_file = tkFileDialog.askopenfilename(initialdir = recipe_path, title = "Sélectionner une recette", filetypes = (("file_type","*.xml"),("all files","*.*")))
    if(recipe_file != ""):
        print('loading recipe : ' + recipe_file)
        recipe = cookbook_api.Recipe(recipe_file)
        update_recipe(recipe)
    else:
        print("Pas de recette sélectionnée.")

def save_recipe():
    print('saving recipe')

def generate_cooking_help():
    print('generating cooking help')

#-----#
# HUD #
#-----#
def button_event():
    print("button pressed")

def create_ingredients_widget(root):
    ingredients_title_frame = customtkinter.CTkFrame(master = root, fg_color = "transparent")
    ingredients_title_frame.pack(side = "top", fill = "x", padx = 50, pady = 20)

    ingredients_title = customtkinter.CTkLabel(master = ingredients_title_frame, text = "Ingrédients", font = ("",24) , fg_color="transparent")
    ingredients_title.pack(side = "left")

    ingredients_frame = customtkinter.CTkFrame(root, fg_color="transparent")
    ingredients_frame.pack(side = "left", fill = "y", padx = (50,20), pady = 5)


    for ingredient in ("ail","pates","amour","supercalifragilispicexpialidocious"):
        ingredient_frame = customtkinter.CTkFrame(ingredients_frame, fg_color="transparent")
        ingredient_frame.pack(side = "top", fill = "x")
        ingredient_label = customtkinter.CTkLabel(master = ingredient_frame, text = ingredient, justify = "left", fg_color="transparent", font = ("",18))
        ingredient_label.pack(side = "left")
    return ingredients_frame
       

def get_cookbook_widget(root):
    frame = customtkinter.CTkFrame(root)
    frame.configure(fg_color = 'lavender')
    frame.pack(fill = "both", expand = True, padx = 10, pady = 10)
    global cookbook_widget 
    cookbook_widget = frame

    cookbook_cover = customtkinter.CTkFrame(frame)
    cookbook_cover.configure(fg_color = 'plum4')
    cookbook_cover.pack(fill = "both", expand = True, padx = 10, pady = 10)

    cookbook_pages = customtkinter.CTkFrame(cookbook_cover)    
    cookbook_pages.pack(fill="both", expand= True, padx = 10, pady = 10)

    cookbook_left_page = customtkinter.CTkFrame(cookbook_pages)
    cookbook_left_page.configure(fg_color = 'blanchedalmond')
    cookbook_left_page.grid(row=0,column=0, sticky="nsew", columnspan=1 , rowspan=1)

    recipe_title = customtkinter.CTkLabel(cookbook_left_page, text="Title", font = ("",50), fg_color="transparent")
    recipe_title.pack(side = "top", pady = 20)
    global title_widget
    title_widget = recipe_title

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
    global portion_widget
    portion_widget = portion_text

    time_logo = customtkinter.CTkImage(light_image=Image.open(DATA_PATH.format(path = 'img/hourglass.png')),
                                  dark_image=Image.open(DATA_PATH.format(path = 'img/hourglass.png')),
                                  size=(25, 25))
    
    time_frame = customtkinter.CTkLabel(master = recipe_info, image = time_logo, fg_color="transparent", text = '')
    time_frame.pack(side = "left", padx = (50,0))
    time_text = customtkinter.CTkLabel(master = recipe_info, text="30 min", fg_color="transparent", font = ("",30))
    time_text.pack(side = "left", padx = (20,0))
    global cooking_time_widget
    cooking_time_widget = time_text

    global ingredients_widget
    ingredients_widget = create_ingredients_widget(cookbook_left_page)

    cookbook_right_page = customtkinter.CTkFrame(cookbook_pages)
    cookbook_right_page.configure(fg_color = 'blanchedalmond')
    cookbook_right_page.grid(row=0,column=1, sticky="nsew", columnspan=1 , rowspan=1)

    cookbook_pages.grid_columnconfigure(0, weight=1, uniform="group1")
    cookbook_pages.grid_columnconfigure(1, weight=1, uniform="group1")
    cookbook_pages.grid_rowconfigure(0, weight=1)

    return frame


def update_title(title):
    global title_widget
    title_widget.configure(text = title)

def update_portion(time):
    global portion_widget
    portion_widget.configure(text = time)

def update_cooking_time(time):
    global cooking_time_widget
    cooking_time_widget.configure(text = time)

def update_ingredients(ingredients):
    print("Change ingredient list")

def update_steps(steps):
    print("Change steps list")

def update_recipe(recipe):
    global cookbook_widget
    update_title(recipe._NAME)
    update_portion(recipe._PORTION)
    update_cooking_time(recipe._COOKING_TIME)
    update_ingredients(recipe._COMPOSITION)
    update_steps(recipe._RECIPE)

def get_cookbook_window_menu(root):
    menu_file = tkinter.Menu(root, tearoff = 0)
    menu_file.add_command(label = "Charger recette", command = load_recipe, font = ("", 12))
    menu_file.add_command(label = "Sauvegarder recette", command = save_recipe, font = ("", 12))
    menu_file.add_command(label = "Générer aide de cuisine", command = generate_cooking_help, font = ("", 12))
    return menu_file