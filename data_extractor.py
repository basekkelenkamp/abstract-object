from pprint import pprint

def cal_average(num):
    sum_num = sum(num)
    return sum_num / len(num)


def most_common_val(li):
    return max(set(li), key=li.count)


all_data_keys = ['co2', 'humidity', 'temperature', 'pressure', 'pm2_5', 'pm10', 'voc', 'noise']


class DataExtractor:
    def __init__(self, data: dict, data_keys: list = None):
        self.raw_data = data['data']
        self.data_keys = [key.lower() for key in data_keys if key.lower() in all_data_keys]
        self.start_time = data.get('start_time')
        self.end_time = data.get('end_time')
        self.current_time = None
        self.latest_raw_data = None
        self.data = []
        self.latest_data = []

        self.averages = [
            {key: {"3_hours_ago": None, "2_hours_ago": None, "1_hours_ago": None, }} for key in self.data_keys
        ]

        self.extract_data()

    def extract_data(self):
        for item in self.raw_data:
            for data in item['sensors']:
                if data['key'].lower() in self.data_keys:
                    self.data.append({
                        data['key']: data['value'],
                        'time': item['time']
                    })

    def save_latest_data(self, latest_data):
        self.latest_raw_data = latest_data['data']
        self.current_time = latest_data['data']['time']

        for data in self.latest_raw_data['sensors']:
            if data['key'].lower() in self.data_keys:
                self.latest_data.append({data['key']: data['value']})

