# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
import re

reserved_words = set(keyword.kwlist)

# 1. 读取原文件内容
with open("random_int.py", "r", encoding="utf-8") as f:
    content = f.read()

# 2. 定义替换函数：保留字不替换，其他小写字母转大写
def replace_word(match):
    word = match.group(0)
    if word in reserved_words:
        return word  # 保留字不修改
    else:
        return word.upper()  # 其他单词转大写

# 3. 匹配所有单词并替换（正则匹配字母/下划线组成的单词）
processed_content = re.sub(r"\b[a-zA-Z_]+\b", replace_word, content)

# 4. 将处理后的内容写入新文件
with open("random_int_converted.py", "w", encoding="utf-8") as f:
    f.write(processed_content)
