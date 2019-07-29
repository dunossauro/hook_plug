from radish import then, world


@then('list_files')
def step_impl(step):
    assert world.files
