import asyncio
from pytonlib import TonlibClient
from pathlib import Path
import requests

from new_wallet_creation import new_wallet, mnemonics
from wallet_creation import wallet, mnemonics

URL = "https://ton.org/testnet-global.config.json"

class Deployes:
    active_wallet_mnemonics = []
    new_wallet_mnemonics = []
    new_wallet = None
    active_wallet = None
    seqno = None
    client = None
    
    def __init__(self):
        self.new_wallet_mnemonics = mnemonics
        self.active_wallet_mnemonics = mnemonics
        self.new_wallet = new_wallet
        self.active_wallet = wallet

        self.config = requests.get(URL).json()

        keystore_dir = '/tmp/ton_keystore'
        Path(keystore_dir).mkdir(parents=True, exist_ok=True)
        self.client = TonlibClient(ls_index=3, config=self.config, keystore=keystore_dir, tonlib_timeout=60)


        print("----------------------------------------")
        print("Кошельки созданы и добавлены")
        print("Клиент инициализирован")
        print(f"Адрес активированного кошелька: {self.active_wallet.address.to_string(True, True, True, True)}")
        print(f"Адрес нового кошелька: {self.new_wallet.address.to_string(True, True, True, True)}")
        print("----------------------------------------")

    
    async def send_transfer_message(self, amount: int):
        await self.client.init()
        data = await self.client.raw_run_method(method='seqno', stack_data=[], address=wallet.address.to_string(True, True, True, True))
        self.seqno = int(data['stack'][0][1], 16)
        state_init = self.new_wallet.create_state_init()['state_init']

        transfer_query = wallet.create_transfer_message(to_addr=self.new_wallet.address.to_string(True, True, True, True), amount=amount, 
                                   seqno=self.seqno, state_init=state_init)

        transfer_message = transfer_query['message'].to_boc(False)

        await self.client.raw_send_message(transfer_message)





