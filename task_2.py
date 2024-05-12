def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 0
 
    while low <= high:

        count += 1
 
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return count, arr[mid]
 
    # якщо елемент не знайдений
    if mid >= 0:
        if arr[mid] < x:
            return count, arr[mid + 1] if mid + 1 < len(arr) else None
        else:
            return count, arr[mid]
    else:
        return count, arr[low] if low < len(arr) else None


