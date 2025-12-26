import asyncio

from wallets.wallet_creation import mnemonics, wallet_address, wallet

from tonsdk.contract.token.ft import JettonWallet
from tonsdk.utils import to_nano, Address

from pytonlib import TonlibClient

import requests
from pathlib import Path

async def get_client():
    url = 'https://ton.org/testnet-global.config.json'

    config = requests.get(url).json()

    keystore_dir = '/tmp/ton_keystore'
    Path(keystore_dir).mkdir(parents=True, exist_ok=True)

    client = TonlibClient(ls_index=2, config=config, keystore=keystore_dir, tonlib_timeout=10)

    await client.init()

    return client


async def get_seqno(client: TonlibClient, address: str):
    data = await client.raw_run_method(method='seqno', stack_data=[], address=address)
    return int(data['stack'][0][1], 16)



async def pytonlib_transfer():
    body = JettonWallet().create_transfer_body(
        to_address=Address('0QDfHyHSMp5GmSSMEnKVZg1jh-MfvyZhKZmWDILCpUF5avbl'),
        jetton_amount=to_nano(50, 'ton'),
    )

    client = await get_client()

    seqno = await get_seqno(client, wallet_address)

    query = wallet.create_transfer_message(to_addr='0QDfHyHSMp5GmSSMEnKVZg1jh-MfvyZhKZmWDILCpUF5avbl', # АДРЕС ДЕРЖАТЕЛЯ ЖЕТОНОВ
                                           amount=to_nano(0.05, 'ton'), seqno=seqno, payload=body)

    await client.raw_send_message(query['message'].to_boc(False))


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(pytonlib_transfer())