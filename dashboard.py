import streamlit as st
import nest_asyncio
import modules


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide",
)
nest_asyncio.apply()

col1, col2 = st.columns([2, 2])


def hackPanel():
    st.markdown("""
            ## Hack
            By pressing the following buttons, you can hack the selected Switchbot
            """)
    opening, moving, others = st.columns([1, 1, 1], gap="small", border=True)
    with opening:
        st.markdown("""
                   ##### Opening & Closing
                   """)
        st.button("Open too far", on_click=modules.openTooFar)
        st.button("Open", on_click=modules.open)
        st.button("Close", on_click=modules.close)
    with moving:
        st.markdown("""
                       ##### Moving indefinitely
                       """)
        st.button("Move indefinitely", on_click=modules.infinite)
        st.button("Stop moving", on_click=modules.stopInfinite)
    with others:
        st.markdown("""
                       ##### Others
                       """)
        st.button("DOS", on_click=modules.dos)
        st.button("Brick", on_click=modules.brick)
        st.button("Remove lighting rules", on_click=modules.clear)
        st.button("Silent mode", on_click=modules.silent)
        st.button("Normal mode", on_click=modules.normal)


def info():
    st.markdown("""
            ## Info
            """)
    modules.info()


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
