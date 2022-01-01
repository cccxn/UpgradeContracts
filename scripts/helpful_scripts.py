from brownie import network, accounts, config
import eth_utils


NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['hardhat', 'development', 'ganache']
LOCAL_BLOCKCHAIN_ENVIRONMENTS = NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS.copy()
LOCAL_BLOCKCHAIN_ENVIRONMENTS.extend(['mainnet_fork', 'binance-fork', 'matic-fork'])


def get_account(number=None):
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if number is not None:
        return accounts[number]
    if network.show_active() in config['networks']:
        return accounts.add(config['wallets']['from_key'])
    return None


def encode_function_data(initializer=None, *args):
    if (len(args) == 0) | (initializer is not None):
        return eth_utils.to_bytes(hexstr='Ox')
    else:
        return initializer.encode_input(*args)


def upgrade(
        account,
        proxy,
        newimplementation_address,
        proxy_admin_contract=None,
        initializer=None,
        *args
):
    txn = None
    if proxy_admin_contract is not None:
        if initializer is not None:
            encoded_function_Call = encode_function_data(initializer, *args)
            txn = proxy_admin_contract.upgradeAndCall(
                proxy.address,
                newimplementation_address,
                encoded_function_Call,
                {'from': account}
            )
        else:
            txn = proxy_admin_contract.upgrade(proxy.address, newimplementation_address, {'from': account})
    else:
        if initializer is not None:
            encoded_function_call = encode_function_data(initializer, *args)
            txn = proxy.upgradeToAndCall(
                newimplementation_address, encoded_function_call, {'from': account}
            )
        else:
            txn = proxy.upgradeTo(newimplementation_address, {'from': account})
    return txn
