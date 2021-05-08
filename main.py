import random

flag = True
new_lines = []
while flag:
    with open('words.txt', 'r', encoding = 'utf-8') as f:
        new_lines = [] 
        num = int(f.readline())
        print(num)
        lines_list = []
        for i in range(20):
            lines_list.append(random.randrange(1, num))
        lines_list.sort()
        index = 1
        beaut_numb = 1
        while index != num:
            if index in lines_list:
                print('{}. - {}'.format(beaut_numb, f.readline()))
                beaut_numb+=1
            else:
                new_lines.append(f.readline())
            index+=1
    answer = input('Устраивает?(y/n): ')
    if answer == 'y':
        flag = False
with open('words.txt', 'w', encoding = 'utf-8') as f:
    f.write(str(len(new_lines)) + '\n')    
    for i in new_lines:
        f.write(i)