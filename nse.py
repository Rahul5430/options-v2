from nsepython import *
from pprint import pprint

print(indices)
oi_data, ltp, crontime = oi_chain_builder("NIFTY")
print(type(oi_data))
# print(oi_data)
# print(ltp)
# print(crontime)
x = oi_data.to_dict()
print(x)
strike_price = x["Strike Price"]
pprint(strike_price)