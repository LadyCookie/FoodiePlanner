import customtkinter

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
# TABVIEW #
#---------#

tabview = customtkinter.CTkTabview(master = root)
tabview.pack(side='bottom', fill='both', expand=True, padx = 20, pady = 20)

tab_1 = tabview.add('Planificateur')
tab_2 = tabview.add('Livre de recette')
tab_3 = tabview.add('Carnet de suivi')

#------#
# MAIN #
#------#

root.mainloop()