namespace py byted

struct FileData
{
	1:required string name,
	2:required binary buff
}

struct ResultTopK
{
	1:required string srcImage,
	2:required list<string> urls
}

service FileInfoExtractService 
{
	ResultTopK uploadFile(1:FileData fileData);	
	string ping();
}
