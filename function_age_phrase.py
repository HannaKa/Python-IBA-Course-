#Для целого числа К от 1 до 9 напечатать фразу "мне К лет", "год", "года".
def age(k):
    if k == 1:
        print ('Мне ', str(k), ' год')
    elif 2 <= k <= 4:
        print ('Мне ', str(k), ' годa')
    else:
        print ('Мне ', str(k), ' лет')
age(1)
age(4)
age(6)
