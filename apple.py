import json
from datetime import datetime

class Apple:
    def __init__(self):
        self.color = 'Red'
        self.weight = 300
        self.leaf = True
        self.timestamp = datetime.now()


def convert_apple(o):
    if isinstance(o, datetime):
            return o.isoformat()
    return o.__dict__


a1 = Apple()
a2 = Apple()

apples = [a1, a2]

json_str = json.dumps(apples, default=lambda o: convert_apple(o), sort_keys=True, indent=4)

print(json_str)

def appleJsonDecod(o):
    try:
        return datetime.fromisoformat(o)
    except:
        return o

apple_objs = json.loads(json_str, cls = Apple, object_hook= lambda o: appleJsonDecod(o))

print(type(apple_objs[0]))

