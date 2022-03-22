import input_while_true
import mock

with mock.patch('builtins.input', side_effect=["two","no","1"]):
    assert input_while_true.ask_number_usr() == 1