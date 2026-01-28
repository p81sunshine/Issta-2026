from solution import *
import math

def test_all():
    box = MyBox("test data")
    assert box.peek() == "test data", "Failed to initialize MyBox with data."

    box = MyBox("peek test")
    assert box.peek() == "peek test", "Failed to peek into MyBox."

    box = MyBox("lock test")
    locked_box = box.lock(1234)
    assert isinstance(locked_box, LockedMyBox), "Failed to lock MyBox."

    # Ensure peeking on the locked box raises an error
    try:
        locked_box.peek()
        assert False, "Should have raised an error when peeking into a locked box."
    except AttributeError:
        assert False, "The LockedMyBox class should have a peek method."
    except Exception:
        pass

    box = MyBox("duplicate test")
    try:  # Ensure there is no method called "duplicate"
        x = box.duplicate
        assert False, "Should not have a duplicate method."
    except AttributeError:
        pass

    box = MyBox("unlock test")
    locked_box = box.lock(4321)

    # Wrong pin should return None
    assert locked_box.unlock(9999) is None, "Unlocked with wrong pin."

    # Correct pin should return unlocked box
    unlocked_box = locked_box.unlock(4321)
    assert isinstance(
        unlocked_box, MyBox), "Failed to unlock LockedMyBox with correct pin."

    box = MyBox("duplicate test")
    locked_box = box.lock(5678)
    # make sure there is no method called "duplicate" on LockedMyBox
    try:
        x = locked_box.duplicate
        assert False, "Should not have a duplicate method."
    except AttributeError:
        pass

    # lock, then unlock, then peek
    box = MyBox("peek test")
    locked_box = box.lock(1234)
    unlocked_box = locked_box.unlock(1234)
    assert unlocked_box is not None, "Failed to unlock box."
    assert unlocked_box.peek() == "peek test", "Failed to peek into unlocked box."

    # lock, then unlock, then lock, then peek
    box = MyBox("peek test")
    locked_box = box.lock(1234)
    unlocked_box = locked_box.unlock(1234)
    assert unlocked_box is not None, "Failed to unlock box."
    assert unlocked_box.lock(1234) is not None, "Failed to lock unlocked box."
    locked_box = unlocked_box.lock(1234)
    try:
        locked_box.peek()
        assert False, "Should have raised an error when peeking into a locked box."
    except AttributeError:
        assert False, "The LockedMyBox class should have a peek method."
    except Exception:
        pass

    # lock, then unlock, then lock, then unlock, then peek
    box = MyBox("peek test")
    locked_box = box.lock(1234)
    unlocked_box = locked_box.unlock(1234)
    assert unlocked_box is not None, "Failed to unlock box."
    assert unlocked_box.lock(1234) is not None, "Failed to lock unlocked box."
    locked_box = unlocked_box.lock(1234)
    unlocked_box = locked_box.unlock(1234)
    assert unlocked_box is not None, "Failed to unlock box."
    assert unlocked_box.peek() == "peek test", "Failed to peek into unlocked box."