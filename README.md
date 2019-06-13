# pyscratch
Scratch interface for Python

## Usage

```python
from pyscratch import *

#Initialization

@run
def main():
    #Processing

```

## Table of Contents

- [Sprite](#sprites)
- [Blocks](#blocks)
- [Cloud](#license)
- [License](#license)

## Sprite
Sprite class

## Blocks
Scratch blocks included in pyscratch
- [Motion](#motion)
- [Looks](#looks)
- [Events] (#events)
- [Control] (#control)
- [Sensing] (#sensing)
- [Custom Blocks] (#custom blocks)

##### Motion
| Scratch | Python | Integrated | Notes |
|---------------------|------------------------|:----------:|--------------------------------------|
| Move `10` steps | sprite.move(10) | ✔️ |  |
| Turn ↻ `15` degrees | sprite.rotate(15, True) | ❌ | Second parameter is False by default |
| Turn ↺ `15` degrees | sprite.rotate(15, False) | ❌ |  |

###### Looks

###### Events

###### Control

###### Sensing

###### Custom Blocks

## Cloud
Cloud connection

## License
[MIT](LICENSE) © Kadir Aksoy
