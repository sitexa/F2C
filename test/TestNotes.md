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

-   下载预训练数据集，保存在了dataset文件夹。
-   进行预训练，保存最新模型和最好模型。
-   记录训练日志
-   进行PPO算法训练，
