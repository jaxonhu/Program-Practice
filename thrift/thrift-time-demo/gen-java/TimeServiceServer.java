import org.apache.thrift.TProcessor;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.server.TServer;
import org.apache.thrift.server.TSimpleServer;
import org.apache.thrift.transport.TServerSocket;
import roctime.TimeService;

public class TimeServiceServer {

	public void startServer() {
		try {
			System.out.println("TimeService Server starting...");

			TServerSocket serverTransport = new TServerSocket(9090);
            TServer.Args args = new TServer.Args(serverTransport);
            TProcessor process = new TimeService.Processor(new TimeServiceImpl());
            TBinaryProtocol.Factory portFactory = new TBinaryProtocol.Factory(true, true);
            args.processor(process);
            args.protocolFactory(portFactory);

            TServer server = new TSimpleServer(args);
            server.serve();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) {
		TimeServiceServer tss = new TimeServiceServer();
		tss.startServer();
	}

}

