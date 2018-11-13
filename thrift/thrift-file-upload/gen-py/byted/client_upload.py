from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol
from thrift.server import TServer
import FileInfoExtractService
import logging
import ttypes


_host = "127.0.0.1"
_port = 9999

targets = "/Users/hujiaxuan/github/Program-Practice/thrift/thrift-file-upload/"
file_name = "test.jpg"


class ClientUploader(FileInfoExtractService.Client):

    def make_data(self):
        fd = ttypes.FileData()
        with open(targets + file_name, 'rb') as f:
            buff = f.read()
            fd.name = file_name
            fd.buff = buff
            f.close()
        return fd


if __name__ == '__main__':

    try:
        transport = TSocket.TSocket(_host, _port)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = ClientUploader(protocol)
        transport.open()
        print client.ping()
        print "uploading..."
        file_data = client.make_data()
        res = client.uploadFile(file_data)
        print res.srcImage
        print res.urls
        print "finished"
        transport.close()
    except Exception, e:
        print e
