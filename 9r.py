def z1():
    import os
    # Путь папке
    source_folder = 'D:/дз/алгоритмизация/9лаб'
    # Путь к папке с обработанные изображения
    destination_folder = 'D:/дз/алгоритмизация/9лаб'
    # Создаем папку обработанных из
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    # Список файлов нужно обработать
    file_names = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    for file_name in file_names:
        # Открываем
        img = Image.open(os.path.join(source_folder, file_name))
        # Применяем чб
        img_gray = img.convert('L')
        # Сохраняем обработанное
        new_file_name = 'new_' + file_name
        img_gray.save(os.path.join(destination_folder, new_file_name))
    print("Обработка завершена.")

def z2():
    import os
    source_folder = 'D:/дз/алгоритмизация/9лаб'
    destination_folder = 'D:/дз/алгоритмизация/9лаб'
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    file_names = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    for file_name in file_names:
        img = Image.open(os.path.join(source_folder, file_name))
        # чб
        img_gray = img.convert('L')
        new_file_name = 'new_' + file_name
        img_gray.save(os.path.join(destination_folder, new_file_name))
    print("Обработка завершена.")

def z3():
    import csv
    fieldnames = ['Product', 'Quantity', 'Price']
    with open("C:/Users/chiku/PycharmProjects/pythonProject1/pythonProject1/sym.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",", fieldnames=fieldnames)
        total_cost = 0
        sym = 0
        print("Нужно купить:")
        for row in reader:
            print(f"Reading row: {row}")
            if row['Quantity'] and row['Price'] and row['Quantity'].isdigit() and row['Price'].isdigit():
                print(row['Product'], "-", row['Quantity'], "шт. за", row['Price'], "р")
                sym += int(row['Quantity']) * int(row['Price'])
            total_cost += 1
        print(f"Итоговая сумма: {sym} р")

from PIL import Image, ImageDraw, ImageFont
def prazd():
    image_path = '../p.hbd.jpg'
    image = Image.open(image_path)
    image.show()
    left = 10
    top = 10
    right = 500
    bottom = 500

    cropped_image = image.crop((left, top, right, bottom))

    new_image_path = 'p.hbd2.jpg'
    cropped_image.save(new_image_path)
    print(f"Обрезанное изображение сохранено как {new_image_path}")
def prazds():
    prazd = {
        'День святого валентина': 'v.pug.jpg',
        'День рождения': 'p.hbd.jpg',
        'Рождество': 'chrism.pug.jpg'
    }
    s = input("Напишите выбранный праздник: ")
    if s == "День святого валентина":
        image_path = prazd[s]
        image = Image.open(image_path)
        image.show()
    elif s == "День рождения":
        image_path = prazd[s]
        image = Image.open(image_path)
        image.show()
    elif s == "Рождество":
        image_path = prazd[s]
        image = Image.open(image_path)
        image.show()
    else:
        print("Введенное значение не найдено в списке.")
def w():
    from PIL import Image, ImageDraw, ImageFont

    name = input("Введите имя: ")
    try:
        image = Image.open("../p.hbd.jpg")
    except IOError:
        print("Ошибка открытия изображения.")
        return

    draw = ImageDraw.Draw(image)

    text = f"{name}, поздравляю!"
    font = ImageFont.truetype('arial.ttf', 20)
    position = ((image.width) // 2, 10)  # Позиция текста в центре вверху
    draw.text(position, text, font=font, fill=(0, 0, 0))  # Исправлено на кортеж RGB
    image.save("new_pug.hbd.png")  #не указываем расширение

while True:
    print('1. обрезка')
    print('2. выбор')
    print('3. знак')
    print('4. Выход')
    a = int(input('Выберите действие: '))
    if a == 1:
        prazd()
    elif a == 2:
        prazds()
    elif a == 3:
        w()
    elif a == 4:
        break
    else:
        print('Неверное действие')