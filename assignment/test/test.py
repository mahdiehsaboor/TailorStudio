from xml.dom.minidom import Document

from assignment.model.da.da import DataAccess
from assignment.model.entity import *

#Entity test
#customer=Customer("Ali","Alipour","+989141632595","alialipour@outlook.com","1234567890", "1374/3/27")
#customer=Customer("Reza","Rezayi","+989126542659","rezarezayi@gmail.com","7426589150","1368/6/15")
#print(customer)
#customer_da = DataAccess(Customer)
#customer_da.save(customer)
#print(customer)

# print(customer_da.find_all())
# print(customer_da.find_by_id('2'))
# print(customer_da.find_by_id(customer.id<3))
# print(customer_da .find_by_family(customer.family =='Alipour'))

#edit
#customer=Customer("Alireza","Alipour","+989141632595","1234567890","1234567890", "1374/3/27")
#customer_da.edit(customer)
#print(customer)

#remove
#customer=Customer("1")
#customer_da.remove(customer)
#print(customer)


#tailor=Tailor("Alireza","Alipouryy","09142561265","5000","4561237890","13743/27")
#print(tailor)
#tailor_da = DataAccess(Tailor)
#tailorr_da.save(tailor)
#print(tailor)

# print(tailor_da.find_all())
# print(tailor_da.find_by_id('1'))
# print(tailor_da .find_by_family('Alipouryy'))

#edit
#tailor=Tailor("Alireza","Alizadeh","09142561265","5000","4561237890","13743/27")
#tailor_da.edit(tailor)
#print(tailor)

#remove
#edit
#tailor=Tailor("Alireza","Alizadeh","09142561265","5000","4561237890","13743/27")
#tailor_da.reove(tailor)
#print(tailor)


#clothes=Clothes("suit","cotton ","gray","450","l","no pocket")
#print(clothes)
#clothes_da = DataAccess(Clothes)
#clothes_da.save(clothes)
#print(clothes)

# print(clothes_da.find_all())
# print(clothes_da.find_by_id('1'))
# print(clothes_da .find_by_name_clothes('suit'))

#edit
#clothes=Clothes("dress","cotton ","gray","450","l","no pocket")
#clothes_da.edit(clothes)
#print(tailor)

#remove
#clothes=Clothes("dress","cotton ","gray","450","l","no pocket")
#clothes_da.remove(clothes)
#print(tailor)


# order=Order("1403/2/15","1403/3/10 ","True","78945612","12345678")
# order=Order("1403/3/15","1403/3/31","True","85674251","59762481")
#print(order)
#order_da = DataAccess(Order)
#order_da.save(order)
#print(order)

# print(order_da.find_all())
# print(order_da.find_by_id('1'))
# print(order_da .find_by_customer_id("78945612"))

#edit
#clothes=Clothes("1403/2/15","1403/3/10 ","canceled","78945612","12345678")
#tailor_da.edit(tailor)
#print(tailor)

#remove
#edit
#clothes=Clothes("1403/2/15","1403/3/10 ","canceled","78945612","12345678")
#tailor_da.remove(tailor)
#print(tailor)

customer = Customer("ali","Alipour","+989142361245","1234567890","1234567890","1374/3/27")
print(customer)
