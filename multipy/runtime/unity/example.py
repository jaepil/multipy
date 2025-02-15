# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

# pyre-unsafe

import numpy as np
import scipy
from scipy import linalg

print("Hello, torch::deploy unity!")
print(f"np.random.rand(5): {np.random.rand(5)}")
print(f"scipy {scipy}")
mat_a = np.array([[1, 0, 0, 0], [1, 1, 0, 0], [1, 2, 1, 0], [1, 3, 3, 1]])
mat_b = linalg.inv(mat_a)
print(mat_b)
