def initialize_model(dataset, model_name, pretrained):
    """
    Initializes a model based on certain conditions.
    """
    # Handle specific cases for the datasets
    if dataset == 'SVHN':
        if model_name == 'LeNet':
            if pretrained:
                return 'Loading pretrained model for LeNet on SVHN'
            else:
                return 'Initializing new model LeNet for SVHN'
    elif dataset == 'CIFAR10':
        if model_name == 'WRN-16-1':
            if pretrained:
                return 'Loading pretrained model for WRN-16-1 on CIFAR10'
            else:
                return 'Initializing new model WRN-16-1 for CIFAR10'
    # Handle specific cases for the models
    elif model_name == 'LeNet':
        if dataset == 'SVHN':
            if pretrained:
                return 'Loading pretrained model for LeNet on SVHN'
            else:
                return 'Initializing new model LeNet for SVHN'
    elif model_name == 'WRN-16-1':
        if dataset == 'CIFAR10':
            if pretrained:
                return 'Loading pretrained model for WRN-16-1 on CIFAR10'
            else:
                return 'Initializing new model WRN-16-1 for CIFAR10'
    # Handle specific cases for the pretrained parameter
    if pretrained:
        return 'Loading pretrained model for {model_name} on {dataset}'.format(model_name=model_name, dataset=dataset)
    else:
        return 'Initializing new model {model_name} for {dataset}'.format(model_name=model_name, dataset=dataset)

# Tests for the function