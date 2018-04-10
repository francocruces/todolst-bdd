Feature: In order to remember my tasks, as a working person, I want to add tasks to a task list
Scenario: Add task
  Given I go to "/tasks"
  When I fill in field with id "new_task" with "Buy bread and milk and beer, it's friday!!!" and I click on "add_task"
  Then I should see "Buy bread and milk and beer, it's friday!!!"