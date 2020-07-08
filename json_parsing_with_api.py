import requests
import json
import datetime

post_codes_req = requests.get("https://api.postcodes.io/postcodes/da161nf")
# print(post_codes_req.content)
# print(post_codes_req.cookies)
# print(post_codes_req.history)
# print(post_codes_req.elapsed.microseconds)
# print(post_codes_req)
# a = int(post_codes_req.elapsed.microseconds / 1000)
# print("ping =", a, "ms")

#

json_data = post_codes_req.json()
print(json_data)

def get_keys():

    for key in json_data:
        print(key)

        json_data_keys = json_data[key]  # rates is the whole dict, x_rates is the nested dict

    for key in json_data_keys:  # Iterates through the input "json_data_keys" which is the list of all the keys in the dict
        json_data_list = []
        json_data_list.append(key)
    print(json_data_list)

get_keys()

class JSONReader:
    def get_all_values(self, nested_dict):
        for key, value in nested_dict.items():
            if type(value) is dict:
                self.get_all_values(value)
            else:
                print(key, ":", value)

json_reader = JSONReader()
print(json_reader)
json_reader.get_all_values(json_data)