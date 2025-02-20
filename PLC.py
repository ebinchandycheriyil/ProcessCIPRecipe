from pycomm3 import LogixDriver,exceptions
# PLC Read Write handled from here

class plcComm():
    def __init__(self):
        self.__PLCAddr = '192.168.0.1'

    def readTag(self, tagName):

        return 0

    def writeTag(self, tagName,value):
        # print(f"addr : {tagName}       val - {value}")


        with LogixDriver(self.__PLCAddr) as plc:

            plc.write([tagName, value[0][0]])
            # print(f"{value}      {plc.read(tagName)}")

    def writeList(self,list):
        with LogixDriver(self.__PLCAddr) as plc:

            plc.write(*list)
            tagList = [plc.read(list[0][0]) , plc.read(list[1][0]) ]

    def readList(self, list):
        try:
            print('hdh')
            with LogixDriver(self.__PLCAddr) as plc:

               valList =  plc.read(*list)
               retVal = []
               for val in valList:
                   retVal.append(val[1])
               print(retVal)
               return retVal
        except exceptions.CommError:
            print('**************')
            return '-'

