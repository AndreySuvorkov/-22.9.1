num_str = input('Введите последовательность чисел через пробел: ') # получаем последовательность чисел
num_list = list(map(int, num_str.split())) # преобразовываем последовательность в список целых чисел
num = int(input('Введите любое число: ')) # получаем число для поиска и преобразовываем в целое число
def my_sort(array): # определяем функцию для сортировки списка по возрастанию
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx-1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array

num_list_sort = my_sort(num_list)
print('Список отсортированный по возрастанию элементов: ', num_list_sort)
def bi_search(a, array): # определяем функцию для поиска позиции
    left, right = 0, len(array)
    while left < right:
        middle = (left + right) // 2
        if array[middle] < a:
            left = middle + 1
        else:
            right = middle
    return left

item = bi_search(num, num_list_sort)

if num > num_list_sort[-1]:  # добавляем проверку что введенное число соответствует условию
    print(f'Введенное число {num} больше любого числа в последовательности {num_list}')
elif num < num_list_sort[0]:
    print(f'Введенное число {num} меньше любого числа в последовательности {num_list}')
else:
    print(f'Число {num_list_sort[item - 1]} на позиции {item - 1} меньше числа {num}')
    print(f'Число {num_list_sort[item]} на позиции {item} больше либо равно числу {num}')