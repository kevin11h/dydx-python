from decimal import Decimal

# ------------ Universal Constants ------------
NETWORK_ID = 1
MAX_SOLIDITY_UINT = 115792089237316195423570985008687907853269984665640564039457584007913129639935  # noqa: E501
FOUR_WEEKS_IN_SECONDS = 2419200

# ------------ Addresses ------------
TAKER_ACCOUNT_OWNER = '0xf809e07870dca762B9536d61A4fBEF1a17178092'

# ------------ Contract Addresses ------------
CANONICAL_ORDERS_ADDRESS = '0xCd81398895bEa7AD9EFF273aeFFc41A9d83B4dAD'
SOLO_MARGIN_ADDRESS = '0x1E0447b19BB6EcFdAe1e4AE1694b0C3659614e4e'
PAYABLE_PROXY_ADDRESS = '0xa8b39829cE2246f89B31C013b8Cde15506Fb9A76'
P1_ORDERS_ADDRESS = '0x6779c1C4033ffD75a563CfB1BbC86C12D732591f'
PERPETUAL_ADDRESS = '0xD029c869dEc40A3a53a3799A1181306B0f747AdD'
WETH_ADDRESS = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
SAI_ADDRESS = '0x89d24A6b4CcB1B6fAA2625fE562bDD9a23260359'
USDC_ADDRESS = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
DAI_ADDRESS = '0x6B175474E89094C44Da98b954EedeAC495271d0F'

# ------------ Protocol Enums ------------
ACTION_TYPE_DEPOSIT = 0
ACTION_TYPE_WITHDRAW = 1

REFERENCE_DELTA = 0
REFERENCE_TARGET = 1

# ------------ Markets ------------
MARKET_ETH = 0
MARKET_WETH = 0
MARKET_SAI = 1
MARKET_USDC = 2
MARKET_DAI = 3
MARKET_PBTC = 'PBTC'
MARKET_INVALID = 4

# ------------ Pairs ------------
PAIR_WETH_DAI = 'WETH-DAI'
PAIR_WETH_USDC = 'WETH-USDC'
PAIR_DAI_USDC = 'DAI-USDC'
PAIR_PBTC_USDC = 'PBTC-USDC'

DECIMALS_WETH = 18
DECIMALS_SAI = 18
DECIMALS_USDC = 6
DECIMALS_DAI = 18
DECIMALS_PBTC = 8

# ------------ Sides ------------
SIDE_BUY = 'BUY'
SIDE_SELL = 'SELL'

# ------------ Fees ------------
FROM_BIPS = Decimal('1e-4')
SMALL_TRADE_SIZE_WETH = 0.5 * (10 ** DECIMALS_WETH)
SMALL_TRADE_SIZE_DAI = 100 * (10 ** DECIMALS_DAI)
SMALL_TRADE_SIZE_PBTC = 0.01 * (10 ** DECIMALS_PBTC)
FEE_SMALL_WETH = Decimal(50) * FROM_BIPS
FEE_LARGE_WETH = Decimal(15) * FROM_BIPS
FEE_SMALL_DAI = Decimal(50) * FROM_BIPS
FEE_LARGE_DAI = Decimal(5) * FROM_BIPS
FEE_LARGE_PBTC = Decimal(7.5) * FROM_BIPS
FEE_SMALL_PBTC = Decimal(50) * FROM_BIPS
FEE_MAKER_PBTC = Decimal(-2.5) * FROM_BIPS
FEE_ZERO = Decimal(0)

# ------------ Transaction Constants ------------
DEFAULT_GAS_AMOUNT = 250000
DEFAULT_GAS_MULTIPLIER = 1.5
DEFAULT_GAS_PRICE = 4000000000
DEFAULT_GAS_PRICE_ADDITION = 3

# ------------ Protocol ------------
MINIMUM_COLLATERALIZATION = 1.15
PRICE_ORACLE_USD_MULTIPLIER = 10 ** 36

# ------------ Math ------------
BASE_DECIMAL = Decimal(10 ** 18)
