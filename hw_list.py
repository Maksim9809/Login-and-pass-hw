account1 = {'login': 'ivan' , 'password': 'q1'} 
account2 = {'login': 'petr' , 'password': 'q2'}
account3 = {'login':'olga' , 'password': 'q3'}
account4 = {'login':'anna' , 'password': 'q4'}

user1 = {'name': 'Иван' , 'age': 20 , 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27 , 'account': account4}

account = {'login': '' , 'password': '' }
user = { 'name': '' , 'age': '', 'account': account}

user_list = [user1 , user2 , user3 , user4]

question = input('Введите ключ (name или account): ')

up_low = question.lower()
if up_low == 'name':
    print('''
    значение ключа name для юзера 0 = Иван
    значение ключа name для юзера 1 = Петр
    значение ключа name для юзера 2 = Ольга
    значение ключа name для юзера 3 = Анна''')

    question2 = input('Введите порядковый номер: ')
    if question2 < '5':
        task = int(question2)
        pass_log = user_list[task]
        login_account = pass_log['account']
        login_account2 = login_account['login']
        password_account = login_account['password']       
        print(f'Данные по юзеру №{question2}: ')
        
        print(f'Имя: {user_list[task]["name"]}')
       
        print(f'Возраст: {user_list[task]["age"]}')
        
        print(f'Логин: {login_account2}')
       
        print(f'Пароль: {password_account}')
        add_in_list = input('Введите индекс пользователя данные которого хотите изменить: ')
        if add_in_list < '5':
            conc = int(add_in_list)
            delete_from_list = user_list.pop(conc)
            in_list = user_list.append(delete_from_list)
            
            print(user_list)
    else:
        print('Пользователь с указанным номером не найден.')    
else:
        print('Вы ввели неправильное значение.')



    
print(user_list)