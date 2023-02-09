import os
from pathlib import Path

import streamlit as st
import wx

if 'init' not in st.session_state: st.session_state['init'] = False
if not st.session_state.init:
    st.session_state.init = True
    st.session_state.data_folder = os.getcwd()


def main():
    # Render the readme as markdown using st.markdown.
    readme_text = st.markdown(Path("instructions.md").read_text())

    # Once we have the dependencies, add a selector for the app mode on the sidebar.
    st.sidebar.title("What to do")
    app_mode = st.sidebar.selectbox("Choose the app mode",
                                    ["Run the app", "Show instructions"])
    if app_mode == "Show instructions":
        st.sidebar.success('To continue select "Run the app".')
    elif app_mode == "Run the app":
        readme_text.empty()
        run_the_app()


def get_data_folder_frame():
    app = wx.App()
    clicked = st.button('Where data is located', key="FolderSelectionButton")
    folder_path = st.session_state.data_folder
    if clicked:
        dlg_obj = wx.DirDialog(None, "Choose input directory", "",
                               wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)

        if dlg_obj.ShowModal() == wx.ID_OK:
            folder_path = dlg_obj.GetPath()
            st.session_state.data_folder = folder_path
            st.experimental_rerun()

    return folder_path


def run_the_app():
    st.text('Test directory chooser dialog')
    st.text('Data folder: ' + st.session_state.data_folder)
    get_data_folder_frame()



if __name__ == "__main__":
    main()
