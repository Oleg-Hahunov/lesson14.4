import validators

pincode = ['1239', '3333', '1234', '10011', '8765']
pin_rezalt =[]

userpass = ['secretd00r', 'huskyeye5', 'secret', 'm3wm3wm3w', 'fh43j_!']
pass_rezalt = []

useradress = ['local@skypro', 'you(at)sky.pro', 'me@sky.pro', '@lizaveta', 'alarm@gmail.com']
adress_rezalt =[]

username = ['Данил', 'Р_и_т_а', 'К0нстантин', 'А Ф', 'Елена']
name_rezalt =[]


for i in range(5):
    pin = pincode[i]
    pin_rezalt.append(validators.check_pin(pin))

    pas_ = userpass[i]
    pass_rezalt.append(validators.check_pass(pas_))

    mail = useradress[i]
    adress_rezalt.append(validators.check_mail(mail))

    name = username[i]
    name_rezalt.append(validators.check_name(name))

print(pin_rezalt)
print(pass_rezalt)
print(adress_rezalt)
print(name_rezalt)


