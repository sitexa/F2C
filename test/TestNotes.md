##  1 第一次运行
```python main.py --method=MVSSM --missing_view_num=0 --seed=0 --use_collected_data=True```
结果：
```text
============================================================================================
/home/kemove/miniconda3/envs/fuse2control/lib/python3.7/site-packages/torch/cuda/__init__.py:125: UserWarning: 
NVIDIA GeForce RTX 4090 with CUDA capability sm_89 is not compatible with the current PyTorch installation.
The current PyTorch install supports CUDA capabilities sm_37 sm_50 sm_60 sm_61 sm_70 sm_75 compute_37.
If you want to use the NVIDIA GeForce RTX 4090 GPU with PyTorch, please check the instructions at https://pytorch.org/get-started/locally/

  warnings.warn(incompatible_device_warn.format(device_name, capability, " ".join(arch_list), device_name))
Device set to : NVIDIA GeForce RTX 4090
============================================================================================
{'env_name': 'BipedalWalker-v3', 'batch_size': 512, 'n_latents': 24, 'hidden_size': 64, 'epochs': 50, 'lr': 0.0003, 'anneal_epochs': 0, 'log_interval': 100, 'cuda': False, 'is_MV': True, 'activation': 'leakyrelu', 'rec_coeff': 5000.0, 'impute_style': 'mean', 'save_model': True, 'even_dim_recon': False, 'use_prior_expert': False, 'max_ep_len': 1000, 'max_training_timesteps': 3000000, 'print_freq': 10000, 'log_freq': 2000, 'save_model_freq': 2000, 'action_std': 0.6, 'action_std_decay_rate': 0.05, 'min_action_std': 0.1, 'action_std_decay_freq': 250000, 'update_timestep': 4000, 'K_epochs': 80, 'lr_actor': 0.0003, 'lr_critic': 0.001, 'gamma': 0.99, 'rl_algorithm': 'PPO', 'save_keys_reps': ['method', 'action_std', 'min_action_std', 'max_training_timesteps', 'action_std_decay_freq', 'update_timestep', 'hidden_size', 'rec_coeff', 'activation', 'seed'], 'save_keys_train': ['rl_algorithm', 'env_name', 'method', 'action_std', 'min_action_std', 'missing_view_num', 'max_training_timesteps', 'action_std_decay_freq', 'update_timestep', 'hidden_size', 'rec_coeff', 'activation', 'seed'], 'collect_data': True, 'pretrain_reps': True, 'train_policy': True}
Method: MVSSM
DOWNLOAD PRE-COLLECTED TRAIN DATASET
100% [......................................................................] 894827600 / 894827600DOWNLOAD PRE-COLLECTED VALID DATASET
100% [......................................................................] 164365614 / 164365614Pretraining Representation from the scratch!
INFO:root:Reading `./dataset/pretrain_train_data_PPO.pkl` file...
INFO:root:Reading `./dataset/pretrain_valid_data_PPO.pkl` file...
Num train :  2534882
Num valid :  465618
Binary
/home/kemove/miniconda3/envs/fuse2control/lib/python3.7/site-packages/torch/nn/_reduction.py:44: UserWarning: size_average and reduce args will be deprecated, please use reduction='none' instead.
  warnings.warn(warning.format(ret))

Train Epoch: 1 [0/2534882 (0%)]	Loss: 41473.429688	anneal-Factor: 1.000
Train Epoch: 1 [51200/2534882 (2%)]	Loss: 25902.605469	anneal-Factor: 1.000
Train Epoch: 1 [102400/2534882 (4%)]	Loss: 17943.896484	anneal-Factor: 1.000
Train Epoch: 1 [153600/2534882 (6%)]	Loss: 13523.208008	anneal-Factor: 1.000
Train Epoch: 1 [204800/2534882 (8%)]	Loss: 10553.304688	anneal-Factor: 1.000
Train Epoch: 1 [256000/2534882 (10%)]	Loss: 8644.248047	anneal-Factor: 1.000
Train Epoch: 1 [307200/2534882 (12%)]	Loss: 7312.938477	anneal-Factor: 1.000
Train Epoch: 1 [358400/2534882 (14%)]	Loss: 6342.500000	anneal-Factor: 1.000
Train Epoch: 1 [409600/2534882 (16%)]	Loss: 5604.031250	anneal-Factor: 1.000
Train Epoch: 1 [460800/2534882 (18%)]	Loss: 5017.974609	anneal-Factor: 1.000
Train Epoch: 1 [512000/2534882 (20%)]	Loss: 4541.836426	anneal-Factor: 1.000
Train Epoch: 1 [563200/2534882 (22%)]	Loss: 4149.314453	anneal-Factor: 1.000
Train Epoch: 1 [614400/2534882 (24%)]	Loss: 3820.390137	anneal-Factor: 1.000
Train Epoch: 1 [665600/2534882 (26%)]	Loss: 3541.013916	anneal-Factor: 1.000
Train Epoch: 1 [716800/2534882 (28%)]	Loss: 3301.002197	anneal-Factor: 1.000
Train Epoch: 1 [768000/2534882 (30%)]	Loss: 3092.455811	anneal-Factor: 1.000
Train Epoch: 1 [819200/2534882 (32%)]	Loss: 2909.562256	anneal-Factor: 1.000
Train Epoch: 1 [870400/2534882 (34%)]	Loss: 2747.835938	anneal-Factor: 1.000
Train Epoch: 1 [921600/2534882 (36%)]	Loss: 2603.748291	anneal-Factor: 1.000
Train Epoch: 1 [972800/2534882 (38%)]	Loss: 2474.636230	anneal-Factor: 1.000
Train Epoch: 1 [1024000/2534882 (40%)]	Loss: 2358.093506	anneal-Factor: 1.000
Train Epoch: 1 [1075200/2534882 (42%)]	Loss: 2252.525635	anneal-Factor: 1.000
Train Epoch: 1 [1126400/2534882 (44%)]	Loss: 2156.400391	anneal-Factor: 1.000
Train Epoch: 1 [1177600/2534882 (46%)]	Loss: 2068.476807	anneal-Factor: 1.000
Train Epoch: 1 [1228800/2534882 (48%)]	Loss: 1987.779907	anneal-Factor: 1.000
Train Epoch: 1 [1280000/2534882 (51%)]	Loss: 1912.947388	anneal-Factor: 1.000
Train Epoch: 1 [1331200/2534882 (53%)]	Loss: 1843.309937	anneal-Factor: 1.000
Train Epoch: 1 [1382400/2534882 (55%)]	Loss: 1778.657104	anneal-Factor: 1.000
Train Epoch: 1 [1433600/2534882 (57%)]	Loss: 1718.515503	anneal-Factor: 1.000
Train Epoch: 1 [1484800/2534882 (59%)]	Loss: 1662.450195	anneal-Factor: 1.000
Train Epoch: 1 [1536000/2534882 (61%)]	Loss: 1610.052124	anneal-Factor: 1.000
Train Epoch: 1 [1587200/2534882 (63%)]	Loss: 1560.973511	anneal-Factor: 1.000
Train Epoch: 1 [1638400/2534882 (65%)]	Loss: 1514.919556	anneal-Factor: 1.000
Train Epoch: 1 [1689600/2534882 (67%)]	Loss: 1471.635864	anneal-Factor: 1.000
Train Epoch: 1 [1740800/2534882 (69%)]	Loss: 1430.857666	anneal-Factor: 1.000
Train Epoch: 1 [1792000/2534882 (71%)]	Loss: 1392.372437	anneal-Factor: 1.000
Train Epoch: 1 [1843200/2534882 (73%)]	Loss: 1355.987183	anneal-Factor: 1.000
Train Epoch: 1 [1894400/2534882 (75%)]	Loss: 1321.552002	anneal-Factor: 1.000
Train Epoch: 1 [1945600/2534882 (77%)]	Loss: 1288.907227	anneal-Factor: 1.000
Train Epoch: 1 [1996800/2534882 (79%)]	Loss: 1257.928101	anneal-Factor: 1.000
Train Epoch: 1 [2048000/2534882 (81%)]	Loss: 1228.478394	anneal-Factor: 1.000
Train Epoch: 1 [2099200/2534882 (83%)]	Loss: 1200.441284	anneal-Factor: 1.000
Train Epoch: 1 [2150400/2534882 (85%)]	Loss: 1173.722168	anneal-Factor: 1.000
Train Epoch: 1 [2201600/2534882 (87%)]	Loss: 1148.229614	anneal-Factor: 1.000
Train Epoch: 1 [2252800/2534882 (89%)]	Loss: 1123.884644	anneal-Factor: 1.000
Train Epoch: 1 [2304000/2534882 (91%)]	Loss: 1100.607056	anneal-Factor: 1.000
Train Epoch: 1 [2355200/2534882 (93%)]	Loss: 1078.334961	anneal-Factor: 1.000
Train Epoch: 1 [2406400/2534882 (95%)]	Loss: 1056.986450	anneal-Factor: 1.000
Train Epoch: 1 [2457600/2534882 (97%)]	Loss: 1036.517700	anneal-Factor: 1.000
Train Epoch: 1 [2508800/2534882 (99%)]	Loss: 1016.877563	anneal-Factor: 1.000
====> Epoch: 1	Loss: 1007.5353
======> Valid: 1	Loss: 66.4849
---- Save latest model ----
---- Save best model (valid loss :  tensor(66.4849)  )
...........................
...Train Epoch: 2 ~ 49 ....
...........................
Train Epoch: 50 [0/2534882 (0%)]	Loss: 40.379147	anneal-Factor: 1.000
Train Epoch: 50 [51200/2534882 (2%)]	Loss: 40.754738	anneal-Factor: 1.000
Train Epoch: 50 [102400/2534882 (4%)]	Loss: 40.685619	anneal-Factor: 1.000
Train Epoch: 50 [153600/2534882 (6%)]	Loss: 40.675858	anneal-Factor: 1.000
Train Epoch: 50 [204800/2534882 (8%)]	Loss: 40.688076	anneal-Factor: 1.000
Train Epoch: 50 [256000/2534882 (10%)]	Loss: 40.679165	anneal-Factor: 1.000
Train Epoch: 50 [307200/2534882 (12%)]	Loss: 40.688969	anneal-Factor: 1.000
Train Epoch: 50 [358400/2534882 (14%)]	Loss: 40.680660	anneal-Factor: 1.000
Train Epoch: 50 [409600/2534882 (16%)]	Loss: 40.663994	anneal-Factor: 1.000
Train Epoch: 50 [460800/2534882 (18%)]	Loss: 40.658707	anneal-Factor: 1.000
Train Epoch: 50 [512000/2534882 (20%)]	Loss: 40.661434	anneal-Factor: 1.000
Train Epoch: 50 [563200/2534882 (22%)]	Loss: 40.659004	anneal-Factor: 1.000
Train Epoch: 50 [614400/2534882 (24%)]	Loss: 40.664261	anneal-Factor: 1.000
Train Epoch: 50 [665600/2534882 (26%)]	Loss: 40.663788	anneal-Factor: 1.000
Train Epoch: 50 [716800/2534882 (28%)]	Loss: 40.661301	anneal-Factor: 1.000
Train Epoch: 50 [768000/2534882 (30%)]	Loss: 40.674320	anneal-Factor: 1.000
Train Epoch: 50 [819200/2534882 (32%)]	Loss: 40.676685	anneal-Factor: 1.000
Train Epoch: 50 [870400/2534882 (34%)]	Loss: 40.668381	anneal-Factor: 1.000
Train Epoch: 50 [921600/2534882 (36%)]	Loss: 40.666447	anneal-Factor: 1.000
Train Epoch: 50 [972800/2534882 (38%)]	Loss: 40.669216	anneal-Factor: 1.000
Train Epoch: 50 [1024000/2534882 (40%)]	Loss: 40.668064	anneal-Factor: 1.000
Train Epoch: 50 [1075200/2534882 (42%)]	Loss: 40.667992	anneal-Factor: 1.000
Train Epoch: 50 [1126400/2534882 (44%)]	Loss: 40.666782	anneal-Factor: 1.000
Train Epoch: 50 [1177600/2534882 (46%)]	Loss: 40.669121	anneal-Factor: 1.000
Train Epoch: 50 [1228800/2534882 (48%)]	Loss: 40.664879	anneal-Factor: 1.000
Train Epoch: 50 [1280000/2534882 (51%)]	Loss: 40.669483	anneal-Factor: 1.000
Train Epoch: 50 [1331200/2534882 (53%)]	Loss: 40.668709	anneal-Factor: 1.000
Train Epoch: 50 [1382400/2534882 (55%)]	Loss: 40.675041	anneal-Factor: 1.000
Train Epoch: 50 [1433600/2534882 (57%)]	Loss: 40.671833	anneal-Factor: 1.000
Train Epoch: 50 [1484800/2534882 (59%)]	Loss: 40.671345	anneal-Factor: 1.000
Train Epoch: 50 [1536000/2534882 (61%)]	Loss: 40.668591	anneal-Factor: 1.000
Train Epoch: 50 [1587200/2534882 (63%)]	Loss: 40.670273	anneal-Factor: 1.000
Train Epoch: 50 [1638400/2534882 (65%)]	Loss: 40.670418	anneal-Factor: 1.000
Train Epoch: 50 [1689600/2534882 (67%)]	Loss: 40.669754	anneal-Factor: 1.000
Train Epoch: 50 [1740800/2534882 (69%)]	Loss: 40.666122	anneal-Factor: 1.000
Train Epoch: 50 [1792000/2534882 (71%)]	Loss: 40.664936	anneal-Factor: 1.000
Train Epoch: 50 [1843200/2534882 (73%)]	Loss: 40.664268	anneal-Factor: 1.000
Train Epoch: 50 [1894400/2534882 (75%)]	Loss: 40.659660	anneal-Factor: 1.000
Train Epoch: 50 [1945600/2534882 (77%)]	Loss: 40.658443	anneal-Factor: 1.000
Train Epoch: 50 [1996800/2534882 (79%)]	Loss: 40.657398	anneal-Factor: 1.000
Train Epoch: 50 [2048000/2534882 (81%)]	Loss: 40.656494	anneal-Factor: 1.000
Train Epoch: 50 [2099200/2534882 (83%)]	Loss: 40.654819	anneal-Factor: 1.000
Train Epoch: 50 [2150400/2534882 (85%)]	Loss: 40.653561	anneal-Factor: 1.000
Train Epoch: 50 [2201600/2534882 (87%)]	Loss: 40.652004	anneal-Factor: 1.000
Train Epoch: 50 [2252800/2534882 (89%)]	Loss: 40.653107	anneal-Factor: 1.000
Train Epoch: 50 [2304000/2534882 (91%)]	Loss: 40.652679	anneal-Factor: 1.000
Train Epoch: 50 [2355200/2534882 (93%)]	Loss: 40.654408	anneal-Factor: 1.000
Train Epoch: 50 [2406400/2534882 (95%)]	Loss: 40.654366	anneal-Factor: 1.000
Train Epoch: 50 [2457600/2534882 (97%)]	Loss: 40.653130	anneal-Factor: 1.000
Train Epoch: 50 [2508800/2534882 (99%)]	Loss: 40.653950	anneal-Factor: 1.000
====> Epoch: 50	Loss: 40.6532
======> Valid: 50	Loss: 36.4004
---- Save latest model ----
---- Save best model (valid loss :  tensor(36.4004)  )

============================================================================================
./representations/MVSSM/PPO_pretrained/MVSSM_0.6_0.1_3000000_250000_4000_64_5000.0_leakyrelu_0_best.pth
training environment name : BipedalWalker-v3
/home/kemove/miniconda3/envs/fuse2control/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
current logging run number for BipedalWalker-v3 :  0
logging at : PPO_logs/BipedalWalker-v3/PPO_BipedalWalker-v3_rep_PPO_BipedalWalker-v3_MVSSM_0.6_0.1_0_3000000_250000_4000_64_5000.0_leakyrelu_0_log.csv
save checkpoint path : rep_PPO_Trained/BipedalWalker-v3/repPPO_BipedalWalker-v3_MVSSM_0.6_0.1_0_3000000_250000_4000_64_5000.0_leakyrelu_0.pth
--------------------------------------------------------------------------------------------
max training timesteps :  3000000
max timesteps per episode :  1000
model saving frequency : 2000 timesteps
log frequency : 2000 timesteps
printing average reward over episodes in last : 10000 timesteps
--------------------------------------------------------------------------------------------
state space dimension :  24
action space dimension :  4
--------------------------------------------------------------------------------------------
Initializing a continuous action space policy
--------------------------------------------------------------------------------------------
starting std of action distribution :  0.6
decay rate of std of action distribution :  0.05
minimum std of action distribution :  0.1
decay frequency of std of action distribution : 250000 timesteps
--------------------------------------------------------------------------------------------
PPO update frequency : 4000 timesteps
PPO K epochs :  80
PPO epsilon clip :  0.2
discount factor (gamma) :  0.99
--------------------------------------------------------------------------------------------
optimizer learning rate actor :  0.0003
optimizer learning rate critic :  0.001
setting random seed to  0
============================================================================================
Binary
Pretrained MVSSM is loaded.
Started training at (GMT) :  2023-09-08 03:06:36
============================================================================================
Traceback (most recent call last):
  File "main.py", line 60, in <module>
    train_policy.train(config)
  File "/home/kemove/Projects/F2C/train_policy.py", line 295, in train
    action = agent.select_action(state)
  File "/home/kemove/Projects/F2C/PPO.py", line 176, in select_action
    action, action_logprob = self.policy_old.act(state)
  File "/home/kemove/Projects/F2C/PPO.py", line 88, in act
    dist = MultivariateNormal(action_mean, cov_mat)
  File "/home/kemove/miniconda3/envs/fuse2control/lib/python3.7/site-packages/torch/distributions/multivariate_normal.py", line 149, in __init__
    self._unbroadcasted_scale_tril = torch.cholesky(covariance_matrix)
RuntimeError: CUDA error: no kernel image is available for execution on the device

```

