from nose.tools import * 
from bin.app import app
from tests.tools import assert_response

def test_index():
    # check that we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp, status="303")

    # test our first GET request to /game
    resp = app.request("/game")
    assert_response(resp)

    # make sure default values work for the form
    resp = app.request("/game", method="POST")
    assert_response(resp, status="303")

    # test that we get expected values
    resp = app.request("/game", method="GET")
    assert_response(resp, status="200")

def test_game():
	#check that we get a 200 on /game
	resp = app.request("/game")
	assert_response(resp)

	#check that we have response data on a form submit
	resp = app.request("/game",method='POST')
	assert_response(resp,status="303")

