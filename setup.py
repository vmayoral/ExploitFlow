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

import os
from collections import OrderedDict
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    dependencies = f.read().strip().split('\n')

setup(
    name="exploitflow",
    version="0.2.0",
    description="ExploitFlow, a library to produce cybersecurity exploitation routes",
    long_description="""
    ExploitFlow (EF) is a modular library to produce cybersecurity exploitation routes (exploit flows). It allows to combine and compose exploits from different sources and frameworks, capturing the state of the system being tested in a *flow* after every discrete action.

    It's main motivation is to facilitate and empower Artificial Intelligence (AI) research in cybersecurity. EF's software architecture is inspired by the success of TensorFlow. To facilitate usage, exploits are grouped by categories following the security kill chain.
    """,
    author="Víctor Mayoral-Vilches",
    author_email="v.mayoralv@gmail.com",
    maintainer="Víctor Mayoral-Vilches",
    maintainer_email="v.mayoralv@gmail.com",
    url="https://github.com/vmayoral/ExploitFlow",
    project_urls=OrderedDict(
        (
            ("Code", "https://github.com/vmayoral/ExploitFlow"),
            ("Issue tracker", "https://github.com/vmayoral/ExploitFlow/issues"),
        )
    ),
    license="Apache License",
    install_requires=dependencies,
    packages=find_packages(),
)
