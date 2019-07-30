from plugins.list_files import ListFiles
from plugins.tagged import Tagged
from hook_plug import environment_hooks, register_hooks

register_hooks(ListFiles(), Tagged())


def before_scenario(context, scenario):
    environment_hooks.hook.before_scenario(context=context, scenario=scenario)


def before_tag(context, tag):
    environment_hooks.hook.before_tag(context=context, tag=tag)
