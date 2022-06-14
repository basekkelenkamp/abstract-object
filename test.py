from data_extractor import DataExtractor

# /data endpoint response
response = {'data': [], 'start_time': '2022-06-10T07:26:15.821779', 'end_time': '2022-06-10T10:26:15.821779'}

# /latest endpoint response
response_latest = {
    'data': {'box_id': 'testid0987654321'},
    'sensors': [
        {'co2': 550},
        {'pm10': 4},
        {'audio': 54.84664},
        {'pm2_5': 3},
        {'bme_temp': 22.81},
        {'bme_humidity': 53.528},
        {'visible_light': 328},
    ],
    'status': "Excellent",
    'time': '2022-06-08T13:26+00:00'
}

extractor = DataExtractor(response, ['CO2'])
print(extractor.__dict__)

breakpoint()
