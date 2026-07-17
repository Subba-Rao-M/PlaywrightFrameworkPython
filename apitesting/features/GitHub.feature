
Feature: GitHub API validation
  # Enter feature description here

  @session
  Scenario: Session management check
    Given I have github auth credentials
    When I hit getRepo API of github
    Then status code of response should be 200
    # Enter steps here