from solution import *
import math

def test_all():
    assert ImageMessage("image").process(
    ) == "Processed image message with description: image"
    assert TextMessage("text").process() == "Processed text message: text"
    assert MessageFactory.get_message(
        "text", "text").process() == "Processed text message: text"
    assert MessageFactory.get_message("image", "image").process(
    ) == "Processed image message with description: image"

    # assert that ImageMessage and TextMessage are subclasses of Message
    assert issubclass(ImageMessage, Message)
    assert issubclass(TextMessage, Message)

    # assert that Message defines an abstract method called process
    assert "process" in Message.__abstractmethods__

    try:
        MessageFactory.get_message("unknown", "unknown")
        assert False
    except:
        pass