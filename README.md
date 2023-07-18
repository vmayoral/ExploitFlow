# ExploitFlow

ExploitFlow (`EF`) is a modular library to produce cybersecurity exploitation routes (*exploit flows*). It aims to combine and compose exploits from different sources and frameworks, capturing the state of the system being tested in a *flow* after every discrete action.

It's main motivation is to facilitate and empower Game Theory and Artificial Intelligence (AI) research in cybersecurity. To facilitate adoption, EF's syntax and architecture is inspired by TensorFlow[^1][^2]. To simplify exploitation, EF represents each action in an exploitation route with the superclass `Exploit`, including *reconnaissance* and *control* actions[^4]. Exploits are grouped in 6 major categories inspired by the security kill chain [^3]:

1. Reconnaissance and weaponization - *reconnaissance*
2. Exploitation - *exploitation*
3. Privilege escalation - *escalation*
4. Lateral movement - *lateral*
5. Data exfiltration - *exfiltration*
6. Command and control - *control*

`EF` is a modular, extensible (accepting connectors for other exploitation frameworks and/or individual exploits) and composeable library to empower Artificial Intelligence (AI) research in cybersecurity. EF is <ins>**not an exploitation framework**</ins>.


### Antigoals

**Legal disclaimer**
*Access to this library and the use of information, materials (or portions thereof), is not intended, and is prohibited, where such access or use violates applicable laws or regulations.  By no means the authors encourage or promote the unauthorized tampering with running systems. This can cause serious human harm and material damages*.

*By no means the authors of ExploitFlow encourage or promote the unauthorized tampering with compute systems*. Please don't use the source code in  here to:

- Favour cybercrime. Pentest instead for good.
- Create yet another exploitation framework, there're already too many.
- Create a new exploit database. Contribute an adapter instead.

### Usage
```python
import exploitflow as ef

flow = ef.Flow()
a = ef.placeholder()
print(flow.run(a))  # None
```

### Simplified development
ExploitFlow has been developed and integrated in both Theia and VSCode. More the more complex setups, this repo allows to ["Develop inside of a Container"](https://code.visualstudio.com/docs/remote/containers#_quick-start-try-a-development-container). If you wish to test things out, try the following:

```
- Open repository in VSCode
- Install/Launch Docker in your OS
- (inside of VSCode toolbar) Remote-Containers: Reopen in Container
- (inside of VSCode toolbar) Dev Containers: Reopen Folder Locally (to exit from container)
- (inside of VSCode toolbar) Dev Containers: Rebuild and Reopen Folder in Container (to rebuild container)
```

Then, to launch an example, open one of the [`examples`](examples), e.g. `0_empty.py` and then press `fn + ctrl + F5` to execute (or `fn + F5` do debug).


## Adapters
Adapters are EF's connectors to other exploitation frameworks, so that their exploits can be used while building *exploit flows*. Through adapters EF remains both modular and extensible.

Currently the following adapters are available:
- `AdapterMSF`: an adapter for the **M**eta**S**ploit **F**ramework



[^1]: Tensorflow. See https://www.tensorflow.org.

[^2]: MiniFlow. A minimal numerical computation library with TensorFlow APIs.

[^3]: Kamhoua, C. A., Leslie, N. O., & Weisman, M. J. (2018). Game theoretic modeling of advanced persistent threat in internet of things. Journal of Cyber Security and Information Systems.

[^4]: We are well aware that strictly speaking reconnaissance scripts don't meet the formal definition of an exploit but still insist on grouping all action under the same common class (`Exploit`) to simplify the production of exploitation flows (routes).