comparison_df = pd.merge(
    conventional_df,
    adaptive_df,
    on="Circuit Depth",
    suffixes=(
        "_Conventional",
        "_Adaptive"
    )
)

comparison_df
