import asyncio
from pytonlib import TonlibClient
from pathlib import Path
from tonsdk.utils import to_nano
import requests

from wallets.new_wallet_creation import new_wallet, mnemonics
from wallets.wallet_creation import wallet, mnemonics

from mint_bodies import create_state_init_jetton

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
        self.client = TonlibClient(ls_index=2, config=self.config, keystore=keystore_dir, tonlib_timeout=60)


        print("----------------------------------------")
        print("Кошельки созданы и добавлены")
        print("Клиент инициализирован")
        print(f"Адрес активированного кошелька: {self.active_wallet.address.to_string(True, True, True, True)}")
        print(f"Адрес нового кошелька: {self.new_wallet.address.to_string(True, True, True, True)}")
        print("----------------------------------------")

    
    async def deploy_minter(self):
        await self.client.init()
        data = await self.client.raw_run_method(method='seqno', stack_data=[], address=wallet.address.to_string(True, True, True, True))
        self.seqno = int(data['stack'][0][1], 16)

        state_init, jetton_address = create_state_init_jetton()

        transfer_query = wallet.create_transfer_message(to_addr=jetton_address, amount=to_nano(0.05, 'ton'), 
                                   seqno=self.seqno, state_init=state_init)

        transfer_message = transfer_query['message'].to_boc(False)

        await self.client.raw_send_message(transfer_message)





