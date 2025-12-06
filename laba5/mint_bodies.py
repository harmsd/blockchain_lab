from tonsdk.contract.token.ft import JettonMinter, JettonWallet
from tonsdk.utils import Address, to_nano

address = '0QCaMK2ZLSB17ZewOiIwzE54R--epHZ2SFGhwbN1lF-kFdH5'
content = 'https://raw.githubusercontent.com/harmsd/blockchain_lab/refs/heads/master/laba5/token_data.json'


def create_state_init_jetton():
    minter = JettonMinter(admin_address=Address(address),
                          jetton_content_uri=content,
                          jetton_wallet_code_hex=JettonWallet.code)

    return minter.create_state_init()['state_init'], minter.address.to_string()


def increase_supply():
    minter = JettonMinter(admin_address=Address(address),
                          jetton_content_uri=content,
                          jetton_wallet_code_hex=JettonWallet.code)

    body = minter.create_mint_body(destination=Address(address),
                            jetton_amount=to_nano(100000, 'ton'))
    return body


def change_owner():
    minter = JettonMinter(admin_address=Address(address),
                          jetton_content_uri=content,
                          jetton_wallet_code_hex=JettonWallet.code)

    body = minter.create_change_admin_body(new_admin_address=Address('EQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM9c'))
    return body