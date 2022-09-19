import re

text = "House no: 5, Phone number: 01823503392, 01732094401, 01935819301, 01711101001, 000001100010101"
result = re.findall('01[356789]\s*\d{8}',text)
#{11} means 11 digits simultaneously. Otherwise it will give the first digit it would find
#\d{3}\s*\d{8} means 1st 3 digits then cn have spaces or not and again 8 more digits
print(result)
s = "<li>Tamim</li><li>Shakib</li><li>Mahmudullah</li><li>Mominul</li>"
print(re.findall(r'<li>(.*?)</li>',s))

"""if we write "<li>.*?</li>" we will get output including <li>, </li>.
So to remove these we will add "()" and would write the  desired proportion 
insise brackets"""
