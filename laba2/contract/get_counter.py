from wallet_creation import wallet
from pytonlib_toncenter import get_seqno
from make_msg import make_msg_body

from pytonlib import TonlibClient
from tonsdk.utils import to_nano
from pathlib import Path
from tonsdk.utils import b64str_to_bytes
from tonsdk.boc import Cell
from ton.utils import read_address


import requests
import asyncio

async def main():   
    url = "https://ton.org/testnet-global.config.json"
    
    config = requests.get(url).json()

    keystore_dir = '/tmp/ton_keystore'
    Path(keystore_dir).mkdir(parents=True, exist_ok=True)

    client = TonlibClient(ls_index=1, config=config, keystore=keystore_dir, tonlib_timeout=15)
    await client.init()

    data = await client.raw_run_method(address='kQDofYngQ-AK9ENUU7apjnP51fclbqRHMRHGyUTHkjfOPdBq', method='get_contract_storage_data', stack_data=[])

    stack = data['stack'][0][1], data['stack'][1][1]['bytes']

    counter_value = int(stack[0], 16)
    address = read_address(Cell.one_from_boc(b64str_to_bytes(stack[1])))
    
    print('\n ------------------------------------- \n')
    print(f"Счетчик - {counter_value}")
    print(f"Адрес последнего кошелька - {address.to_string(True, True, True, True)}")
    print('\n ------------------------------------- \n')


if __name__ == "__main__":
    asyncio.run(main())