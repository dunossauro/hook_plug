from hook_plug import tag_behavior
from os import listdir


class ListFiles:
    @tag_behavior
    def before_scenario(self, context, scenario):
        context.files = listdir()

    @tag_behavior
    def before_tag(self, context, tag):
        if tag == 'tagged_file':
            context.tag_files = {'before_tag files': listdir()}
