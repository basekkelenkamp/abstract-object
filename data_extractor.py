
def cal_average(num):
    sum_num = sum(num)
    return sum_num / len(num)


def most_common_val(li):
    return max(set(li), key=li.count)


all_data_keys = ['co2', 'humidity', 'temperature', 'pressure', 'pm2.5', 'pm10', 'voc', 'noise']


class DataExtractor:
    def __init__(self, data: dict, data_keys: list = None):
        self.raw_data = data['data']
        self.data_keys = [key.lower() for key in data_keys if key.lower() in all_data_keys]
        self.start_time = data['start_time']
        self.end_time = data['end_time']

        self.extract_data()

    def extract_data(self):
        print(f"raw data: {self.raw_data}")

