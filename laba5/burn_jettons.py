import asyncio
from pathlib import Path

import requests
from pytonlib import TonlibClient
from tonsdk.contract.token.ft import JettonWallet
from tonsdk.utils import to_nano, Address

from wallets.wallet_creation import wallet, wallet_address

JETTON_WALLET_ADDR = "kQBpOMv8pQYER6YFI1twB879mm4OluE-iXANRURGwsIH3Vuv"

async def get_client():
    url = "https://ton.org/testnet-global.config.json"
    config = requests.get(url).json()
    keystore_dir = "/tmp/ton_keystore"
    Path(keystore_dir).mkdir(parents=True, exist_ok=True)

    client = TonlibClient(ls_index=2, config=config, keystore=keystore_dir, tonlib_timeout=30)
    await client.init()
    return client

async def get_seqno(client: TonlibClient, address: str) -> int:
    data = await client.raw_run_method(method="seqno", stack_data=[], address=address)
    return int(data["stack"][0][1], 16)

async def pytonlib_burn():
    client = await get_client()

    DECIMALS = 9
    JETTON_WALLET_ADDR = "0QDfHyHSMp5GmSSMEnKVZg1jh-MfvyZhKZmWDILCpUF5avbl" 
    OWNER_ADDR = "0QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACkT"

    amount_tokens = 50
    jetton_amount = amount_tokens * (10 ** DECIMALS)

    body = JettonWallet().create_burn_body(
        jetton_amount=jetton_amount,
        response_address=Address(OWNER_ADDR),
    )

    seqno = await get_seqno(client, wallet_address)

    query = wallet.create_transfer_message(
        to_addr=JETTON_WALLET_ADDR,
        amount=to_nano(0.05, "ton"), 
        seqno=seqno,
        payload=body,
    )


async def burn():
    client = await get_client()
    seqno = await get_seqno(client, wallet_address)

    body = JettonWallet().create_burn_body(
        jetton_amount=to_nano(50000, 'ton'),
    )

    query = wallet.create_transfer_message(to_addr='0QDfHyHSMp5GmSSMEnKVZg1jh-MfvyZhKZmWDILCpUF5avbl', amount=to_nano(0.05, 'ton'), seqno=seqno, payload=body)

    await client.raw_send_message(query["message"].to_boc(False))
    

if __name__ == "__main__":
    asyncio.run(burn())
