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
    open, close = st.columns(2);
    with open:
        st.button("Open", on_click=modules.open)
    with close:
        st.button("Close", on_click=modules.close)
    st.button("DOS", on_click=modules.dos)
    st.button("Remove lighting rules", on_click=modules.clear)
    start, stop = st.columns(2);
    with start:
        st.button("Move indefinitely", on_click=modules.infinite())
    with stop:
        st.button("Stop moving", on_click=modules.stopInfinite())
    st.button("Brick", on_click=modules.brick)
    silent, normal = st.columns(2);
    with silent:
        st.button("Silent mode", on_click=modules.silent())
    with normal:
        st.button("Normal mode", on_click=modules.normal())

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
