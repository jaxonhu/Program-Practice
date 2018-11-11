from thrift.protocol import TBinaryProtocol, TCompactProtocol
from thrift.server import TServer
from thrift.transport import TSocket, TTransport

import FileInfoExtractService
import ttypes
import logging

_host = "127.0.0.1"
_port = 9999


class ServerListener(FileInfoExtractService.Iface):

    def __init__(self):
        self.upload_dir = "/Users/hujiaxuan/github/Program-Practice/thrift/thrift-file-upload"

    def uploadFile(self, file_data):
        # top k fetch
        file_name = file_data.name
        file_buff = file_data.buff
        print 'buffer: '
        print file_buff
        with open(self.upload_dir + '/upload_' + file_name, 'wb') as f:
            f.write(file_buff)
            f.close()
        # to match
        result = ttypes.ResultTopK("picture1", ["url1", "url2", "url3"])
        return result

    def ping(self):
        return "ping success"


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    listener = ServerListener()
    processor = FileInfoExtractService.Processor(listener)
    transport = TSocket.TServerSocket(host=_host, port=_port)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TCompactProtocol.TCompactProtocolFactory()

    server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)
    print "starting server..."
    server.serve()
    print "server stop"
    transport.close()
