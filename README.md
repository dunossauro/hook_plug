# Hook Plug

[![Build Status](https://travis-ci.com/dunossauro/hook_plug.svg?branch=master)](https://travis-ci.com/dunossauro/hook_plug)

Hook Plug is an extension for testing frameworks. This provides the possibility of decoupling hook responsibilities and extending it with plugins.


## [Behave example](.examples/behave)

environment.py
```Python
from plugins.list_files import ListFiles
from hook_plug import environment_hooks, register_hooks

register_hooks(ListFiles())


def before_scenario(context, scenario):
    environment_hooks.hook.before_scenario(context=context, scenario=scenario)
```

list_files.py - A plugin

```Python
from hook_plug import tag_behavior
from os import listdir


class ListFiles:
    @tag_behavior
    def before_scenario(self, context, scenario):
        context.files = listdir()
```

steps.py - using context plugged values

```Python
@then('list_files')
def step_impl(context):
    assert context.files
```

## [Radish example](./examples/radish)

terrain.py
```Python
from radish import before, world
from hook_plug import environment_hooks, register_hooks

from hook_plug import tag_behavior
from os import listdir


class ListFiles:
    @tag_behavior
    def before_scenario(self, context, scenario):
        context.files = listdir()

register_hooks(ListFiles())


@before.each_scenario
def before_scenario(scenario):
    environment_hooks.hook.before_scenario(context=world, scenario=scenario)
```
