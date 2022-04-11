def check_pin(pin):
    if len(pin) != 4:
        return False
    elif int(pin) % 1111 == 0:
        return False
    elif int(pin) == 1234:
        return False
    else:
        return True


def check_pass(pas_):
    flag_num = 0
    flag_smb = 0
    if len(pas_) < 8:
        return False
    for i in range(len(pas_)):
        if pas_[i].isdigit() == True:
            flag_num = 1
        elif pas_[i].isalpha() == True:
            flag_smb = 1
    if flag_smb == 0 or flag_num == 0:
        return False
    else:
        return True


def check_mail(mail):
    flag_dog = 0
    flag_dot = 0
    for i in range(len(mail)):
        if mail[i] == "@":
            flag_dog = 1
        elif mail[i] == '.':
            flag_dot = 1

    if flag_dog == 1 and flag_dot == 1:
        return True
    else:
        return False


def check_name(name):
    letters = 'аАбБвВгГдДеЕёЁжЖзЗиИкКлЛмМнНоОпПрРсСтТуУфФхХцЦчЧшШщЩъЪыЫьЬэЭюЮяЯ '
    for i in range(len(name)):
        if name[i] not in letters:
            return False
    return True
