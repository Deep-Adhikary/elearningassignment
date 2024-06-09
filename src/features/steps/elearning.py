from behave import given,when,then

import sys
import os

sys.path.append(os.path.abspath('./'))

from repository.landing_page import LandingPage
from repository.project_page import ProjectPage

@given('User has navigated to the projects page')
def user_hase_navigated_to_project_page(context):
    context.driver.get(context.page_url)
    context.landing_page=LandingPage(context.driver,context.explicit_wait_time)
    context.landing_page.page_header.is_displayed()
    context.screenshot.capture()
    context.landing_page.start_button.click()

@when('User opens the learning "{learning_name}"')
def user_opens_project(context,learning_name):
    context.landing_page.get_project_link(learning_name).is_displayed()
    context.screenshot.capture()
    context.landing_page.get_project_link(learning_name).click()
    context.screenshot.capture()

@then('The learning with header "{learning_header}" should open')
def project_should_open(context,learning_header):
    context.project_page=ProjectPage(context.driver,context.explicit_wait_time)
    context.project_page.get_project_header(learning_header).is_displayed()
    context.screenshot.capture()
     
@when('User read the learning score')
def user_read_learning_score(context):
    context.score=context.landing_page.learning_score.text

@then('The score should be in numbers')
def the_score_should_be_in_numbers(context):
    context.screenshot.capture()
    assert context.score.isnumeric()==True

@when('The user has navigated to Judging page')
def the_user_has_navigated_to_judging_page(context):
    context.project_page=ProjectPage(context.driver,context.explicit_wait_time)
    context.screenshot.capture()
    context.project_page.get_judge_button.click()

@when('The user vote option "{option}"')
def the_user_vote(context,option):
    context.project_page.get_answer_radio_button(option).click()
    context.screenshot.capture()
    context.project_page.vote_button.click()

@then('response should be "{option}"')
def the_user_response_should_be(context,option):
    context.screenshot.capture()
    assert context.project_page.get_response_header_text(option).is_displayed()==True