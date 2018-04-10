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
def step_impl(context,text):
    br = context.browser
    assert text in br.page_source