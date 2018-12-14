from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol
from thrift.server import TServer
import FileInfoExtractService
import logging
import ttypes
import os
import sys


__host = "127.0.0.1"
__port = 9990

targets = os.getcwd() + '/../../'
file_name = "test.jpg"

defaultK = 3

class ClientUploader(FileInfoExtractService.Client):
    def make_data(self):
        fd = ttypes.FileData()
        with open(os.path.join(targets, file_name), 'rb') as f:
            buff = f.read()
            fd.name = file_name
            fd.buff = buff
            f.close()
        return fd




if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            topk = int(sys.argv[1])
        else:
            topk = defaultK

        print "Usage: top k = %s " % topk

        logging.basicConfig(level=logging.DEBUG)
        transport = TSocket.TSocket(host=__host, port=__port)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TCompactProtocol.TCompactProtocol(transport)

        client = ClientUploader(protocol)
        transport.open()
        print client.ping()
        print 'uploading'
        file_data = client.make_data()
        res = client.uploadFile(file_data, topk=topk)
        print res

        print 'finished'
        transport.close()
    except Exception, e:
        print e