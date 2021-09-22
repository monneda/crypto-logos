import sys
import shlex
import subprocess

# From cryptocoins.co
URL = 'https://cdn.jsdelivr.net/gh/atomiclabs/cryptocurrency-icons@d5c68edec1f5eaec59ac77ff2b48144679cebca1/svg/color/%s.svg'

# Those available on cryptodatadownload.com/data/binance/
COINS = {
    'BTC', 'ETH', 'LTC', 'NEO', 'BNB', 'XRP', 'LINK', 'EOS', 'TRX', 'ETC',
    'XLM', 'ZEC', 'ADA', 'QTUM', 'DASH', 'XMR', 'BAT', 'BTT', 'ZEC', 'USDC',
    'TUSD', 'MATIC', 'PAX', 'CELR', 'ONE', 'DOT', 'UNI', 'ICP', 'SOL', 'VET',
    'FIL', 'AAVE', 'DAI', 'MKR', 'ICX', 'CVC', 'SC', 'LRC'
}


def download(coin: str):
    url = URL % coin.lower()
    cmd = shlex.split(f'curl -s {url} -o imgs/{coin}.svg')
    subprocess.run(cmd)


if __name__ == '__main__':
    total = len(COINS)
    longest_name = max(COINS, key=len)
    for i, coin in enumerate(COINS):
        remaining = total - i
        alignment = ' ' * (len(longest_name) - len(coin))  # >.<
        print(f'Downloading {coin} {alignment} ({remaining}/{total})')
        download(coin)

