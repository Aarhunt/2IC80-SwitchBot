import streamlit as st
import nest_asyncio
import modules


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide",
)
nest_asyncio.apply()

col1, col2 = st.columns(2);

def hackPanel():
    st.markdown("""
            ## Hack
            By pressing the following buttons, you can hack the selected Switchbot
            """)
    leftB, rightB = st.columns(2);
    with leftB:
        st.button("Open", on_click=modules.hack, args=("Open",))
    with rightB:
        st.button("Close", on_click=modules.hack, args=("Close",))
    st.button("DOS", on_click=modules.hack, args=("DOS",))
    st.button("Remove lighting rules", on_click=modules.hack, args=("Clear",))
    st.button("Move indefinitely", on_click=modules.hack, args=("Infinite",))

def info():
   st.markdown("""
            ## Info
            """)

def scan():
    st.markdown("""
            ## Scan
            """)
    st.button("Scan", on_click=modules.scan())

with col1:
    scan()

with col2:
    hackPanel()
    info()
