import pandas as pd
import pandas_datareader as web
import plotly.graph_objects as go

df = web.naver.NaverDailyReader('353200', start='20200521').read().astype(int)

print(df)