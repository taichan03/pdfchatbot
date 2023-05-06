from dotenv import load_dotenv
import os
import streamlit as st

def main():
    load_dotenv()
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF")

    pdf = st.file_uploader("Upload your PDF")

if __name__== '__main__':
    main()