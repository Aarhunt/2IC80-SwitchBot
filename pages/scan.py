import streamlit as st
from bleak import BleakClient
from bleak import BleakScanner
import pandas as pd

st.markdown("""
            ## Scan
            On this page there will be a list of scanned bluetooth devices. It will suggest a WoCurtain device if it has one. If not, you can pick one yourself if you know its the WoCurtain device. It will then save the address so we can use it somewhere. 
            """)

async def discoverDevices():
    devices = await BleakScanner.discover()

    return pd.dataframe(data = {
        'address': [d.address for d in devices ],
        'name': [d.name for d in devices ],
        'details': [d.details for d in devices ],
                                }) 


st.dataframe(await discoverDevices())
