# Hook Plug

[![Build Status](https://travis-ci.com/dunossauro/hook_plug.svg?branch=master)](https://travis-ci.com/dunossauro/hook_plug)
[![Coverage Status](https://coveralls.io/repos/github/dunossauro/hook_plug/badge.svg?branch=master)](https://coveralls.io/github/dunossauro/hook_plug?branch=master)

Are you tired of repeating the same components in every project? Are you tired of writing modules and more modules to hook interaction with Python BDD frameworks? Have problems with external modules that need to be rewritten to conform to BDD hooks?

The main idea of `hook plug` is generate an integration mechanism for your modules and reuse the structure created for other modules.



### Why I need this?

For example, imagine stuffing your environment configuration file with all your `befores` and` afters`

```Python
from my_module import (
    before_all,
    after_all,
    before_tag
)
import my_similar_module  # YES, namespace sucks
from my_third_module import context_variables, tag_action


def before_scenario(context, scenario):
    before_all(context, scenario)
    my_second_module.before_all(context, scenario)
    context.context_variables = context_variables


def after_all(context):
    after_all(context)
    my_second_module.after_all(context)


def before_tag(context, tag):
    if context.context_variables.selectec == tag:
        tag_action()
    before_tag(context, tag)
    my_second_module.before_tag(context, tag)
```



### WOW that's cool. But how would you solve this problem?

Using `hook plug` you could write your modules in plugins and registers format in` environment_hooks`, using `register_hooks` function, and no longer worry about module interactions that pollute your environment file. Let's see the simple example:

environment.py

```Python
from plugins import ListFiles, Browser_stuff  # my plugin
from hook_plug import environment_hooks, register_hooks

register_hooks(ListFiles(), Browser_stuff())


def before_scenario(context, scenario):
    environment_hooks.hook.before_scenario(context=context, scenario=scenario)  # yes, it's not so cool, but works.


def after_all(context):
    environment_hooks.hook.after_all(context=context)
```

plugins.py - Two plugins example

```Python
from hook_plug import tag_behavior
from selenium import webdriver
from requests import get
from os import listdir


class ListFiles:
    @tag_behavior
    def before_scenario(self, context, scenario):
        context.files = listdir()


class Browser_stuff:
    def _check_selenium_grid(grid_url):
        return get(grid_url).status_code == 200

    @tag_behavior
     def before_all(self, context):
        if _check_selenium_grid(context.config.userdata.get('SELENIUM_GRID')):
        	context.browser = webdriver.Firefox()
         context.browser = None
        context.url_prefix = 'https'

    @tag_behavior
    def before_tag(self, context, tag):
		if tag == 'no_ssl':
            context.url_prefix = 'http'
```

steps.py - using context plugged values

```Python
@then('check files in path')
def check_files(context):
    assert context.files

@when('acess the google page')
def get_url(context):
    assert context.browser.get(f'{context.url_prefix}://google.com')
```

That's it, all the complexity of the module and big things that can be implemented in more than one project or pollute your configuration file can become plugins and live totally uncoupled from your project. This is the idea of `hook plug`
