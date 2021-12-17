class Header:
    cont_head = None
    drop_head = None


class Value:
    content_type = None
    dropbox_api = None


class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getHeaders(self):

        headers = Headers()

        head = self.__builder.getHeader()
        headers.setContHeader(head.cont_head)
        headers.setDropHeader(head.drop_head)

        value = self.__builder.getValue()
        headers.setCont(value.content_type)
        headers.setDrop(value.dropbox_api)

        return headers

class Headers:
    def __init__(self):
        self.__cont_head = None
        self.__drop_head = None
        self.__content_type = None
        self.__dropbox_api = None

    def setContHeader(self, cont_head):
        self.__cont_head = cont_head

    def setDropHeader(self, drop_head):
        self.__drop_head = drop_head

    def setCont(self, content_type):
        self.__content_type = content_type

    def setDrop(self, dropbox_api):
        self.__dropbox_api = dropbox_api

    def createJSN(self):
        if self.__drop_head == None :
            my_headers = {self.__cont_head: self.__content_type}
        else:
            my_headers = {self.__cont_head: self.__content_type, self.__drop_head: self.__dropbox_api}
        return my_headers

class Builder:
    def getHeader(self): pass
    def getValue(self): pass


class GetAndDelHeadBuilder(Builder):

    def getHeader(self):
        head = Header()
        head.cont_head = "Content-Type"
        return head
    def getValue(self):
        value = Value()
        value.content_type = "application/json"
        return value

class UploadHeadBuilder(Builder):

    def getHeader(self):
        head = Header()
        head.cont_head = "Content-Type"
        head.drop_head = "Dropbox-API-Arg"
        return head
    def getValue(self):
        value = Value()
        value.content_type = "application/octet-stream"
        value.dropbox_api = '{"path": "/webapi26_testing/kotik1.jpg", "mode": "add", "autorename": true, "mute": false, "strict_conflict": false}'
        return value

