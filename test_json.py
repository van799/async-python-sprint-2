import json


class Apple:
    def __init__(self):
        self.color = 'red'
        self.weight = 300
        self.volume = 200

    def list(self):
        self.list1 = ['faf', 'fa']
        self.a = 'ada'

    def to_json(self):
        # self.list()
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=4
                          )


apple = Apple()
apple_json = apple.to_json()
print(apple_json)
