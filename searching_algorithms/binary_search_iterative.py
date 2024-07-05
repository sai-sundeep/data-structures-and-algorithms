# Created by Sai at 7/5/2024
from sorting_algorithms.merge_sort import merge_sort


def binary_search(arr, key):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def run_test_client():
    test_arrs = [
        [426, 549, 710, 599, 921, 12, 258, 983, 66, 996],
        [32, 422, 167, 304, 482, 631, 305, 895, 642, 838],
        [25, -815, 860, -70, -670, 17, 606, -869, -737, -289],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
        [9450, 1614, 12229, 4827, 13866, 5408, 7363, 14852, 9213, 8038, 12192, 14820, 8165, 4489, 12507, 2197, 12625, 589, 6792, 7925, 8855, 2275, 6908, 8456, 13692, 6894, 4330, 13470, 8682, 14520, 3388, 10479, 6947, 13786, 6176, 381, 5245, 10625, 6295, 7217, 4822, 4838, 7910, 1892, 14854, 13472, 85, 9306, 2553, 1591, 11023, 3635, 10294, 11804, 4445, 9877, 3185, 8209, 7957, 12950, 4872, 14256, 10395, 6526, 3466, 7997, 7672, 6256, 907, 11477, 12604, 5009, 5872, 1864, 817, 5074, 13662, 11089, 898, 238, 4695, 3554, 10918, 7518, 9756, 4806, 1265, 10974, 11896, 10226, 6434, 8036, 6506, 11060, 11517, 14514, 6998, 9284, 9860, 1721],
        [-5794, -3781, -5180, -6770, -5132, -8046, -8694, -3781, -6693, -8141, -6990, -7340, -9109, -9052, -5236, -3088, -2348, -7079, -5723, -2980, -9479, -2398, -2588, -9618, -6306, -6906, -8602, -8269, -2557, -7159, -4840, -8016, -7460, -548, -6570, -2089, -2697, -2131, -4845, -484, -3654, -1807, -8181, -2676, -6208, -2923, -746, -7676, -1912, -375, -7673, -1340, -1630, -5149, -1233, -9855, -6143, -4906, -1655, -9415, -5686, -3363, -1935, -3279, -5012, -8207, -4615, -4552, -5765, -1116, -6969, -117, -2053, -4560, -2791, -9099, -1753, -3672, -2923, -6693, -2438, -9546, -9282, -2683, -4356, -3537, -5709, -3261, -6288, -6782, -992, -9760, -6510, -555, -831, -98, -2421, -1156, -9897, -1856]
    ]
    test_keys = [921, 4390, 606, -1, 9877, -5794]
    for arr, key in zip(test_arrs, test_keys):
        merge_sort(arr, 0, len(arr))  # Binary Search requires arr to be pre-sorted
        # print(arr)  # Uncomment for debug
        key_index = binary_search(arr, key)
        if key_index != -1:
            print(f"{key} is located at index {key_index}")
        else:
            print(f"{key} not present in the list.")


if __name__ == "__main__":
    run_test_client()
