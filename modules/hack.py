import asyncio
from bleak import BleakClient
from crccheck.crc import Crc8Maxim
from bleak import BleakScanner
import streamlit as st



# async def main(address):
#     device = await BleakScanner.find_device_by_name("WoCurtain")
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
    #     await client.write_gatt_char(model, open)
    #     await client.write_gatt_char(model, close)

    # await client.write_gatt_char(model, start)
    # await client.write_gatt_char(model, iets)
    # await client.write_gatt_char(model, anders)
    # await client.write_gatt_char(model, ltr)
    # await client.write_gatt_char(model, gaan)
    #
    # await client.write_gatt_char(model, stop)

async def dos():
    close = bytes.fromhex("570f450101010000")
    open = bytes.fromhex("570f45010101ff00")

    await executeLooped(model, [open, close])

async def infinite():
    start = bytes.fromhex("570f450406010101")
    iets = bytes.fromhex("570f4504020100")
    anders = bytes.fromhex("570f450501")
    ltr = bytes.fromhex("570f450508010101")
    gaan = bytes.fromhex("570f4505040001")
    stop = bytes.fromhex("570f45050500")

    await execute(model, [start, iets, anders, ltr, gaan, stop])

async def clear():
    clear = bytes.fromhex("570f450303")

    await execute(model, clear)
    
async def open():
    open = bytes.fromhex("570f45010101ff00")

    await execute(model, open)

async def close():
    close = bytes.fromhex("570f450101010000")

    await execute(model, close)

async def execute(model, toExecute):
    address = st.session_state.df.loc[st.session_state.address.selection.rows[0]]
    async with BleakClient(address) as client:
        for command in toExecute():
            await client.write_gatt_char(model, command)

async def executeLooped(model, toExecute):
    address = st.session_state.df.loc[st.session_state.address.selection.rows[0]]
    async with BleakClient(address) as client:
        for i in range(1000):
            for command in toExecute():
                await client.write_gatt_char(model, command)

def hack(function):
    # address = "DA:2E:1C:E1:05:23"
    if ("address" not in st.session_state):
        st.write("No object selected yet")
    else:
        st.write("Object selected!")
    global model 
    model = "cba20002-224d-11e6-9fb8-0002a5d5c51b"

    loop = asyncio.get_event_loop()
    try:
        match function:
            case "Clear":
                loop.run_until_complete(clear())
            case "Open":
                loop.run_until_complete(open())
            case "Close":
                loop.run_until_complete(close())
            case "DOS":
                loop.run_until_complete(dos())
            case "Infinite":
                loop.run_until_complete(infinite())
    except Exception as e:
        print(e)

# asyncio.run(main(address))

# import asyncio
# from bleak import BleakScanner
#
# async def main():
#     devices = await BleakScanner.discover()
#     for d in devices:
#         print(d)
#
# asyncio.run(main())
