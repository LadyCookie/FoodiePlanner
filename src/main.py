import tkinter
import customtkinter
from cookbook import cookbook

#------------------#
# GENERAL SETTINGS #
#------------------#

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

#------#
# ROOT #
#------#

root = customtkinter.CTk()  

# Sizing root window
def resize():
    root.state('zoomed')

root.after(0,resize)

# Flavour
root.title("Foodie Planner")

#---------#
# TOOLBAR #
#---------#

menu_bar = tkinter.Menu(root)
menu_cookbook = cookbook.get_cookbook_window_menu(menu_bar)
menu_bar.add_cascade(label="Recettes", menu = menu_cookbook)

root.config(menu = menu_bar)

#---------#
# TABVIEW #
#---------#

# CONSTS #

tab_1_name = 'Planificateur'
tab_1_color = 'lightskyblue'
tab_1_hover_color = 'lightskyblue1'
tab_1_bg_color = 'azure1'

tab_2_name = 'Livre de recette'
tab_2_color = 'mediumpurple3'
tab_2_hover_color = 'mediumpurple2'
tab_2_bg_color = 'lavender'

tab_3_name = 'Carnet de suivi'
tab_3_color = 'seagreen3'
tab_3_hover_color = 'seagreen2'
tab_3_bg_color = 'honeydew1'

#--------#

tabview = customtkinter.CTkTabview(master = root)
tabview.pack(side='bottom', fill='both', expand=True, padx = 20, pady = 20)

tab_1 = tabview.add(tab_1_name)
tab_2 = tabview.add(tab_2_name)
tab_3 = tabview.add(tab_3_name)

cookbook_widget = cookbook.get_cookbook_widget(tab_2)

def change_tabview_color_scheme(tabview):
    active_tab = tabview.get()
    if(active_tab == tab_1_name):
        tabview.configure(segmented_button_selected_color = tab_1_color)
        tabview.configure(segmented_button_selected_hover_color = tab_1_hover_color)
        tabview.configure(segmented_button_unselected_hover_color = tab_1_hover_color)
        tabview.configure(fg_color = tab_1_bg_color)
    if(active_tab == tab_2_name):
        tabview.configure(segmented_button_selected_color = tab_2_color)
        tabview.configure(segmented_button_selected_hover_color = tab_2_hover_color)
        tabview.configure(segmented_button_unselected_hover_color = tab_2_hover_color)
        tabview.configure(fg_color = tab_2_bg_color)
    if(active_tab == tab_3_name):
        tabview.configure(segmented_button_selected_color = tab_3_color)
        tabview.configure(segmented_button_selected_hover_color = tab_3_hover_color)
        tabview.configure(segmented_button_unselected_hover_color = tab_3_hover_color)
        tabview.configure(fg_color = tab_3_bg_color)
    
tabview.configure(segmented_button_selected_color = tab_1_color)
tabview.configure(segmented_button_selected_hover_color = tab_1_hover_color)
tabview.configure(segmented_button_unselected_hover_color = tab_1_hover_color)
tabview.configure(command = lambda: change_tabview_color_scheme(tabview))
tabview.configure(fg_color = tab_1_bg_color)

#------#
# MAIN #
#------#

root.mainloop()