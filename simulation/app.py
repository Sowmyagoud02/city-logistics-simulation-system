import streamlit as st
import pandas as pd
import io

# <-- NEW: All data comes from the API now
from api_client.client import (
    get_summary,
    get_all_deliveries,
    get_delivery_by_id,
    get_deliveries_by_driver,
    simulate_new_delivery,
    filter_deliveries,
    simulate_batch
)

st.title("City Logistics Simulation Dashboard")
page = st.sidebar.selectbox("Navigation", ["Home", "Analytics Summary", "Visualizations", "Raw Data", "Simulate Delivery", "Filters","Batch Simulation"])

# -----------------------------
# HOME PAGE
# -----------------------------
if page == "Home":
    st.header("📦 Welcome to the City Logistics Simulation System")

    st.write("""
    This dashboard is powered by a real API connected to a discrete-event simulation.
    Explore performance, delays, routes, and driver statistics generated dynamically.
    """)

    st.subheader("✨ What You Can Do Here")
    st.markdown("""
    - View high-level analytics  
    - Explore interactive visualizations  
    - Inspect the raw delivery logs  
    - Trigger new delivery simulations  
    """)

    st.info("The dashboard communicates with the FastAPI backend using API calls.")


# -----------------------------
# ANALYTICS SUMMARY PAGE
# -----------------------------
elif page == "Analytics Summary":
    st.header("📊 Analytics Summary")

    with st.spinner("Connecting to backend…"):
        wake_backend()

        try:
            summary = get_summary()
        except BackendUnavailable:
            st.warning("⏳ Backend is waking up. Please wait 10–15 seconds and refresh.")
            st.stop()

    # Top metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Travel Time (mins)", round(summary["avg_travel_time"], 2))
    col2.metric("Avg Delay (mins)", round(summary["avg_delay"], 2))
    col3.metric("Delay Rate (%)", f"{round(summary['delay_rate'], 2)}%")

    st.subheader("🚚 Route & Delivery Insights")

    busiest = summary["busiest_route"]
    st.write(f"**Busiest Route:** {busiest['route']} ({busiest['count']} deliveries)")

    fastest = summary["fastest_delivery"]
    st.write(f"**Fastest Delivery:** ID {fastest['delivery_id']} — {round(fastest['travel_time_minutes'], 2)} mins")

    slowest = summary["slowest_delivery"]
    st.write(f"**Slowest Delivery:** ID {slowest['delivery_id']} — {round(slowest['travel_time_minutes'], 2)} mins")

    st.subheader("🧑‍🔧 Driver Performance (Avg Travel Time)")

    df = pd.DataFrame(summary["driver_performance"])
    df["travel_time_minutes"] = df["travel_time_minutes"].round(2)

    st.dataframe(
        df.style.highlight_min("travel_time_minutes", color="lightgreen")
              .highlight_max("travel_time_minutes", color="pink")
    )


# -----------------------------
# VISUALIZATIONS PAGE
# -----------------------------
elif page == "Visualizations":
    st.header("📊 Visual Dashboard")

    st.write("All visualizations below are generated live from API data.")

    deliveries = get_all_deliveries()

    if deliveries:
        df = pd.DataFrame(deliveries)

        import matplotlib.pyplot as plt

        # Histogram
        fig, ax = plt.subplots()
        ax.hist(df["travel_time_minutes"], bins=10, edgecolor="black")
        ax.set_title("Travel Time Distribution")
        st.pyplot(fig)

        # Delay Reason Bar Chart
        fig, ax = plt.subplots()
        delay_counts = df["delay_reason"].value_counts()
        ax.bar(delay_counts.index, delay_counts.values)
        ax.set_title("Delay Reason Frequency")
        st.pyplot(fig)

    else:
        st.warning("No deliveries found.")


