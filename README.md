# Tesla Stock Analysis

> **A reproducible research notebook for market signals, forecasting experiments, and sentiment analysis.**

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white" alt="Jupyter" />
  <img src="https://img.shields.io/badge/XGBoost-0B2B3C?logo=xgboost&logoColor=F4B942" alt="XGBoost" />
  <img src="https://img.shields.io/badge/LSTM-0B8F8C?logo=tensorflow&logoColor=white" alt="LSTM" />
  <img src="https://img.shields.io/badge/educational%20research-MIT-F4B942" alt="Educational research" />
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
| **Reproducibility** | Notebook workflow plus a small plotting utility |

## Start here

| Goal | File |
| --- | --- |
| Review the main forecasting experiment | [`Hossein_Dehghan_Tesla_Stock_Prediction_XGBoost_LSTM.ipynb`](Hossein_Dehghan_Tesla_Stock_Prediction_XGBoost_LSTM.ipynb) |
| Explore historical behavior | [`tesla_stock_analysis_Hossein_Dehghan_.ipynb`](tesla_stock_analysis_Hossein_Dehghan_.ipynb) |
| Inspect the sentiment workflow | [`colab_sentiment_code.ipynb`](colab_sentiment_code.ipynb) |
| Recreate the sentiment plot | [`recreate_sentiment_plot.py`](recreate_sentiment_plot.py) |
| See the broader engineering portfolio | [Hossein Dehghan on GitHub](https://github.com/hossiendehghan989) |

## Run locally

```bash
git clone https://github.com/hossiendehghan989/Tesla-Stock-Analysis.git
cd Tesla-Stock-Analysis
python -m venv .venv
source .venv/bin/activate
pip install jupyter pandas numpy matplotlib xgboost
jupyter notebook
```

Open a notebook and run the cells in order. The notebooks may require small dependency or data-source adjustments because they are research artifacts rather than a packaged production application.

## How to read the results

The experiments depend on the selected historical period, feature engineering choices, data availability, preprocessing, and model configuration. Forecasting output should be interpreted as an experiment in modeling—not as a trading signal or investment recommendation. A stronger next step would be a leakage-audited, walk-forward benchmark with explicit baselines and transaction-cost assumptions.

## Next research directions

- Add a chronological walk-forward evaluation protocol
- Compare against naive and seasonal baselines
- Separate exploratory features from production-eligible features
- Document missing-data handling and train/test boundaries
- Add error analysis by market regime
- Package the workflow with pinned dependencies and reproducible artifacts

## Author

Built by [Hossein Dehghan](https://github.com/hossiendehghan989), an Industrial Engineering graduate focused on **applied AI, data science, energy intelligence, and operational decision support**.
