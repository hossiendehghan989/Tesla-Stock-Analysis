"""Recreate the sentiment-over-time plot from a documented local CSV."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def recreate_plot(input_path: Path, output_path: Path) -> None:
    """Create the sentiment plot from a CSV containing Date and compound columns."""
    df = pd.read_csv(input_path)
    required = {"Date", "compound"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

    df["Date"] = pd.to_datetime(df["Date"])
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df["Date"], df["compound"], color="green", linewidth=1, label="Compound sentiment")
    ax.axvline(pd.Timestamp("2019-01-01"), color="red", linestyle="--", linewidth=1.5, label="Train/test split")
    ax.set_title("Tesla-market sentiment over time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Compound sentiment score")
    ax.set_ylim(-1.0, 1.0)
    ax.grid(True, which="both", linestyle="-", alpha=0.3)
    ax.legend(loc="lower left")
    fig.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="CSV containing Date and compound columns")
    parser.add_argument("--output", type=Path, default=Path("artifacts/sentiment_over_time.png"))
    args = parser.parse_args()
    recreate_plot(args.input, args.output)
    print(f"Saved plot to {args.output}")


if __name__ == "__main__":
    main()
