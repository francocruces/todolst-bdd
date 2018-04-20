Feature: In order to remember my tasks, as a working person, I want to add tasks to a task list
Scenario: Add a single task
  Given I go to "/tasks"
  When I fill in field with id "new_task" with "Buy bread, milk and beer, it's friday!!!" and I click on "add_task"
  Then I should see "Buy bread, milk and beer, it's friday!!!"
  
Scenario: Add another task
  Given I go to the "/tasks" and there is already a task "Buy bread, milk and beer, it's friday!!!"
  When I fill in field with id "new_task" with "Shave the cat" and I click on "add_task"
  Then I should see both "Buy bread, milk and beer, it's friday!!!" and "Shave the cat"