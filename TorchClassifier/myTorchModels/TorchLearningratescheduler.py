import torch
import torch.optim as optim
from torch.optim import lr_scheduler

#https://pytorch.org/docs/stable/optim.html#how-to-adjust-learning-rate
def setupLearningratescheduler(name, optimizer, EPOCHS, STEPS_PER_EPOCH):
    if name =='StepLR':
        # Decay LR by a factor of 0.1 every 7 epochs
        scheduler = lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.1)
    elif name == 'ConstantLR':
        scheduler = lr_scheduler.ConstantLR(optimizer, factor=0.5, total_iters=4)
        #total_iters (int) – The number of steps that the scheduler decays the learning rate. Default: 5.
        #factor (float) – The number we multiply learning rate until the milestone. Default: 1./3.
    elif name == 'ExponentialLR':
        scheduler = lr_scheduler.ExponentialLR(optimizer, gamma=0.9)
    elif name == 'MultiStepLR':
        #https://pytorch.org/docs/stable/generated/torch.optim.lr_scheduler.MultiStepLR.html#torch.optim.lr_scheduler.MultiStepLR
        scheduler = lr_scheduler.MultiStepLR(optimizer, milestones=[30,80], gamma=0.1)
    elif name == 'OneCycleLR':
        #STEPS_PER_EPOCH = len(train_iterator)
        TOTAL_STEPS = EPOCHS * STEPS_PER_EPOCH
        MAX_LRS = [p['lr'] for p in optimizer.param_groups]
        scheduler = lr_scheduler.OneCycleLR(optimizer,
                                    max_lr = MAX_LRS,
                                    total_steps = TOTAL_STEPS)
    return scheduler