import pandas_datareader as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stocks = ['005930', '000660', '005380', '035420']

df = pd.DataFrame()
for stock in stocks:
    df[stock] = web.naver.NaverDailyReader(stock, start='20160104' , end='20180427').read()['Close'].astype(int)


daily_ret = df.pct_change() # 일간변동율 -> 다음일시세 / 전일시세 - 1
annual_ret = daily_ret.mean() * 252 # 연간 수익률 -> 일간 변동율의 평균값에 252 ( 1년 평균 개장 일 )를 곱한 값
daily_cov = daily_ret.cov() # 일간변동율의 공분산
annual_cov = daily_cov * 252 # 연간수익률의 공분산

print(annual_cov)

port_ret = []
port_risk = []
port_weights = []
sharpe_ratio = []

for _ in range(20000): # for 안에서 반복횟수를 사용할 일이 없다면 관습적으로 _ 변수에 할당한다.
    # 4개의 랜덤 숫자로 구성된 배열 생성
    weights = np.random.random(len(stocks))
    # 위에서 구한 4개의 랜덤 숫자를 랜덤 숫자의 총합으로 나눠 4종목의 비중의 합이 1이 되도록 조정한다.
    weights /= np.sum(weights)

    returns = np.dot(weights, annual_ret)
    risk = np.sqrt(np.dot(weights.T, np.dot(annual_cov, weights)))

    port_ret.append(returns)
    port_risk.append(risk)
    port_weights.append(weights)
    sharpe_ratio.append(returns/risk)

portfolio = {'Returns': port_ret, 'Risk': port_risk, 'Sharpe': sharpe_ratio}
for i, s in enumerate(stocks):
    portfolio[s] = [weight[i] for weight in port_weights]

df = pd.DataFrame(portfolio)
df = df[['Returns', 'Risk', 'Sharpe'] + [s for s in stocks]]

max_sharpe = df.loc[df['Sharpe'] == df['Sharpe'].max()]
min_risk = df.loc[df['Risk'] == df['Risk'].min()]

print(max_sharpe)
print(min_risk)

df.plot.scatter(x='Risk', y='Returns', c='Sharpe', cmap='viridis', edgecolors='k', figsize=(11, 7), grid=True)
plt.scatter(x=max_sharpe['Risk'], y=max_sharpe['Returns'], c='r', marker='*', s=300)
plt.scatter(x=min_risk['Risk'], y=min_risk['Returns'], c='r', marker='X', s=200)
plt.show()