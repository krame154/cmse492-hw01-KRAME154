"""Main analysis script for the starter repository.
Run with: python src/analysis.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


def resolve_project_root() -> Path:
    env_root = os.getenv("STARTER_REPO_ROOT") or os.getenv("PROJECT_ROOT")
    if env_root:
        candidate = Path(env_root).expanduser().resolve()
        if candidate.exists():
            return candidate
    return Path(__file__).resolve().parent.parent


def configure_paths(project_root: Path) -> None:
    extra_paths = [
        project_root / "src" / "my_scripts",
        project_root / "src" / "utility",
    ]
    for p in extra_paths:
        sys.path.insert(0, str(p))


def make_revenue_per_unit_plot(summary_df, out_path: Path) -> None:
    plot_df = (
        summary_df.groupby("region", as_index=False)["revenue_per_unit"]
        .mean()
        .sort_values("revenue_per_unit", ascending=False)
    )

    plt.figure(figsize=(8, 4))
    sns.barplot(data=plot_df, x="region", y="revenue_per_unit")
    plt.title("Average Revenue per Unit by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue per Unit (USD)")
    plt.tight_layout()
    plt.savefig(out_path, dpi=120)
    plt.close()


def main() -> None:
    project_root = resolve_project_root()
    configure_paths(project_root)

    from clean_data_v1 import build_summary_table, load_inputs
    from file_stuff import ensure_folder, save_csv
    from plot_helpers import make_revenue_plot

    sales_path = project_root / "data" / "datafiles" / "sales_jan.csv"
    customers_path = project_root / "data" / "datafiles" / "customer_lookup.csv"

    sales_df, customer_df = load_inputs(sales_path, customers_path)
    summary = build_summary_table(sales_df, customer_df)

    summary["revenue_per_unit"] = (
        summary["total_revenue"] / summary["total_units"]
    ).round(2)

    output_dir = ensure_folder(project_root / "results" / "outputs")
    summary_path = output_dir / "summary_by_region.csv"
    plot_path = output_dir / "revenue_by_region.png"
    new_plot_path = output_dir / "revenue_per_unit_by_region.png"

    save_csv(summary, summary_path)
    make_revenue_plot(summary, plot_path)
    make_revenue_per_unit_plot(summary, new_plot_path)

    print("Analysis complete.")
    print(f"Rows in summary: {len(summary)}")
    print(f"Summary written to: {summary_path}")
    print(f"Plot written to: {plot_path}")
    print(f"New plot written to: {new_plot_path}")


if __name__ == "__main__":
    main()


