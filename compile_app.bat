python -m PyInstaller --noconfirm --log-level=WARN ^
    --onefile --noconsole ^
    --hidden-import=customtkinter ^
    ../src/foodie_planner/main.py