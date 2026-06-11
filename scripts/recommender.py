"""
Bluestock Mutual Fund Analytics Capstone

This script provides mutual fund recommendations based on an
investor's risk appetite by filtering schemes according to
risk grade and ranking them using Sharpe Ratio performance.
"""

import pandas as pd


def recommend_funds():
    """
    Recommend mutual funds based on risk appetite.

    The function accepts a user's risk preference, filters
    matching mutual fund schemes, ranks them by Sharpe Ratio,
    and displays the top-performing recommendations.

    Returns
    -------
    pandas.DataFrame
        Top recommended mutual fund schemes.
    """

    perf = pd.read_csv(
        "data/processed/clean_scheme_performance.csv"
    )

    risk = input(
        "Enter Risk Appetite (Low/Moderate/High): "
    )

    recommendations = (
        perf[
            perf["risk_grade"]
            .str.contains(
                risk,
                case=False,
                na=False
            )
        ]
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    print(
        recommendations[
            [
                "scheme_name",
                "sharpe_ratio",
                "return_3yr_pct"
            ]
        ]
    )

    return recommendations


if __name__ == "__main__":
    recommend_funds()