from thrift.protocol import TBinaryProtocol, TCompactProtocol
from thrift.transport import TSocket, TTransport
from thrift.server import TServer
import FileInfoExtractService
import  subprocess
import logging
import ttypes
import re

_host = "127.0.0.1"
_port = 9999


class ServerListener(FileInfoExtractService.Iface):

    def __init__(self):
        self.upload_dir = "/Users/hujiaxuan/github/Program-Practice/thrift/thrift-file-upload"

    def uploadFile(self, file_data):
        # top k fetch
        file_name = file_data.name
        file_buff = file_data.buff
        with open(self.upload_dir + '/upload_' + file_name, 'wb') as f:
            f.write(file_buff)
            f.close()
        # to match
        out_std = None
        try:
            out_std = subprocess.check_output(['python', 'image_pair.py', '../../upload_'+file_name,
                                      '/Users/hujiaxuan/github/Program-Practice/taobao-sprider/imgs/', '3'])
        except subprocess.CalledProcessError as e:
            out_bytes = e.output  # Output generated before error
            code = e.returncode  # Return code
            print out_bytes.decode('utf-8')
            print code
        std_out = out_std.encode('utf-8')
        imgs = re.split('\n', std_out, maxsplit=2, )
        result = ttypes.ResultTopK(file_name,imgs)
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
