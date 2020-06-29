name=(input("姓名："))
studentID=(input("学号："))
sensitive_character = '你好','病毒','干','傻' 
test_sentence = input('请输入一段话:')
for line in sensitive_character: 
 if line in test_sentence: 
    test_sentence = test_sentence.replace(line, '*')
print(test_sentence)
