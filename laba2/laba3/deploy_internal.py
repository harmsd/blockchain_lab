from pytonlib import TonlibClient
from tonsdk.utils import to_nano
from pathlib import Path
import requests
import asyncio
import webbrowser

from wallet_creation import wallet
from new_wallet_creation import new_wallet


async def get_seqno(client: TonlibClient, address: str):
    data = await client.raw_run_method(method='seqno', stack_data=[], address=address)
    return(int(data['stack'][0][1], 16))

async def main():
    url = "https://ton.org/testnet-global.config.json"
    
    config = requests.get(url).json()

    keystore_dir = '/tmp/ton_keystore'
    Path(keystore_dir).mkdir(parents=True, exist_ok=True)

    client = TonlibClient(ls_index=2, config=config, keystore=keystore_dir, tonlib_timeout=15)
    wallet_address = wallet.address.to_string(True, True, True, True)
    new_wallet_address = new_wallet.address.to_string(True, True, True, True)
    print(f"Адрес кошелька: {wallet_address}")
    print(f"Адрес нового кошелька: {new_wallet_address}")

    await client.init()

    seqno = await get_seqno(client, wallet_address)

    state_init = new_wallet.create_state_init()['state_init']

    transfer_query = wallet.create_transfer_message(to_addr="0QCUnfNH-4eadKCAE6_rU9BKQQFG0RDxDFYiabywnr6lEDE8", amount=to_nano(0.06, 'ton'), 
                                   seqno=seqno, state_init=state_init)

    transfer_message = transfer_query['message'].to_boc(False)
    await client.raw_send_message(transfer_message)


if __name__ == '__main__':
    asyncio.run(main())