from src.fetch_data import get_stock_data
from src.database import save_to_db
from src.analysis import basic_analysis
from src.strategy import moving_average_strategy
from src.visualize import plot_data

ticker = "AAPL"

data = get_stock_data(ticker)

save_to_db(data, "AAPL_data")

analysis = basic_analysis(data)
print(analysis)

data = moving_average_strategy(data)

plot_data(data)

print("Project executed successfully!")
