
import os
import defermi.gui

def run_gui():
    path_gui_main = defermi.gui.__file__.replace('__init__.py', 'main.py')
    os.system(f"streamlit run {path_gui_main}")

def main():
    run_gui()

if __name__ == "__main__":
    main()