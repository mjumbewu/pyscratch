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
- [Parameters](#parameters)
- [Cloud](#license)
- [License](#license)

## Sprite
Sprite class

## Blocks
Scratch blocks included in pyscratch
- [Motion](#motion)
- [Looks](#looks)
- [Events](#events)
- [Control](#control)
- [Sensing](#sensing)
- [Pen](#pen)
- [Custom Blocks](#custom blocks)

###### Motion
| Scratch | Python | Integrated | Notes |
|---------------------------------|----------------------------|:-----------:|-----------------------------------------|
| Move `10` steps | sprite.move(10) | ✔️ |  |
| Turn ↻ `15` degrees | sprite.rotate(15, True) | ❌ | Second parameter is False by default |
| Turn ↺ `15` degrees | sprite.rotate(15, False) | ❌ | Second parameter is False by default |
| Go to `object` | sprite.goto(object) | ❌ | See [parameters](#parameters) reference |
| Go to x: `0` y: `0` | sprite.goto((0, 0)) | ❌ |  |
| Glide `1` secs to `object` | sprite.glide(1, object) | ❌ | See [parameters](#parameters) reference |
| Glide `1` secs to x: `0` y: `0` | sprite.glide(1, (0, 0)) | ❌ |  |
| Point in direction `90` | sprite.point_dir(90) | ❌ |  |
| Point towards `object` | sprite.point_to(object) | ❌ | See [parameters](#parameters) reference |
| Set x to `0` | sprite.set_x(0) | ❌ |  |
| Set y to `0` | sprite.set_y(0) | ❌ |  |
| Change x by `10` | sprite.add_x(10) | ❌ |  |
| Change y by `10` | sprite.add_y(10) | ❌ |  |
| If on edge, bounce | sprite.edge_bounce = True | ❌ | It is False by default |
| Set rotation style `rotation` | sprite.set_rot(rotation) | ❌ | See [parameters](#parameters) reference |
| X position | sprite.x | ❌ | Attribute |
| Y position | sprite.y | ❌ | Attribute |
| Direction | sprite.dir | ❌ | Attribute |

###### Looks
| Scratch | Python | Integrated | Notes |
|--------------------------------|-----------------------------------|:----------:|----------------------------------------------|
| Say `Hello!` | sprite.say("Hello!") | ❌ |  |
| Say `Hello!` for `2` seconds | sprite.say("Hello!", 2) | ❌ |  |
| Think `Hmm.` | sprite.think("Hmm.") | ❌ |  |
| Think `Hmm.` for `2` seconds | sprite.think("Hmm.", 2) | ❌ |  |
| Switch costume to `costume1` | sprite.set_costume("costume1") | ❌ | Costume's name is determined by user |
| Next costume | sprite.next_costume() | ❌ |  |
| Switch backdrop to `backdrop1` | sprite.set_backdrop("backdrop1") | ❌ | Backdrop's name is determined by user |
| Next backdrop | sprite.next_backdrop() | ❌ |  |
| Change size by `10` | sprite.change_size(10) | ❌ |  |
| Set size to `100`% | sprite.set_size(100) | ❌ |  |
| Set `effect` effect to `0` | sprite.set_effect(effect, 0) | ❌ | See [parameters](#parameters) reference |
| Change `effect` effect by `25` | sprite.change_effect(effect, 25) | ❌ | See [parameters](#parameters) reference |
| Clear graphic effects | sprite.clear_effects() | ❌ |  |
| Show | sprite.show() | ❌ |  |
| Hide | sprite.hide() | ❌ |  |
| Go to `layer` layer | sprite.set_layer(layer) | ❌ | Only params are `"front"` and `"back"` |
| Go `forward` `1` layers | sprite.change_layer("forward", 1) | ❌ | Only params are `"forward"` and `"backward"` |
| Costume `number` | sprite.costume("number") | ❌ | Only params are `"number"` and `"name"` |
| Backdrop `number` | sprite.backdrop("number") | ❌ |  |
| Size | sprite.size | ❌ | Attribute |

###### Events

###### Control

###### Sensing

###### Pen

###### Custom Blocks

## Parameters
`object` parameter can be
- Random position → `"random-position"`
- Mouse pointer's position → `"mouse-position"`
- Another sprite's position → [Sprite](#sprite) instance

`rotation` parameter can be
- Only left and right → `"left-right"`
- No rotations → `"no-rotate"`
- All around → `"all-around"`

`effect` parameter can be
- Color → `"color"`
- Ghost → `"ghost"`

## Cloud
Cloud connection

## License
[MIT](LICENSE) © Kadir Aksoy
