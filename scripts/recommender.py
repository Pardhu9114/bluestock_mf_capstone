import pandas as pd

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