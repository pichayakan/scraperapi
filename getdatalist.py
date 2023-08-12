import requests

url = "http://127.0.0.1:5000/gold_prices"  # Replace with the actual URL

response = requests.get(url)
if response.status_code == 200:
    json_data = response.json()
    error_message = json_data[1]
    ## test dataset ##
    # error_message =['12/08/2566 09:26', '1', '31,750.00', '31,850.00', '31,184.12', '32,350.00', '1,914.50', '35.12', '0']
    # error_message = {"error","Data not available"}
    print(error_message)

    if "error" in error_message:
        print("Data not available")
    else:
        # Find last index of list
        last_index_data = json_data[len(json_data) - 1]

        last_update = last_index_data[0]
        change_time = last_index_data[1]
        gold_bar_buy = last_index_data[2]
        gold_bar_sell = last_index_data[3]
        gold_buy = last_index_data[4]
        gold_sell = last_index_data[5]
        gold_spot = last_index_data[6]
        bath_us = last_index_data[7]
        change_price = last_index_data[8]
        print(last_update)

    # print(error_message)
    # print(json_data)
