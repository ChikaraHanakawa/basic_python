import nfc

def conectedcard(tag):
    idm, pmm = tag.polling(system_code=0x81e1)
    tag.idm, tag.pmm, tag.sys = idm, pmm, 0xfe00
    sc = nfc.tag.tt3.ServiceCode(192, 0x0b)
    bc = nfc.tag.tt3.BlockCode(0, service=0)
    data_num = tag.read_without_encryption([sc], [bc])
    data_num = data_num.decode('ASCII')
    print(data_num[0:7])

def read_student_info():
    with nfc.ContactlessFrontend('usb') as clf:
        try:
            clf.connect(rdwr={'on-connect': conectedcard})
        except:
            pass

if __name__ == '__main__':
    read_student_info()
