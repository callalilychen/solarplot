import streamlit as st
import plotly.graph_objects as go

# Data
production_kwh_every_month = [0, 7, 80, 109, 117, 116, 130, 136, 83, 51, 20, 5]
consumption_kwh_every_month = [210, 200, 220, 210, 200, 200, 230, 190, 205, 210, 200, 220]
solar_consumption_kwh_every_month = 
solar_module_without_battery = 460  # Initial cost of the solar module
current_price = 0.31  # Price per kWh in euros

def calculate_savings(production, consumption, price, module_cost):
    """
    Calculate the savings and determine profitability.
    """
    index = []
    monthly_savings = []
    cumulative_savings = []
    total_savings = -1 * module_cost
    profitability_year = None

    for year in range(10):
        for month, (prod, cons) in enumerate(zip(production, consumption)):
            saved_kwh = min(prod, cons)  # Only save what is consumed
            monthly_saving = saved_kwh * price
            total_savings += monthly_saving
            monthly_savings.append(monthly_saving)
            cumulative_savings.append(total_savings)
            index.append(month*0.1 + year )

            if profitability_year is None and total_savings >= 0:
                profitability_year = year + 1 + month * 0.1 + 0.1  # Year starts from 1

    return index, monthly_savings, cumulative_savings, profitability_year

def plot_savings(years, cumulative_savings, module_cost, profitability_year):
    """
    Plot cumulative savings over the years and mark profitability.
    """
    fig = go.Figure()

    # Add cumulative savings
    fig.add_trace(go.Scatter(
        x=years,
        y=cumulative_savings,
        mode='lines',
        name="Cumulative Savings (€)",
        line=dict(color='green')
    ))

    # Add cost line
    fig.add_trace(go.Scatter(
        x=[1],
        y=[-1 * module_cost],
        mode='markers+text',
        name="Module Cost (€)",
        line=dict(color='red', dash='dash')
    ))

    # Add profitability annotation
    if profitability_year:
        fig.add_trace(go.Scatter(
            x=[profitability_year],
            y=[0],
            mode='markers+text',
            text=["Profitability Achieved"],
            textposition="top center",
            marker=dict(color='blue', size=10)
        ))

    fig.update_layout(
        title="Photovoltaic Module Profitability",
        xaxis_title="Year",
        yaxis_title="Amount (€)",
        legend_title="Legend",
        template="plotly_white"
    )
    return fig

def main():
    st.write("Calculate savings and profitability for a photovoltaic module over 10 years.")

    # Perform calculations
    index, monthly_savings, cumulative_savings, profitability_year = calculate_savings(
        production_kwh_every_year, consumption_kwh_every_year, current_price, solar_module_without_battery
    )

    # Display results
    st.write(f"Initial module cost: €{solar_module_without_battery}")
    st.write(f"Price per kWh: €{current_price:.2f}")
    if profitability_year:
        st.write(f"The module becomes profitable in year {profitability_year}.")
    else:
        st.write("The module does not become profitable within the given time frame.")

    # Plot and display
    fig = plot_savings(index, cumulative_savings, solar_module_without_battery, profitability_year)
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
