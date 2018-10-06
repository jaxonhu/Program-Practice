### Thrift Demo

#### Thrift IDL

- WhatTime.thrift

向服务器请求当前时间

#### 生成thrift 代码

`
 thrift --gen java WhatTime.thrift
`

生成 gen-java目录

gen-java目录中包含roctime/TimeService.java 和 roctime/Work.java两个自动生成的文件

#### Client代码

需要自己实现，参考Client.java

#### Server实现

需要自己实现 TimeServiceImpl 类，这个类会实现TimeService.java里的Iface接口，填充服务器逻辑

然后编写 TimeServiceServer 主类，开启服务器监控进程。