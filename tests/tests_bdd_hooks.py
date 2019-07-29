from unittest import TestCase
from hook_plug.hook_plug import BDDHooks, environment_hooks
from hook_plug import register_hooks, tag_behavior


class BlankFakePluggin:
    ...


class BeforeAllWrongFakePluggin:
    @tag_behavior
    def before_all():
        return 42


class BeforallFakePluggin:
    @tag_behavior
    def before_all(context):
        return 42


class TestBDDHooks(TestCase):
    def test_should_has_bdd_env_methods(self):
        bdd_methods = [
            'before_all',
            'before_feature',
            'before_scenario',
            'before_tag',
            'before_step',
            'after_all',
            'after_feature',
            'after_scenario',
            'after_tag',
            'after_step',
        ]
        for method in bdd_methods:
            with self.subTest(method=method):
                self.assertTrue(hasattr(BDDHooks, method))


class TestRegisterHooks(TestCase):
    def test_should_registrate_plugins(self):
        register_hooks(BlankFakePluggin())
        self.assertIsInstance(
            environment_hooks.get_plugins().pop(),
            BlankFakePluggin
        )


class TestTagBehavior(TestCase):
    def test_should_raise_when_call_wrong_definition(self):
        register_hooks(BeforeAllWrongFakePluggin())

        with self.assertRaises(TypeError):
            environment_hooks.hook.before_all()
