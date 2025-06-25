import streamlit as st
import threading
from bleak import BleakScanner
import asyncio
from streamlit_autorefresh import st_autorefresh
from apscheduler.schedulers.background import BackgroundScheduler

# Replace with your target MAC address
target_mac = None

shared_data = {
    "battery": 0,
    "light_level": 0,
    "position": 0,
    "moving": False,
    "callibrated": False,
    "allow_connect": False,
}


def interpret(data):
    hex = int(data, 16)
    bytestring = bin(hex)[2:].zfill(len(data) * 4)
    shared_data["allow_connect"] = bytestring[8]
    shared_data["callibrated"] = bytestring[9]
    shared_data["battery"] = int(bytestring[17:24], 2)
    shared_data["moving"] = int(bytestring[24])
    shared_data["position"] = int(bytestring[25:32], 2)
    shared_data["light_level"] = int(bytestring[32:37], 2)

def detection_callback(device, advertisement_data):
    print(advertisement_data)
    advertisement_data = advertisement_data["props"]
    interpret(list(advertisement_data["ServiceData"].values())[0].hex())


async def scan_for_device():
    scanner = BleakScanner()
    if target_mac is None:
        return
    device = asyncio.create_task(scanner.find_device_by_address(target_mac))
    await device
    try:
        detection_callback(device.result(), device.result().details)
    except Exception as e:
        global shared_data
        shared_data = {
            "battery": 0,
            "light_level": 0,
            "position": 0,
            "moving": False,
            "callibrated": False,
            "allow_connect": False,
        }


async def run_device_scan():
    while True:
        await scan_for_device()
        await asyncio.sleep(3)


def info():
    if "address" not in st.session_state:
        st.error("No object selected!")
    elif len(st.session_state.address.selection.rows) == 0:
        st.error("No object selected!")
    else:
        st.markdown(f"""Battery level: {shared_data["battery"]}🔋""")
        st.progress(shared_data["light_level"] * 10, text="Light level 💡")
        st.progress(shared_data["position"], text="Device position")
        st.markdown(f"""Is moving: {True if shared_data["moving"] == 1 else False}""")
        st_autorefresh(interval=1000, limit=None, key="refresh")
        global target_mac
        if (
            st.session_state.df.loc[
                st.session_state.address.selection.rows[0], "address"
            ]
            != target_mac
        ):
            target_mac = st.session_state.df.loc[
                st.session_state.address.selection.rows[0], "address"
            ]
        asyncio.run(run_device_scan())
    return
