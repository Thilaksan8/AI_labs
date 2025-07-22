def smartCarTrade(prices):
    min_loss = float('inf')
    n = len(prices)
    
    # Create list of (price, year) pairs
    price_year = [(price, i) for i, price in enumerate(prices)]
    # Sort by price ascending
    price_year.sort(key=lambda x: x[0])
    
    # Check consecutive prices in sorted order
    for i in range(n - 1):
        price1, year1 = price_year[i]
        price2, year2 = price_year[i + 1]
        
        # buy year should be earlier than sell year
        if year1 > year2:
            loss = price2 - price1
            if 0 < loss < min_loss:
                min_loss = loss

    return min_loss
result = smartCarTrade([10000, 8000, 12000, 7000, 9000])
print(result)