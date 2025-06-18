import streamlit as st
import threading
from bleak import BleakScanner
import asyncio
from streamlit_autorefresh import st_autorefresh
from apscheduler.schedulers.background import BackgroundScheduler

# Replace with your target MAC address
TARGET_MAC = "DA:2E:1C:E1:05:23"
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
    # st.session_state.print(data)
    bytestring = bin(hex)[2:].zfill(len(data) * 4)
    # st.session_state.print(bytestring)
    # st.session_state.encryption = bytestring[0]
    # st.session_state.dev_type = bytestring[1:8]
    shared_data["allow_connect"] = bytestring[8]
    shared_data["callibrated"] = bytestring[9]
    # st.session_state.nc = bytestring[10:16]
    # st.session_state.update_utc_flag = bytestring[16]
    shared_data["battery"] = int(bytestring[17:24], 2)
    shared_data["moving"] = int(bytestring[24])
    shared_data["position"] = int(bytestring[25:32], 2)
    shared_data["light_level"] = int(bytestring[32:37], 2)
    # st.session_state.device_chain = bytestring[37:]

    # print("=== Device Info ===")
    # print(f"Encryption        : {st.session_state.encryption}")
    # print(f"Device Type       : {st.session_state.dev_type}")
    # print(f"Allow Connect     : {st.session_state.allow_connect}")
    # print(f"Calibrated        : {st.session_state.callibrated}")
    # print(f"NC                : {st.session_state.nc}")
    # print(f"Update UTC Flag   : {st.session_state.update_utc_flag}")
    # print(f"Battery           : {st.session_state.battery}")
    # print(f"Moving            : {st.session_state.moving}")
    # print(f"Device Position   : {st.session_state.device_position}")
    # print(f"Light Level       : {st.session_state.light_level}")
    # print(f"Device Chain      : {st.session_state.device_chain}")


def detection_callback(device, advertisement_data):
    # print("callback")
    advertisement_data = advertisement_data["props"]
    # print(f"device address: {device.address.upper()}")
    # print(f"\n📡 Found target device: {device.name} [{device.address}]")
    # print(f"RSSI: {device.rssi}")
    # print("🔍 Advertisement Data:")
    ## print(f"  Local Name: {advertisement_data.local_name}")
    # print(f"  Manufacturer Data: {advertisement_data['ManufacturerData']}")
    # print(f"  Service UUIDs: {advertisement_data['UUIDs']}")
    # print(
    #    f"  Service Data: {interpret(list(advertisement_data['ServiceData'].values())[0].hex())}"
    # )
    interpret(list(advertisement_data["ServiceData"].values())[0].hex())
    # print(f"  TX Power: {advertisement_data.tx_power}")
    # print(f"  Platform Data: {advertisement_data.platform_data}")


async def scan_for_device():
    scanner = BleakScanner()
    # try:
    #    target_mac = st.session_state.df.loc[
    #        st.session_state.address.selection.rows[0], "address"
    #    ].upper()
    #    print(target_mac)
    # except Exception:
    #    return
    # scanner.register_detection_callback(detection_callback)
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


#
# def update_data():
#    st.session_state.battery = shared_data["battery"]
#    st.session_state.moving = shared_data["moving"]
#    st.session_state.position = shared_data["position"]
#    st.session_state.light_level = shared_data["light_level"]
#    st.session_state.callibrated = shared_data["callibrated"]
#    st.session_state.allow_connect = shared_data["allow_connect"]
#


def info():
    if len(st.session_state.address.selection.rows) == 0:
        st.error("No object selected!")
    else:
        st.markdown(f"""Battery level: {shared_data["battery"]}🔋""")
        st.progress(shared_data["light_level"] * 10, text="Light level 💡")
        st.progress(shared_data["position"], text="device position")
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
        # scheduler = BackgroundScheduler()
        # scheduler.add_job(run_device_scan, "interval", seconds=5)
        # scheduler.start()
    return
