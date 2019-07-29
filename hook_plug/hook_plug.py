"""Tag plugger."""
from pluggy import HookspecMarker, HookimplMarker, PluginManager

hookspec = HookspecMarker('Tag Plug')
environment_hooks = PluginManager('Tag Plug')
tag_behavior = HookimplMarker("Tag Plug")


class BDDHooks:
    @hookspec
    def before_all(self, context):
        ...

    @hookspec
    def before_feature(self, context, feature):
        ...

    @hookspec
    def before_scenario(self, context, scenario):
        ...

    @hookspec
    def before_tag(self, context, tag):
        ...

    @hookspec
    def before_step(self, context, step):
        ...

    @hookspec
    def after_all(self, context):
        ...

    @hookspec
    def after_feature(self, context, feature):
        ...

    @hookspec
    def after_scenario(self, context, scenario):
        ...

    @hookspec
    def after_tag(self, context, tag):
        ...

    @hookspec
    def after_step(self, context, step):
        ...


environment_hooks.add_hookspecs(BDDHooks)


def register_hooks(*plugins):
    for plugin in plugins:
        environment_hooks.register(plugin)
