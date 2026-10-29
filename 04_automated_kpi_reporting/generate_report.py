from pathlib import Path
import pandas as pd

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "daily_kpis_synthetic.csv"
OUT = ROOT / "output" / "daily_kpi_report.md"

def main():
    df = pd.read_csv(DATA, parse_dates=["date"])
    required = {"date", "orders", "on_time_rate", "cancellation_rate", "avg_delivery_min"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    if df.empty:
        raise ValueError("Input file has no rows.")

    latest = df.sort_values("date").iloc[-1]
    previous = df.sort_values("date").iloc[-2] if len(df) > 1 else None

    lines = [
        "# Daily KPI Report — Synthetic Data",
        "",
        "> Illustrative report generated from fictional portfolio data.",
        "",
        f"- Reporting date: {latest['date'].date()}",
        f"- Orders: {int(latest['orders']):,}",
        f"- On-time rate: {latest['on_time_rate']:.1%}",
        f"- Cancellation rate: {latest['cancellation_rate']:.1%}",
        f"- Average delivery duration: {latest['avg_delivery_min']:.1f} minutes",
    ]
    if previous is not None:
        lines += [
            "",
            "## Change versus previous date",
            f"- Orders: {int(latest['orders'] - previous['orders']):+,}",
            f"- On-time rate: {(latest['on_time_rate'] - previous['on_time_rate']):+.1%} points",
            f"- Cancellation rate: {(latest['cancellation_rate'] - previous['cancellation_rate']):+.1%} points",
            f"- Average delivery duration: {(latest['avg_delivery_min'] - previous['avg_delivery_min']):+.1f} minutes",
        ]
    lines += ["", "## Follow-up", "- Validate unusual changes and assign an owner before escalating.", ""]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report written to: {OUT}")
    print("\n".join(lines))

if __name__ == "__main__":
    main()
