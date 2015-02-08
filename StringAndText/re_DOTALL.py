import re
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
text1 = '/* this is a comment */'
text2 = '''/* this is a
        multiline comment */
'''
print(comment.findall(text1))
print(comment.findall(text2))
