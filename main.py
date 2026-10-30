import json
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Minecraft Enchantments")

with open("data.json") as f:
    payload = json.load(f)

df = pd.DataFrame(payload["data"])


# Sidebar filters
st.sidebar.header("Filters")
category = st.sidebar.selectbox("Category", ["All"] + sorted(df["category"].unique()))
min_level = st.sidebar.slider("Minimum max level", 1, int(df["maxLevel"].max()), 1)
treasure_only = st.sidebar.checkbox("Treasure enchantments only", value=False)
st.sidebar.caption("Treasure enchantments are those that cannot be obtained from enchanting tables.")

# Apply filters from sidebar
filtered = df[df["maxLevel"] >= min_level]
if category != "All":
    filtered = filtered[filtered["category"] == category]
if treasure_only:
    filtered = filtered[filtered["treasureOnly"]]


filtered = filtered.rename(columns={"weight": "weight (rarity)", "maxLevel": "max level", "versionAdded": "version added", "treasureOnly": "treasure only"})



tables, plots = st.tabs(["Data", "Charts"])

with tables:
    st.subheader("Enchantments")
    st.dataframe(filtered[["name", "category", "max level", "weight (rarity)",
                           "treasure only", "version added"]])
    st.caption(f"{len(filtered)} of {len(df)} enchantments shown")
    st.caption("Greater weight = more common. Lower weight = more rare.")

    # only max level and weight are numeric
    st.dataframe(filtered[["max level", "weight (rarity)"]].describe())
    st.caption("Descriptive Statistics")

with plots:
    if filtered.empty:
        st.warning("No enchantments match these filters.")
    else:
        # a DF that contains each category grouped by whether they are treasured, and, for each group, counts total number of objects inside.
        counts = (filtered.groupby(["category", "treasure only"])
                          .size()
                          .reset_index(name="count"))

        # filter by treasureOnly in bar chart
        counts["source"] = counts["treasure only"].map(
            {True: "Treasure", False: "Obtainable"})
        
        fig1 = px.bar(counts,
                      x="category",
                      y="count",
                      color="source",
                      title="Number of Enchantments per Category",
                      labels={"category": "Category",
                              "count": "Number of Enchantments",
                              "source": "Source"})
        st.plotly_chart(fig1)

        fig2 = px.scatter(filtered,
                          x="weight (rarity)",
                          y="max level",
                          color="category",
                          hover_name="name",
                          title="Enchantment Weight vs Max Level",
                          labels={"weight (rarity)": "Weight (rarity)",
                                  "max level": "Max Level",
                                  "category": "Category"})
        st.plotly_chart(fig2)
        st.caption("Some enchantments overlap, so you may not see every single one.")
