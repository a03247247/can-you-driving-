country = str(input('請問您的國家是?'))



if country == '台灣' or country == 'Taiwan' :

    age = int(input('輸入年齡'))
    if age >= 18:
        print('你可以考駕照')
    else:
        print('你還不能考駕照')
        print('還差' , 18-age,'歲')
else:
    print('sorry 你不符合資格')
