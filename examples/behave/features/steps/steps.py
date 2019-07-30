from behave import then


@then('list files')
def step_impl(context):
    assert context.files


@then('list tag files')
def step_impl(context):
    assert context.tag_files
    assert context.tagged
