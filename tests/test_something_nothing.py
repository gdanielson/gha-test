import logging
import pytest
from src.something_nothing import main


def test_main_normal_flow(mocker):
    # Spy on the logging methods
    spy_info = mocker.spy(logging, "info")
    spy_error = mocker.spy(logging, "error")

    # Execute the main function
    main()

    # Assert logging.info was called with expected messages
    expected_info_calls = [
        mocker.call("This is the main function"),
        mocker.call(
            "This is a sub-function called with the name: This is just dome output"
        ),
    ]
    spy_info.assert_has_calls(expected_info_calls, any_order=True)

    # Assert logging.error was called once with the expected message
    spy_error.assert_called_once_with("Error: Something went wrong!")
