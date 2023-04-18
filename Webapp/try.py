from tkinter import filedialog
import subprocess
folder_selected = filedialog.askdirectory()
print(folder_selected)
if (folder_selected):
    # subprocess.Popen("cd /Users/niteeshkumarpandey/MFPorjectz/Webapp", shell=True)
    subprocess.Popen(f"streamlit run /Users/niteeshkumarpandey/MFPorjectz/Webapp/app.py -- --folder_selected '{folder_selected}'", shell=True)
    print("Ho")
print("End")