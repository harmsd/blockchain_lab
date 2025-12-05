from tonsdk.contract.token.ft import JettonMinter, JettonWallet
from tonsdk.utils import Address

def create_state_init_jetton():
    minter = JettonMinter(admin_address=Address('0QCaMK2ZLSB17ZewOiIwzE54R--epHZ2SFGhwbN1lF-kFdH5'),
                          jetton_content_uri='https://raw.githubusercontent.com/yungwine/pyton-lessons/refs/heads/master/lesson-6/token_data.json',
                          jetton_wallet_code_hex=JettonWallet.code)

    return minter.create_state_init()['state_init'], minter.address.to_string()