# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 00:13:31 2024

@author: Abhi1
"""
import pandas as pd
import plotly.graph_objects as go
import numpy as np

data = pd.read_csv('new_data.csv')
data_use = data[['price','area','Price_sqft']]
data_use

train_data = data_use.iloc[0:500]

# Your data
x1 = np.array(train_data['area'])
x2 = np.array(train_data['Price_sqft'])
y1 = [0.16069174734216848 + 471.4525436144296 * i + 1362.0435314903864 * j for i, j in zip(x1, x2)]
y2 = [1.7609253341529016 + 4267.242700454717 * i for i in x1]
y3 = [9002.804967935417 * i - 3749370.5602099495 for i in x1]

# Equation of the specified line
line1_x1 = np.linspace(min(x1), max(x1), 100)
line1_x2 = np.linspace(min(x2), max(x2), 100)
line1_y = 0.16069174734216848 + 471.4525436144296 * line1_x1 + 1362.0435314903864 * line1_x2

# Equation of the second line
line2_y = 1.7609253341529016 + 4267.242700454717 * line1_x1

# Equation of the third line
line3_y = 9002.804967935417 * line1_x1 - 3749370.5602099495

# Create a 3D scatter plot
scatter = go.Scatter3d(x=x1, y=x2, z=y1, mode='markers', marker=dict(size=5), name='Data Points')

# Plot the specified line
line1_trace = go.Scatter3d(x=line1_x1, y=line1_x2, z=line1_y, mode='lines', line=dict(color='red', width=2), name='gradient descent method with variables price, price per square foot and area ')

# Plot the second line
line2_trace = go.Scatter3d(x=line1_x1, y=line1_x2, z=line2_y, mode='lines', line=dict(color='blue', width=2), name='gradient descent method with variables price and area ')

# Plot the third line
line3_trace = go.Scatter3d(x=line1_x1, y=line1_x2, z=line3_y, mode='lines', line=dict(color='green', width=2), name='correlation method with variables price and area ')

# Create layout
layout = go.Layout(
    scene=dict(
        xaxis=dict(title='Area'),
        yaxis=dict(title='Price per sqft'),
        zaxis=dict(title='Price'),
    ),
    title='Interactive 3D Scatter Plot with Regression Lines'
)

# Create figure
fig = go.Figure(data=[scatter, line1_trace, line2_trace, line3_trace], layout=layout)



# Show the interactive plot in full screen
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Fullscreen', method='relayout', args=['fullscreen', True])])])


# Show the interactive plot
fig.show()
