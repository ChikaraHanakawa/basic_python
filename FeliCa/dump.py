import nfc

def on_connect(tag):
  print(tag)
  for i in tag.dump():
    print(i)
clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': on_connect})