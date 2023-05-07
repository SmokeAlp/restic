import json

tpl = ('1221', 2131, [12312,'123'], (313,'dwqqwe'), {'1': 'ome', '2': 2})





print(tpl,'\n')

json_tpl = json.dumps(tpl)
print(json_tpl)
json_tpl = json.loads(json_tpl)
print(json_tpl)


class House():
    def __init__(self, street):
        self.street = street

    def built(self):
        print('bebbeb' + self.street)

h = House('Лен')
print(h)



