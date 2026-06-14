def get_stock_status(stock_level):

    if stock_level <= 0:
        return "ERROR"
    elif stock_level < 10:
        return "LOW STOCK"
    elif 10 <= stock_level <= 30:
        return "OK"
    else:
        return "OVERSTOCK"