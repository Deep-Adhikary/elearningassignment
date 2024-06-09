Feature: Elearning Test

    Scenario Outline: Verify correct learning is loaded
        Given User has navigated to the projects page
        When User opens the learning "<learning_name>"
        Then The learning with header "<expected_header>" should open

        Examples:
            | learning_name               | expected_header                   |
            | Making a case against Kevin | murder has been committed         |
            | Who is to blame?            | young man has been in an accident |

    Scenario: Verify learning score
        Given User has navigated to the projects page
        When User read the learning score
        Then The score should be in numbers

    Scenario Outline: Verify Case 01 learning page with "" judgement
        Given User has navigated to the projects page
        When User opens the learning "Making a case against Kevin"
        And The user has navigated to Judging page
        And The user vote option "Guilty"
        Then response should be "GUILTY!"

        Examples:
            | learning_name               | expected_header           | vote_option | response    |
            | Making a case against Kevin | murder has been committed | Guilty      | GUILTY!     |
            | Making a case against Kevin | murder has been committed | Not Guilty  | NOT GUILTY! |

