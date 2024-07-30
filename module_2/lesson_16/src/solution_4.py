x = []

quantity_of_goods = int(input("Введите кол-во полок: "))
sales_by_product = input("Продажи по товарам: ")
out = "".join(i for i in sales_by_product if i not in (';', ','))
out = [int(i) for i in out] 

count = quantity_of_goods

while quantity_of_goods <= len(out):
    list = out[:quantity_of_goods]
    x.append(list)
    del out[:quantity_of_goods]
    count += count

print(x)

