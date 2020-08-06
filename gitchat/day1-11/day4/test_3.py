from random import uniform
from pyecharts.charts import Scatter
import pyecharts.options as opts


def draw_uniform_points():
    x,y=[i for i in range(100)],[round(uniform(0,10),2) for _ in range(100)]
    c=(Scatter().add_xaxis(x).add_yaxis('y',y))
    c.render()
draw_uniform_points()