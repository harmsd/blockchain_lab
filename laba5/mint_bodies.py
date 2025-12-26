from tonsdk.contract.token.ft import JettonMinter, JettonWallet
from tonsdk.utils import Address, to_nano
from wallets.new_wallet_creation import new_wallet

# address = new_wallet.address.to_string(True, True, True, True)
# ['defy', 'govern', 'theme', 'fox', 'major', 'found', 'dumb', 'sea', 'garage', 'cigar', 'build', 'coin', 'nominee', 'employ', 'column', 'glass', 'cash', 'symbol', 'bench', 'rifle', 'office', 'puzzle', 'prefer', 'hire']
address = "kQDD5xF0VW14U1KYxxBDitiVl3z_N__MpzyP1DpWerLMD5Zs"
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