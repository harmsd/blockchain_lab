import warnings
warnings.filterwarnings("ignore", message="pkg_resources is deprecated")

from tonsdk.contract.wallet import Wallets, WalletVersionEnum
from tonsdk.utils import to_nano
from pytonlib import TonlibClient
import requests
from pathlib import Path
import asyncio
from contract import create_contract

TESTNET_CONFIG_URLS = [
    "https://ton.org/testnet-global.config.json",
    "https://newton-blockchain.github.io/testnet-global.config.json",
    "https://raw.githubusercontent.com/ton-community/testnet-config/main/testnet.json"
]

async def get_url():
    for url in TESTNET_CONFIG_URLS:
        try:
            config = requests.get(url, timeout=5).json()
            return config
        except:
            continue
    raise Exception("Все конфиги недоступны")

def init_wallet():
    mnemonics = ['ridge', 'vote', 'flip', 'office', 'that', 'scissors', 'earn', 'escape', 
             'novel', 'clarify', 'defense', 'chief', 'alert', 'female', 'audit', 'audit', 'limit', 'busy', 'giant', 
             'destroy', 'flower', 'fat', 'major', 'column']

    mnemonics, public_key, private_key, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v3r2, workchain=0)
    wallet_address = wallet.address.to_string(True, True, True, True)
    return wallet, wallet_address

async def get_seqno(client: TonlibClient, wallet_address: str):
    try:
        data = await client.raw_run_method(method='seqno', stack_data=[], address=wallet_address)
        return int(data['stack'][0][1], 16)
    except Exception as e:
        print(f"Ошибка при получении seqno: {e}")
        return 0
    
async def get_seqno(wallet_address: str, client: TonlibClient):
    try:
        # account_info = await client.raw_get_account_state(wallet_address)
        # # status = account_info.get('status', 'not_found')
        # balance = account_info.get('balance', 0) / 1e9

        # if status != 'active':
        #     print("Кошелек не активен")
        #     return False
        
        seqno = await get_seqno(client, wallet_address)

    except Exception as e:
        print(f"Кошелек не найден в блокчейне: {e}")
        return False
    
    return seqno
    
async def main():
    try:
        config = await get_url()
        keystore_dir = '/tmp/ton_keystore'
        Path(keystore_dir).mkdir(parents=True, exist_ok=True)
        client = TonlibClient(ls_index=2, config=config,keystore=keystore_dir,tonlib_timeout=30)
        await client.init()

        wallet, wallet_address = init_wallet()
        seqno = await get_seqno(wallet_address, client)

        transfer_query = wallet.create_transfer_message(to_addr='UQCPqlzkFukDdWCXw__x1QIOoJF-SLIim-j5lu3abKDVZAt4', amount=to_nano(0.01, 'ton'),
                                                        seqno=seqno,
                                                        payload=f'Address: {wallet_address}')
        transfer_msg = transfer_query['message'].to_boc(False)
        print(transfer_msg)
        await client.raw_send_message(transfer_msg)
        await create_contract('UQCPqlzkFukDdWCXw__x1QIOoJF-SLIim-j5lu3abKDVZAt4', wallet_address)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())