"""
Test module to test board setup.
"""
# from pytest_bdd import scenario, given, when, then
# from code.idioten_setup import game_setup
#
# BOARD = []
#
# @pytest.fixture()
# def board_empty():
#     board == []
#     return board
#
# @scenario('idioten_setup.feature', 'Verify board setup and empty when initiated')
# def test_board_set_up():
#     pass
#
# @given('board not setup', BOARD)
# def board_not_setup(board_empty):
#     board = board_empty()
#     assert board == []
#
# @when('setup is called', BOARD)
# def call_setup(BOARD):
#     board = game_setup()
#     return board
#
# @then('board is setup', BOARD)
# def board_is_setup():
#     pass