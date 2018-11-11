### 一点小坑

#### 问题一：客户端 TSocket read 0 bytes

```python
    try:
        transport = TSocket.TSocket(_host, _port)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = FileInfoExtractService.Client(protocol)
        transport.open()
        print client.ping()
        print "uploading..."
        file_data = make_data()
        # client.uploadFile(file_data)
        print "finished"
        transport.close()
    except Exception, e:
        print e
```
经过测试，当时用TCompactProtocol时，服务器端获取不到数据。使用TBinaryProtocol就可以正常，我认为transport和protocol是需要搭配起来使用。buffer的方式和compact的协议可能存在冲突，还需要确认一下


#### 问题二： 服务器端 TTransport raise EOFError()

好吧，其实这个问题我也没复现，后来重构一遍就好了。。