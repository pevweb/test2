from escpos.connections import getUSBPrinter


#printer = getUSBPrinter()(idVendor=0x04F9,
 #                         idProduct=0x20A8,
  #                        inputEndPoint=0x82,
   #                       outputEndPoint=0x01)
#
#This
#47
#Decimal VendorID=2867 & ProductID=1794
#39
#Hexadecimal VendorID=0xb33 & ProductID=0x702


printer = getUSBPrinter(commandSet='Generic')(idVendor=0x04f9, idProduct=0x20a8)
#dev = usb.core.find(idVendor=0x04F9, idProduct=0x20A8)
printer.text("Hello World")
printer.lf()


https://download.brother.com/welcome/dlfp100575/ql1110nwbpdrv-2.1.4-0.i386.deb