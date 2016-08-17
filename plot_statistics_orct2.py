import plotly
import plotly.graph_objs as go
import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

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
    
    title = "Plot of RCT2_ADDRESS, RCT2_CALL, and RCT2_GLOBAL occurrences per commit"
    yaxis_title = "Number of occurrences"
    filename = "orct2_graph.html"
    
    _plot(data, title, yaxis_title, filename)
    
    # Matplotlib
    plt.figure(figsize=(20,10))
    plt.ylabel('Number of occurrences')
    plt.xlabel('Timestamp of commit')
    plt.title("Plot of RCT2_ADDRESS, RCT2_CALL, and RCT2_GLOBAL occurrences per commit")
    plt.grid(True)
    plt_address, = plt.plot(count_data["timestamp"], count_data["count_address"])
    plt_call, = plt.plot(count_data["timestamp"], count_data["count_call"])
    plt_global, = plt.plot(count_data["timestamp"], count_data["count_global"])
    plt.legend([plt_address, plt_call, plt_global], ["RCT2_ADRESS", "RCT2_CALL", "RCT2_GLOBAL"], loc=2)
    #plt.show()
    plt.savefig("plt_all.pdf")
    plt.savefig("plt_all.png")
    
def _plot_plt(data_x, data_y, title, filename):
    # Matplotlib
    plt.figure(figsize=(20,10))
    plt.ylabel('Number of occurrences')
    plt.xlabel('Timestamp of commit')
    plt.title(title)
    plt.grid(True)
    plt.plot(data_x, data_y)
    #plt.show()
    plt.savefig(filename + ".pdf")
    plt.savefig(filename + ".png")

def plot_global():
    data = [
        go.Scatter(x=count_data["timestamp"], y=count_data["count_global"])
    ]
    
    _plot_plt(count_data["timestamp"], count_data["count_global"], "Plot of RCT2_GLOBAL occurrences per commit", "plt_global")
    _plot(data, "Plot of RCT2_GLOBAL occurrences per commit", "Number of occurrences", "orct2_graph_global.html")

def plot_address():
    data = [
        go.Scatter(x=count_data["timestamp"], y=count_data["count_address"])
    ]
    
    _plot_plt(count_data["timestamp"], count_data["count_address"], "Plot of RCT2_ADDRESS occurrences per commit", "plt_address")
    _plot(data, "Plot of RCT2_ADDRESS occurrences per commit", "Number of occurrences", "orct2_graph_address.html")

def plot_call():
    data = [
        go.Scatter(x=count_data["timestamp"], y=count_data["count_call"])
    ]
    
    _plot_plt(count_data["timestamp"], count_data["count_call"], "Plot of RCT2_CALL occurrences per commit", "plt_call")
    _plot(data, "Plot of RCT2_CALL occurrences per commit", "Number of occurrences", "orct2_graph_call.html")

plot_global()
plot_address()
plot_call()
plot_all()