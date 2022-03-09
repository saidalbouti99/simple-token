from brownie import SimpleToken, config, network, accounts
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")
def deploy_token():
    account=get_account()
    simple_token=SimpleToken.deploy(initial_supply, {"from": account})
    print(f"{simple_token.name()} deployed to {simple_token.address}")
    # print(f"Token Supply is {simple_token.viewTotalSupply()}")

def main():
    deploy_token()