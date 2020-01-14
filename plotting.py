from motion_detection import df # make available DataFrame from motion_detectoin in this file
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_str"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_str"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S") 

cds = ColumnDataSource(df)

p = figure(x_axis_type = 'datetime', height = 300, width = 600,  title = 'Motion Graph')
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start", "@Start_str"), ("End", "@End_str")])
p.add_tools(hover)

q = p.quad(left="Start", right = "End", top = 1, bottom = 0, color = "green", source = cds)

output_file("Graph.html")
show(p)