# Copyright 2022 Víctor Mayoral-Vilches. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# A exploit flow that combines various
# basic operations over trivial exploits
# (Constant, Bool), etc.
#
# Aims to demonstrate composition of exploits.
#
# ┌────────────┐  []   ┌────────────┐
# │ Constant_1 │ ◀──── │    Init    │
# └────────────┘       └────────────┘
#   │                    │
#   │ [3]                │ []
#   ▼                    ▼
# ┌────────────┐       ┌────────────┐
# │   Mul_1    │       │  Constant  │
# └────────────┘       └────────────┘
#   │                    │
#   │                    │ [1]
#   │                    ▼
#   │                  ┌────────────┐
#   │                  │    Mul     │
#   │                  └────────────┘
#   │                    │
#   │                    │ [1]
#   │                    ▼
#   │                  ┌────────────┐
#   │                  │ Constant_0 │
#   │                  └────────────┘
#   │                    │
#   │                    │ [1, 2]
#   │                    ▼
#   │                  ┌────────────┐
#   │                  │   Mul_0    │
#   │                  └────────────┘
#   │                    │
#   │                    │
#   │                    ▼
#   │                  ┌────────────┐
#   └────────────────▶ │    Add     │
#                      └────────────┘
#                        │
#                        │ [1, 2, 3]
#                        ▼
#                      ┌────────────┐
#                      │    Bool    │
#                      └────────────┘
#                        │
#                        │ [1, 2, 3]
#                        ▼
#                      ┌────────────┐
#                      │   Mul_2    │
#                      └────────────┘


import exploitflow as ef
from exploitflow.state import State_v0

flow = ef.Flow(State_v0)  # use basic data model
init = ef.Init()

c = ef.Constant(1)  # Constant
d = ef.Constant(2)  # Constant_0
e = ef.Constant(3)  # Constant_1
f = ef.Boolean(False)

print(flow.run(((init * c * d) + (init * e)) * f, debug=False, target="127.0.0.1"))
print(flow.ascii())