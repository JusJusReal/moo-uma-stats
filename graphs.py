import pandas as pd
import matplotlib.pyplot as plt
import re

from colors import Horse as horse
from colors import RunnerType as runner_type

def read_file(csv_path):
    # chat gpt lol
    df = pd.read_csv(csv_path, skip_blank_lines=True).dropna(how='all')
    df = df.rename(columns=df.iloc[0]).drop(df.index[0]).reset_index(drop=True)
    df.columns = pd.io.common.dedup_names(df.columns, is_potential_multiindex=False)
    df = df.dropna(subset=['Status'])

    
    # Get main colors by name
    main_color_map = {h.name.replace('_', ' '): h.main_color for h in horse}
    
    # Combine all the values in x, y, z into one column
    df["Uma"] = df[["Uma 1", "Uma 2", "Uma 3"]].values.tolist()
    df["Role"] = df[["Role", "Role.1", "Role.2"]].values.tolist()
    df["Running Style"] = df[["Running Style", "Running Style.1", "Running Style.2"]].values.tolist()

    # The new format of the df after explosion
    df = df[["Player IGN", "Status", "Uma", "Role", "Running Style", "No. of Wins","No. of Games", "R1D1 WR%"]]

    # Turn the comma-seperated values into new rows based off the list we made previously
    df = df.explode(["Uma", "Role", "Running Style"])

    search(df, uma='GOLD SHIP', running_style='FRONT RUNNER')

def count_umas(df_long):
    style_counts = df_long.groupby(["Uma", "Running Style"]).size().unstack(fill_value=0)

    # Plot stacked bar, sorted by total count using sum(axis=1) + sort_values + loc
    style_counts = style_counts.loc[style_counts.sum(axis=1).sort_values(ascending=False).index]

    # Define desired stacking order (bottom → top)
    desired_order = ["FRONT RUNNER", "PACE CHASER", "LATE SURGER", "END CLOSER"]

    # Keep only styles that exist in the data
    columns_in_data = [col for col in desired_order if col in style_counts.columns]

    # Reorder columns to control stack order
    style_counts = style_counts[columns_in_data]

    style_counts.plot(kind="bar", stacked=True, figsize=(12,6), colormap="tab20")
    
    plt.title("Stacked Bar Chart of Running Styles per Uma")
    plt.xlabel("Uma")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.legend(title="Running Style")
    plt.tight_layout()
    plt.show()

def count_role(df_long):
    counts = df_long["Role"].value_counts()

    plt.figure(figsize=(12,6))
    counts.plot(kind="bar")  # use kind="bar" for categorical counts
    plt.title("Histogram of Uma Appearances")
    plt.xlabel("Uma")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.show()

def count_running_style(df_long):
    counts = df_long["Running Style"].value_counts()

    plt.figure(figsize=(12,6))
    counts.plot(kind="bar")  # use kind="bar" for categorical counts
    plt.title("Histogram of Uma Appearances")
    plt.xlabel("Uma")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.show()

def search(df, player_ign="", status="", uma="", role="", running_style=""):
    # Build a dictionary of criteria only for non-empty arguments
    criteria = {}
    if player_ign:
        criteria["Player IGN"] = player_ign
    if status:
        criteria["Status"] = status
    if uma:
        criteria["Uma"] = uma
    if role:
        criteria["Role"] = role
    if running_style:
        criteria["Running Style"] = running_style

    # Start with a mask of all True
    mask = pd.Series(True, index=df.index)
    for col, val in criteria.items():
        mask &= df[col] == val

    # Filter the DataFrame
    filtered_df = df[mask]

    print(filtered_df)

    return filtered_df