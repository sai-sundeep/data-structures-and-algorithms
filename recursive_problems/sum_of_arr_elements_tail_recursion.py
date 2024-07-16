"""
Author: Sai Sundeep Rayidi
Date: 7/16/2024

Description:
[Description of what the file does, its purpose, etc.]

Additional Notes:
[Any additional notes or information you want to include.]

License: 
MIT License

Copyright (c) 2024 Sai Sundeep Rayidi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Contact:
[Optional: How to reach you for questions or collaboration.]

"""

import numpy as np
np.random.seed(10)


def tail_recursive_summation(arr, n, curr_sum=0):
    if n == 0:
        return curr_sum
    return tail_recursive_summation(arr, n - 1, arr[n-1] + curr_sum)


def run_test_client():
    test_arrs = [
        np.random.randint(1, 100, 10),
        np.random.randint(-100, 100, 20),
        np.random.randint(1, 10000, 20),
        np.random.randint(-100000, 100000, 20),
        np.random.randint(0, 2, 200)
    ]
    for arr in test_arrs:
        print(arr)
        print(f"Sum: {tail_recursive_summation(arr, len(arr))}")
        print("=" * 100)


if __name__ == "__main__":
    run_test_client()