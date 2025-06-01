import streamlit as st
import nest_asyncio
import modules

nest_asyncio.apply()

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide",
)
st.markdown("""
            ## Home
            Homepage!
            """)

col1, col2 = st.columns(2);

def hack():
    st.markdown("""
            ## Hack
            By pressing the following buttons, you can hack the selected Switchbot
            """)
    leftB, rightB = st.columns(2);
    with leftB:
        st.button("Open")
    with rightB:
        st.button("Close")
    st.button("DOS")
    st.button("Remove lighting rules")
    st.button("Move indefinitely")

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
    hack()
    info()
