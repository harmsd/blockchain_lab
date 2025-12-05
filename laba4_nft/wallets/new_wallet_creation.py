from tonsdk.contract.wallet import Wallets, WalletVersionEnum

mnemonics, public_key, private_key, new_wallet = Wallets.create(version=WalletVersionEnum.v3r2, workchain=0)

def get_wallet_from_mnemonics(mnemonics):
    mnemonics, public_key, private_key, wallet_from_mnemonics = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v3r2, workchain=0)
    return wallet_from_mnemonics

if __name__ == "__main__":
    print(new_wallet.address.to_string(True, True, True, True))
