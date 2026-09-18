from langchain_core.tools import tool


@tool
def reynolds_number(density, velocity, diameter, viscosity):
    """Calculate the Reynolds number for fluid flow."""
    reynolds = (density * velocity * diameter) / viscosity
    return reynolds


@tool
def heat_duty(mass_flow, heat_capacity, temperature_change):
    """Calculate the heat duty of a flowing fluid."""
    heat_duty = mass_flow * heat_capacity * temperature_change
    return heat_duty


@tool
def pressure_drop(friction_factor, length, diameter, density, velocity):
    """Calculate pressure drop in a pipe using the Darcy-Weisbach equation."""
    pressure_drop = friction_factor * (length / diameter) * (density * velocity**2 / 2)
    return pressure_drop