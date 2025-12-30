import pandas as pd

INPUT_CSV = "data/input/test_traffic.csv"
OUTPUT_CSV = "data/input/test_traffic_200.csv"

TOTAL_ROWS = 200        
ANOMALY_RATIO = 0.25    

df = pd.read_csv(INPUT_CSV)

traffic_score = df.sum(axis=1)

df_scored = df.copy()
df_scored["score"] = traffic_score

df_sorted = df_scored.sort_values("score")

normal_count = int(TOTAL_ROWS * (1 - ANOMALY_RATIO))
anomaly_count = TOTAL_ROWS - normal_count

normal_samples = df_sorted.head(normal_count)
anomaly_samples = df_sorted.tail(anomaly_count)

final_df = pd.concat([normal_samples, anomaly_samples]) \
              .sample(frac=1, random_state=42) \
              .drop(columns=["score"])

final_df.to_csv(OUTPUT_CSV, index=False)

print("Reduced CSV created")
print(f"   File: {OUTPUT_CSV}")
