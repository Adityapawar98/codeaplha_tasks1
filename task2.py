class Stock:
    def __init__(self, symbol, quantity, purchase_price, current_price):
        self.symbol = symbol.upper()
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.current_price = current_price

    def market_value(self):
        return self.quantity * self.current_price

    def profit_loss(self):
        return (self.current_price - self.purchase_price) * self.quantity

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity, purchase_price, current_price):
        symbol = symbol.upper()
        if symbol in self.stocks:
            print(f"Updating {symbol}: Adding {quantity} shares.")
            existing = self.stocks[symbol]
            total_quantity = existing.quantity + quantity
            avg_price = ((existing.quantity * existing.purchase_price) + (quantity * purchase_price)) / total_quantity
            existing.quantity = total_quantity
            existing.purchase_price = avg_price
            existing.current_price = current_price
        else:
            self.stocks[symbol] = Stock(symbol, quantity, purchase_price, current_price)
        print(f"Added/Updated stock: {symbol}")

    def remove_stock(self, symbol):
        symbol = symbol.upper()
        if symbol in self.stocks:
            del self.stocks[symbol]
            print(f"Removed {symbol} from portfolio.")
        else:
            print(f"{symbol} not found in portfolio.")

    def update_price(self, symbol, new_price):
        symbol = symbol.upper()
        if symbol in self.stocks:
            self.stocks[symbol].current_price = new_price
            print(f"Updated {symbol} current price to ${new_price:.2f}")
        else:
            print(f"{symbol} not found in portfolio.")

    def view_portfolio(self):
        total_value = 0
        total_pl = 0
        print("\nYour Portfolio:")
        print(f"{'Symbol':<10}{'Qty':<8}{'Buy Price':<12}{'Current':<12}{'Value':<12}{'P/L':<12}")
        print("-" * 66)

        for stock in self.stocks.values():
            value = stock.market_value()
            pl = stock.profit_loss()
            total_value += value
            total_pl += pl
            print(f"{stock.symbol:<10}{stock.quantity:<8}{stock.purchase_price:<12.2f}"
                  f"{stock.current_price:<12.2f}{value:<12.2f}{pl:<12.2f}")

        print("-" * 66)
        print(f"{'Total':<42}{total_value:<12.2f}{total_pl:<12.2f}\n")

def main():
    portfolio = Portfolio()

    while True:
        print("\n--- Stock Portfolio Tracker ---")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Update Current Price")
        print("4. View Portfolio")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            symbol = input("Enter stock symbol: ").strip()
            quantity = int(input("Enter quantity: ").strip())
            buy_price = float(input("Enter purchase price: ").strip())
            current_price = float(input("Enter current price: ").strip())
            portfolio.add_stock(symbol, quantity, buy_price, current_price)

        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").strip()
            portfolio.remove_stock(symbol)

        elif choice == '3':
            symbol = input("Enter stock symbol to update: ").strip()
            new_price = float(input("Enter new current price: ").strip())
            portfolio.update_price(symbol, new_price)

        elif choice == '4':
            portfolio.view_portfolio()

        elif choice == '5':
            print("Exiting Portfolio Tracker.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
