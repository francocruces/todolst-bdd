@given(u'I go to "{url}')
def step_impl(context,url):
    br = context.browser
    br.get(context.base_url + url)


@when(u'I fill in field with id "{field}" with "{text}" and I click on "{button}"')
def step_impl(context,field,text,button):
    br = context.browser
    br.find_element_by_id(field).send_keys(text)
    br.find_element_by_id(button).click()


@then(u'I should see "{text}"')
def step_impl(context, text):
    br = context.browser
    assert text in br.page_source

@given(u'I go to the "{url}" and there is already a task "{task}"')
def step_impl(context, url, task):
    br = context.browser
    br.get(context.base_url + url)
    br.find_element_by_id('new_task').send_keys(task)
    br.find_element_by_id('add_task').click()

@then(u'I should see both "{text}" and "{text2}"')
def step_impl(context, text, text2):
    br = context.browser
    assert text in br.page_source
    assert text2 in br.page_source