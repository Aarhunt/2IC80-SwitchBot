import streamlit as st
from bleak import BleakClient
from bleak import BleakScanner
from bleak.backends.device import BLEDevice
import pandas as pd
import asyncio
import numpy as np

DEVICE_NAME_UUID = "00002a00-0000-1000-8000-00805f9b34fb"

async def read_name(address):
    async with BleakClient(address) as client:
        name = await client.read_gatt_char(DEVICE_NAME_UUID)

    return name.decode('utf-8').rstrip('\x00')

async def discoverDevices():
    devices = await BleakScanner.discover(return_adv = True)

    for v in devices.values():
        if 2409 in list(v[1].manufacturer_data.keys()):
            if await read_name(v[0].address) == "WoCurtain":
                st.success("A Curtain device has been found, and can be selected below! It is named WoCurtain")
                v[0].name = "WoCurtain"

    return pd.DataFrame(
        data={
            "address": [d[0].address for d in devices.values()],
            "name": [d[0].name for d in devices.values()],
        }
    )

def scan():
    loop = asyncio.get_event_loop()
    try:
        if "df" not in st.session_state:
            st.session_state.df = loop.run_until_complete(discoverDevices())
        st.session_state.address = st.dataframe(
            st.session_state.df,
            key="devices",
            on_select="rerun",
            selection_mode="single-row",
            hide_index=True,
        )

        st.markdown("#### Selected")
        st.write(st.session_state.df.loc[st.session_state.address.selection.rows[0]])
    except Exception as e:
        print(e)
