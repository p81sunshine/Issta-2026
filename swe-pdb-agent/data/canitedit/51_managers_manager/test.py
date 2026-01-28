from solution import *
import math

def test_all():
    """
    CEO
        Manager3
            Manager2
                Manager1
                    IC (Alice)
                    IC (Bob)
                    IC (David)
                IC (Alice)
            Manager4
                IC (Eva)
                IC (Frank)
            Manager5
                IC (Grace)
    """

    ceo = Manager("CEO", [])
    manager1 = Manager("Manager1", [])
    manager2 = Manager("Manager2", [])
    manager3 = Manager("Manager3", [])
    ic1 = IC("Alice")
    ic2 = IC("Bob")
    ic3 = IC("Alice")
    manager1.team = [ic1, ic2]
    manager2.team.append(ic3)
    ceo.team.append(manager3)
    manager4 = Manager("Manager4", [])
    manager5 = Manager("Manager5", [])
    ic4 = IC("David")
    ic5 = IC("Eva")
    ic6 = IC("Frank")
    ic7 = IC("Grace")

    ceo.team.extend([manager3])
    manager3.team.extend([manager2, manager4, manager5])
    manager2.team.extend([manager1, ic3])
    manager1.team.extend([ic1, ic2, ic4])
    manager4.team.extend([ic5, ic6])
    manager5.team.extend([ic7])

    alice_mm2 = ceo.find_manager_n("Alice", 2)
    assert alice_mm2 == sorted(
        list(set(["Manager2", "Manager3"]))), f"Test 1 Failed: {alice_mm2}"
    eva_mm2 = ceo.find_manager_n("Eva", 2)
    assert eva_mm2 == ["Manager3"], f"Test 2 Failed: {eva_mm2}"
    assert ceo.find_manager_n("Unknown", 2) == [], "Test 3 Failed"
    bob_mm2 = ceo.find_manager_n("Bob", 2)
    assert bob_mm2 == ["Manager2"], f"Test 4 Failed: {bob_mm2}"
    manager2_mm2 = ceo.find_manager_n("Manager2", 2)
    assert manager2_mm2 == ["CEO"], f"Test 5 Failed: {manager2_mm2}"
    ceo_mm2 = ceo.find_manager_n("CEO", 2)
    assert ceo_mm2 == [], f"Test 6 Failed: {ceo_mm2}"
    manager3_mm2 = ceo.find_manager_n("Manager3", 2)
    assert manager3_mm2 == [], f"Test 7 Failed: {manager3_mm2}"

    alice_mm3 = ceo.find_manager_n("Alice", 3)
    assert alice_mm3 == sorted(
        list(set(["Manager3", "CEO"]))), f"Test 1 Failed: {alice_mm3}"
    eva_mm3 = ceo.find_manager_n("Eva", 3)
    assert eva_mm3 == ["CEO"], f"Test 2 Failed: {eva_mm3}"
    assert ceo.find_manager_n("Unknown", 3) == [], "Test 3 Failed"
    bob_mm3 = ceo.find_manager_n("Bob", 3)
    assert bob_mm3 == ["Manager3"], f"Test 4 Failed: {bob_mm3}"
    manager2_mm3 = ceo.find_manager_n("Manager2", 3)
    assert manager2_mm3 == [], f"Test 5 Failed: {manager2_mm3}"
    ceo_mm3 = ceo.find_manager_n("CEO", 3)
    assert ceo_mm3 == [], f"Test 6 Failed: {ceo_mm3}"
    manager3_mm3 = ceo.find_manager_n("Manager3", 3)
    assert manager3_mm3 == [], f"Test 7 Failed: {manager3_mm3}"