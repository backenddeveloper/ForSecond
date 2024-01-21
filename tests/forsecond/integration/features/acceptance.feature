Feature: The technical test solution
    For Second Mind to evaluate if I can code in Python

    Scenario: The example given in the brief
    Given a mock file containing the following data:
        '''
        George,Beth, Sue
        Rick,Anne
        Anne,Beth
        Beth, Anne  ,George
         Sue,Beth
        '''
    When we run the application with the mock file
    Then we get the following output:
        '''
        If you start from rick, you can reach 5 <players>
        '''

    Scenario: It complains about an empty file
    Given a mock file containing the following data:
        '''
        '''
    When we run the application with the mock file
    Then it raises an exception with the message:
        '''
        empty graph generated from file
        '''

    Scenario: It complains about an empty name
    Given a mock file containing the following data:
        '''
        ,
        '''
    When we run the application with the mock file
    Then it raises an exception with the message:
        '''
        found an empty name
        '''
