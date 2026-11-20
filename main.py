from pathlib import Path
def insertion_sort(numbers):
    arr = numbers.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])
    return merge(left, right)
def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def main():
    filename = Path(__file__).resolve().parent / "date.txt"
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: date.txt does not exist!")
        return
    except OSError as error:
        print("Error reading file:", error)
        return
    if len(lines) < 2:
        print("Error: The file must contain two input lines!")
        return
    try:
        numbers = [int(x) for x in lines[0].split()]
        if not numbers:
            print("Error: No numbers found in the file!")
            return
    except ValueError:
        print("Error: Invalid numbers! Please enter integers only.")
        return
    algorithm = lines[1].strip().lower()
    if algorithm == "insertion":
        result = insertion_sort(numbers)
        algorithm_name = "Insertion"
    elif algorithm == "merge":
        result = merge_sort(numbers)
        algorithm_name = "Merge"
    else:
        print("Error: Unknown algorithm! Use Insertion or Merge.")
        return
    output = algorithm_name + ": " + " ".join(map(str, result))
    original_data = lines[0].rstrip("\r\n") + "\n"
    original_data += lines[1].rstrip("\r\n") + "\n"
    try:
        with open(filename, "w") as file:
            file.write(original_data)
            file.write(output + "\n")
    except OSError as error:
        print("Error writing file:", error)
        return
    print("Sorting completed successfully!")
    print(output)

if __name__ == "__main__":
    main()
