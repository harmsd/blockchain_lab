from pytonlib import TonlibClient
from tonsdk.utils import to_nano
from pathlib import Path
import requests
import asyncio

from wallets.wallet_creation import wallet
from mint_bodies import *

URL = "https://ton.org/testnet-global.config.json"

async def get_seqno(client: TonlibClient, address: str):
    data = await client.raw_run_method(method='seqno', stack_data=[], address=address)
    return(int(data['stack'][0][1], 16))

async def deploy_collection():
    url = "https://ton.org/testnet-global.config.json"
    config = requests.get(url).json()
    keystore_dir = '/tmp/ton_keystore'
    Path(keystore_dir).mkdir(parents=True, exist_ok=True)
    client = TonlibClient(ls_index=1, config=config, keystore=keystore_dir, tonlib_timeout=30)
    wallet_address = wallet.address.to_string(True, True, True, True)

    await client.init()

    collection = create_collection_mint2()
    state_init = collection.create_state_init()['state_init']

    seqno = await get_seqno(client, wallet_address)

    transfer_query = wallet.create_transfer_message(to_addr=collection.address.to_string(True, True, True, True), amount=to_nano(0.05, 'ton'), 
                                   seqno=seqno, state_init=state_init)

    transfer_message = transfer_query['message'].to_boc(False)
    await client.raw_send_message(transfer_message)

    print("\n----------------------------------------------\n")
    print(f"Адрес кошелька: {wallet_address}")
    print(f"Адрес коллекции: {collection.address.to_string(True, True, True, True)}")
    print("\n----------------------------------------------\n")
    
async def deploy_one_item():
    url = "https://ton.org/testnet-global.config.json"
    config = requests.get(url).json()
    keystore_dir = '/tmp/ton_keystore'
    Path(keystore_dir).mkdir(parents=True, exist_ok=True)
    client = TonlibClient(ls_index=2, config=config, keystore=keystore_dir, tonlib_timeout=60)
    wallet_address = wallet.address.to_string(True, True, True, True)

    await client.init()

    seqno = await get_seqno(client, wallet_address)

    collection = create_collection_mint2()
    body = create_nft_mint()

    transfer_query = wallet.create_transfer_message(to_addr=collection.address.to_string(True, True, True, True), amount=to_nano(0.08, 'ton'), 
                                   seqno=seqno, payload=body)

    transfer_message = transfer_query['message'].to_boc(False)
    await client.raw_send_message(transfer_message)

    print("\n----------------------------------------------\n")
    print(f"Адрес кошелька: {wallet_address}")
    print(f"Адрес коллекции: {collection.address.to_string(True, True, True, True)}")
    print("\n----------------------------------------------\n")


if __name__ == '__main__':
    asyncio.run(deploy_one_item())