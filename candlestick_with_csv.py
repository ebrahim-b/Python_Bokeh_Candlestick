import io
from math import pi
import pandas as pd
from bokeh.plotting import figure, show, output_file

df = pd.read_csv('AAPL.csv') 
df = df[['Date', 'Open', 'High', 'Low', 'Close']] 

df = df[df["Date"] > "2015-01-01"]
df = df[df["Date"] < "2016-01-01"]


df["Date"] = pd.to_datetime(df["Date"])

inc = df.Close > df.Open
dec = df.Open > df.Close
w = 12*60*60*1000

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title= "Candlestick")


p.segment(df.Date, df.High, df.Date, df.Low, color="black")
p.vbar(df.Date[inc], w, df.Open[inc], df.Close[inc], fill_color="#D5E1DD", line_color="green")
p.vbar(df.Date[dec], w, df.Open[dec], df.Close[dec], fill_color="#F2583E", line_color="red")

output_file("candlestick_AAPL.html", title="candlestick_AAPL example")

show(p)