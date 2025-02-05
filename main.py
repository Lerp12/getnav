






from mftool import Mftool
mf = Mftool()
print(mf)

# result = mf.get_available_schemes('ICICI')
# print(result)

# q = mf.get_scheme_quote('119597') # it's ok to use both string or integer as codes.
# print(q)

# mf.get_scheme_details("117865")


# all_scheme_codes = mf.get_scheme_codes() # you can use as_json=True to get all codes in json format
# print(all_scheme_codes)


# data = mf.get_scheme_historical_nav("119597",as_json=True)
# print(data)

# amc_details = mf.get_all_amc_profiles(True)
# print(amc_details)



df = mf.history('0P0000XVAA',start=None,end=None,period='3mo',as_dataframe=True)
print(df.columns)