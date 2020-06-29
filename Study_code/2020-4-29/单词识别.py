tues_or_thurs = {'h': 'Thursday', 'u': 'Tuesday'}
weekend = {'a': 'Saturday', 'u': 'Sunday'}
week = {'t': tues_or_thurs, 's': weekend,
    'm': 'Monday', 'w': 'Wednesday',
    'f': 'Friday'}
first_char = input('请输入第一位字母：').lower().strip()
if first_char in ['a', 't', 's', 'm', 'w', 'f']:
    if week[first_char] == tues_or_thurs or week[first_char] == weekend:
        second_char = input('请输入第二位字母：').lower().strip()
        if second_char in ['u', 'h', 'a']:
            print(week[first_char][second_char])
        else:
            print('请输入正确字母')
    else:
        print(week[first_char])
else:
    print('请输入正确的字母')
