python -m PyInstaller --noconfirm --log-level=WARN ^
    --onefile --noconsole ^
    --name FoodiePlanner ^
    --hidden-import=customtkinter ^
    ./src/foodie_planner/main.py