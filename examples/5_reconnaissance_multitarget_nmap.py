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

# A exploit flow that performs reconnaissance locating multiple targets 
# in the local area network and then conducting scans on each one 
# of them to fill up the state

# ┌─────────────────────────────────────────────────────────────────────┐
# │                                Init                                 │
# └─────────────────────────────────────────────────────────────────────┘
#   │
#   │ {}
#   ▼
# ┌─────────────────────────────────────────────────────────────────────┐
# │                           TargetsExploit                            │
# └─────────────────────────────────────────────────────────────────────┘
#   │
#   │ {'192.168.1.1': {'exploits': ['TargetsExploit'], 'ports': []},
#   │ '192.168.1.5': {'exploits': ['TargetsExploit'], 'ports': []},
#   │ '192.168.1.6': {'exploits': ['TargetsExploit'], 'ports': []}}
#   ▼
# ┌─────────────────────────────────────────────────────────────────────┐
# │                                Mul_0                                │
# └─────────────────────────────────────────────────────────────────────┘
#   │
#   │ {'192.168.1.1': {'exploits': ['TargetsExploit'], 'ports': []},
#   │ '192.168.1.5': {'exploits': ['TargetsExploit'], 'ports': []},
#   │ '192.168.1.6': {'exploits': ['TargetsExploit'], 'ports': []}}
#   ▼
# ┌─────────────────────────────────────────────────────────────────────┐
# │                           VersionExploit                            │
# └─────────────────────────────────────────────────────────────────────┘
#   │
#   │ {'192.168.1.1': {'exploits': ['VersionExploit', 'TargetsExploit'],
#   │ 'ports': ['port: 111, name: rpcbind, version: 2-4']},
#   │ '192.168.1.5': {'exploits': ['TargetsExploit'], 'ports': []},
#   │ '192.168.1.6': {'exploits': ['TargetsExploit'], 'ports': []}}
#   ▼
# ┌─────────────────────────────────────────────────────────────────────┐
# │                                 Mul                                 │
# └─────────────────────────────────────────────────────────────────────┘

import exploitflow as ef

flow = ef.Flow()
init = ef.Init()

# Build nmap reconnaissance exploit
recon = ef.Targets()
# versions = ef.Versions(ports=ef.state.TARGET_PORTS_BASIC)
versions = ef.Versions(ports=ef.state.TARGET_PORTS_COMPLETE)


# initialize state and pass it over a recon action
# resulting flow should deliver a state annotated
# with the results from the reconnaissance step
state = flow.run(init * recon * versions, target="192.168.2.10")
# print(flow.run(init))

# ASCII-depict graph
print(flow.ascii())
flow.to_dot("/tmp/exploitflow.dot")

