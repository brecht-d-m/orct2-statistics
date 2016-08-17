import plotly
import plotly.graph_objs as go
import os
import pandas as pd

count_data = pd.read_csv("orct2_statistics.csv", header=0)
count_data["timestamp"] = pd.to_datetime(count_data["timestamp"])

def _plot(data, title, yaxis_title, filename):

    layout = go.Layout(
        title=title,
        yaxis=dict(title=yaxis_title),
        xaxis=dict(title="Timestamp of commit", rangeslider=dict(), type='date')
    )

    fig = go.Figure(data=data, layout=layout)

    # plot it for offline editing
    HTMLlink = plotly.offline.plot(fig, show_link=False, auto_open=False)[7:] #remove the junk characters
    # now need to open the HTML file
    with open(HTMLlink, 'r') as file :
        tempHTML = file.read()
    # Replace the target strings
    tempHTML = tempHTML.replace('displayModeBar:!0', 'displayModeBar:!1')
    tempHTML = tempHTML.replace('displaylogo:!0', 'displaylogo:!1')
    tempHTML = tempHTML.replace('modeBarButtonsToRemove:[]', 'modeBarButtonsToRemove:["toImage","sendDataToCloud","zoom2d", "pan2d", "select2d", "lasso2d", "zoomIn2d", "zoomOut2d", "autoScale2d", "resetScale2d", "hoverClosestCartesian", "hoverCompareCartesian"]')

    with open(filename, 'w') as file:
        file.write(tempHTML)
    del tempHTML
    
    os.remove("temp-plot.html")

def plot_all():
    count_global = go.Scatter(
        x=count_data["timestamp"], 
        y=count_data["count_global"],
        name="RCT2_GLOBAL"
    )
    
    count_call = go.Scatter(
        x=count_data["timestamp"], 
        y=count_data["count_call"],
        name="RCT2_CALL"
    )
    
    count_address = go.Scatter(
        x=count_data["timestamp"], 
        y=count_data["count_address"],
        name="RCT2_ADDRESS"
    )
    
    data = [
        count_address,
        count_call,
        count_global
    ]
    
    title = "Scatter plot of RCT2_ADDRESS, RCT2_CALL, and RCT2_GLOBAL occurrences per commit"
    yaxis_title = "Number of occurrences"
    filename = "orct2_graph.html"
    
    _plot(data, title, yaxis_title, filename)
    
def plot_global():
    data = [
        go.Scatter(x=count_data["timestamp"], y=count_data["count_global"])
    ]
    
    _plot(data, "Scatter plot of RCT2_GLOBAL occurrences per commit", "Number of occurrences", "graph_orct2_global.html")

def plot_address():
    data = [
        go.Scatter(x=count_data["timestamp"], y=count_data["count_address"])
    ]
    
    _plot(data, "Scatter plot of RCT2_ADDRESS occurrences per commit", "Number of occurrences", "graph_orct2_address.html")

def plot_call():
    data = [
        go.Scatter(x=count_data["timestamp"], y=count_data["count_call"])
    ]
    
    _plot(data, "Scatter plot of RCT2_CALL occurrences per commit", "Number of occurrences", "graph_orct2_call.html")

plot_global()
plot_address()
plot_call()
plot_all()