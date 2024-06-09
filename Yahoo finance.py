import yfinance as yf
import matplotlib.pyplot as plt

# url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"
# response = requests.get(url)
# with open('apple.json', 'wb') as f:
#     f.write(response.content)

# with open('apple.json') as json_file:
#     apple_info = json.load(json_file)
#     print("Type:", type(apple_info))
#     print(apple_info)

# apple = yf.Ticker("NVDA")
# apple_share_price_data = apple.history(period="max")
# print(apple_share_price_data)
# print(apple_share_price_data.head())
try:
    apple = yf.Ticker("AAPL")
    apple_share_price_data = apple.history(period="180d")
    print(apple_share_price_data)
except Exception as e:
    print(f"Error fetching data for AAPL: {e}")

plt.figure(figsize=(10, 6))
plt.plot(apple_share_price_data['Open'], label='Apple Open Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Apple Stock Price (Open)')
plt.legend()
plt.show()

apple_dividends = apple.dividends
print(apple_dividends)

plt.figure(figsize=(10, 6))
plt.plot(apple_dividends, marker='o', linestyle='-', color='b')
plt.xlabel('Date')
plt.ylabel('Dividend Amount')
plt.title('Apple Dividends')
plt.grid(True)
plt.show()
