from hook_plug import tag_behavior


class Tagged:
    @tag_behavior
    def before_tag(self, context, tag):
        if tag == 'tagged':
            context.tagged = True
