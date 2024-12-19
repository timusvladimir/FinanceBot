import pandas as pd
import requests
from matplotlib import pyplot as plt

import requests
print(requests.get('https://iss.moex.com/iss/securities.json?q=Yandex').json())


j = requests.get('http://iss.moex.com/iss/engines/stock/markets/shares/securities/YNDX/candles.json?from=2024-05-25&till=2024-06-26&interval=24').json()
data = [{k : r[i] for i, k in enumerate(j['candles']['columns'])} for r in j['candles']['data']]
frame = pd.DataFrame(data)
plt.plot(list(frame['close']))
plt.savefig("shares.png")