# -----------------------------
# RAW DATA PAGE
# -----------------------------
elif page == "Raw Data":
    st.header("📄 Raw Delivery Data")

    deliveries = get_all_deliveries()
    df = pd.DataFrame(deliveries)

    st.dataframe(df, use_container_width=True)

    # CSV download
    csv_data = df.to_csv(index=False)
    st.download_button("Download CSV", csv_data, "deliveries.csv", "text/csv")

    # Excel download
    excel_buffer = io.BytesIO()
    df.to_excel(excel_buffer, index=False, engine="xlsxwriter")
    excel_buffer.seek(0)
    st.download_button(
        "Download Excel", 
        excel_buffer, 
        "deliveries.xlsx", 
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    # JSON download
    json_data = df.to_json()
    st.download_button("Download JSON", json_data, "deliveries.json", "application/json")


# -----------------------------
# SIMULATE NEW DELIVERY PAGE
# -----------------------------
elif page == "Simulate Delivery":
    st.header("🚀 Generate New Delivery")

    st.write("Trigger the simulation engine to create one new delivery and save it to the database.")

    if st.button("Generate Delivery"):
        response = simulate_new_delivery()
        st.success("New delivery generated successfully!")
        st.json(response)

# ---------------------------------
# ADD FILTERS OPTION
# ---------------------------------
elif page == "Filters":
    st.header("🔍 Filter Deliveries")

    st.write("Use the controls below to filter deliveries using the API.")

    # ---inputs----
    driver_id = st.number_input("Driver ID (optional)", min_value=1, max_value=20, step=1, value=1)
    apply_driver = st.checkbox("Filter by Driver ID", value=False)

    route_type = st.selectbox(
        "Route Type (optional)",
        ["", "city_center", "suburbs", "industrial", "rural"]
    )

    min_time = st.number_input("Min Travel Time (mins)", min_value=0.0, value=0.0)
    max_time = st.number_input("Max Travel Time (mins)", min_value=0.0, value=0.0)

    if st.button("Apply Filters"):
        with st.spinner("Fetching filtered results..."):
            result = filter_deliveries(
                driver_id=driver_id if apply_driver else None,
                route_type=route_type if route_type != "" else None,
                min_time=min_time if min_time > 0 else None,
                max_time=max_time if max_time > 0 else None
            )

        if not result:
            st.warning("No deliveries found with selected filters.")
        else:
            df = pd.DataFrame(result)
            st.success(f"Found {len(df)} matching deliveries.")
            st.dataframe(df, use_container_width=True)

            import matplotlib.pyplot as plt

            # -------------------- TRAVEL TIME HISTOGRAM --------------------
            st.subheader("⏱ Travel Time Distribution")
            fig1, ax1 = plt.subplots()
            ax1.hist(df["travel_time_minutes"], bins=10, edgecolor="black")
            ax1.set_xlabel("Travel Time (mins)")
            ax1.set_ylabel("Count")
            st.pyplot(fig1)

            # -------------------- DELAY REASON BAR CHART --------------------
            st.subheader("⚠ Delay Reason Frequency")
            if df["delay_reason"].notna().any():
                fig2, ax2 = plt.subplots()
                delay_counts = df["delay_reason"].value_counts()
                ax2.bar(delay_counts.index, delay_counts.values)
                ax2.set_ylabel("Count")
                st.pyplot(fig2)
            else:
                st.info("No delays in filtered results.")

            # -------------------- ROUTE TYPE PIE CHART --------------------
            st.subheader("🛣 Route Type Breakdown")
            fig3, ax3 = plt.subplots()
            route_counts = df["route_type"].value_counts()
            ax3.pie(route_counts.values, labels=route_counts.index, autopct="%1.1f%%")
            st.pyplot(fig3)

# ----------------------------
# Batch simulation 
# --------------------------------

elif page == "Batch Simulation":
    st.header("🚀 Run Batch Simulation")
    count = st.slider("Number of deliveries to generate:", 10, 500, 50)

    if st.button("Run Batch Simulation"):
        response = simulate_batch(count)
        st.success(f"{response['total']} deliveries generated!")
        st.json(response)