### 运行结果

-  下载预训练数据集，保存在了dataset文件夹。(成功)
-  进行预训练，保存最新模型和最好模型。（成功）
-  记录训练日志。（成功）
-  进行PPO算法训练。（失败）
-  错误日志：```RuntimeError: CUDA error: no kernel image is available for execution on the device```
-  原因：硬件NVIDIA GeForce RTX 4090与编程架构CUDA的功能sm_89不兼容当前的PyTorch安装版本。
   当前的PyTorch安装支持CUDA功能sm_37 sm_50 sm_60 sm_61 sm_70 sm_75 compute_37。
   如果您想使用NVIDIA GeForce RTX 4090 GPU与PyTorch，请查看https://pytorch.org/get-started/locally/的说明
-  CUDA: Compute Unified Device Architecture，是NVIDIA推出的一种通用并行计算架构，该架构使GPU能够解决复杂的计算问题。

### 错误日志

- PyTorch版本(pytorch==1.6.0 torchvision==0.7.0 cudatoolkit=10.2)与硬件不匹配，
- 根据官网指导，重新安装：```conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch -c conda-forge```

### 小技巧

-  检查GPU是否安装并配置成功：```nvidia-smi```
-  检查CUDA toolkit版本：```nvcc --version```
   ```
   nvcc: NVIDIA (R) Cuda compiler driver
   Copyright (c) 2005-2023 NVIDIA Corporation
   Built on Tue_Aug_15_22:02:13_PDT_2023
   Cuda compilation tools, release 12.2, V12.2.140
   Build cuda_12.2.r12.2/compiler.33191640_0
   ```
