import pandas as pd

# Load actual data
df = pd.read_csv("data/flows/clean_flows.csv")

# Drop unwanted columns
df = df.drop(columns=["Label"], errors="ignore")

# Take samples
test_df = df.sample(n=2000, random_state=42)

# Save as input file
test_df.to_csv("data/input/test_traffic.csv", index=False)

print("test_traffic.csv created successfully")
