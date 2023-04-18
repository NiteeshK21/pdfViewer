import streamlit as st
import sys
import re
def highlight_text(text, keyword):
    if(st.get_option("theme.base")=='dark'):
        colour="#A020F0"
    else:
        colour="#4DED30"
    highlighted_text = re.sub(f'({keyword})', rf'<span style="background-color: {colour}">\1</span>', text, flags=re.IGNORECASE)
    return highlighted_text
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
arg1 = sys.argv[2]
arg2 = sys.argv[4]
highlighted_text = highlight_text(arg2, arg1)
st.markdown(highlighted_text, unsafe_allow_html=True)