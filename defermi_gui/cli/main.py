
import os
import defermi_gui

def run_gui():
    path_gui_main = defermi_gui.__file__.replace('__init__.py', 'main.py')
    os.system(f"streamlit run {path_gui_main}")

def main():
    run_gui()

if __name__ == "__main__":
    main()