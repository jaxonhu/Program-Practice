import org.apache.thrift.TException;
import roctime.TimeService;

public class TimeServiceImpl implements TimeService.Iface {

	public TimeServiceImpl() {

	}

	@Override
	public int TellMeTime() throws TException {
		return (int)System.currentTimeMillis();
	}

}
