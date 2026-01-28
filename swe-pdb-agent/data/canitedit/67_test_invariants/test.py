from solution import *
import math

def test_all():
    def assert_raises(exc_type, func, *args, **kwargs):
        try:
            func(*args, **kwargs)
        except exc_type:
            pass
        else:
            raise AssertionError(
                f"{func.__name__} did not raise {exc_type.__name__}")

    # specifically test check_worker_invariants and check_public_worker_invariants
    # with bad inputs

    # simple cases
    assert_raises(AssertionError, check_worker_invariants,
                  Worker("John Doe", -1, Employer("Acme", 100)))
    assert_raises(AssertionError, check_worker_invariants,
                  Worker("John Doe Doe", 1, Employer("Acme", 100)))
    assert_raises(AssertionError, check_worker_invariants,
                  Worker("John", 1, Employer("Acme", 100)))

    assert_raises(AssertionError, check_public_worker_invariants,
                  PublicWorker("John Doe", -1, Employer("Acme", 100)))
    check_public_worker_invariants(
        PublicWorker("John Doe", 1, Employer("Acme", -100)))  # should not raise
    assert_raises(AssertionError, check_public_worker_invariants,
                  PublicWorker("John Doe Doe", 1, Employer("Acme", 100)))
    assert_raises(AssertionError, check_public_worker_invariants,
                  PublicWorker("John", 1, Employer("Acme", 100)))

    # now test that the money and funds are correct after paying
    # and giving a raise
    w = Worker("John Doe", 1, Employer("Acme", 100))
    w.givePay()
    assert w.money == 1
    assert w.company.funds == 99
    w.giveRaise(0.1)
    assert w.pay == 1.1

    # just test .lastName
    assert w.lastName() == "Doe"

    w = PublicWorker("John Doe", 1, Employer("Acme", 100))
    w.givePay()
    assert w.money == 1
    assert w.company.funds == 100
    w.giveRaise(0.1)
    assert w.pay == 1.1
    assert w.company.funds == 100

    class WorkerMoneyFromNowhere(Worker):
        def givePay(self):
            self.money += self.pay

    w = WorkerMoneyFromNowhere("John Doe", 1, Employer("Acme", 100))
    assert_raises(AssertionError, check_worker_invariants, w)
    # should not raise, since the company's funds are not touched
    check_public_worker_invariants(w)  # type: ignore

    class WorkerGetsNoRaise(Worker):
        def giveRaise(self, percent):
            pass

    w = WorkerGetsNoRaise("John Doe", 1, Employer("Acme", 100))
    assert_raises(AssertionError, check_worker_invariants, w)
    assert_raises(AssertionError, check_public_worker_invariants,
                  w)  # should be fine

    class WorkerGetsNoPayButCompanyLoses(Worker):
        def givePay(self):
            self.company.funds -= self.pay

    w = WorkerGetsNoPayButCompanyLoses("John Doe", 1, Employer("Acme", 100))
    assert_raises(AssertionError, check_worker_invariants, w)
    assert_raises(AssertionError, check_public_worker_invariants,
                  w)  # should be fine

    # test that worker with test_public_worker_invariants asserts
    # correctly when it should
    assert_raises(AssertionError, check_public_worker_invariants,
                  Worker("John Doe", 1, Employer("Acme", 100)))