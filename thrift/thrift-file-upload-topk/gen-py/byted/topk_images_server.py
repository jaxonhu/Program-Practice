from thrift.protocol import TBinaryProtocol, TCompactProtocol
from thrift.transport import TSocket, TTransport
from thrift.server import TServer
import FileInfoExtractService
import ttypes
import subprocess
import logging
import os
import re

__host = '127.0.0.1'
__port = 9990


class ServerListener(FileInfoExtractService.Iface):

    def __init__(self):
        self.upload_dir = os.path.join(os.getcwd(), '../../')
        # print self.upload_dir


    def uploadFile(self, fileData, topk):
        _topk = topk
        #top k fetch
        file_name = fileData.name
        file_buff = fileData.buff

        print self.upload_dir + '/upload_' + file_name
        with open(self.upload_dir + '/upload_' + file_name, 'wb') as f:
            f.write(file_buff)
            f.close()
            # to match
            out_std = None
            try:
                out_std = subprocess.check_output(['python', 'image_pair.py', '../../upload_' + file_name,
                                                   os.getcwd() + '/../../../../taobao-sprider/imgs/', str(_topk)])
            except subprocess.CalledProcessError as e:
                out_bytes = e.output  # Output generated before error
                code = e.returncode  # Return code
                print out_bytes.decode('utf-8')
                print code
            std_out = out_std.encode('utf-8')
            imgs = re.split('\n', std_out, maxsplit=_topk, )[:-1]
            imgs = map(lambda s: s[s.find('\t') + 1:], imgs)
            result = ttypes.ResultTopK(file_name, imgs)
            return result



    def ping(self):
        return 'ping success'




if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    listener = ServerListener()
    processor = FileInfoExtractService.Processor(listener)
    transport = TSocket.TServerSocket(host=__host, port=__port)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TCompactProtocol.TCompactProtocolFactory()

    server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)
    print 'starting server...'
    server.serve()
    print 'server stop'
    transport.close()

