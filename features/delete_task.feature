Feature: In order to delete
Scenario: Delete task
  Given I want to delete"/tasks2"
  When ba "new_task2" ab "Buy bread and milk and beer,2 it's friday!!!" ba "add_2task"
  Then beee "Buy bread and milk and beer, it's friday2!!!"