-  检查PyTorch版本：```python -c "import torch; print(torch.__version__)"```
-  检查GPU是否安装和配置成功：```lspci | grep -i nvidia```
-  检查GPU存储容量：```nvidia-smi -q | grep -i 'memory usage' -A 2```

### 解决问题
-  重新安装CudaToolkit: ```https://developer.nvidia.com/cuda-gpus```
   ```text
   wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
   sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
   wget https://developer.download.nvidia.com/compute/cuda/12.2.2/local_installers/cuda-repo-ubuntu2204-12-2-local_12.2.2-535.104.05-1_amd64.deb
   sudo dpkg -i cuda-repo-ubuntu2204-12-2-local_12.2.2-535.104.05-1_amd64.deb
   sudo cp /var/cuda-repo-ubuntu2204-12-2-local/cuda-*-keyring.gpg /usr/share/keyrings/
   sudo apt-get update
   sudo apt-get -y install cuda
   ```
-  重新安装PyTorch: ```conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia```

### 重新运行主程序

```python main.py --method=MVSSM --missing_view_num=0 --seed=0 --use_collected_data=True```
```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121
```

日志：

```text
============================================================================================
Device set to : cpu
============================================================================================
{'env_name': 'BipedalWalker-v3', 'batch_size': 512, 'n_latents': 24, 'hidden_size': 64, 'epochs': 50, 'lr': 0.0003, 'anneal_epochs': 0, 'log_interval': 100, 'cuda': False, 'is_MV': True, 'activation': 'leakyrelu', 'rec_coeff': 5000.0, 'impute_style': 'mean', 'save_model': True, 'even_dim_recon': False, 'use_prior_expert': False, 'max_ep_len': 1000, 'max_training_timesteps': 3000000, 'print_freq': 10000, 'log_freq': 2000, 'save_model_freq': 2000, 'action_std': 0.6, 'action_std_decay_rate': 0.05, 'min_action_std': 0.1, 'action_std_decay_freq': 250000, 'update_timestep': 4000, 'K_epochs': 80, 'lr_actor': 0.0003, 'lr_critic': 0.001, 'gamma': 0.99, 'rl_algorithm': 'PPO', 'save_keys_reps': ['method', 'action_std', 'min_action_std', 'max_training_timesteps', 'action_std_decay_freq', 'update_timestep', 'hidden_size', 'rec_coeff', 'activation', 'seed'], 'save_keys_train': ['rl_algorithm', 'env_name', 'method', 'action_std', 'min_action_std', 'missing_view_num', 'max_training_timesteps', 'action_std_decay_freq', 'update_timestep', 'hidden_size', 'rec_coeff', 'activation', 'seed'], 'collect_data': True, 'pretrain_reps': True, 'train_policy': True}
Method: MVSSM
Fully trained Representation already exists!!!
============================================================================================
./representations/MVSSM/PPO_pretrained/MVSSM_0.6_0.1_3000000_250000_4000_64_5000.0_leakyrelu_0_best.pth
training environment name : BipedalWalker-v3
/home/kemove/miniconda3/envs/fuse2control/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: WARN: Box bound precision lowered by casting to float32
  warnings.warn(colorize('%s: %s'%('WARN', msg % args), 'yellow'))
current logging run number for BipedalWalker-v3 :  0
logging at : PPO_logs/BipedalWalker-v3/PPO_BipedalWalker-v3_rep_PPO_BipedalWalker-v3_MVSSM_0.6_0.1_0_3000000_250000_4000_64_5000.0_leakyrelu_0_log.csv
save checkpoint path : rep_PPO_Trained/BipedalWalker-v3/repPPO_BipedalWalker-v3_MVSSM_0.6_0.1_0_3000000_250000_4000_64_5000.0_leakyrelu_0.pth
--------------------------------------------------------------------------------------------
max training timesteps :  3000000
max timesteps per episode :  1000
model saving frequency : 2000 timesteps
log frequency : 2000 timesteps
printing average reward over episodes in last : 10000 timesteps
--------------------------------------------------------------------------------------------
state space dimension :  24
action space dimension :  4
--------------------------------------------------------------------------------------------
Initializing a continuous action space policy
--------------------------------------------------------------------------------------------
starting std of action distribution :  0.6
decay rate of std of action distribution :  0.05
minimum std of action distribution :  0.1
decay frequency of std of action distribution : 250000 timesteps
--------------------------------------------------------------------------------------------
PPO update frequency : 4000 timesteps
PPO K epochs :  80
PPO epsilon clip :  0.2
discount factor (gamma) :  0.99
--------------------------------------------------------------------------------------------
optimizer learning rate actor :  0.0003
optimizer learning rate critic :  0.001
setting random seed to  0
============================================================================================
Binary
/home/kemove/miniconda3/envs/fuse2control/lib/python3.7/site-packages/torch/nn/_reduction.py:42: UserWarning: size_average and reduce args will be deprecated, please use reduction='none' instead.
  warnings.warn(warning.format(ret))
Pretrained MVSSM is loaded.
Started training at (GMT) :  2023-09-08 20:46:17
============================================================================================
============================================================================================
Episode : 33 		 Timestep : 10000 		 Average Reward : -94.54 		 Time: 0:00:10
Episode : 75 		 Timestep : 20000 		 Average Reward : -99.43 		 Time: 0:00:19
Episode : 99 		 Timestep : 30000 		 Average Reward : -87.42 		 Time: 0:00:28
Episode : 125 		 Timestep : 40000 		 Average Reward : -84.77 		 Time: 0:00:38
Episode : 147 		 Timestep : 50000 		 Average Reward : -85.55 		 Time: 0:00:47
Episode : 159 		 Timestep : 60000 		 Average Reward : -49.01 		 Time: 0:00:56
Episode : 170 		 Timestep : 70000 		 Average Reward : -42.13 		 Time: 0:01:06
Episode : 180 		 Timestep : 80000 		 Average Reward : -32.64 		 Time: 0:01:15
Episode : 191 		 Timestep : 90000 		 Average Reward : -40.09 		 Time: 0:01:24
Episode : 201 		 Timestep : 100000 		 Average Reward : -25.75 		 Time: 0:01:34
Episode : 211 		 Timestep : 110000 		 Average Reward : -31.62 		 Time: 0:01:43
Episode : 222 		 Timestep : 120000 		 Average Reward : -27.42 		 Time: 0:01:52
Episode : 232 		 Timestep : 130000 		 Average Reward : -12.87 		 Time: 0:02:01
Episode : 244 		 Timestep : 140000 		 Average Reward : -25.21 		 Time: 0:02:10
Episode : 254 		 Timestep : 150000 		 Average Reward : 0.3 		 Time: 0:02:20
Episode : 264 		 Timestep : 160000 		 Average Reward : 11.53 		 Time: 0:02:29
Episode : 274 		 Timestep : 170000 		 Average Reward : 1.72 		 Time: 0:02:38
Episode : 286 		 Timestep : 180000 		 Average Reward : -6.0 		 Time: 0:02:47
Episode : 296 		 Timestep : 190000 		 Average Reward : 18.77 		 Time: 0:02:56
Episode : 306 		 Timestep : 200000 		 Average Reward : 22.75 		 Time: 0:03:06
Episode : 317 		 Timestep : 210000 		 Average Reward : 21.22 		 Time: 0:03:15
Episode : 328 		 Timestep : 220000 		 Average Reward : 27.35 		 Time: 0:03:24
Episode : 340 		 Timestep : 230000 		 Average Reward : 22.73 		 Time: 0:03:33
Episode : 353 		 Timestep : 240000 		 Average Reward : 17.16 		 Time: 0:03:42
--------------------------------------------------------------------------------------------
setting actor output action_std to :  0.55
--------------------------------------------------------------------------------------------
Episode : 366 		 Timestep : 250000 		 Average Reward : 20.48 		 Time: 0:03:51
Episode : 378 		 Timestep : 260000 		 Average Reward : 24.96 		 Time: 0:04:01
Episode : 388 		 Timestep : 270000 		 Average Reward : 67.12 		 Time: 0:04:10
Episode : 399 		 Timestep : 280000 		 Average Reward : 45.37 		 Time: 0:04:19
Episode : 410 		 Timestep : 290000 		 Average Reward : 54.23 		 Time: 0:04:28
Episode : 422 		 Timestep : 300000 		 Average Reward : 54.43 		 Time: 0:04:38
Episode : 432 		 Timestep : 310000 		 Average Reward : 61.59 		 Time: 0:04:47
Episode : 444 		 Timestep : 320000 		 Average Reward : 65.4 		 Time: 0:04:56
Episode : 455 		 Timestep : 330000 		 Average Reward : 68.68 		 Time: 0:05:05
Episode : 465 		 Timestep : 340000 		 Average Reward : 71.66 		 Time: 0:05:14
Episode : 475 		 Timestep : 350000 		 Average Reward : 103.0 		 Time: 0:05:24
Episode : 488 		 Timestep : 360000 		 Average Reward : 37.97 		 Time: 0:05:33
Episode : 499 		 Timestep : 370000 		 Average Reward : 73.26 		 Time: 0:05:42
Episode : 510 		 Timestep : 380000 		 Average Reward : 77.77 		 Time: 0:05:51
Episode : 522 		 Timestep : 390000 		 Average Reward : 84.84 		 Time: 0:06:00
Episode : 533 		 Timestep : 400000 		 Average Reward : 101.24 		 Time: 0:06:10
Episode : 543 		 Timestep : 410000 		 Average Reward : 111.98 		 Time: 0:06:19
Episode : 553 		 Timestep : 420000 		 Average Reward : 102.45 		 Time: 0:06:28
Episode : 564 		 Timestep : 430000 		 Average Reward : 101.12 		 Time: 0:06:37
Episode : 575 		 Timestep : 440000 		 Average Reward : 85.43 		 Time: 0:06:46
Episode : 586 		 Timestep : 450000 		 Average Reward : 97.48 		 Time: 0:06:55
Episode : 597 		 Timestep : 460000 		 Average Reward : 58.46 		 Time: 0:07:04
Episode : 611 		 Timestep : 470000 		 Average Reward : 49.19 		 Time: 0:07:13
Episode : 622 		 Timestep : 480000 		 Average Reward : 87.07 		 Time: 0:07:23
Episode : 632 		 Timestep : 490000 		 Average Reward : 110.3 		 Time: 0:07:32
--------------------------------------------------------------------------------------------
setting actor output action_std to :  0.5
--------------------------------------------------------------------------------------------
......
......
Episode : 3039 		 Timestep : 2750000 		 Average Reward : 152.49 		 Time: 0:42:00
Episode : 3051 		 Timestep : 2760000 		 Average Reward : 85.31 		 Time: 0:42:09
Episode : 3062 		 Timestep : 2770000 		 Average Reward : 131.57 		 Time: 0:42:18
Episode : 3073 		 Timestep : 2780000 		 Average Reward : 117.75 		 Time: 0:42:28
Episode : 3083 		 Timestep : 2790000 		 Average Reward : 150.53 		 Time: 0:42:37
Episode : 3094 		 Timestep : 2800000 		 Average Reward : 129.4 		 Time: 0:42:46
Episode : 3104 		 Timestep : 2810000 		 Average Reward : 165.38 		 Time: 0:42:55
Episode : 3117 		 Timestep : 2820000 		 Average Reward : 83.47 		 Time: 0:43:04
Episode : 3127 		 Timestep : 2830000 		 Average Reward : 128.96 		 Time: 0:43:13
Episode : 3137 		 Timestep : 2840000 		 Average Reward : 159.74 		 Time: 0:43:23
Episode : 3148 		 Timestep : 2850000 		 Average Reward : 138.47 		 Time: 0:43:32
Episode : 3159 		 Timestep : 2860000 		 Average Reward : 108.49 		 Time: 0:43:41
Episode : 3171 		 Timestep : 2870000 		 Average Reward : 106.71 		 Time: 0:43:50
Episode : 3181 		 Timestep : 2880000 		 Average Reward : 133.32 		 Time: 0:43:59
Episode : 3193 		 Timestep : 2890000 		 Average Reward : 114.26 		 Time: 0:44:08
Episode : 3204 		 Timestep : 2900000 		 Average Reward : 122.7 		 Time: 0:44:18
Episode : 3216 		 Timestep : 2910000 		 Average Reward : 97.74 		 Time: 0:44:26
Episode : 3226 		 Timestep : 2920000 		 Average Reward : 136.56 		 Time: 0:44:36
Episode : 3236 		 Timestep : 2930000 		 Average Reward : 146.58 		 Time: 0:44:45
Episode : 3247 		 Timestep : 2940000 		 Average Reward : 124.26 		 Time: 0:44:54
Episode : 3257 		 Timestep : 2950000 		 Average Reward : 153.38 		 Time: 0:45:03
Episode : 3268 		 Timestep : 2960000 		 Average Reward : 144.33 		 Time: 0:45:12
Episode : 3280 		 Timestep : 2970000 		 Average Reward : 88.64 		 Time: 0:45:21
Episode : 3292 		 Timestep : 2980000 		 Average Reward : 102.07 		 Time: 0:45:31
Episode : 3303 		 Timestep : 2990000 		 Average Reward : 124.87 		 Time: 0:45:39
--------------------------------------------------------------------------------------------
setting actor output action_std to min_action_std :  0.1
--------------------------------------------------------------------------------------------
Episode : 3315 		 Timestep : 3000000 		 Average Reward : 98.59 		 Time: 0:45:49
============================================================================================
Started training at (GMT) :  2023-09-08 20:46:17
Finished training at (GMT) :  2023-09-08 21:32:06
Total training time  :  0:45:49
============================================================================================
```

从上面的运行日志看，```set device to CPU```, GPU没有启用成功。

