import json
 
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

def recursion_print_elements(first_element, section):
    print (first_element)
    for element in first_element:
        print (element + ":")
        print (parsed_string[section][element])
        print ("\n")
        if parsed_string[section][element] in element:
            print ("true")
        
        #recursion_print_elements(parsed_string[element],element)
    #if "RobotizationCalls" in "script_types":
        #print ("true")
    #else:
        #print ("false")
        
with open("RobotizationCalls.json", "r", encoding='utf-8') as read_file:
    parsed_string = json.load(read_file)

#print (globals_params)
section = "globals"
globals_params = (parsed_string[section])
recursion_print_elements(globals_params, section)