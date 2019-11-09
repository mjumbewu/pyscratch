<p align="center">
  <img src="https://github.com/kadir014/pyscratch/blob/master/pyscratch/assets/pyscratch-logo-bg.png"><br>
  <img src="https://img.shields.io/badge/python-3%2B-green.svg">
  <img src="https://img.shields.io/badge/pygame-1.9.6%2B-green.svg">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg">
  <img src="https://img.shields.io/badge/status-pre--alpha-red.svg">
</p>

---
[Scratch](https://en.wikipedia.org/wiki/Scratch_(programming_language)) is a block-based visual programming language and **pyscratch** is an interface to use Scratch in Python. Unfortunately you can not import or export Scratch project files **for now.**

## Usage
```python
from pyscratch import *

#Initialization
project.size = (640, 480)
project.name = "Scratch Project"

@run
def main():
    #Processing
```

## Table of Contents
- [Sprite](#sprite)
- [Blocks](#blocks)
- [Parameters](#parameters)
- [Cloud](#license)
- [License](#license)

## Sprite
The sprite class which has the same properties with Scratch sprites, you can add costume to your sprite with `Sprite.add_costume(costume_name, filepath)` both parameters are string, costume name can be whatever you want. Example filepath: `"pyscratch/assets/scratch-cat.png"`

## Blocks
Scratch blocks included in pyscratch
- [Motion](#motion)
- [Looks](#looks)
- [Events](#events)
- [Control](#control)
- [Sensing](#sensing)
- [Pen](#pen)
- [Custom Blocks](#custom-blocks)

###### Motion
| Scratch | Python | Integrated | Notes |
|---------------------------------|----------------------------|:-----------:|-----------------------------------------|
| Move `10` steps | Sprite.move(10) | ✔️ |  |
| Turn ↻ `15` degrees | Sprite.turn(15, True) | ✔️ | Second parameter is False by default |
| Turn ↺ `15` degrees | Sprite.turn(15, False) | ✔️ | Second parameter is False by default |
| Go to `location` | Sprite.goto(location) | ✔️ | See [parameters](#parameters) reference |
| Go to x: `0` y: `0` | Sprite.goto((0, 0)) | ✔️ |  |
| Glide `1` secs to `location` | Sprite.glide(1, location) | ❌ | See [parameters](#parameters) reference |
| Glide `1` secs to x: `0` y: `0` | Sprite.glide(1, (0, 0)) | ❌ |  |
| Point in direction `90` | Sprite.dir = 90 | ✔️ |  |
| Point towards `location` | Sprite.point_to(location) | ✔️ | See [parameters](#parameters) reference |
| Set x to `0` | Sprite.x = 0 | ✔️ |  |
| Set y to `0` | Sprite.y = 0 | ✔️ |  |
| Change x by `10` | Sprite.x += 10 | ✔️ |  |
| Change y by `10` | Sprite.y += 10 | ✔️ |  |
| If on edge, bounce | Sprite.edge_bounce() | ✔️ |  |
| Set rotation style `rotation` | Sprite.rotation_style(rotation) | ✔️ | See [parameters](#parameters) reference |
| X position | Sprite.x | ✔️ | Attribute |
| Y position | Sprite.y | ✔️ | Attribute |
| Direction | Sprite.dir | ✔️ | Attribute |

###### Looks
| Scratch | Python | Integrated | Notes |
|--------------------------------|-----------------------------------|:----------:|----------------------------------------------|
| Say `Hello!` | Sprite.say("Hello!") | ❌ |  |
| Say `Hello!` for `2` seconds | Sprite.say("Hello!", 2) | ❌ |  |
| Think `Hmm.` | Sprite.think("Hmm.") | ❌ |  |
| Think `Hmm.` for `2` seconds | Sprite.think("Hmm.", 2) | ❌ |  |
| Switch costume to `costume1` | Sprite.set_costume("costume1") | ✔️ | Costume's name was determined by user |
| Next costume | Sprite.next_costume() | ✔️ |  |
| Switch backdrop to `backdrop1` | Sprite.set_backdrop("backdrop1") | ❌ | Backdrop's name is determined by user |
| Next backdrop | Sprite.next_backdrop() | ❌ |  |
| Set size to `100`% | Sprite.set_size(100) | ❌ |  |
| Change size by `10` | Sprite.change_size(10) | ❌ |  |
| Set `effect` effect to `0` | Sprite.set_effect(effect, 0) | ❌ | See [parameters](#parameters) reference |
| Change `effect` effect by `25` | Sprite.change_effect(effect, 25) | ❌ | See [parameters](#parameters) reference |
| Clear graphic effects | Sprite.clear_effects() | ❌ |  |
| Show | Sprite.show() | ✔️ |  |
| Hide | Sprite.hide() | ✔️ |  |
| Go to `front` layer | Sprite.set_layer("front") | ❌ | Only params are `"front"` and `"back"` |
| Go `forward` `1` layers | Sprite.change_layer("forward", 1) | ❌ | Only params are `"forward"` and `"backward"` |
| Costume `number` | Sprite.costume("number") | ✔️ | Only params are `"number"` and `"name"` |
| Backdrop `number` | Sprite.backdrop("number") | ❌ |  |
| Size | Sprite.size | ❌ | Attribute |

###### Events

###### Control

###### Sensing
| Scratch | Python | Integrated | Notes |
|------------------------|----------------------------|:----------:|-------------------------------------------|
| Touching `mouse pointer`? | Sprite.touching("mouse-pointer") | ❌ | Only params are `"mouse-pointer"`, `"edge"` and [Sprite](#sprite) instance |
| Touching color `color`? |  | ❌ | Color reporters may not be done |
| `color` is touching `color`? |  | ❌ |  |
| Distance to `mouse pointer` | Sprite.distance("mouse-pointer") | ❌ | Only params are `"mouse-pointer"` and [Sprite](#sprite) instance |
| Ask `something` and wait | Sprite.ask("something") | ❌ |  |
| Answer | Sprite.answer | ❌ |  |
| Key `space` pressed? | key_pressed("space") | ✔️ | See [Key Dictionary](https://github.com/kadir014/pyscratch/blob/master/pyscratch/keys.py) to see key parameters |
| Mouse down? | mouse_down(button) | ✔️ | Only params are `"left"`, `"right"` and `"middle"` |
| Mouse x | mouse.x | ✔️ |  |
| Mouse y | mouse.y | ✔️ |  |
| Set drag mode `draggable` | Sprite.drag("draggable") | ❌ | Only params are `"draggable"` and `"not-draggable"` |
| Loudness | loudness | ❌ |  |
| Timer | timer.secs | ✔️ |  |
| Reset timer | timer.reset() | ✔️ |  |
| `value` of `sprite` | Sprite["value"] | ❌ |  |
| Current `date` | current(date) | ❌ | See [parameters](#parameters) reference |
| Days since 2000 | days_since_2000 | ❌ |  |
| Username | username | ❌ |  |

###### Pen

###### Custom Blocks

## Parameters
`location` parameter can be
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

`date` parameter can be
- Year → `"year"`
- Month → `"month"`
- Date → `"date"`
- Day of the week → `"day"`
- Hour → `"hour"`
- Minute → `"minute"`
- Second → `"second"`

## Cloud
Cloud connection is in progress.

## License
[MIT](LICENSE) © Kadir Aksoy
