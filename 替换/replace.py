#把s中数字替换
s = "ddddd123456789"
for i in range(10):
g = s.replace(str(i), '')
print(g)

#只能替换最后一个数字,每次调用 s.replace(str(i), '') 时，都是在原始字符串 s 上操作，而非基于前一次替换后的结果 g。因此，所有替换操作互不影响，最终 g 仅保留最后一次替换的结果。

#改为：修正后的代码
s = "ddddd123456789"

# 方法1：直接遍历所有数字字符（0-9），逐次替换
result = s
for i in range(10):  # 覆盖所有数字 0-9
    result = result.replace(str(i), '')
print(result)  # 输出：ddddd

#方法2：使用正则表达式（更高效）
import re
s = "ddddd123456789"
result = re.sub(r'\d', '', s)  # \d 匹配所有数字
print(result)  # 输出：ddddd
