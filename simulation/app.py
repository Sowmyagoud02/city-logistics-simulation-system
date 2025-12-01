import os
import sqlite3
import streamlit as st
import pandas as pd
import io
from dashboard import *
from analytics import *

st.title("City Logistics Simulation Dashboard")
page = st.sidebar.selectbox("Navigation", ["Home", "Analytics Summary", "Visualizations", "Raw Data"])

#home
if page == "Home":
    st.header("📦 Welcome to the City Logistics Simulation System")

    st.write("""
    This dashboard is part of a complete end-to-end simulation project that models a real-world  
    last-mile logistics network (like Amazon, DHL, FedEx).  
    Explore delivery performance, delays, routes, and driver behavior with interactive analytics.
    """)

    st.subheader("✨ What You Can Do Here")
    st.markdown("""
    - View high-level analytics (average delay, busiest route, fastest delivery, etc.)
    - Explore interactive visualizations of simulation data  
    - Inspect the raw SQLite delivery logs  
    - Understand system performance through multiple metrics
    """)

    st.subheader("🧭 How to Navigate")
    st.markdown("""
    Use the sidebar to switch between:
    - **Analytics Summary** → Key metrics  
    - **Visualizations** → Graphs & plots  
    - **Raw Data** → Full delivery table  
    """)

    st.info("This dashboard uses data generated from the simulation engine and stored in the SQLite database.")

#analytics summary page
elif page == "Analytics Summary":
    st.header("📊 Analytics Summary")

    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Travel Time (mins)", f"{average_travel_time()}")
    col2.metric("Avg Delay (mins)", f"{average_delay():.2f}")
    col3.metric("Delay Rate (%)", f"{delay_rate():.2f}%")

    st.subheader("🚚 Route & Delivery Insights")
    busiest = get_busiest_route()[0]
    fastest = fastest_delivery()[0]
    slowest = slowest_delivery()[0]
    st.write(f"**Busiest Route:** {busiest[0]} ({busiest[1]} deliveries)")
    st.write(f"**Fastest Delivery:** ID {fastest[0]} — {fastest[1]:.2f} mins")
    st.write(f"**Slowest Delivery:** ID {slowest[0]} — {slowest[1]:.2f} mins")

    st.subheader("🧑‍🔧 Driver Performance (Avg Travel Time)")

    driver_stats = get_driver_performace()

    # Convert to a DataFrame
    df = pd.DataFrame(driver_stats, columns=["Driver ID", "Avg Travel Time (mins)"])
    # print(df)
    # Proper formatting (2 decimal places)
    df["Avg Travel Time (mins)"] = df["Avg Travel Time (mins)"].round(2)

    # st.dataframe(df, use_container_width=True)
    st.dataframe(df.style.highlight_min(subset=["Avg Travel Time (mins)"], color="lightgreen")
                   .highlight_max(subset=["Avg Travel Time (mins)"], color="pink"))

#visualiztion page
elif page == "Visualizations":
    st.header("📊 Visual Dashboard")
    st.write("Explore delivery patterns with the plots below.")
    figures = generate_all_plots()
    st.pyplot(figures)

else:
    st.header("📄 Raw Delivery Data")
    st.write("Below is the full dataset from the SQLite database")
    data = load_deliveries()
    df = pd.DataFrame(data, columns = ["delivery_id", "driver_id", "route_type", "distance", "start_time", 
    "travel_time_minutes", "delay_minutes", "delay_reason", "end_time"])
    st.dataframe(df, use_container_width = True)

    #create download buttons for csv
    csv_data = df.to_csv(index = False)
    st.download_button(label = "Download CSV",
                        data = csv_data,
                        file_name = "deliveries.csv",
                        mime = "text/csv")

    #create download buttons for csv
    excel_data = io.BytesIO()
    df.to_excel(excel_data, index = False, engine="xlsxwriter")
    excel_data.seek(0)
    st.download_button(label = "Download excel",
                        data = excel_data,
                        file_name = "deliveries.xlsx",
                        mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    #create download buttons for json

    json_data = df.to_json()
    st.download_button(label = "Download json",
                        data = json_data,
                        file_name = "deliveries.json",
                        mime = "application/json")