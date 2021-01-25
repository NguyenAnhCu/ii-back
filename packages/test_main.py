
from image_utils import *
from IQ_generator import * 
import sys


if __name__ == "__main__":
    q = Question(500,500)
    ques_type = random.choice(["1","2","3"])
    if ques_type  == "1" :
        q.generate_random_lines()
    elif ques_type == "2" :
        q.generate_random_hexa()
    elif ques_type == "3" :
        q.generate_random_boxes()
    
    """
    f = open("../question/question_explication.json")
    dict_responce = json.load(f)
    f.close()
    try :
        while True :
            responce = input("enter your responce : \n") 
            print(dict_responce[responce]["status"])
            print(dict_responce[responce]["explication"])
    except KeyboardInterrupt :
        sys.exit(0)
    """