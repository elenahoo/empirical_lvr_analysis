# Empirical Analysis of AMM LVR

This repository provides an **empirical analysis** of the **Liquidity-to-Value Ratio (LVR)** in **UniswapV2 WETH-USDC** pools on **Ethereum**, **Base**, and **Arbitrum**.

The findings from this analysis were presented at [**DevCon SEA**](https://app.devcon.org/schedule/T8BXK3). You can find the recording of the talk via the link 👉 [here](https://www.youtube.com/watch?v=ArILIuH7G2U) and the slides 👉 [here](https://devcon.fileverse.io/devcon7/portal/files/view/0x8cf11a0b9a79487b15281ac81b8234c2).

This repository gives you the data and scripts used in the analysis as well as all the additional charts and code in the **Hex notebook**.

## Data
### UniswapV2
The mint, burn, swap and sync data for WETH-USDC pool used in the analysis is shared in the data folder. 

The data is orignally downloaded from [Allium](https://app.allium.so/); you can also view the queries on Dune below (using Ethereum as an example) to get the same data:
- [mint_event](https://dune.com/queries/4083011)
- [burn_event](https://dune.com/queries/4083070)
- [swap_event](https://dune.com/queries/4083096)
- [sync_event](https://dune.com/queries/4079996)

### CEX & Perpetual 
Binance spot orderbook data at minute frequency is used as the centralised exchange (CEX) data; whereas dYdX v4 data is used as the perpetual data for the analysis. The data are both generated from [CCData](https://data-api.cryptocompare.com/) using the scripts below:
- [`fetch_binance_spot_ob_minute.py`](https://github.com/elenahoo/empirical_lvr_analysis/blob/main/fetch_binance_spot_ob_minute.py)
- [`fetch_dydx_historical_minute.py`](https://github.com/elenahoo/empirical_lvr_analysis/blob/main/fetch_dydx_historical_minute.py)

## LVR Analysis
The full analysis can be found in the following **Hex notebooks**.
- [LVR UniswapV2 Ethereum](https://app.hex.tech/9eb1e790-53f7-4c16-be76-4a22c1aa7d17/hex/d370df01-eb31-4767-986a-fb574d7bef2b/draft/logic?rhid=d370df01-eb31-4767-986a-fb574d7bef2b&view=app)
- [LVR UniswapV2 Base](https://app.hex.tech/9eb1e790-53f7-4c16-be76-4a22c1aa7d17/hex/a01898e6-3eeb-4bb6-a06d-1988e2ab3dde/draft/logic?rhid=a01898e6-3eeb-4bb6-a06d-1988e2ab3dde&view=app)
- [LVR UniswapV2 Arbitrum](https://app.hex.tech/9eb1e790-53f7-4c16-be76-4a22c1aa7d17/app/a31b9eb8-ea6d-4bb5-80b6-3c6bd8a749bc/latest)
- [LVR CamlotV2 Arbitrum](https://app.hex.tech/9eb1e790-53f7-4c16-be76-4a22c1aa7d17/app/0e62c9d8-06e0-417e-a2fd-52d43be5c894/latest)

The comparison analysis across all chains can be found in the [LVR Constant Product Pool Comparison](https://app.hex.tech/9eb1e790-53f7-4c16-be76-4a22c1aa7d17/app/f3d37623-4fdd-443f-a6a7-f65fa5ce647a/latest) notebook.
