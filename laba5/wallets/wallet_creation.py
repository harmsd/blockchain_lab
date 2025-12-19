from tonsdk.contract.wallet import Wallets, WalletVersionEnum

# mnemonics3 = ['nephew', 'draw', 'miss', 'canal', 'nothing', 'cheese', 'runway', 'reveal', 'vast', 'addict', 'broken', 'tube', 'flower', 'patient', 'fatigue', 'impulse', 'section', 'together', 'carpet', 'smoke', 'lecture', 'canvas', 'obscure', 'planet']
# mnemonics2 = ['ridge', 'vote', 'flip', 'office', 'that', 'scissors', 'earn', 'escape', 
#              'novel', 'clarify', 'defense', 'chief', 'alert', 'female', 'audit', 'audit', 'limit', 'busy', 'giant', 
#              'destroy', 'flower', 'fat', 'major', 'column']

mnemonics = ['nephew', 'draw', 'miss', 'canal', 'nothing', 'cheese', 'runway', 'reveal', 'vast', 'addict', 'broken', 'tube', 'flower', 'patient', 'fatigue', 'impulse', 'section', 'together', 'carpet', 'smoke', 'lecture', 'canvas', 'obscure', 'planet']

mnemonics, public_key, private_key, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v3r2, workchain=0)
wallet_address = wallet.address.to_string(True, True, True, True)

if __name__ == "__main__":
    print(mnemonics)
    print(wallet.address.to_string(True, True, True, True))
