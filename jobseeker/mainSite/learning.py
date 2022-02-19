import requests
import json
import deso


# they send a message to us
# we check if it's a valid format
def current_price():
    return deso.Deso().getDeSoPrice()

def test():
    walletData = deso.Users.getWallet("BC1YLiM6eizVjWfSpk12VuSvMYdTS7ZkxiMvoeYJsrL8ALDqHSQ9pLD", includeCreatorCoin = True) # make includeCreatorCoin as false when you don't want to have creator coin investment in the response data
    return walletData
#print(test())