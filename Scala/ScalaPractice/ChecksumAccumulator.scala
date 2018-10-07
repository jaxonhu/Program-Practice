import scala.collection.mutable.Map

<<<<<<< HEAD
class ChecksumAccumulator {
	
	private var sum = 0

	def add(b: Byte) { sum += b }

	def checksum(): Int =  ~(sum &0xFF) + 1
}

object ChecksumAccumulator {

	private val cache = Map[String, Int]()
	def calculate(s: String): Int = 
		if(cache.contains(s))
			cache(s)
		else {
			val acc = new ChecksumAccumulator
			for(c <- s)
=======
object ChecksumAccumulator {
	private val cache = Map[String, Int]()

	def calculate(s : String): Int = 
		if (cache.containes(s))
			cache(s)
		else {
			val acc = new ChecksumAccumulator
			for (c <- s)
>>>>>>> c45455c84dfdc7f2d82721d35386a15b58582927
				acc.add(c.toByte)
			val cs = acc.checksum()
			cache += (s -> cs)
			cs
<<<<<<< HEAD
		}	
}

val ca = new ChecksumAccumulator
ca.add('3'.toByte)
print(ca.checksum)
=======
		}
}

class ChecksumAccumulator {
	private var sum = 0
	def add(b : Byte) { sum += b }
	def checksum(): Int = ~(sum & 0xff) + 1
}

>>>>>>> c45455c84dfdc7f2d82721d35386a15b58582927
