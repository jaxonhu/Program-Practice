namespace java roctime

struct Work {
1: i32 num1 = 0,
2: i32 num2,
4: optional string comment,
}
 

service TimeService {
	i32 TellMeTime()
}