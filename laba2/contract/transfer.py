from wallet_creation import wallet
from pytonlib_toncenter import get_seqno
from make_msg import make_msg_body

from pytonlib import TonlibClient
from tonsdk.utils import to_nano
from pathlib import Path
import requests
import asyncio


async def main():   
    url = "https://ton.org/testnet-global.config.json"
    
    config = requests.get(url).json()

    keystore_dir = '/tmp/ton_keystore'
    Path(keystore_dir).mkdir(parents=True, exist_ok=True)

    client = TonlibClient(ls_index=2, config=config, keystore=keystore_dir, tonlib_timeout=15)
    await client.init()
    first_wallet_address = wallet.address.to_string(True, True, True, True)

    for i in range(5):
        seqno = await get_seqno(client, address=first_wallet_address) #seqno - порядковый номер транзакции

        query = wallet.create_transfer_message(to_addr='kQDofYngQ-AK9ENUU7apjnP51fclbqRHMRHGyUTHkjfOPdBq', amount=to_nano(0.05, 'ton'), 
                                            seqno=seqno, payload=make_msg_body())  

        message = query['message'].to_boc(False) #boc формат который принимает тон

        await client.raw_send_message(message)


if __name__ == "__main__":
    asyncio.run(main())
