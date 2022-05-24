import streamlit as st
import plotly.express as px
import plotly.graph_objs as go

def build_simple_line_chart(x_column, y_column, marker_label, title, x_axis, y_axis):
    fig = go.Figure(
        data=go.Scatter(
            x=x_column.astype(dtype=str), 
            y=y_column, 
            text=marker_label
        ))
    fig.update_layout({
        "title": title,
        "xaxis": {"title":x_axis},
        "yaxis": {"title":y_axis}
       })
    return fig

def build_pie_chart(data,values,names,title):
    fig = px.pie(data, values=values,names=names,title=title)
    return fig