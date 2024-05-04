import streamlit as st
import os
import pdfReader


def upload_file(file):
    try:
        file_path = os.path.join("D:\AI_ML\pdfReader\Document", file.name)
        with open(file_path, "wb") as f:
            f.write(file.read())
        return file_path
    except Exception as e:
        print("An error occurred:", e)
        return "Error: " + str(e)


def main():
    st.title("PDF Query")

    uploaded_file = st.file_uploader("Upload a file")

    if uploaded_file is not None:
        document_search, chain = pdfReader.readPdf(upload_file(uploaded_file))
        st.write(f"File '{uploaded_file.name}' uploaded successfully...")

        query = st.text_input('Enter query related to the uploaded file')

        if st.button("Search"):
            st.write(pdfReader.queryPdf(document_search, chain, query))


if __name__ == "__main__":
    main()
