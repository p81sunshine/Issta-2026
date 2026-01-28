import pytest
from acecode_oss_10834_llama3_1_instruct_45_code import run_experiments

def test_case_0():
    assert run_experiments(['Test1:Param1=10,Param2=20', 'Test2:ParamA=5']) == ['Test1 executed with parameters {Param1: 10, Param2: 20}', 'Test2 executed with parameters {ParamA: 5}']

def test_case_1():
    assert run_experiments(['Test3:Param1=15', 'InvalidExperiment:Param=']) == ['Test3 executed with parameters {Param1: 15}', 'Error']

def test_case_2():
    assert run_experiments([':Param1=10']) == ['Error']

def test_case_3():
    assert run_experiments(['Test4:']) == ['Error']

def test_case_4():
    assert run_experiments(['ExperimentX:Param1=1,Param2=2,Param3=3']) == ['ExperimentX executed with parameters {Param1: 1, Param2: 2, Param3: 3}']

def test_case_5():
    assert run_experiments(['ExperimentY:Param1=100']) == ['ExperimentY executed with parameters {Param1: 100}']

def test_case_6():
    assert run_experiments(['ExperimentZ:Param1=abc,Param2=xyz']) == ['ExperimentZ executed with parameters {Param1: abc, Param2: xyz}']

def test_case_7():
    assert run_experiments(['Test5:InvalidParamValue=1,', 'Test6:ValidParam=2']) == ['Error', 'Test6 executed with parameters {ValidParam: 2}']

def test_case_8():
    assert run_experiments(['Test7:Param1=10,Param2=20,Param3=30', 'Test8:ParamX=100']) == ['Test7 executed with parameters {Param1: 10, Param2: 20, Param3: 30}', 'Test8 executed with parameters {ParamX: 100}']

def test_case_9():
    assert run_experiments(['Test9:Param1=1,Param2=2,Param3=3,']) == ['Error']

def test_case_10():
    assert run_experiments(['Test10:Param1=10,Param2=20', 'Test11:']) == ['Test10 executed with parameters {Param1: 10, Param2: 20}', 'Error']

def test_case_11():
    assert run_experiments([':Param1=10,Param2=20']) == ['Error']

def test_case_12():
    assert run_experiments(['ExperimentA:Param1=1,Param2=2', 'ExperimentB:Param3=3']) == ['ExperimentA executed with parameters {Param1: 1, Param2: 2}', 'ExperimentB executed with parameters {Param3: 3}']

def test_case_13():
    assert run_experiments(['Test12:Param1=10']) == ['Test12 executed with parameters {Param1: 10}']

def test_case_14():
    assert run_experiments(['Test13:Param=Value']) == ['Test13 executed with parameters {Param: Value}']

def test_case_15():
    assert run_experiments(['Test14:Param1=10,Param2=20,Param3=30', 'InvalidTest:Param=']) == ['Test14 executed with parameters {Param1: 10, Param2: 20, Param3: 30}', 'Error']

def test_case_16():
    assert run_experiments(['Test15:Param1=Value1', 'TestInvalid:']) == ['Test15 executed with parameters {Param1: Value1}', 'Error']

def test_case_17():
    assert run_experiments(['Test16:Param1=10,Param2=20', 'Test17:ParamX=100,ParamY=200']) == ['Test16 executed with parameters {Param1: 10, Param2: 20}', 'Test17 executed with parameters {ParamX: 100, ParamY: 200}']

def test_case_18():
    assert run_experiments(['Test18:Param1=1']) == ['Test18 executed with parameters {Param1: 1}']

def test_case_19():
    assert run_experiments(['Test19:InvalidParam=']) == ['Error']