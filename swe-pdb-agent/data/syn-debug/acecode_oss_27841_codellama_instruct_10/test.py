import pytest
from acecode_oss_27841_codellama_instruct_10_code import initialize_model

def test_case_0():
    assert initialize_model('SVHN', 'LeNet', True) == 'Loading pretrained model for LeNet on SVHN'

def test_case_1():
    assert initialize_model('CIFAR10', 'WRN-16-1', False) == 'Initializing new model WRN-16-1 for CIFAR10'

def test_case_2():
    assert initialize_model('CINIC10', 'WRN-40-2', True) == 'Loading pretrained model for WRN-40-2 on CINIC10'

def test_case_3():
    assert initialize_model('CIFAR100', 'WRN-40-1', False) == 'Initializing new model WRN-40-1 for CIFAR100'

def test_case_4():
    assert initialize_model('CIFAR10', 'LeNet', True) == 'Loading pretrained model for LeNet on CIFAR10'

def test_case_5():
    assert initialize_model('SVHN', 'WRN-16-2', False) == 'Initializing new model WRN-16-2 for SVHN'

def test_case_6():
    assert initialize_model('CINIC10', 'WRN-40-1', True) == 'Loading pretrained model for WRN-40-1 on CINIC10'

def test_case_7():
    assert initialize_model('CIFAR100', 'LeNet', False) == 'Initializing new model LeNet for CIFAR100'

def test_case_8():
    assert initialize_model('CIFAR10', 'WRN-16-2', True) == 'Loading pretrained model for WRN-16-2 on CIFAR10'

def test_case_9():
    assert initialize_model('SVHN', 'WRN-40-2', False) == 'Initializing new model WRN-40-2 for SVHN'

def test_case_10():
    assert initialize_model('CINIC10', 'LeNet', True) == 'Loading pretrained model for LeNet on CINIC10'

def test_case_11():
    assert initialize_model('CIFAR100', 'WRN-16-1', False) == 'Initializing new model WRN-16-1 for CIFAR100'

def test_case_12():
    assert initialize_model('SVHN', 'WRN-40-1', True) == 'Loading pretrained model for WRN-40-1 on SVHN'

def test_case_13():
    assert initialize_model('CIFAR10', 'WRN-40-2', False) == 'Initializing new model WRN-40-2 for CIFAR10'

def test_case_14():
    assert initialize_model('CINIC10', 'WRN-16-1', True) == 'Loading pretrained model for WRN-16-1 on CINIC10'

def test_case_15():
    assert initialize_model('CIFAR100', 'WRN-40-2', False) == 'Initializing new model WRN-40-2 for CIFAR100'

def test_case_16():
    assert initialize_model('XYZ', 'LeNet', False) == 'Invalid dataset or model'

def test_case_17():
    assert initialize_model('CIFAR10', 'UnknownModel', True) == 'Invalid dataset or model'

def test_case_18():
    assert initialize_model('UnknownDataset', 'WRN-40-1', False) == 'Invalid dataset or model'

def test_case_19():
    assert initialize_model('CIFAR100', 'WRN-16-2', True) == 'Loading pretrained model for WRN-16-2 on CIFAR100'

def test_case_20():
    assert initialize_model('CINIC10', 'UnknownModel', False) == 'Invalid dataset or model'

def test_case_21():
    assert initialize_model('SVHN', 'InvalidModel', True) == 'Invalid dataset or model'