import json
import os
import re
import sqlite3

def check_db_exist(file):
    db_extension = file + ".db"
    while True:
        if os.path.isfile(db_extension):
            print("База данных {} уже существует. Переписать?".format(db_extension))
            print("(Y)es | (N)o?")

            answer = input()
            pattern_for_yes = '(^[yY]$|^[yY][eE][sS]$|^[дД]$|^[дД][аА]$)'

            if re.match(pattern_for_yes, answer):
                os.remove(db_extension)
                print("Удаляю старую версию базы данных {}".format(db_extension))
            else:
                break
        else:
            create_db(db_extension)
            print("Создана база: {}".format(db_extension))
            parse_phrases(parsed_string["phrases"], db_extension)
            break

       
def create_db(database_file):       
    con = sqlite3.connect(database_file)
    cur = con.cursor()
    cur.execute('CREATE TABLE rule_dicts (id INTEGER PRIMARY KEY, dict_name VARCHAR(128), dict_content TEXT)')
    con.commit()
    con.close()
    

def write_data(database_file, dict_sql):
    con = sqlite3.connect(database_file)
    cur = con.cursor()
    for key, value in dict_sql.items():
        cur.execute('INSERT INTO rule_dicts (id, dict_name, dict_content) VALUES(NULL, \'{}\', \'{}\')'.format(key, value))
    con.commit()
    con.close()
    
            
def format_list_to_str(input_list):
    out_str = ""
    for rule in input_list:
        out_str = out_str + "\"{}\"".format(rule)
        if not input_list.index(rule) == (len(input_list) - 1):
            out_str = out_str + ",\n"
    return out_str
        
        
def read_phrases_dicts(obj):
    only_k_v = ""
    element_level = ""
    if isinstance(obj, dict):
        for key, value in obj.items():
            level =+ 1
            if level == 1:
                element_level = "\t"
            
            only_k_v = element_level + str(key) + ":" + str(value)
            if isinstance(value, dict):
                print (str(key) + ":")
                recursive(value, level)
            else:
                if isinstance(value, list):
                    if (level != 1):
                        only_k_v = format_list_to_str(str(value))
                    else:
                        only_k_v = re.sub(r'(\t|\[.*)', '', only_k_v)
                        only_k_v = re.sub(r'(:)', ':\n\t', only_k_v)
                        only_k_v = only_k_v + format_list_to_str(str(value))
                print(only_k_v)
    
        
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
                print (str(key) + ":")
                recursive(value, level)
            else:
                if isinstance(value, list):
                    if (level != 1):
                        only_k_v = format_list_to_str(str(value))
                    else:
                        only_k_v = re.sub(r'(\t|\[.*)', '', only_k_v)
                        only_k_v = re.sub(r'(:)', ':\n\t', only_k_v)
                        only_k_v = only_k_v + format_list_to_str(str(value))
                        #print (value)
                        #only_k_v = re.sub(r'(:)', ':\n\t', only_k_v)
                        #format_list_to_str(only_k_v)
                        #only_k_v = only_k_v + key
                print(only_k_v)

                
def parse_phrases(rule_dicts, db_extension):
    for key, value in rule_dicts.items():
        pure_value = format_list_to_str(value)
        rule_dicts[key] = pure_value
        print("{}\n{}\n\n".format(key, pure_value))
    write_data(db_extension, rule_dicts)
        
                
#-----------------------------                
with open("RobotizationCalls.json", "r", encoding='utf-8') as read_file:
    parsed_string = json.load(read_file)

check_db_exist("RobotizationCalls.json")