# from tonsdk.contract.token.nft import NFTCollection, NFTItem
# from tonsdk.contract import Address
# from tonsdk.utils import to_nano

# def create_collection_mint():
#     royalty_base = 1000
#     royalty_factor = 55

#     collection = NFTCollection(royalty_base=royalty_base, 
#                                royalty=royalty_factor,
#                                royalty_address=Address('kQDofYngQ-AK9ENUU7apjnP51fclbqRHMRHGyUTHkjfOPdBq'),
#                                owner_address=Address('kQDofYngQ-AK9ENUU7apjnP51fclbqRHMRHGyUTHkjfOPdBq'),
#                                collection_content_uri='https://s.getgems.io/nft/b/c/62fba50217c3fe3cbaad9e7f/meta.json',
#                                nft_item_content_base_uri='https://s.getgems.io/nft/b/c/62fba50217c3fe3cbaad9e7f/',
#                                nft_item_code_hex=NFTItem.code
#                                )
    
#     return collection

# def create_nft_mint(index=0, address='0QD5clkU5m7dkLIs70CmTeyHf8UM_cybz26KyryoLunXYym8'):
#     collection = create_collection_mint()
#     body = collection.create_mint_body(item_index=1, 
#                                 new_owner_address=Address(address), 
#                                 item_content_uri=f'{index+1}/meta.json',
#                                 amount=to_nano(0.02, 'ton'))
    
#     return body

# def create_batch_nft_mint(index=0, address='kQDofYngQ-AK9ENUU7apjnP51fclbqRHMRHGyUTHkjfOPdBq'):
#     collection = create_collection_mint()
#     contents_and_owners = []
#     for i in range(1, 5):
#         contents_and_owners.append((f'{i + 1}/meta.json', Address('kQDofYngQ-AK9ENUU7apjnP51fclbqRHMRHGyUTHkjfOPdBq')))
#     body = collection.create_batch_mint_body(from_item_index=1,
#                                              contents_and_owners=contents_and_owners,
#                                              amount_per_one=to_nano(0.01, 'ton'))
#     return body

from tonsdk.contract.token.nft import NFTCollection, NFTItem
from tonsdk.contract import Address
from tonsdk.utils import to_nano

GITHUB_BASE_URL = "https://raw.githubusercontent.com/dmittriyyy/nft_lab-4/main"

def create_collection_mint():
    royalty_base = 1000
    royalty_factor = 55
    owner = Address('0QCaMK2ZLSB17ZewOiIwzE54R--epHZ2SFGhwbN1lF-kFdH5')
    collection = NFTCollection(
        royalty_base=royalty_base,
        royalty=royalty_factor,
        royalty_address=owner,
        owner_address=owner,
        collection_content_uri=f'{GITHUB_BASE_URL}/meta1.json',
        nft_item_content_base_uri=f'{GITHUB_BASE_URL}/',
        nft_item_code_hex=NFTItem.code
    )
    return collection

def create_collection_mint2(version=1):
    royalty_base = 1000
    royalty_factor = 55
    owner = Address('kQCaMK2ZLSB17ZewOiIwzE54R--epHZ2SFGhwbN1lF-kFYw8')
    collection = NFTCollection(
        royalty_base=royalty_base,
        royalty=royalty_factor,
        royalty_address=owner,
        owner_address=owner,
        collection_content_uri=f'{GITHUB_BASE_URL}/meta.json',
        nft_item_content_base_uri=f'{GITHUB_BASE_URL}/',
        nft_item_code_hex=NFTItem.code
    )
    return collection

def create_nft_mint(index=1, owner_address='kQCaMK2ZLSB17ZewOiIwzE54R--epHZ2SFGhwbN1lF-kFYw8', metadata_url=None):
    if metadata_url is None:
        metadata_url = f'{GITHUB_BASE_URL}/metadata_{index}.json'
    
    collection = create_collection_mint()
    body = collection.create_mint_body(
        item_index=index,
        new_owner_address=Address(owner_address),
        item_content_uri=metadata_url,
        amount=to_nano(0.02, 'ton')
    )
    return body

def create_batch_nft_mint(index=0, address='kQATeRp5YOTP7UkhhVM_P9fE4xpro6gQCwb4ZjHuc2gR0bsu'):
    collection = create_collection_mint()
    contents_and_owners = []
    for i in range(1, 5):
        contents_and_owners.append((f'{i + 1}/meta.json', Address('kQATeRp5YOTP7UkhhVM_P9fE4xpro6gQCwb4ZjHuc2gR0bsu')))
    body = collection.create_batch_mint_body(from_item_index=1,
                                             contents_and_owners=contents_and_owners,
                                             amount_per_one=to_nano(0.01, 'ton'))
    return body
