# Data provenance and reproducibility

This repository contains educational notebook artifacts built around historical Tesla market data and sentiment features. The notebooks are not a live market-data pipeline.

## Before reproducing results

1. Obtain the input CSV through a lawful, documented source.
2. Keep the source file outside Git if its redistribution rights are unclear.
3. Record the source URL, download date, column schema, and any preprocessing in your research notes.
4. Do not commit credentials, scraped personal data, or proprietary datasets.

The notebooks cover historical periods and may depend on the exact source snapshot. Re-running them with a different data snapshot can change results. Treat every result as an experiment, not a trading signal or investment recommendation.

## Repository checks

The CI workflow validates notebook structure and the portable plotting utility. It does not execute every notebook against a live data source; that boundary is intentional so CI remains deterministic and does not depend on external market-data availability.
