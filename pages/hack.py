import streamlit as st

st.title("Perform the hack")

st.markdown("""
            You can click the below buttons to actually hack the thing. Isn't that fun!
            """)

st.button("DOS")
st.button("Remove lighting rules")
st.button("Move indefinitely")



# import asyncio
# from bleak import BleakClient
# from crccheck.crc import Crc8Maxim
# from bleak import BleakScanner
#
# address = "DA:2E:1C:E1:05:23"
#
# async def main(address):
#     model = "cba20002-224d-11e6-9fb8-0002a5d5c51b"
#     device = await BleakScanner.find_device_by_name("WoCurtain")
#     async with BleakClient(address) as client:
#         open = bytes.fromhex("570f45010101ff00")
#         close = bytes.fromhex("570f450101010000")
#         start = bytes.fromhex("570f450406010101")
#         iets = bytes.fromhex("570f4504020100")
#         anders = bytes.fromhex("570f450501")
#         ltr = bytes.fromhex("570f450508010101")
#         gaan = bytes.fromhex("570f4505040001")
#         stop = bytes.fromhex("570f45050500")
#         gaan2 = bytes.fromhex("570f450508010202")
#         gaan3 = bytes.fromhex("570f4505040002")
#         test1 = bytes.fromhex("570f45050301")
#         wya = bytes.fromhex("570f460100")
#         test2 = bytes.fromhex("570f45050302")
#         stopcal = bytes.fromhex("570f450502")
#         crcinst = Crc8Maxim()
#         crcinst.process(close)
#         crcinst.process(open)
#         # while (True):
#         #     await client.write_gatt_char(model, open)
#         #     await client.write_gatt_char(model, close)
#
#         # await client.write_gatt_char(model, start)
#         # await client.write_gatt_char(model, iets)
#         # await client.write_gatt_char(model, anders)
#         # await client.write_gatt_char(model, ltr)
#         # await client.write_gatt_char(model, gaan)
#
#         await client.write_gatt_char(model, stop)
#
#
#
# asyncio.run(main(address))
#
# # import asyncio
# # from bleak import BleakScanner
# #
# # async def main():
# #     devices = await BleakScanner.discover()
# #     for d in devices:
# #         print(d)
# #
# # asyncio.run(main())
