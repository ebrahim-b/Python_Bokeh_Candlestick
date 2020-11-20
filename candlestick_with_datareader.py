from math import pi
import pandas as pd
from pandas_datareader import data, wb
import datetime
from bokeh.plotting import figure, show, output_file

symbol = 'AAPL'


start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2016, 1, 1)

df = data.DataReader(name=symbol,data_source="yahoo",start=start,end=end)


inc = df.Close > df.Open
dec = df.Open > df.Close
w = 12*60*60*1000 #half day in milliseconds

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title="AAPL Candlestick")

p.segment(df.index, df.High, df.index, df.Low, color="black")
#p.vbar(df.index[inc], w, df.Open[inc], df.Close[inc], color="#32CD32", line_color="green")
#p.vbar(df.index[dec], w, df.Open[dec], df.Close[dec], color="#FF4500", line_color="red")

p.rect(df.index[inc], (df.Open[inc]+df.Close[inc])/2, w,  df.Close[inc]-df.Open[inc], fill_color="green")
p.rect(df.index[dec], (df.Open[dec]+df.Close[dec])/2, w,  df.Open[dec]-df.Close[dec], fill_color="red")

output_file("candlestick_AAPL_With_DataReader.html", title="candlestick_AAPL_With_DataReader example")

show(p)
