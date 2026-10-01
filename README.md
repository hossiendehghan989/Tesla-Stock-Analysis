# Tesla Stock Analysis

> **A reproducible educational research artifact for market signals, forecasting experiments, and sentiment analysis.**

<p align="center">
  <img src="https://img.shields.io/badge/CI-notebook%20checks-0B8F8C?logo=githubactions&logoColor=white" alt="CI notebook checks" />
  <img src="https://img.shields.io/badge/license-MIT-0B8F8C.svg" alt="MIT License" />
  <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white" alt="Python 3.11+" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white" alt="Jupyter" />
  <img src="https://img.shields.io/badge/status-educational%20research-F4B942" alt="Educational research" />
</p>

This repository explores historical Tesla-market behavior through **technical indicators, machine-learning forecasting, and sentiment signals**. It is an educational research project intended to make the workflow easy to inspect and reproduce in Jupyter or Google Colab.

> **Important:** This is not financial advice. Historical performance and model predictions do not guarantee future results.

## What this project demonstrates

| Research layer | Included work |
| --- | --- |
| **Market data** | Historical Tesla price analysis for 2015–2020 |
| **Feature engineering** | Technical indicators and social/sentiment features |
| **Forecasting** | XGBoost and LSTM experiments |
| **Interpretation** | Exploratory visualizations and sentiment analysis |
| **Reproducibility** | Pinned dependencies, notebook validation, and documented data boundaries |

## Start here

| Goal | File |
| --- | --- |
| Review the main forecasting experiment | [`Hossein_Dehghan_Tesla_Stock_Prediction_XGBoost_LSTM.ipynb`](Hossein_Dehghan_Tesla_Stock_Prediction_XGBoost_LSTM.ipynb) |
| Explore historical behavior | [`tesla_stock_analysis_Hossein_Dehghan_.ipynb`](tesla_stock_analysis_Hossein_Dehghan_.ipynb) |
| Inspect the sentiment workflow | [`colab_sentiment_code.ipynb`](colab_sentiment_code.ipynb) |
| Recreate the sentiment plot | [`recreate_sentiment_plot.py`](recreate_sentiment_plot.py) |
| Understand data boundaries | [`docs/DATA_PROVENANCE.md`](docs/DATA_PROVENANCE.md) |
| See the broader engineering portfolio | [Hossein Dehghan on GitHub](https://github.com/hossiendehghan989) |

## Run locally

```bash
git clone https://github.com/hossiendehghan989/Tesla-Stock-Analysis.git
cd Tesla-Stock-Analysis
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install pytest==8.4.2 nbformat==5.10.4
python -m pytest -q
jupyter lab
```

Open a notebook and run the cells in order. The notebooks may require a locally supplied data snapshot; follow [`docs/DATA_PROVENANCE.md`](docs/DATA_PROVENANCE.md) first.

To recreate the sentiment figure without a machine-specific path:

```bash
python recreate_sentiment_plot.py path/to/data.csv --output artifacts/sentiment_over_time.png
```

## How to read the results

The experiments depend on the selected historical period, feature engineering choices, data availability, preprocessing, and model configuration. Forecasting output should be interpreted as an experiment in modeling—not as a trading signal or investment recommendation. A stronger next step is a leakage-audited, walk-forward benchmark with explicit baselines and transaction-cost assumptions.

## Research boundaries

The CI workflow validates notebook structure and the portable plotting utility. It does not execute every notebook against a live data source; that boundary keeps CI deterministic and avoids depending on external market-data availability.

## Next research directions

- Add a chronological walk-forward evaluation protocol
- Compare against naive and seasonal baselines
- Separate exploratory features from production-eligible features
- Document missing-data handling and train/test boundaries
- Add error analysis by market regime
- Publish a versioned data manifest for each reproducible experiment

## Author

Built by [Hossein Dehghan](https://github.com/hossiendehghan989), an Industrial Engineering graduate focused on **applied AI, data science, energy intelligence, and operational decision support**.
