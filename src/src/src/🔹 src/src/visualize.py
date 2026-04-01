import matplotlib.pyplot as plt

def plot_data(df):
    plt.plot(df['Close'])
    plt.title("Stock Price Trend")
    plt.savefig("outputs/stock_plot.png")
    plt.close()
