import asyncio
from bleak import BleakClient
from crccheck.crc import Crc8Maxim
from bleak import BleakScanner

address = "DA:2E:1C:E1:05:23"
model = "cba20002-224d-11e6-9fb8-0002a5d5c51b"

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

    await executeLooped(address, model, [open, close])

async def infinite():
    start = bytes.fromhex("570f450406010101")
    iets = bytes.fromhex("570f4504020100")
    anders = bytes.fromhex("570f450501")
    ltr = bytes.fromhex("570f450508010101")
    gaan = bytes.fromhex("570f4505040001")
    stop = bytes.fromhex("570f45050500")

    await execute(address, model, [start, iets, anders, ltr, gaan, stop])

async def clear():
    clear = bytes.fromhex("570f450303")

    await execute(address, model, clear)
    
async def open():
    open = bytes.fromhex("570f45010101ff00")

    await execute(address, model, open)

async def close():
    close = bytes.fromhex("570f450101010000")

    await execute(address, model, close)

async def execute(address, model, toExecute):
    async with BleakClient(address) as client:
        for command in toExecute():
            await client.write_gatt_char(model, command)

async def executeLooped(address, model, toExecute):
    async with BleakClient(address) as client:
        for i in range(1000):
            for command in toExecute():
                await client.write_gatt_char(model, command)


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
