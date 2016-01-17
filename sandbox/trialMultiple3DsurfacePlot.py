import plotly
from plotly.graph_objs import Surface

z1 = [
    [1, 2, 3],
    [],
    [2, 4, 6],
    [3, 6, 9]
]

z2 = [[zij+1 for zij in zi] for zi in z1]
z3 = [[zij-1 for zij in zi] for zi in z1]

plotly.offline.plot([
    dict(z=z1, type='surface'),
    dict(z=z2, showscale=False, opacity=0.9, type='surface'),
    dict(z=z3, showscale=False, opacity=0.9, type='surface')],
    filename='python-docs/multiple-surfaces')
