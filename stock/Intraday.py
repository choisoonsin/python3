"""
    일중강도율 + 볼린저밴드
    매수: 주가가 하단 밴드 부근에서 W형 패턴을 나타내고, 강세지표가 확증할 때 매수(%b가 0.05보다 작고 II%가 0보다 크면 매수)
    매도: 상단 밴드 부근에서 일련의 주가 태그가 일어나며, 약세지표가 확증할 때 매도(%b가 0.95보다 크고 II%가 0보다 작으면 배도)

    일중강도
    II는 트레이더들의 움직임을 나타내는데, 종가가 거래 범위 천정권에서 형성되면 1, 중간에서 형성되면 0, 바닥권에서 형성되면 -1이다.
"""
import matplotlib.pyplot as plt
import pandas_datareader as web

df = web.naver.NaverDailyReader('000660', start='20181101').read().astype(int)

print(df.tail(5))

df['MA20'] = df['Close'].rolling(window=20).mean()
df['stddev'] = df['Close'].rolling(window=20).std()
df['upper'] = df['MA20'] + ( df['stddev'] * 2 )
df['lower'] = df['MA20'] - ( df['stddev'] * 2 )
df['PB'] = (df['Close'] - df['lower']) / (df['upper'] - df['lower'])

df['II'] = ( 2 * df.Close - df.High - df.Low ) / ( df.High - df.Low ) * df.Volume
df['IIP21'] = df['II'].rolling(window=21).sum() / df['Volume'].rolling(window=21).sum() * 100

print(df.tail(10))

plt.figure(figsize=(9, 9))
plt.subplot(3, 1, 1)
plt.title('SK Hynix Bollinger Band(20 day, 2 std) - Reversals')
plt.plot(df.index, df['Close'], 'b', label='Close')
plt.plot(df.index, df['upper'], 'r--', label='Upper band')
plt.plot(df.index, df['MA20'], 'k--', label='Moving average 20')
plt.plot(df.index, df['lower'], 'c--', label='Lower band')
plt.fill_between(df.index, df['upper'], df['lower'], color='0.9')
for i in range(0, len(df['Close'])):
    if df.PB.values[i] < 0.05 and df.IIP21.values[i] > 0:
        plt.plot(df.index.values[i], df.Close.values[i], 'r^')
    elif df.PB.values[i] > 0.95 and df.IIP21.values[i] < 0:
        plt.plot(df.index.values[i], df.Close.values[i], 'bv')

plt.legend(loc='best')
plt.subplot(3, 1, 2)
plt.plot(df.index, df['PB'], 'b', label='%b')
plt.grid(True)
plt.legend(loc='best')

plt.subplot(3, 1, 3)
plt.bar(df.index, df['IIP21'], color='g', label='II% 21day')
for i in range(0, len(df['Close'])):
    if df.PB.values[i] < 0.05 and df.IIP21.values[i] > 0:
        plt.plot(df.index.values[i], 0, 'r^')
    elif df.PB.values[i] > 0.95 and df.IIP21.values[i] < 0:
        plt.plot(df.index.values[i], 0, 'bv')
plt.grid(True)
plt.legend(loc='best')
plt.show()




