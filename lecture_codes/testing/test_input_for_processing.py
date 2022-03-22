import input_for_processing
import mock

def test_ask_from_user():
    with mock.patch('builtins.input', return_value="yes"):
        assert input_for_processing.ask_from_user() == True
def test_ask_from_user2():
    with mock.patch('builtins.input', return_value="ghhghg"):
        assert input_for_processing.ask_from_user() == False

