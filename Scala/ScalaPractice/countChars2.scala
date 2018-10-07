import scala.io.Source

def widthOfLength(s: String) = s.length.toString.length

if( args.length > 0) {
	val lines = Source.fromFile(args(0)).getLines.toList
	val longestLine = lines.reduceLeft((l1, l2) => if(l1.length > l2.length) l1 else l2)
	val maxWidth = widthOfLength(longestLine)
	for(line <- lines) {
		val numSpaces = maxWidth - widthOfLength(line)
		val padding = " " * numSpaces
		println(padding + line.length + " | " + line)
	}		
}
else
	Console.err.println("Please enter filename")