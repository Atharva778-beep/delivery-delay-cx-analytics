import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Delivery Delay Dashboard",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = Path(__file__).resolve().parent.parent
EXPORTS = BASE_DIR / "exports"
ACCENT = "#0F766E"
ACCENT_LIGHT = "#14B8A6"

@st.cache_data
def load_csv(name):
    return pd.read_csv(EXPORTS / name)

st.markdown("""
<style>
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 1rem;
}
.main-title {
    font-size: 34px;
    font-weight: 700;
    color: #0F172A;
    margin-bottom: 0.15rem;
}
.sub-title {
    font-size: 15px;
    color: #475569;
    margin-bottom: 1.2rem;
}
.section-title {
    font-size: 22px;
    font-weight: 600;
    color: #0F172A;
    margin-top: 0.5rem;
    margin-bottom: 0.8rem;
}
div[data-testid="metric-container"] {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 2px 8px rgba(15, 23, 42, 0.05);
}
div[data-testid="stDataFrame"] {
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Delivery Delay Analysis Dashboard</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Business dashboard for exploring delivery delay trends across time, location, product categories, and payment types.</div>',
    unsafe_allow_html=True
)

with st.sidebar:
    st.header("Navigation")
    page = st.radio(
        "Select View",
        [
            "Overview",
            "Monthly Trend",
            "State Analysis",
            "City Analysis",
            "Category Analysis",
            "Payment Analysis",
        ]
    )

def style_plot(fig):
    fig.update_layout(
        template="plotly_white",
        title_font_size=22,
        title_font_color="#0F172A",
        plot_bgcolor="white",
        paper_bgcolor="white",
        margin=dict(l=20, r=20, t=60, b=20),
        height=500
    )
    fig.update_xaxes(showgrid=True, gridcolor="#E2E8F0")
    fig.update_yaxes(showgrid=True, gridcolor="#E2E8F0")
    return fig

if page == "Overview":
    st.markdown('<div class="section-title">Executive Overview</div>', unsafe_allow_html=True)

    try:
        month_df = load_csv("delay_by_month.csv")
        total_orders = int(month_df["total_orders"].sum())
        delayed_orders = int(month_df["delayed_orders"].sum())
        avg_delay = float(month_df["delay_percentage"].mean())

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Orders", f"{total_orders:,}")
        col2.metric("Delayed Orders", f"{delayed_orders:,}")
        col3.metric("Average Delay %", f"{avg_delay:.2f}%")

        st.info(
            "Use the sidebar to explore monthly trends, regional delivery issues, city-level delays, "
            "product category performance, and payment-type patterns."
        )

    except Exception as e:
        st.error(f"Could not load overview data: {e}")

elif page == "Monthly Trend":
    st.markdown('<div class="section-title">Monthly Trend</div>', unsafe_allow_html=True)

    df = load_csv("delay_by_month.csv")
    xcol = "order_month" if "order_month" in df.columns else df.columns[0]

    fig = px.line(
        df.sort_values(xcol),
        x=xcol,
        y="delay_percentage",
        markers=True,
        title="Monthly Delivery Delay Trend"
    )
    fig.update_traces(line_color=ACCENT, marker_color=ACCENT_LIGHT, line_width=3)
    fig = style_plot(fig)

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df, use_container_width=True)

elif page == "State Analysis":
    st.markdown('<div class="section-title">State Analysis</div>', unsafe_allow_html=True)

    df = load_csv("delay_by_state.csv").sort_values("delay_percentage", ascending=False)

    fig = px.bar(
        df.sort_values("delay_percentage"),
        x="delay_percentage",
        y="customer_state",
        orientation="h",
        title="Delivery Delay by State",
        color_discrete_sequence=[ACCENT]
    )
    fig = style_plot(fig)

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df, use_container_width=True)

elif page == "City Analysis":
    st.markdown('<div class="section-title">City Analysis</div>', unsafe_allow_html=True)

    df = load_csv("delay_by_city.csv").sort_values("delay_percentage", ascending=False).head(20)

    fig = px.bar(
        df.sort_values("delay_percentage"),
        x="delay_percentage",
        y="customer_city",
        orientation="h",
        title="Top 20 Cities by Delivery Delay",
        color_discrete_sequence=[ACCENT]
    )
    fig = style_plot(fig)

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df, use_container_width=True)

elif page == "Category Analysis":
    st.markdown('<div class="section-title">Category Analysis</div>', unsafe_allow_html=True)

    df = load_csv("delay_by_category.csv").dropna(subset=["product_category_name"])
    df = df.sort_values("delay_percentage", ascending=False).head(20)

    fig = px.bar(
        df.sort_values("delay_percentage"),
        x="delay_percentage",
        y="product_category_name",
        orientation="h",
        title="Top 20 Product Categories by Delivery Delay",
        color_discrete_sequence=[ACCENT]
    )
    fig = style_plot(fig)

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df, use_container_width=True)

elif page == "Payment Analysis":
    st.markdown('<div class="section-title">Payment Analysis</div>', unsafe_allow_html=True)

    df = load_csv("delay_by_payment.csv").sort_values("delay_percentage", ascending=False)

    fig = px.bar(
        df.sort_values("delay_percentage"),
        x="delay_percentage",
        y="payment_type",
        orientation="h",
        title="Delivery Delay by Payment Type",
        color_discrete_sequence=[ACCENT]
    )
    fig = style_plot(fig)

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df, use_container_width=True)