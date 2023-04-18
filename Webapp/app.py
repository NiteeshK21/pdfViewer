import streamlit as st
from pathlib import Path
from tika import parser
import subprocess
import time
def searchText(folder,search_text):
    files=list(folder.glob("*Index.txt"))
    found=0
    for file in files:
        parsed = parser.from_file(str(file))
        text=parsed["content"]
        if (text.find(search_text)>=0):
            subprocess.Popen(f"streamlit run /Users/niteeshkumarpandey/MFPorjectz/Webapp/app2.py -- --search_text '{search_text}' --text '{text}'", shell=True)
            found=1
    if(found==0):
        warn_message=st.empty()
        warn_message.warning("Not Found")
        time.sleep(1)
        warn_message.empty()
def main():
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    folder_selected = st.sidebar.text_input("Enter folder path")
    if(folder_selected):
        text=""
        server_folder = Path(folder_selected)
        folder=Path(server_folder)
        files=list(folder.glob("*.pdf"))
        files+=list(folder.glob("*.docx"))
        text = st.text_input('Enter text to search: ',value="")
        st.header("Files in server: ")
        for item in files:
            parsed = parser.from_file(str(item))
            with open(f'{server_folder}/{Path(item).stem}Index.txt', 'w') as f:
                try:
                    f.write(parsed["content"])
                except:
                    f.write("None")
            st.write(Path(item).stem)
        if(text):
            searchText(folder,text)
main()
