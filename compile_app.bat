python -m PyInstaller --noconfirm --log-level=WARN ^
    --onefile --noconsole ^
    --name FoodiePlanner ^
    --hidden-import=customtkinter ^
    --icon ./src/common/logo.ico ^
    --add-data ./src/cliqual/data/XML_2020_07_07/*;cliqual/data/XML_2020_07_07/ ^
    --add-data ./src/cookbook/data/img/*;cookbook/data/img/ ^
    --add-data ./src/common/logo.ico;common/ ^
    ./src/main.py 