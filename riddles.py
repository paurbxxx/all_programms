
print('Разгадай все три загадки!')
def answer():
    for l in range(3):
        if l == 0:
            print('1 загадка - я не вода, но по воде плаваю ')

            answer_for_one = 'льдина'
            input_for_one = input('Ваш ответ: ').lower()

            if input_for_one == answer_for_one:
                print(f'Молодец! Ответ {input_for_one} правильный')
                
            else: 
                print(f'Не правильный ответ, правильный ответ - {answer_for_one}')
                break
        elif l == 1:
            print('2 загадка - меня все топчут, а я все лучше) ')

            answer_for_two = 'тропинка'
            input_for_two = input('Ваш ответ: ').lower()

            if input_for_two == answer_for_two:
                print(f'Молодец! Ответ {input_for_two} правильный')
                
            else: 
                print(f'Не правильный ответ, правильный ответ - {answer_for_two}')
                break
        
        elif l == 2:
            print('3 загадка - что невоможно удержать и 10 минут, хоть оно легче перышка? ')

            answer_for_three = 'льдина'
            input_for_three = input('Ваш ответ: ').lower()

            if input_for_three == answer_for_three:
                print(f'Молодец! Ответ {input_for_three} правильный')
                
            else: 
                print(f'Не правильный ответ, правильный ответ - {answer_for_three}')
                break

answer()

colibration = bool(1)
while colibration:
    answer = input('Кто может передвинуть и слона, и коня? - ').lower()
    guess = 'шахматист'
    reply = 'сдаюсь'
    if answer == guess:
        print('Красава')
        break
    elif answer == reply:
       break
    else:
        print('Попробуй заново')
