from DataLogicLair.get_conection import get_connection
from DataLogicLair.options import Options

cnc = get_connection()
cursor = cnc.cursor()
opt = Options()

cursor.execute(opt.get_needed_products_amount_and_id_for_good_by_good_id + ' 6')
r = cursor.fetchall()
for i in r:
    print(i)
l = list(map(lambda x: x[0], r))
print(l)

f = {'bebeb': 123, 'jfjfjfj': 555}

for i in f:
    print(i, f.get(i))
    f[i] = 'ttt'
print(f.values())
print(type(cursor.execute(opt.get_product_amount_by_id + ' 1').fetchval()))

g = {13}

print(g)