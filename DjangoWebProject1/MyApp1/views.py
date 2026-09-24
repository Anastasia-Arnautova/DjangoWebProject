import asyncio
from django.shortcuts import render

# Масив даних
data = [2, 7, 5, 6, 9, 3, 2, 7, 9, 1, 3, 9]

class AsyncTasks:
    def __init__(self, data):
        self.data = data

    # 1 задача - сума сусідніх елементів
    async def sum_of_neighbors(self):
        result = [self.data[i] + self.data[i + 1] for i in range(len(self.data) - 1)]
        await asyncio.sleep(1)  # Симуляція асинхронного виконання
        return result

    # 2 задача - добуток сусідніх елементів
    async def product_of_neighbors(self):
        result = [self.data[i] * self.data[i + 1] for i in range(len(self.data) - 1)]
        await asyncio.sleep(1)
        return result

    # 3 задача - сортування бульбашкою
    async def bubble_sort(self):
        sorted_data = self.data[:]
        n = len(sorted_data)
        for i in range(n):
            for j in range(0, n-i-1):
                if sorted_data[j] > sorted_data[j+1]:
                    sorted_data[j], sorted_data[j+1] = sorted_data[j+1], sorted_data[j]
        await asyncio.sleep(1)
        return sorted_data

# Асинхронна view-функція для рендеру результатів на веб-сторінку
async def async_view(request):
    tasks = AsyncTasks(data)

    # Виконання всіх задач одночасно
    sum_result, product_result, sorted_result = await asyncio.gather(
        tasks.sum_of_neighbors(),
        tasks.product_of_neighbors(),
        tasks.bubble_sort()
    )

    # Передаємо результати у шаблон
    context = {
        'sum_of_neighbors': sum_result,
        'product_of_neighbors': product_result,
        'bubble_sort': sorted_result
    }

    # Рендеримо HTML-сторінку з результатами
    return render(request, 'MyApp1/index.html', context)
