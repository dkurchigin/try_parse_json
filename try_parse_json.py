import json
import re
 
# строка которую будем парсить
json_string = """{
  "orderID": 42,
  "customerName": "John Smith",
  "customerPhoneN": "555-1234",
  "orderContents": [
    {
      "productID": 23,
      "productName": "keyboard",
      "quantity": 1
    },
    {
      "productID": 13,
      "productName": "mouse",
      "quantity": 1
    }
  ],
  "orderCompleted": true
} """
 
# распарсенная строка
#parsed_string = json.loads(json_string)
#f = open("RobotizationCalls.json", 'r', encoding='utf-8')
#for line in f:
    #print (line)

def format_list_to_str(list):
    return re.sub(r'(\[\'|\'\])', '', list)
        
def recursive(obj, level):
    only_k_v = ""
    element_level = ""
    if isinstance(obj, dict):
        for key, value in obj.items():
            level =+ 1
            if level == 1:
                element_level = "\t"
            
            only_k_v = element_level + str(key) + ":" + str(value)
            if isinstance(value, dict):
                print (key)
                recursive(value, level)
            else:
                if isinstance(value, list):
                    only_k_v = format_list_to_str(str(value))
                print(only_k_v)

                
with open("RobotizationCalls.json", "r", encoding='utf-8') as read_file:
    parsed_string = json.load(read_file)

recursive(parsed_string, 0)