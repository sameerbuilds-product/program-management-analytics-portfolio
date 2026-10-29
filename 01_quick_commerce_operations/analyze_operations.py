from pathlib import Path
import pandas as pd

DATA = Path(__file__).parent / "data" / "orders_synthetic.csv"

def main():
    df = pd.read_csv(DATA)
    df["is_late"] = df["actual_delivery_min"] > df["promised_delivery_min"]
    df["is_cancelled"] = df["status"].eq("cancelled")

    print("\nQUICK COMMERCE OPERATIONS — SYNTHETIC DATA")
    print("=" * 48)
    print(f"Orders: {len(df):,}")
    print(f"Cancellation rate: {df['is_cancelled'].mean():.1%}")
    completed = df[df["status"].eq("delivered")]
    if len(completed):
        print(f"On-time rate among delivered orders: {(completed['actual_delivery_min'] <= completed['promised_delivery_min']).mean():.1%}")
        print(f"Average delivery time: {completed['actual_delivery_min'].mean():.1f} minutes")

    by_store = df.groupby("store_id").agg(
        orders=("order_id", "count"),
        late_rate=("is_late", "mean"),
        cancellation_rate=("is_cancelled", "mean"),
        avg_delivery_min=("actual_delivery_min", "mean")
    ).sort_values(["late_rate", "orders"], ascending=[False, False])

    print("\nStore-level diagnostic (highest late rate first):")
    print(by_store.round(3).to_string())

    by_slot = df.groupby("time_slot").agg(
        orders=("order_id", "count"),
        late_rate=("is_late", "mean"),
        cancellation_rate=("is_cancelled", "mean")
    ).sort_values("late_rate", ascending=False)
    print("\nTime-slot diagnostic:")
    print(by_slot.round(3).to_string())

    print("\nSuggested next step: validate the pattern with dispatch, staffing, and inventory data before choosing an intervention.")

if __name__ == "__main__":
    main()
