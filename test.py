from data_extractor import DataExtractor

response = {'data': [], 'start_time': '2022-06-10T07:26:15.821779', 'end_time': '2022-06-10T10:26:15.821779'}
extractor = DataExtractor(response, ['CO2'])
print(extractor.__dict__)

breakpoint()
