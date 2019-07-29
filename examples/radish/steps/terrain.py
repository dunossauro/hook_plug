from radish import before, world
from hook_plug import environment_hooks, register_hooks

from hook_plug import tag_behavior
from os import listdir


class ListFiles:
    @tag_behavior
    def before_scenario(self, context, scenario):
        context.files = listdir()

    @tag_behavior
    def before_tags(self, context, tag):
        context.tag_files = {'before_tags files': listdir()}


register_hooks(ListFiles())


@before.each_scenario
def before_scenario(scenario):
    environment_hooks.hook.before_scenario(context=world, scenario=scenario)
