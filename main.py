# def process_stock_data(stock_data):
#     # Parsing the data
#     stock_dict = {}
#     for item in stock_data:
#         company, value = item.split(':')
#         company = company.strip(" '\"")
#         value = int(value.strip())
#         stock_dict[company] = value
#
#     # Finding min and max
#     min_company = min(stock_dict, key=stock_dict.get)
#     max_company = max(stock_dict, key=stock_dict.get)
#
#     # Sorting the stock data
#     sorted_stock = sorted(stock_dict.items(), key=lambda x: x[1])
#
#     # Output
#     print((stock_dict[min_company], min_company))
#     print((stock_dict[max_company], max_company))
#     print(sorted_stock)
#
# # Example usage
# stock_market = (
#     'AXIS BANK : 7',
#     'BHARTI AIRTEL: 5',
#     'COAL INDIA: 10',
#     'ITC: 1',
#     'TCS: 3',
#     'L&T: 2',
#     'RELIANCE: 9',
#     'KOTAK BANK: 8',
#     'AMERICAN EXPRESS: 11'
# )
#
# process_stock_data(stock_market)