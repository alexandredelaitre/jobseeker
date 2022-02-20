import requests
import json
import deso


# they send a message to us
# we check if it's a valid format
def current_price():
    return deso.Deso().getDeSoPrice()

def test():
    walletData = deso
    return walletData
print(test())
