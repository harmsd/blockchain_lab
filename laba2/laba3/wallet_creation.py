from tonsdk.contract.wallet import Wallets, WalletVersionEnum


mnemonics = ['crack', 'legal', 'indicate', 'marriage', 'dirt', 'gentle', 'chuckle', 'found', 'room', 'alter', 'strategy', 'angle', 
             'eagle', 'picnic', 'congress', 'divert', 'sentence', 'erode', 'divorce', 'vault', 'flat', 'father', 'shift', 'govern']

mnemonics, public_key, private_key, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v3r2, workchain=0)

if __name__ == "__main__":
    print(mnemonics)
    print(wallet.address.to_string(True, True, True, True))
