关键区别：
f:对象（列表、字典等）
json.load(f)：从文件对象中读取JSON数据（直接操作文件）。
string=f.read()
json.loads(string)：从字符串中解析JSON数据（需要先读取文件内容到字符串）。
