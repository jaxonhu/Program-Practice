### Thrift Demo 运行说明

#### 启动server

`
java -Djava.library.path=/Users/hujiaxuan/tools/thrift-0.11.0/lib/java/build/lib -cp .:lib/libthrift-0.11.0.jar:roctime/roctime.jar:/Users/hujiaxuan/tools/thrift-0.11.0/lib/java/build/lib/slf4j-api-1.7.12.jar Client
`

#### 启动client

`
java -Djava.library.path=/Users/hujiaxuan/tools/thrift-0.11.0/lib/java/build/lib -cp .:lib/libthrift-0.11.0.jar:roctime/roctime.jar:/Users/hujiaxuan/tools/thrift-0.11.0/lib/java/build/lib/slf4j-api-1.7.12.jar Client
`

#### 注意

需要提前将thrift生成的TimeService.java编译打包成jar包

`
javac -cp "/Users/hujiaxuan/github/Program-Practice/thrift/thrift-time-demo/gen-java/lib/libthrift-0.11.0.jar:/Users/hujiaxuan/tools/thrift-0.11.0/lib/java/build/lib/slf4j-api-1.7.12.jar:/Users/hujiaxuan/tools/thrift-0.11.0/lib/java/build/lib/slf4j-log4j12-1.7.12.jar:/Users/hujiaxuan/tools/thrift-0.11.0/lib/java/build/lib/log4j-1.2.17.jar" roctime/*.java -d roctime
`

这样写比较啰嗦，可以把jar包都放到一个lib文件夹里，然后加到classpath，但是我的java版本貌似不支持 /* 通配符。

