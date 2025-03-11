from PIL import Image
import numpy as np

def bilinear_interpolation_downscale(image_input_path, image_output_path, scale_factor=2):
    img = Image.open(image_input_path)
    img = img.convert('RGB')

    # Получаем размеры исходного изображения
    width, height = img.size

    # Вычисляем размеры нового изображения
    new_width = int(width / scale_factor)
    new_height = int(height / scale_factor)

    # Создаем новое изображение
    new_img = Image.new('RGB', (new_width, new_height))

    # Перебираем пиксели нового изображения
    for x in range(new_width):
        for y in range(new_height):
            # Вычисляем координаты в исходном изображении
            x_src = x * scale_factor
            y_src = y * scale_factor

            # Вычисляем индексы ближайших пикселей
            x1 = int(np.floor(x_src))
            y1 = int(np.floor(y_src))
            x2 = min(x1 + 1, width - 1)
            y2 = min(y1 + 1, height - 1)

            # Вычисляем веса для интерполяции
            t = x_src - x1
            u = y_src - y1

            # Получаем значения пикселей
            p1 = img.getpixel((x1, y1))
            p2 = img.getpixel((x2, y1))
            p3 = img.getpixel((x2, y2))
            p4 = img.getpixel((x1, y2))

            # Вычисляем значения компонентов цвета
            r = int(p1[0] * (1 - t) * (1 - u) + p2[0] * t * (1 - u) + p3[0] * t * u + p4[0] * (1 - t) * u)
            g = int(p1[1] * (1 - t) * (1 - u) + p2[1] * t * (1 - u) + p3[1] * t * u + p4[1] * (1 - t) * u)
            b = int(p1[2] * (1 - t) * (1 - u) + p2[2] * t * (1 - u) + p3[2] * t * u + p4[2] * (1 - t) * u)

            # Устанавливаем пиксель в новом изображении
            new_img.putpixel((x, y), (r, g, b))

    # Сохраняем новое изображение
    new_img.save(image_output_path)
