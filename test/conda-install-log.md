
```text
conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch -c conda-forge
```

Collecting package metadata (current_repodata.json): - WARNING conda.models.version:get_matcher(556): Using .* with relational operator is superfluous and deprecated and will be removed in a future version of conda. Your spec was 1.7.1.*, but conda is ignoring the .* and treating it as 1.7.1
done
Solving environment: unsuccessful initial attempt using frozen solve. Retrying with flexible solve.
Solving environment: unsuccessful attempt using repodata from current_repodata.json, retrying with next repodata source.
Collecting package metadata (repodata.json): - WARNING conda.models.version:get_matcher(556): Using .* with relational operator is superfluous and deprecated and will be removed in a future version of conda. Your spec was 1.8.0.*, but conda is ignoring the .* and treating it as 1.8.0
WARNING conda.models.version:get_matcher(556): Using .* with relational operator is superfluous and deprecated and will be removed in a future version of conda. Your spec was 1.9.0.*, but conda is ignoring the .* and treating it as 1.9.0
WARNING conda.models.version:get_matcher(556): Using .* with relational operator is superfluous and deprecated and will be removed in a future version of conda. Your spec was 1.6.0.*, but conda is ignoring the .* and treating it as 1.6.0
done
Solving environment: unsuccessful initial attempt using frozen solve. Retrying with flexible solve.
Solving environment: / 
Found conflicts! Looking for incompatible packages.
This can take several minutes.  Press CTRL-C to abort.
failed                                                           -                                          -                                        -  

UnsatisfiableError: The following specifications were found
to be incompatible with the existing python installation in your environment:

Specifications:

  - libxml2 -> python=3.10
  - pytorch -> python[version='*|2.7.*|3.5.*|3.6.*|>=3.6|>=3.7|3.4.*|>=3.5|>=3.8|>=3.6,<3.7|3.9.*|3.10.*|3.8.*|3.11.*|3.9.16|3.8.16|3.9.10|3.8.12|3.7.12|3.7.10|3.7.10|3.6.12|3.7.9|3.6.12|3.6.9|3.6.9|3.6.9|3.6.9|3.7.*|>=3',build='3_73_pypy|4_73_pypy|5_73_pypy|5_73_pypy|*_cpython|0_73_pypy|0_73_pypy|0_73_pypy|0_73_pypy|0_73_pypy|1_73_pypy|0_73_pypy|2_73_pypy|1_73_pypy|0_73_pypy']
  - torchaudio -> python[version='2.7.*|3.5.*|3.6.*|>=2.7,<2.8.0a0|3.4.*|3.9.*']

Your python: python=3.7.5

If python is on the left-most side of the chain, that's the version you've asked for.
When python appears to the right, that indicates that the thing on the left is somehow
not available for the python version you are constrained to. Note that conda will not
change your python version to a different minor version unless you explicitly specify
that.

The following specifications were found to be incompatible with a past
explicit spec that is not an explicit spec in this operation (pytorch-cuda):

  - cudatoolkit=11.1
  - pytorch -> cudatoolkit[version='10.0.*|10.0|10.0.*|10.1|10.1.*|10.2|10.2.*|>=10.1,<10.2|>=10.2,<10.3|>=11.3,<11.4|>=11.6,<11.7|>=11.5,<11.6|>=11.1,<11.2|>=11.0,<11.1|>=9.2,<9.3|>=11.2,<12|11.0|11.0.*|11.1|11.1.*|>=11.2,<12.0a0|9.2|9.2.*|>=11.8.0,<11.9.0a0|>=11.3.1,<11.4.0a0|>=10.1.243,<10.2.0a0|>=9.2,<9.3.0a0|>=10.0.130,<10.1.0a0|9.2.*|>=9.0,<9.1.0a0|>=8.0,<8.1.0a0|9.0.*|8.0.*|7.5.*']
  - pytorch -> cudnn[version='>=8.8.0.121,<9.0a0'] -> cudatoolkit[version='10.2.*|11.*|>=9.0,<9.1|>=10.0,<10.1|>=11.8.0|8.*|>=10.2.89,<10.3.0a0']
  - pytorch -> pytorch-cuda[version='>=11.6,<11.7|>=11.7,<11.8|>=11.8,<11.9']
  - torchaudio -> cudatoolkit[version='>=10.2,<10.3|>=11.3,<11.4|>=11.6,<11.7|>=11.1,<11.2|>=11.5,<11.6']
  - torchaudio -> pytorch-cuda[version='11.6.*|11.7.*|11.8.*']
  - torchaudio -> pytorch==2.0.1 -> cudatoolkit[version='10.0|10.0.*|10.1|10.1.*|10.2|10.2.*|>=11.2,<12|>=11.8.0,<11.9.0a0|>=11.3.1,<11.4.0a0|11.0|11.0.*|11.1|11.1.*|>=11.2,<12.0a0|>=10.1,<10.2|>=11.0,<11.1|>=9.2,<9.3|9.2|9.2.*']
  - torchaudio -> pytorch==2.0.1 -> pytorch-cuda[version='>=11.6,<11.7|>=11.7,<11.8|>=11.8,<11.9']
  - torchaudio -> pytorch[version='1.10.0|1.10.1|1.10.2|1.11.0|1.12.0|1.12.1|1.13.0|1.13.1|2.0.0|2.0.1|1.9.1|1.9.0|1.8.1|1.8.0|1.7.1|1.7.0|1.6.0|1.5.1']
  - torchvision -> cudatoolkit[version='10.2|10.2.*|11.0|11.0.*|11.1|11.1.*|>=10.1,<10.2|>=10.2,<10.3|>=11.3,<11.4|>=11.6,<11.7|>=11.5,<11.6|>=11.1,<11.2|>=11.0,<11.1|>=9.2,<9.3|>=11.2,<12|>=11.2,<12.0a0|>=11.8.0,<11.9.0a0|>=10.0.130,<10.1.0a0|>=9.2,<9.3.0a0|>=9.0,<9.1.0a0']
  - torchvision -> pytorch-cpu -> pytorch[version='1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.0|1.10.1|1.10.1|1.10.1|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.13.0|1.13.0|1.13.0|1.13.0|1.13.1|1.13.1|1.13.1|1.13.1|1.13.1|1.13.1|1.13.1|1.13.1|2.0.0|1.9.1|1.9.1|1.9.1|1.9.1|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.7.1|1.7.1|1.7.1|1.7.1|1.7.1|1.7.1|1.7.1|1.7.1|1.6.0|1.6.0|1.6.0|1.6|2.0.0|2.0.0|2.0.0|2.0.0|2.0.0|2.0.0|2.0.0|2.0.0|2.0.0|2.0.0|2.0.0|1.13.1|1.13.1|1.13.1|1.13.1|1.13.0|1.13.0|1.13.0|1.13.0|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.1|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.12.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.11.0|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.2|1.10.1|1.10.1|1.10.1|1.10.1|1.10.1|1.10.1|1.10.1|1.10.1|1.10.1|1.10.1|1.10.1|1.10.1|1.9.1|1.9.1|1.9.1|1.9.1|1.9.1|1.9.1|1.9.1|1.9.1|1.9.1|1.9.1|1.9.1|1.9.1|1.9.1|1.9.1|1.9.1|1.9.1|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.9.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.8.0|1.7.1|1.7.1|1.7.1|1.7.1|1.7.1|1.7.1|1.7.1|1.7.1|1.7.1|1.7.1|1.7.1|1.7.1|1.7.1|1.7.1|1.7.1|1.7.1|1.6.0|1.6.0|1.6.0|1.6.0|1.6.0|1.6.0|1.6.0|1.6.0|1.6.0|1.6.0|1.6.0|1.6.0|1.6.0|1.6.0|1.6.0|1.6.0',build='cuda92py36h7ecc001_1|cuda100py36hd82b6f9_1|cuda102py36h8620ce9_1|cuda102py37h4d98c68_1|cuda100py37h50b9e00_1|cuda101py37h7589291_1|cuda101py38h2499a06_1|cuda100py38h679e3f5_1|cuda92py39hde86683_1|cuda100py39h2b73809_1|cuda101py39h41d04a9_1|cuda92py36h7ecc001_1|cuda100py36hd82b6f9_1|cuda100py37h50b9e00_1|cuda101py38h2499a06_1|cuda100py39h2b73809_1|cuda100py38h679e3f5_1|cuda101py39h41d04a9_1|cuda102py38h540557e_0|cuda110py38h65e529b_0|cuda110py39hbc72f07_0|cuda112py37h946b90b_1|cuda111py39hc274426_1|cuda102py36he3537ca_1|cuda102py38hf03d9dd_1|cuda110py36h768fbb7_1|cuda112py39hbeb36f3_1|cuda102py39h9bf10ef_1|cuda112py36h755b813_1|cuda111py37h78388d7_1|cuda110py39hd6acddb_1|cuda112py38h3d13190_1|cuda111py37he371307_3|cuda112py37h3bec1eb_3|cuda111py38h2f85826_3|cuda110py36he570edd_3|cuda110py38hf84197b_3|cuda111py37he371307_0|cuda102py38ha031fbe_0|cuda110py37h4a33b93_0|cuda102py37h98b7ee3_0|cuda111py39hb4a4491_0|cuda112py37haf94430_1|cuda112py38had345c2_1|cuda102py38h17946ce_1|cuda111py39h7295ad4_1|cuda111py38h9575ccd_1|cuda110py39h423d6c6_1|cuda110py37h7b7832c_1|cuda111py37h07fa5b8_1|cuda102py37hc804c4d_0|cuda102py39hfe0cb5b_0|cuda112py38h6425f36_0|cuda111py38hc64aeea_0|cuda110py39he47eb21_0|cuda110py37h4121e64_0|cuda112py38h6425f36_0|cuda110py39he47eb21_0|cuda110py37h4121e64_0|cuda102py37hc804c4d_0|cuda102py38h9fb240c_0|cuda102py37hc804c4d_1|cuda112py38h6425f36_1|cuda110py37h4121e64_1|cuda110py39he47eb21_1|cuda102py39hfe0cb5b_1|cuda112py39h4de5995_1|cuda102py39hfe0cb5b_0|cuda102py38hfdb21e3_1|cuda112py38habe9d5a_1|cuda110py38h386aa8f_1|cuda110py37h0def887_1|cuda111py37hdb2541a_1|cuda110py310hfdf97d1_1|cuda102py39hbbcd3cb_1|cuda112py39ha0cca9b_1|cuda111py38h2d04dd0_1|cuda110py39h0a9da28_1|cuda102py39hbbcd3cb_202|cuda102py310hdf4a2db_202|cuda102py37haad9b4f_202|cuda110py39h0a9da28_202|cuda110py310hfdf97d1_202|cuda111py38h2d04dd0_202|cuda112py39ha0cca9b_202|cuda112py38habe9d5a_202|cuda112py310h51fe464_202|cuda110py38h386aa8f_200|cuda110py310hfdf97d1_200|cuda111py39h9f128c5_200|cuda102py39hbbcd3cb_200|cuda112py39ha0cca9b_200|cuda110py39h0a9da28_200|cuda112py310h51fe464_200|cuda111py310h385535d_200|cuda112py38habe9d5a_202|cuda110py310hfdf97d1_202|cuda111py39h9f128c5_202|cuda102py39hbbcd3cb_202|cuda112py39ha0cca9b_202|cuda111py38h2d04dd0_202|cuda102py39hbbcd3cb_200|cuda112py37hfcfbd4c_200|cuda112py39ha0cca9b_200|cuda112py38habe9d5a_200|cuda110py310hfdf97d1_200|cuda110py38h386aa8f_200|cuda111py39h2c296c9_201|cuda111py38h6bd3925_201|cuda112py39hb0b7ed5_201|cuda112py37h6a44366_201|cuda112py38hd94e077_201|cuda110py310he962cc7_201|cuda102py39h5d53aaf_201|cuda112py311h13fee9e_200|cuda112py310he33e0d6_200|cuda112py310he33e0d6_200|cuda112py311h13fee9e_200|cuda112py39ha9981d0_200|cuda112py38h5e67e12_200|cuda112py310he33e0d6_200|cuda112py39ha9a2dba_301|cuda112py39h14ee7d9_302|cuda112py310he0931da_302|cpu_py37hf1c21f6_1|cpu_py38h36eccb8_1|cpu_py39h714fb45_1|cpu_py37hf1c21f6_1|cpu_py39h714fb45_2|cpu_py38h36eccb8_2|cpu_py37hf1c21f6_2|cpu_py36h2ecc29a_0|cpu_py37hafa7651_0|cpu_py38he614459_0|cpu_py37ha70c682_1|cpu_py39h0fbb4fb_1|cpu_py38hd248515_1|cpu_py37hd5260e0_2|cpu_py38h91ab35c_2|cpu_py39hfbcbfe4_2|cpu_py37hd5260e0_3|cpu_py38h91ab35c_0|cpu_py36h3564fbe_1|cpu_py36h1c7b8ea_2|cpu_py39h818de69_2|cpu_py39hc5866cc_3|cpu_py38h1ee18c8_3|cpu_py37hf3cc979_0|cpu_py38h1ee18c8_0|cpu_py37h2761dfd_1|cpu_py38h7c5583f_1|cpu_py38hb2150b6_0|cpu_py37h76afcab_0|cpu_py39h5e9ed0b_0|cpu_py37h76afcab_0|cpu_py38hb2150b6_0|cpu_py37h76afcab_1|cpu_py38hde1b6bc_0|cpu_py37h14e09b7_1|cpu_py310h75c9ab6_2|cpu_py38h39c826d_2|cpu_py39h5d22d69_0|cpu_py38h39c826d_0|cpu_py37h14e09b7_1|cpu_py38h39c826d_1|cpu_py38h39c826d_2|cpu_py39h5d22d69_2|cpu_py38h39c826d_0|cpu_py39h5d22d69_0|cpu_py310h75c9ab6_0|cpu_py38h23e632a_0|cpu_py39h3439074_0|cpu_py311h410fd25_0|cpu_py38hbac4b8a_1|cpu_py310hd11e9c7_1|cpu_py311h410fd25_1|cpu_py39h14c4022_1|cpu_py311h410fd25_0|cpu_generic_py311h7ba3f10_1|cpu_generic_py310h7ffd2bf_1|cpu_generic_py39h000fad7_1|cpu_generic_py39h08b6d46_2|cpu_generic_py38hbf964b3_2|cpu_mkl_py311hd1ebf82_101|cpu_mkl_py38h85d2d9a_101|cpu_mkl_py39h5fe9f1c_102|cpu_mkl_py310h44e7ea7_102|cpu_mkl_py38ha58350c_102|cpu_mkl_py311h6acbe2c_102|cpu_mkl_py310h402c8e3_101|cpu_mkl_py39h9f63279_101|cpu_generic_py311h59ffd09_2|cpu_generic_py310h21fa2ab_2|cpu_generic_py38h1f6ab43_1|cpu_py39he4d1dc0_0|cpu_py310hd11e9c7_0|cpu_py38h019455c_0|cpu_py310hd11e9c7_0|cpu_py38hbac4b8a_0|cpu_py39h14c4022_0|cpu_py311h854973f_0|cpu_py310h02c325b_0|cpu_py310h02c325b_1|cpu_py38h23e632a_1|cpu_py39h3439074_1|cpu_py37h167888a_1|cpu_py37h14e09b7_0|cpu_py310h75c9ab6_2|cpu_py37h14e09b7_2|cpu_py310h75c9ab6_1|cpu_py39h5d22d69_1|cpu_py37h14e09b7_0|cpu_py310h75c9ab6_0|cpu_py39h5d22d69_2|cpu_py37h14e09b7_2|cpu_py39h5d22d69_1|cpu_py310h75c9ab6_1|cpu_py38h39c826d_1|cpu_py310h2272b30_0|cpu_py39h7613f69_0|cpu_py37hd754017_0|cpu_py39h5e9ed0b_1|cpu_py38hb2150b6_1|cpu_py39h5e9ed0b_0|cpu_py39hc70245e_1|cpu_py39hc5866cc_0|cpu_py36ha8b20dc_3|cpu_py37hf3cc979_3|cpu_py38h4bbe6ce_2|cpu_py37hb06efa0_2|cpu_py39h818de69_1|cpu_py37hff829bd_1|cpu_py38hfb3baa6_1|cpu_py36h95c28ec_0|cpu_py37hd5260e0_0|cpu_py39hfbcbfe4_0|cpu_py39hfbcbfe4_3|cpu_py36h95c28ec_3|cpu_py38h91ab35c_3|cpu_py36h95c28ec_2|cpu_py36h2d15a6b_1|cpu_py39h0fbb4fb_0|cpu_py36h63cae03_2|cpu_py36h63cae03_1|cpu_py38h36eccb8_1|cpu_py36h63cae03_1|cuda112py38hf22b3e7_302|cuda112py310h21def76_301|cuda112py38haa925fe_301|cuda112py311hc11b779_301|cuda112py311h13fee9e_200|cuda112py38hd94e077_200|cuda112py39hb0b7ed5_200|cuda112py38hd94e077_200|cuda112py39hb0b7ed5_200|cuda102py38h6471756_201|cuda102py37h60b181b_201|cuda110py38haf7ec07_201|cuda110py37h54de3e3_201|cuda102py310ha664643_201|cuda110py39h10c7883_201|cuda112py310he33e0d6_201|cuda111py310h338e39d_201|cuda111py37he43340c_201|cuda110py39h0a9da28_200|cuda110py37h0def887_200|cuda102py37haad9b4f_200|cuda111py310h385535d_200|cuda111py37hdb2541a_200|cuda112py310h51fe464_200|cuda102py38hfdb21e3_200|cuda111py38h2d04dd0_200|cuda111py39h9f128c5_200|cuda102py310hdf4a2db_200|cuda111py310h385535d_202|cuda112py310h51fe464_202|cuda110py39h0a9da28_202|cuda102py37haad9b4f_202|cuda112py37hfcfbd4c_202|cuda111py37hdb2541a_202|cuda110py37h0def887_202|cuda110py38h386aa8f_202|cuda102py310hdf4a2db_202|cuda102py38hfdb21e3_202|cuda111py38h2d04dd0_200|cuda102py37haad9b4f_200|cuda112py37hfcfbd4c_200|cuda111py37hdb2541a_200|cuda110py37h0def887_200|cuda102py310hdf4a2db_200|cuda112py38habe9d5a_200|cuda102py38hfdb21e3_200|cuda112py37hfcfbd4c_202|cuda111py310h385535d_202|cuda111py39h9f128c5_202|cuda111py37hdb2541a_202|cuda110py37h0def887_202|cuda110py38h386aa8f_202|cuda102py38hfdb21e3_202|cuda111py310h385535d_1|cuda112py310h51fe464_1|cuda111py39h9f128c5_1|cuda102py37haad9b4f_1|cuda112py37hfcfbd4c_1|cuda102py310hdf4a2db_1|cuda110py38hade5236_0|cuda111py39h930882a_1|cuda102py38h9fb240c_1|cuda111py38hc64aeea_1|cuda110py38hf0a79ac_1|cuda112py37hc1ee5ce_1|cuda111py37hc0ce48b_1|cuda102py39hfe0cb5b_0|cuda110py38hf0a79ac_0|cuda111py37hc0ce48b_0|cuda111py39h930882a_0|cuda111py38hc64aeea_0|cuda112py37hc1ee5ce_0|cuda112py39h4de5995_0|cuda110py38hf0a79ac_0|cuda111py37hc0ce48b_0|cuda111py39h930882a_0|cuda112py37hc1ee5ce_0|cuda112py39h4de5995_0|cuda102py38h9fb240c_0|cuda102py37h689c94d_1|cuda102py39h06ffc54_1|cuda110py38h68479e5_1|cuda112py39h3ad47f5_1|cuda112py39h4e14dd4_0|cuda110py39h5cf7045_0|cuda112py38h4f2a933_0|cuda111py38h2f85826_0|cuda112py37h3bec1eb_0|cuda102py39h2fcd037_0|cuda110py38hf84197b_0|cuda110py39h5cf7045_3|cuda110py37h4a33b93_3|cuda102py39h2fcd037_3|cuda102py38ha031fbe_3|cuda102py37h98b7ee3_3|cuda102py36h3d4679f_3|cuda111py39hb4a4491_3|cuda112py39h4e14dd4_3|cuda111py36h8a2106e_3|cuda112py36h36e649e_3|cuda112py38h4f2a933_3|cuda102py37h92fd811_1|cuda110py37h00edf66_1|cuda111py36hc5445e6_1|cuda112py37hcb91bf2_1|cuda110py38hc2289b8_1|cuda111py38h5169e65_1|cuda111py37h50e976f_1|cuda112py36h5fea6e2_1|cuda111py36h3cb1cac_1|cuda112py39h716d6ff_1|cuda111py39h37e5b68_1|cuda112py38h3bc52bc_1|cuda111py38he2736ed_1|cuda110py37h5fb8b0b_0|cuda110py36h7ef7e1d_0|cuda102py39hf89b2ab_0|cuda102py37h4454d97_0|cuda102py36hf4eb8d7_0|cuda102py38h9f8c3ab_1|cuda101py36h42dc283_1|cuda92py38hb6ed0dd_1|cuda102py39h09d0254_1|cuda92py39hde86683_1|cuda102py37h4d98c68_1|cuda92py37hc3ec645_1|cuda101py37h7589291_1|cuda102py36h8620ce9_1|cuda102py38h9f8c3ab_1|cuda102py39h09d0254_1|cuda92py38hb6ed0dd_1|cuda92py37hc3ec645_1|cuda101py36h42dc283_1']
  - torchvision -> pytorch-cuda[version='11.6.*|11.7.*|11.8.*']
  - torchvision -> pytorch==1.13.1 -> cudatoolkit[version='10.0.*|10.0|10.0.*|10.1|10.1.*|>=11.3.1,<11.4.0a0|9.2|9.2.*|11.*|10.2.*|>=10.1.243,<10.2.0a0|9.2.*|>=8.0,<8.1.0a0|9.0.*|8.0.*|7.5.*']
  - torchvision -> pytorch==2.0.1 -> pytorch-cuda[version='>=11.6,<11.7|>=11.7,<11.8|>=11.8,<11.9']
  - torchvision -> pytorch[version='*|*|1.10.*|1.10.*|1.10|1.10|1.10.0|1.10.1|1.10.2|1.11.0|1.12.0|1.12.1|1.13.0|1.13.1|2.0.0|2.0.1|1.9.1|1.9.0|1.8.1|1.8.0|1.7.1|1.7.0|1.6.0|1.5.1|>=2.0.0,<2.1.0a0|>=1.13.1,<1.14.0a0|>=1.13.0,<1.14.0a0|>=1.12.0,<1.13.0a0|>=1.11.0,<1.12.0a0|>=1.10.2,<1.11.0a0|1.10.0.*|>=1.8.0|>=1.8.0|1.7.1.*|1.3.1.*|1.2.0.*|1.1.*|>=0.4|>=0.3',build='cuda*|cpu*|cpu*|cuda*|cpu*|cuda*|cuda*|cpu*']

The following specifications were found to be incompatible with each other:

Output in format: Requested package -> Available versions

Package libstdcxx-ng conflicts for:
libcublas -> libstdcxx-ng[version='>=12']
pip -> python[version='>=3.7'] -> libstdcxx-ng[version='>=11.2.0|>=4.9|>=7.3.0|>=7.5.0|>=9.3.0|>=9.4.0|>=7.2.0']
libnpp -> libstdcxx-ng[version='>=12']
numpy -> python[version='>=3.9,<3.10.0a0'] -> libstdcxx-ng[version='>=7.2.0|>=9.3.0']
mkl -> libstdcxx-ng[version='>=11.2.0']
openjpeg -> libstdcxx-ng[version='>=10.3.0|>=12|>=9.3.0|>=7.3.0|>=4.9|>=7.5.0|>=7.2.0']
pytorch -> libstdcxx-ng[version='>=10.3.0|>=12|>=7.5.0|>=9.4.0|>=11.2.0|>=9.3.0|>=7.3.0|>=5.4.0']
icu -> libstdcxx-ng[version='>=10.3.0|>=12|>=9.4.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
ffmpeg -> libstdcxx-ng[version='>=10.3.0|>=12|>=7.3.0|>=9.4.0|>=9.3.0|>=7.5.0|>=4.9|>=7.2.0']
libtiff -> zstd[version='>=1.5.2,<1.6.0a0'] -> libstdcxx-ng[version='>=10.3.0']
libcurand -> libstdcxx-ng[version='>=12']
libhwloc -> libstdcxx-ng[version='>=10.3.0|>=12|>=7.5.0|>=9.4.0|>=9.3.0|>=7.3.0|>=4.9']
llvm-openmp -> zstd[version='>=1.5.2,<1.6.0a0'] -> libstdcxx-ng[version='>=10.3.0|>=12|>=9.4.0|>=11.2.0|>=7.5.0']
torchvision -> libstdcxx-ng[version='>=10.3.0|>=12|>=7.5.0|>=9.4.0|>=11.2.0|>=7.3.0|>=5.4.0']
requests -> python[version='>=3.7'] -> libstdcxx-ng[version='>=11.2.0|>=4.9|>=7.3.0|>=7.5.0|>=9.3.0|>=9.4.0|>=7.2.0']
mkl -> tbb=2021 -> libstdcxx-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0']
cuda-nvrtc -> libstdcxx-ng[version='>=12']
cudatoolkit=11.1 -> libstdcxx-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0']
libblas -> mkl[version='>=2022.1.0,<2023.0a0'] -> libstdcxx-ng[version='>=11.2.0|>=7.5.0']
blas-devel -> mkl[version='>=2022.1.0,<2023.0a0'] -> libstdcxx-ng[version='>=11.2.0']
openh264 -> libstdcxx-ng[version='>=12|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9']
libcufft -> libstdcxx-ng[version='>=12']
sqlite -> ncurses[version='>=6.2,<7.0.0a0'] -> libstdcxx-ng[version='>=7.2.0|>=7.5.0']
libffi -> libstdcxx-ng[version='>=11.2.0|>=4.9|>=7.3.0|>=7.5.0|>=9.4.0|>=7.2.0']
nettle -> gmp[version='>=6.1.2,<7.0a0'] -> libstdcxx-ng[version='>=7.2.0|>=7.5.0']
cuda-cudart -> libstdcxx-ng[version='>=12']
freetype -> libstdcxx-ng[version='>=4.9']
cuda-nvtx -> libstdcxx-ng[version='>=12']
tbb -> libstdcxx-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
typing_extensions -> python[version='>=3.7'] -> libstdcxx-ng[version='>=11.2.0|>=4.9|>=7.3.0|>=7.5.0|>=9.3.0|>=9.4.0|>=7.2.0']
certifi -> python[version='>=3.7'] -> libstdcxx-ng[version='>=11.2.0|>=4.9|>=7.3.0|>=7.5.0|>=9.3.0|>=9.4.0|>=7.2.0']
urllib3 -> brotli-python[version='>=1.0.9'] -> libstdcxx-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=11.2.0|>=7.3.0|>=4.9|>=7.2.0']
lerc -> libstdcxx-ng[version='>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0']
zstd -> libstdcxx-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0']
python_abi -> python=3.9 -> libstdcxx-ng[version='>=11.2.0|>=7.5.0|>=9.3.0|>=7.3.0|>=9.4.0|>=4.9|>=7.2.0']
pysocks -> python[version='>=3.8'] -> libstdcxx-ng[version='>=11.2.0|>=7.3.0|>=7.5.0|>=9.3.0|>=9.4.0|>=4.9|>=7.2.0']
setuptools -> python[version='>=3.7'] -> libstdcxx-ng[version='>=11.2.0|>=4.9|>=7.3.0|>=7.5.0|>=9.3.0|>=9.4.0|>=7.2.0']
ncurses -> libstdcxx-ng[version='>=4.9|>=7.3.0|>=7.5.0|>=7.2.0']
lcms2 -> libtiff[version='>=4.6.0,<4.7.0a0'] -> libstdcxx-ng[version='>=11.2.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0']
gmp -> libstdcxx-ng[version='>=4.9|>=7.3.0|>=7.5.0|>=7.2.0']
pillow -> libtiff[version='>=4.5.1,<4.6.0a0'] -> libstdcxx-ng[version='>=10.3.0|>=12|>=9.3.0|>=7.3.0|>=9.4.0|>=4.9|>=7.2.0']
pytorch -> python[version='>=3.7,<3.8.0a0'] -> libstdcxx-ng[version='>=3.4|>=4.9|>=7.2.0']
llvm-openmp -> libstdcxx-ng[version='>=7.3.0']
torchvision -> ffmpeg[version='>=4.2'] -> libstdcxx-ng[version='>=3.4|>=4.9|>=9.3.0|>=8.4.0|>=7.2.0']
charset-normalizer -> python[version='>=3.7'] -> libstdcxx-ng[version='>=11.2.0|>=4.9|>=7.3.0|>=7.5.0|>=9.3.0|>=9.4.0|>=7.2.0']
libhwloc -> cudatoolkit[version='>=11.2,<12'] -> libstdcxx-ng[version='>=11.2.0']
_openmp_mutex -> llvm-openmp[version='>=9.0.1'] -> libstdcxx-ng[version='>=7.3.0']
pillow -> libstdcxx-ng[version='>=11.2.0|>=7.5.0|>=8.4.0']
nettle -> libstdcxx-ng[version='>=4.9|>=7.3.0']
libtiff -> libstdcxx-ng[version='>=11.2.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=7.2.0']
sqlite -> libstdcxx-ng[version='>=4.9|>=7.3.0']
cuda-libraries -> cuda-cudart=12.0.107 -> libstdcxx-ng[version='>=12']
torchaudio -> numpy[version='>=1.11'] -> libstdcxx-ng[version='>=10.3.0|>=12|>=9.4.0|>=7.3.0|>=4.9|>=11.2.0|>=7.5.0|>=9.3.0|>=7.2.0']
gnutls -> gmp[version='>=6.1.2,<7.0a0'] -> libstdcxx-ng[version='>=7.2.0']
gnutls -> libstdcxx-ng[version='>=12|>=7.5.0|>=7.3.0|>=4.9']
python=3.7.5 -> libstdcxx-ng[version='>=7.3.0|>=9.3.0']
libxml2 -> icu[version='>=73.2,<74.0a0'] -> libstdcxx-ng[version='>=10.3.0|>=12|>=9.4.0|>=7.5.0|>=7.3.0|>=4.9|>=7.2.0|>=11.2.0']
libcusparse -> libstdcxx-ng[version='>=12']
openjpeg -> libtiff[version='>=4.5.0,<4.6.0a0'] -> libstdcxx-ng[version='>=11.2.0|>=9.4.0']
readline -> ncurses[version='>=6.2,<7.0.0a0'] -> libstdcxx-ng[version='>=4.9|>=7.3.0|>=7.5.0|>=7.2.0']
python=3.7.5 -> libffi[version='>=3.3,<3.4.0a0'] -> libstdcxx-ng[version='>=4.9|>=7.5.0|>=7.2.0']
libcufile -> libstdcxx-ng[version='>=12']
cuda-cupti -> libstdcxx-ng[version='>=12']
wheel -> python[version='>=3.7'] -> libstdcxx-ng[version='>=11.2.0|>=4.9|>=7.3.0|>=7.5.0|>=9.3.0|>=9.4.0|>=7.2.0']
idna -> python[version='>=3.6'] -> libstdcxx-ng[version='>=11.2.0|>=4.9|>=7.3.0|>=7.5.0|>=9.3.0|>=9.4.0|>=7.2.0']
numpy -> libstdcxx-ng[version='>=10.3.0|>=12|>=9.4.0|>=7.3.0|>=4.9|>=11.2.0|>=7.5.0']
brotli -> libstdcxx-ng[version='>=4.9|>=7.3.0|>=7.5.0|>=9.3.0|>=7.2.0']
blas -> llvm-openmp[version='>=9.0.1'] -> libstdcxx-ng[version='>=11.2.0|>=7.3.0']
mkl-devel -> mkl==2023.1.0=h213fc3f_46343 -> libstdcxx-ng[version='>=11.2.0']
libcusolver -> libstdcxx-ng[version='>=12']
libnvjpeg -> libstdcxx-ng[version='>=12']

Package _openmp_mutex conflicts for:
libffi -> libgcc-ng[version='>=9.4.0'] -> _openmp_mutex[version='>=4.5']
freetype -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
ffmpeg -> libgcc-ng[version='>=7.3.0'] -> _openmp_mutex[version='>=4.5']
pthread-stubs -> libgcc-ng[version='>=7.5.0'] -> _openmp_mutex[version='>=4.5']
libblas -> libopenblas[version='>=0.3.24,<0.3.25.0a0'] -> _openmp_mutex[version='*|>=4.5',build=*_llvm]
libbrotlicommon -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libcusparse -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
nettle -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
icu -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libcblas -> libgcc-ng[version='>=9.3.0'] -> _openmp_mutex[version='>=4.5']
libbrotlienc -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libxml2 -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
cudatoolkit=11.1 -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
lame -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libsqlite -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
blas -> libgcc-ng[version='>=10.3.0'] -> _openmp_mutex
cuda-cudart -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
xz -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
gmp -> libgcc-ng[version='>=7.5.0'] -> _openmp_mutex[version='>=4.5']
libhwloc -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
gnutls -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
openjpeg -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libnpp -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
brotli -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libbrotlidec -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
xorg-libxau -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libtiff -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libcufile -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libcufft -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
lerc -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libdeflate -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
brotli-bin -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libcublas -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libwebp-base -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
mkl-devel -> mkl==2023.2.0=h84fe81f_49572 -> _openmp_mutex[version='*|>=4.5',build=*_llvm]
zstd -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libpng -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
pillow -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
python=3.7.5 -> libgcc-ng[version='>=9.3.0'] -> _openmp_mutex[version='>=4.5']
liblapack -> libgcc-ng[version='>=9.3.0'] -> _openmp_mutex[version='>=4.5']
cuda-nvrtc -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
openssl -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
torchaudio -> pytorch==2.0.1 -> _openmp_mutex[version='>=4.5']
mkl -> _openmp_mutex[version='*|>=4.5',build=*_llvm]
liblapacke -> libgcc-ng[version='>=9.3.0'] -> _openmp_mutex[version='>=4.5']
readline -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
blas -> _openmp_mutex[version='*|>=4.5',build=*_llvm]
libzlib -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
sqlite -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
xorg-libxdmcp -> libgcc-ng[version='>=9.3.0'] -> _openmp_mutex[version='>=4.5']
lcms2 -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
llvm-openmp -> libgcc-ng[version='>=7.3.0'] -> _openmp_mutex[version='>=4.5']
pytorch -> _openmp_mutex[version='>=4.5']
ncurses -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
blas-devel -> openblas=0.3.24 -> _openmp_mutex[version='*|>=4.5',build=*_llvm]
numpy -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='*|>=4.5',build=*_llvm]
bzip2 -> libgcc-ng[version='>=9.3.0'] -> _openmp_mutex[version='>=4.5']
cuda-nvtx -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libgcc-ng -> _openmp_mutex[version='>=4.5']
jpeg -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
pytorch -> blas=[build=mkl] -> _openmp_mutex[version='*|>=5.1',build=*_llvm]
zlib -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libnvjpeg -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
openh264 -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libxcb -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libcurand -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
mkl -> libgcc-ng[version='>=11.2.0'] -> _openmp_mutex
libcusolver -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
tbb -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
torchvision -> pytorch==2.0.1 -> _openmp_mutex[version='>=4.5']
cuda-cupti -> libgcc-ng[version='>=12'] -> _openmp_mutex[version='>=4.5']
libiconv -> libgcc-ng[version='>=10.3.0'] -> _openmp_mutex[version='>=4.5']

Package libgcc-ng conflicts for:
torchvision -> libgcc-ng[version='>=10.3.0|>=12|>=7.5.0|>=9.4.0|>=11.2.0|>=7.3.0|>=5.4.0']
libhwloc -> libgcc-ng[version='>=10.3.0|>=12|>=7.5.0|>=9.4.0|>=9.3.0|>=7.3.0']
gnutls -> libidn2[version='>=2,<3.0a0'] -> libgcc-ng[version='>=10.3.0|>=11.2.0|>=9.3.0|>=9.4.0|>=7.2.0']
ncurses -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
ffmpeg -> libgcc-ng[version='>=10.3.0|>=12|>=7.3.0|>=9.4.0|>=9.3.0|>=7.5.0|>=4.9|>=7.2.0']
readline -> libgcc-ng[version='>=11.2.0|>=12|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=7.2.0']
lerc -> libgcc-ng[version='>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0']
blas-devel -> liblapack==3.9.0[build=*netlib] -> libgcc-ng[version='>=10.3.0|>=11.2.0|>=12|>=7.5.0|>=9.3.0|>=9.4.0|>=7.3.0|>=4.9']
pysocks -> python[version='>=3.8'] -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=11.2.0|>=4.9|>=7.2.0']
openjpeg -> libpng[version='>=1.6.39,<1.7.0a0'] -> libgcc-ng[version='>=11.2.0|>=9.4.0']
libcblas -> libgcc-ng[version='>=7.3.0|>=7.5.0|>=9.3.0']
libffi -> libgcc-ng[version='>=11.2.0|>=4.9|>=7.3.0|>=7.5.0|>=9.4.0|>=7.2.0']
libcusparse -> libgcc-ng[version='>=12']
xorg-libxdmcp -> libgcc-ng[version='>=4.9|>=7.3.0|>=9.3.0']
openh264 -> zlib[version='>=1.2.11,<1.3.0a0'] -> libgcc-ng[version='>=10.3.0|>=11.2.0|>=7.2.0']
numpy -> libopenblas[version='>=0.3.2,<0.3.3.0a0'] -> libgcc-ng[version='>=8.2.0']
libcufft -> libgcc-ng[version='>=12']
blas -> openblas -> libgcc-ng[version='>=11.2.0|>=4.9']
liblapacke -> libgcc-ng[version='>=7.3.0|>=7.5.0|>=9.3.0']
libtiff -> libgcc-ng[version='>=11.2.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=7.2.0']
mkl -> tbb=2021 -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0']
libbrotlienc -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=11.2.0']
libdeflate -> libgcc-ng[version='>=11.2.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0']
tbb -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=11.2.0|>=7.2.0']
libxcb -> libgcc-ng[version='>=12|>=9.4.0|>=9.3.0|>=7.3.0|>=4.9|>=7.5.0|>=7.2.0']
brotli-bin -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=11.2.0']
libblas -> libgcc-ng[version='>=7.3.0|>=7.5.0|>=9.3.0']
setuptools -> python[version='>=3.7'] -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
idna -> python[version='>=3.6'] -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
python_abi -> python=3.11 -> libgcc-ng[version='>=10.3.0|>=11.2.0|>=12|>=9.4.0|>=7.5.0|>=9.3.0|>=7.3.0|>=4.9|>=7.2.0']
certifi -> python[version='>=3.7'] -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
libbrotlicommon -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=11.2.0']
zstd -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
readline -> ncurses[version='>=6.3,<7.0a0'] -> libgcc-ng[version='>=10.3.0|>=9.4.0']
gmp -> libgcc-ng[version='>=4.9|>=7.3.0|>=7.5.0|>=7.2.0']
liblapack -> libgcc-ng[version='>=7.3.0|>=7.5.0|>=9.3.0']
cudatoolkit=11.1 -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0']
typing_extensions -> python[version='>=3.7'] -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
libwebp-base -> libgcc-ng[version='>=11.2.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0']
charset-normalizer -> python[version='>=3.7'] -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
ffmpeg -> freetype[version='>=2.10.2,<3.0a0'] -> libgcc-ng[version='>=11.2.0']
libiconv -> libgcc-ng[version='>=10.3.0|>=7.5.0|>=7.3.0|>=4.9|>=7.2.0']
lcms2 -> libtiff[version='>=4.5.0,<4.6.0a0'] -> libgcc-ng[version='>=10.3.0|>=11.2.0|>=9.4.0|>=7.2.0']
llvm-openmp -> libzlib[version='>=1.2.13,<1.3.0a0'] -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=11.2.0|>=7.5.0']
libhwloc -> cudatoolkit[version='>=11.2,<12'] -> libgcc-ng[version='>=11.2.0|>=4.9|>=7.2.0']
libtiff -> zstd[version='>=1.5.2,<1.6.0a0'] -> libgcc-ng[version='>=10.3.0']
cuda-cupti -> libgcc-ng[version='>=12']
gnutls -> libgcc-ng[version='>=12|>=7.5.0|>=7.3.0|>=4.9']
pytorch -> libgcc-ng[version='>=10.3.0|>=12|>=7.5.0|>=9.4.0|>=11.2.0|>=9.3.0|>=7.3.0|>=5.4.0']
libcusolver -> libgcc-ng[version='>=12']
bzip2 -> libgcc-ng[version='>=4.9|>=7.3.0|>=7.5.0|>=9.3.0|>=7.2.0']
pip -> python[version='>=3.7'] -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
libcublas -> libgcc-ng[version='>=12']
libnpp -> libgcc-ng[version='>=12']
libpng -> zlib[version='>=1.2.11,<1.3.0a0'] -> libgcc-ng[version='>=10.3.0']
libbrotlidec -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=11.2.0']
cuda-nvrtc -> libgcc-ng[version='>=12']
wheel -> python[version='>=3.7'] -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
jpeg -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=7.5.0|>=7.3.0|>=11.2.0|>=7.2.0']
nettle -> gmp[version='>=6.1.2,<7.0a0'] -> libgcc-ng[version='>=7.2.0']
mkl -> libgcc-ng[version='>=11.2.0']
lcms2 -> libgcc-ng[version='>=12|>=9.3.0|>=7.5.0|>=7.3.0']
torchaudio -> numpy[version='>=1.11'] -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
xz -> libgcc-ng[version='>=11.2.0|>=12|>=7.5.0|>=7.3.0|>=4.9|>=7.2.0']
python=3.7.5 -> libgcc-ng[version='>=7.3.0|>=9.3.0']
libcurand -> libgcc-ng[version='>=12']
freetype -> libgcc-ng[version='>=11.2.0|>=12|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=7.2.0']
icu -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
libnvjpeg -> libgcc-ng[version='>=12']
openh264 -> libgcc-ng[version='>=12|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9']
pillow -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=8.4.0|>=7.2.0']
blas -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0']
mkl-devel -> blas=[build=mkl] -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=11.2.0']
libpng -> libgcc-ng[version='>=11.2.0|>=12|>=7.5.0|>=7.3.0|>=4.9|>=7.2.0']
libxml2 -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
libzlib -> libgcc-ng[version='>=10.3.0|>=12|>=7.5.0']
zlib -> libgcc-ng[version='>=10.3.0|>=12|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
openssl -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
libblas -> blis[version='>=0.9.0,<0.9.1.0a0'] -> libgcc-ng[version='>=10.3.0|>=12|>=11.2.0|>=9.4.0']
nettle -> libgcc-ng[version='>=12|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9']
cuda-libraries -> cuda-cudart=12.0.107 -> libgcc-ng[version='>=12']
numpy -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
brotli -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
pytorch -> python[version='>=3.7,<3.8.0a0'] -> libgcc-ng[version='>=3.0|>=4.9|>=7.2.0|>=8.2.0']
urllib3 -> brotli-python[version='>=1.0.9'] -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=11.2.0|>=7.3.0|>=4.9|>=7.2.0']
libcufile -> libgcc-ng[version='>=12']
libsqlite -> libgcc-ng[version='>=12']
xorg-libxau -> libgcc-ng[version='>=12|>=9.3.0|>=7.3.0|>=4.9']
python=3.7.5 -> libffi[version='>=3.3,<3.4.0a0'] -> libgcc-ng[version='>=10.3.0|>=12|>=7.5.0|>=9.4.0|>=11.2.0|>=4.9|>=7.2.0']
sqlite -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
pthread-stubs -> libgcc-ng[version='>=4.9|>=7.3.0|>=7.5.0|>=7.2.0']
openjpeg -> libgcc-ng[version='>=10.3.0|>=12|>=9.3.0|>=7.3.0|>=4.9|>=7.5.0|>=7.2.0']
llvm-openmp -> libgcc-ng[version='>=7.3.0']
cuda-cudart -> libgcc-ng[version='>=12']
freetype -> zlib[version='>=1.2.11,<1.3.0a0'] -> libgcc-ng[version='>=10.3.0']
torchvision -> ffmpeg[version='>=4.2'] -> libgcc-ng[version='>=3.0|>=4.9|>=7.2.0|>=9.3.0|>=8.4.0']
_openmp_mutex -> llvm-openmp[version='>=9.0.1'] -> libgcc-ng[version='>=7.3.0']
requests -> python[version='>=3.7'] -> libgcc-ng[version='>=10.3.0|>=12|>=9.4.0|>=9.3.0|>=7.5.0|>=7.3.0|>=4.9|>=11.2.0|>=7.2.0']
lame -> libgcc-ng[version='>=12|>=9.3.0|>=7.3.0|>=4.9']
cuda-nvtx -> libgcc-ng[version='>=12']

Package idna conflicts for:
torchvision -> requests -> idna[version='>=2.5,<2.6|>=2.5,<2.7|>=2.5,<2.8|>=2.5,<2.9|>=2.5,<3|>=2.5,<4']
urllib3 -> cryptography[version='>=1.3.4'] -> idna[version='>=2.1']
requests -> urllib3[version='>=1.21.1,<3'] -> idna[version='>=2.0.0']
requests -> idna[version='>=2.5,<2.6|>=2.5,<2.7|>=2.5,<2.8|>=2.5,<2.9|>=2.5,<3|>=2.5,<4']
urllib3 -> idna[version='>=2.0.0']

Package openssl conflicts for:
pillow -> pypy3.9[version='>=7.3.11'] -> openssl[version='1.0.*|>=1.0.2o,<1.0.3a|>=1.0.2p,<1.0.3a|>=1.1.1a,<1.1.2a|>=1.1.1d,<1.1.2a|>=1.1.1e,<1.1.2a|>=1.1.1f,<1.1.2a|>=1.1.1g,<1.1.2a|>=1.1.1h,<1.1.2a|>=1.1.1i,<1.1.2a|>=1.1.1j,<1.1.2a|>=1.1.1k,<1.1.2a|>=1.1.1l,<1.1.2a|>=1.1.1n,<1.1.2a|>=1.1.1o,<1.1.2a|>=1.1.1s,<1.1.2a|>=3.0.7,<4.0a0|>=3.1.0,<4.0a0|>=3.1.2,<4.0a0|>=3.0.3,<4.0a0|>=3.0.2,<4.0a0|>=3.0.0,<4.0a0|>=3.0.10,<4.0a0|>=1.1.1v,<1.1.2a|>=1.1.1u,<1.1.2a|>=3.0.9,<4.0a0|>=3.0.8,<4.0a0|>=1.1.1t,<1.1.2a|>=1.1.1q,<1.1.2a|>=3.1.1,<4.0a0|>=3.0.5,<4.0a0|>=1.1.1m,<1.1.2a|>=1.1.1c,<1.1.2a|>=1.1.1b,<1.1.2a|>=1.0.2n,<1.0.3a|>=1.0.2m,<1.0.3a|>=1.0.2l,<1.0.3a']
idna -> python[version='>=3.6'] -> openssl[version='1.0.*|>=1.0.2o,<1.0.3a|>=1.0.2p,<1.0.3a|>=1.1.1a,<1.1.2a|>=1.1.1d,<1.1.2a|>=1.1.1e,<1.1.2a|>=1.1.1f,<1.1.2a|>=1.1.1g,<1.1.2a|>=1.1.1h,<1.1.2a|>=1.1.1i,<1.1.2a|>=1.1.1j,<1.1.2a|>=1.1.1k,<1.1.2a|>=1.1.1l,<1.1.2a|>=1.1.1n,<1.1.2a|>=1.1.1o,<1.1.2a|>=1.1.1q,<1.1.2a|>=1.1.1s,<1.1.2a|>=3.1.0,<4.0a0|>=3.1.1,<4.0a0|>=3.1.2,<4.0a0|>=3.0.7,<4.0a0|>=3.0.5,<4.0a0|>=3.0.3,<4.0a0|>=3.0.2,<4.0a0|>=3.0.0,<4.0a0|>=3.0.10,<4.0a0|>=1.1.1v,<1.1.2a|>=1.1.1u,<1.1.2a|>=3.0.9,<4.0a0|>=3.0.8,<4.0a0|>=1.1.1t,<1.1.2a|>=1.1.1m,<1.1.2a|>=1.1.1c,<1.1.2a|>=1.1.1b,<1.1.2a|>=1.0.2n,<1.0.3a|>=1.0.2m,<1.0.3a|>=1.0.2l,<1.0.3a']
requests -> python[version='>=3.7'] -> openssl[version='1.0.*|>=1.0.2o,<1.0.3a|>=1.0.2p,<1.0.3a|>=1.1.1a,<1.1.2a|>=1.1.1d,<1.1.2a|>=1.1.1e,<1.1.2a|>=1.1.1f,<1.1.2a|>=1.1.1g,<1.1.2a|>=1.1.1h,<1.1.2a|>=1.1.1i,<1.1.2a|>=1.1.1j,<1.1.2a|>=1.1.1k,<1.1.2a|>=1.1.1l,<1.1.2a|>=1.1.1n,<1.1.2a|>=1.1.1o,<1.1.2a|>=1.1.1q,<1.1.2a|>=1.1.1s,<1.1.2a|>=3.1.0,<4.0a0|>=3.1.1,<4.0a0|>=3.1.2,<4.0a0|>=3.0.7,<4.0a0|>=3.0.5,<4.0a0|>=3.0.3,<4.0a0|>=3.0.2,<4.0a0|>=3.0.0,<4.0a0|>=3.0.10,<4.0a0|>=1.1.1v,<1.1.2a|>=1.1.1u,<1.1.2a|>=3.0.9,<4.0a0|>=3.0.8,<4.0a0|>=1.1.1t,<1.1.2a|>=1.1.1m,<1.1.2a|>=1.1.1c,<1.1.2a|>=1.1.1b,<1.1.2a|>=1.0.2n,<1.0.3a|>=1.0.2m,<1.0.3a|>=1.0.2l,<1.0.3a']
python_abi -> python=3.11 -> openssl[version='1.0.*|>=1.0.2o,<1.0.3a|>=1.0.2p,<1.0.3a|>=1.1.1a,<1.1.2a|>=1.1.1d,<1.1.2a|>=1.1.1e,<1.1.2a|>=1.1.1f,<1.1.2a|>=1.1.1g,<1.1.2a|>=1.1.1h,<1.1.2a|>=1.1.1i,<1.1.2a|>=1.1.1j,<1.1.2a|>=1.1.1k,<1.1.2a|>=1.1.1l,<1.1.2a|>=1.1.1n,<1.1.2a|>=1.1.1o,<1.1.2a|>=1.1.1q,<1.1.2a|>=1.1.1s,<1.1.2a|>=3.1.0,<4.0a0|>=3.1.1,<4.0a0|>=3.1.2,<4.0a0|>=3.0.7,<4.0a0|>=3.0.5,<4.0a0|>=3.0.10,<4.0a0|>=1.1.1v,<1.1.2a|>=1.1.1u,<1.1.2a|>=3.0.9,<4.0a0|>=3.0.8,<4.0a0|>=1.1.1t,<1.1.2a|>=3.0.3,<4.0a0|>=3.0.2,<4.0a0|>=3.0.0,<4.0a0|>=1.1.1m,<1.1.2a|>=1.1.1c,<1.1.2a|>=1.1.1b,<1.1.2a|>=1.0.2n,<1.0.3a|>=1.0.2m,<1.0.3a|>=1.0.2l,<1.0.3a']
pip -> python[version='>=3.7'] -> openssl[version='1.0.*|>=1.0.2o,<1.0.3a|>=1.0.2p,<1.0.3a|>=1.1.1a,<1.1.2a|>=1.1.1d,<1.1.2a|>=1.1.1e,<1.1.2a|>=1.1.1f,<1.1.2a|>=1.1.1g,<1.1.2a|>=1.1.1h,<1.1.2a|>=1.1.1i,<1.1.2a|>=1.1.1j,<1.1.2a|>=1.1.1k,<1.1.2a|>=1.1.1l,<1.1.2a|>=1.1.1n,<1.1.2a|>=1.1.1o,<1.1.2a|>=1.1.1q,<1.1.2a|>=1.1.1s,<1.1.2a|>=3.1.0,<4.0a0|>=3.1.1,<4.0a0|>=3.1.2,<4.0a0|>=3.0.7,<4.0a0|>=3.0.5,<4.0a0|>=3.0.3,<4.0a0|>=3.0.2,<4.0a0|>=3.0.0,<4.0a0|>=3.0.10,<4.0a0|>=1.1.1v,<1.1.2a|>=1.1.1u,<1.1.2a|>=3.0.9,<4.0a0|>=3.0.8,<4.0a0|>=1.1.1t,<1.1.2a|>=1.1.1m,<1.1.2a|>=1.1.1c,<1.1.2a|>=1.1.1b,<1.1.2a|>=1.0.2n,<1.0.3a|>=1.0.2m,<1.0.3a|>=1.0.2l,<1.0.3a']
wheel -> python[version='>=3.7'] -> openssl[version='1.0.*|>=1.0.2o,<1.0.3a|>=1.0.2p,<1.0.3a|>=1.1.1a,<1.1.2a|>=1.1.1d,<1.1.2a|>=1.1.1e,<1.1.2a|>=1.1.1f,<1.1.2a|>=1.1.1g,<1.1.2a|>=1.1.1h,<1.1.2a|>=1.1.1i,<1.1.2a|>=1.1.1j,<1.1.2a|>=1.1.1k,<1.1.2a|>=1.1.1l,<1.1.2a|>=1.1.1n,<1.1.2a|>=1.1.1o,<1.1.2a|>=1.1.1q,<1.1.2a|>=1.1.1s,<1.1.2a|>=3.1.0,<4.0a0|>=3.1.1,<4.0a0|>=3.1.2,<4.0a0|>=3.0.7,<4.0a0|>=3.0.5,<4.0a0|>=3.0.3,<4.0a0|>=3.0.2,<4.0a0|>=3.0.0,<4.0a0|>=3.0.10,<4.0a0|>=1.1.1v,<1.1.2a|>=1.1.1u,<1.1.2a|>=3.0.9,<4.0a0|>=3.0.8,<4.0a0|>=1.1.1t,<1.1.2a|>=1.1.1m,<1.1.2a|>=1.1.1c,<1.1.2a|>=1.1.1b,<1.1.2a|>=1.0.2n,<1.0.3a|>=1.0.2m,<1.0.3a|>=1.0.2l,<1.0.3a']
numpy -> pypy3.9[version='>=7.3.11'] -> openssl[version='1.0.*|>=1.0.2o,<1.0.3a|>=1.0.2p,<1.0.3a|>=1.1.1a,<1.1.2a|>=1.1.1d,<1.1.2a|>=1.1.1e,<1.1.2a|>=1.1.1f,<1.1.2a|>=1.1.1g,<1.1.2a|>=1.1.1h,<1.1.2a|>=1.1.1i,<1.1.2a|>=1.1.1j,<1.1.2a|>=1.1.1k,<1.1.2a|>=1.1.1l,<1.1.2a|>=1.1.1n,<1.1.2a|>=1.1.1o,<1.1.2a|>=1.1.1s,<1.1.2a|>=3.0.7,<4.0a0|>=3.1.0,<4.0a0|>=3.1.2,<4.0a0|>=3.0.3,<4.0a0|>=3.0.2,<4.0a0|>=3.0.0,<4.0a0|>=3.0.10,<4.0a0|>=1.1.1v,<1.1.2a|>=1.1.1u,<1.1.2a|>=3.0.9,<4.0a0|>=3.0.8,<4.0a0|>=1.1.1t,<1.1.2a|>=1.1.1q,<1.1.2a|>=3.1.1,<4.0a0|>=3.0.5,<4.0a0|>=1.1.1m,<1.1.2a|>=1.1.1c,<1.1.2a|>=1.1.1b,<1.1.2a|>=1.0.2n,<1.0.3a|>=1.0.2m,<1.0.3a|>=1.0.2l,<1.0.3a']
setuptools -> python[version='>=3.7'] -> openssl[version='1.0.*|>=1.0.2o,<1.0.3a|>=1.0.2p,<1.0.3a|>=1.1.1a,<1.1.2a|>=1.1.1d,<1.1.2a|>=1.1.1e,<1.1.2a|>=1.1.1f,<1.1.2a|>=1.1.1g,<1.1.2a|>=1.1.1h,<1.1.2a|>=1.1.1i,<1.1.2a|>=1.1.1j,<1.1.2a|>=1.1.1k,<1.1.2a|>=1.1.1l,<1.1.2a|>=1.1.1n,<1.1.2a|>=1.1.1o,<1.1.2a|>=1.1.1q,<1.1.2a|>=1.1.1s,<1.1.2a|>=3.1.0,<4.0a0|>=3.1.1,<4.0a0|>=3.1.2,<4.0a0|>=3.0.7,<4.0a0|>=3.0.5,<4.0a0|>=3.0.3,<4.0a0|>=3.0.2,<4.0a0|>=3.0.0,<4.0a0|>=3.0.10,<4.0a0|>=1.1.1v,<1.1.2a|>=1.1.1u,<1.1.2a|>=3.0.9,<4.0a0|>=3.0.8,<4.0a0|>=1.1.1t,<1.1.2a|>=1.1.1m,<1.1.2a|>=1.1.1c,<1.1.2a|>=1.1.1b,<1.1.2a|>=1.0.2n,<1.0.3a|>=1.0.2m,<1.0.3a|>=1.0.2l,<1.0.3a']
pytorch -> python[version='>=3.9,<3.10.0a0'] -> openssl[version='1.0.*|>=1.0.2o,<1.0.3a|>=1.0.2p,<1.0.3a|>=1.1.1a,<1.1.2a|>=1.1.1d,<1.1.2a|>=1.1.1e,<1.1.2a|>=1.1.1f,<1.1.2a|>=1.1.1g,<1.1.2a|>=1.1.1h,<1.1.2a|>=1.1.1i,<1.1.2a|>=1.1.1j,<1.1.2a|>=1.1.1k,<1.1.2a|>=1.1.1l,<1.1.2a|>=1.1.1n,<1.1.2a|>=1.1.1o,<1.1.2a|>=1.1.1s,<1.1.2a|>=3.0.7,<4.0a0|>=3.1.2,<4.0a0|>=3.0.3,<4.0a0|>=3.0.2,<4.0a0|>=3.0.0,<4.0a0|>=3.0.10,<4.0a0|>=1.1.1v,<1.1.2a|>=1.1.1u,<1.1.2a|>=3.0.9,<4.0a0|>=3.0.8,<4.0a0|>=1.1.1t,<1.1.2a|>=1.1.1q,<1.1.2a|>=3.1.1,<4.0a0|>=3.1.0,<4.0a0|>=3.0.5,<4.0a0|>=1.1.1m,<1.1.2a|>=1.1.1c,<1.1.2a|>=1.1.1b,<1.1.2a|>=1.0.2n,<1.0.3a|>=1.0.2m,<1.0.3a|>=1.0.2l,<1.0.3a']
pysocks -> python[version='>=3.8'] -> openssl[version='1.0.*|>=1.0.2o,<1.0.3a|>=1.0.2p,<1.0.3a|>=1.1.1a,<1.1.2a|>=1.1.1d,<1.1.2a|>=1.1.1e,<1.1.2a|>=1.1.1f,<1.1.2a|>=1.1.1g,<1.1.2a|>=1.1.1h,<1.1.2a|>=1.1.1i,<1.1.2a|>=1.1.1j,<1.1.2a|>=1.1.1k,<1.1.2a|>=1.1.1l,<1.1.2a|>=1.1.1n,<1.1.2a|>=1.1.1o,<1.1.2a|>=1.1.1q,<1.1.2a|>=1.1.1s,<1.1.2a|>=3.1.0,<4.0a0|>=3.1.1,<4.0a0|>=3.1.2,<4.0a0|>=3.0.7,<4.0a0|>=3.0.5,<4.0a0|>=3.0.3,<4.0a0|>=3.0.2,<4.0a0|>=3.0.0,<4.0a0|>=3.0.10,<4.0a0|>=1.1.1v,<1.1.2a|>=1.1.1u,<1.1.2a|>=3.0.9,<4.0a0|>=3.0.8,<4.0a0|>=1.1.1t,<1.1.2a|>=1.1.1m,<1.1.2a|>=1.1.1c,<1.1.2a|>=1.1.1b,<1.1.2a|>=1.0.2n,<1.0.3a|>=1.0.2m,<1.0.3a|>=1.0.2l,<1.0.3a']
ffmpeg -> openssl[version='>=1.1.1d,<1.1.2a']
charset-normalizer -> python[version='>=3.7'] -> openssl[version='1.0.*|>=1.0.2o,<1.0.3a|>=1.0.2p,<1.0.3a|>=1.1.1a,<1.1.2a|>=1.1.1d,<1.1.2a|>=1.1.1e,<1.1.2a|>=1.1.1f,<1.1.2a|>=1.1.1g,<1.1.2a|>=1.1.1h,<1.1.2a|>=1.1.1i,<1.1.2a|>=1.1.1j,<1.1.2a|>=1.1.1k,<1.1.2a|>=1.1.1l,<1.1.2a|>=1.1.1n,<1.1.2a|>=1.1.1o,<1.1.2a|>=1.1.1q,<1.1.2a|>=1.1.1s,<1.1.2a|>=3.1.0,<4.0a0|>=3.1.1,<4.0a0|>=3.1.2,<4.0a0|>=3.0.7,<4.0a0|>=3.0.5,<4.0a0|>=3.0.3,<4.0a0|>=3.0.2,<4.0a0|>=3.0.0,<4.0a0|>=3.0.10,<4.0a0|>=1.1.1v,<1.1.2a|>=1.1.1u,<1.1.2a|>=3.0.9,<4.0a0|>=3.0.8,<4.0a0|>=1.1.1t,<1.1.2a|>=1.1.1m,<1.1.2a|>=1.1.1c,<1.1.2a|>=1.1.1b,<1.1.2a|>=1.0.2n,<1.0.3a|>=1.0.2m,<1.0.3a|>=1.0.2l,<1.0.3a']
python=3.7.5 -> openssl[version='>=1.1.1d,<1.1.2a|>=1.1.1i,<1.1.2a']
torchvision -> ffmpeg[version='>=4.2'] -> openssl[version='1.0.*|>=1.0.2o,<1.0.3a|>=1.0.2p,<1.0.3a|>=1.1.1a,<1.1.2a|>=1.1.1d,<1.1.2a|>=3.1.1,<4.0a0|>=3.0.7,<4.0a0|>=1.1.1s,<1.1.2a|>=3.0.2,<4.0a0|>=1.1.1n,<1.1.2a|>=3.0.0,<4.0a0|>=1.1.1l,<1.1.2a|>=1.1.1k,<1.1.2a|>=1.1.1j,<1.1.2a|>=1.1.1i,<1.1.2a|>=1.1.1h,<1.1.2a|>=1.1.1g,<1.1.2a|>=1.1.1f,<1.1.2a|>=1.1.1e,<1.1.2a|>=3.0.10,<4.0a0|>=1.1.1v,<1.1.2a|>=3.0.9,<4.0a0|>=1.1.1u,<1.1.2a|>=3.0.8,<4.0a0|>=1.1.1t,<1.1.2a|>=1.1.1q,<1.1.2a|>=3.1.2,<4.0a0|>=3.0.3,<4.0a0|>=1.1.1o,<1.1.2a|>=3.1.0,<4.0a0|>=3.0.5,<4.0a0|>=1.1.1m,<1.1.2a|>=1.1.1c,<1.1.2a|>=1.1.1b,<1.1.2a|>=1.0.2n,<1.0.3a|>=1.0.2m,<1.0.3a|>=1.0.2l,<1.0.3a']
torchaudio -> python[version='>=3.9,<3.10.0a0'] -> openssl[version='1.0.*|>=1.0.2o,<1.0.3a|>=1.0.2p,<1.0.3a|>=1.1.1a,<1.1.2a|>=1.1.1d,<1.1.2a|>=1.1.1e,<1.1.2a|>=1.1.1f,<1.1.2a|>=1.1.1g,<1.1.2a|>=1.1.1h,<1.1.2a|>=1.1.1i,<1.1.2a|>=1.1.1j,<1.1.2a|>=1.1.1k,<1.1.2a|>=1.1.1l,<1.1.2a|>=1.1.1n,<1.1.2a|>=1.1.1o,<1.1.2a|>=1.1.1s,<1.1.2a|>=3.0.7,<4.0a0|>=3.1.2,<4.0a0|>=3.0.3,<4.0a0|>=3.0.2,<4.0a0|>=3.0.0,<4.0a0|>=3.0.10,<4.0a0|>=1.1.1v,<1.1.2a|>=1.1.1u,<1.1.2a|>=3.0.9,<4.0a0|>=3.0.8,<4.0a0|>=1.1.1t,<1.1.2a|>=1.1.1q,<1.1.2a|>=3.1.1,<4.0a0|>=3.1.0,<4.0a0|>=3.0.5,<4.0a0|>=1.1.1m,<1.1.2a|>=1.1.1c,<1.1.2a|>=1.1.1b,<1.1.2a|>=1.0.2n,<1.0.3a|>=1.0.2m,<1.0.3a|>=1.0.2l,<1.0.3a']
typing_extensions -> python[version='>=3.7'] -> openssl[version='1.0.*|>=1.0.2o,<1.0.3a|>=1.0.2p,<1.0.3a|>=1.1.1a,<1.1.2a|>=1.1.1d,<1.1.2a|>=1.1.1e,<1.1.2a|>=1.1.1f,<1.1.2a|>=1.1.1g,<1.1.2a|>=1.1.1h,<1.1.2a|>=1.1.1i,<1.1.2a|>=1.1.1j,<1.1.2a|>=1.1.1k,<1.1.2a|>=1.1.1l,<1.1.2a|>=1.1.1n,<1.1.2a|>=1.1.1o,<1.1.2a|>=1.1.1q,<1.1.2a|>=1.1.1s,<1.1.2a|>=3.1.0,<4.0a0|>=3.1.1,<4.0a0|>=3.1.2,<4.0a0|>=3.0.7,<4.0a0|>=3.0.5,<4.0a0|>=3.0.3,<4.0a0|>=3.0.2,<4.0a0|>=3.0.0,<4.0a0|>=3.0.10,<4.0a0|>=1.1.1v,<1.1.2a|>=1.1.1u,<1.1.2a|>=3.0.9,<4.0a0|>=3.0.8,<4.0a0|>=1.1.1t,<1.1.2a|>=1.1.1m,<1.1.2a|>=1.1.1c,<1.1.2a|>=1.1.1b,<1.1.2a|>=1.0.2n,<1.0.3a|>=1.0.2m,<1.0.3a|>=1.0.2l,<1.0.3a']
certifi -> python[version='>=3.7'] -> openssl[version='1.0.*|>=1.0.2o,<1.0.3a|>=1.0.2p,<1.0.3a|>=1.1.1a,<1.1.2a|>=1.1.1d,<1.1.2a|>=1.1.1e,<1.1.2a|>=1.1.1f,<1.1.2a|>=1.1.1g,<1.1.2a|>=1.1.1h,<1.1.2a|>=1.1.1i,<1.1.2a|>=1.1.1j,<1.1.2a|>=1.1.1k,<1.1.2a|>=1.1.1l,<1.1.2a|>=1.1.1n,<1.1.2a|>=1.1.1o,<1.1.2a|>=1.1.1q,<1.1.2a|>=1.1.1s,<1.1.2a|>=3.1.0,<4.0a0|>=3.1.1,<4.0a0|>=3.1.2,<4.0a0|>=3.0.7,<4.0a0|>=3.0.5,<4.0a0|>=3.0.3,<4.0a0|>=3.0.2,<4.0a0|>=3.0.0,<4.0a0|>=3.0.10,<4.0a0|>=1.1.1v,<1.1.2a|>=1.1.1u,<1.1.2a|>=3.0.9,<4.0a0|>=3.0.8,<4.0a0|>=1.1.1t,<1.1.2a|>=1.1.1m,<1.1.2a|>=1.1.1c,<1.1.2a|>=1.1.1b,<1.1.2a|>=1.0.2n,<1.0.3a|>=1.0.2m,<1.0.3a|>=1.0.2l,<1.0.3a']
urllib3 -> python[version='>=3.7'] -> openssl[version='1.0.*|>=1.0.2o,<1.0.3a|>=1.0.2p,<1.0.3a|>=1.1.1a,<1.1.2a|>=1.1.1d,<1.1.2a|>=1.1.1e,<1.1.2a|>=1.1.1f,<1.1.2a|>=1.1.1g,<1.1.2a|>=1.1.1h,<1.1.2a|>=1.1.1i,<1.1.2a|>=1.1.1j,<1.1.2a|>=1.1.1k,<1.1.2a|>=1.1.1l,<1.1.2a|>=1.1.1n,<1.1.2a|>=1.1.1o,<1.1.2a|>=1.1.1q,<1.1.2a|>=1.1.1s,<1.1.2a|>=3.1.0,<4.0a0|>=3.1.1,<4.0a0|>=3.1.2,<4.0a0|>=3.0.7,<4.0a0|>=3.0.5,<4.0a0|>=3.0.3,<4.0a0|>=3.0.2,<4.0a0|>=3.0.0,<4.0a0|>=3.0.10,<4.0a0|>=1.1.1v,<1.1.2a|>=1.1.1u,<1.1.2a|>=3.0.9,<4.0a0|>=3.0.8,<4.0a0|>=1.1.1t,<1.1.2a|>=1.1.1m,<1.1.2a|>=1.1.1c,<1.1.2a|>=1.1.1b,<1.1.2a|3.*|<1.1.2a|>=1.0.2n,<1.0.3a|>=1.0.2m,<1.0.3a|>=1.0.2l,<1.0.3a']

Package numpy conflicts for:
torchvision -> numpy[version='>1.11|>=1.11|>=1.23.5|>=1.21.6,<2.0a0|>=1.23.5,<2.0a0|>=1.20.3,<2.0a0|>=1.19.5,<2.0a0|>=1.21.5,<2.0a0|>=1.18.5,<2.0a0|>=1.17.5,<2.0a0|>=1.16.6,<2.0a0|>=1.21.2,<2.0a0|>=1.19.2,<2.0a0|>=1.23.1,<2.0a0']
torchvision -> pytorch==2.0.0 -> numpy[version='>=1.11.3,<2.0a0|>=1.16.5,<2.0a0|>=1.19.4,<2.0a0|>=1.19|>=1.19,<2|>=1.21,<2|>=1.22.4,<2.0a0|>=1.23,<2|>=1.19.2,<2|>=1.21.2,<2|>=1.14.6,<2.0a0|>=1.9.3,<2.0a0|>=1.9']
pytorch -> numpy[version='>=1.11.3,<2.0a0|>=1.11|>=1.19|>=1.22.4,<2.0a0|>=1.23.5,<2.0a0|>=1.21.6,<2.0a0|>=1.20.3,<2.0a0|>=1.19.5,<2.0a0|>=1.21.5,<2.0a0|>=1.18.5,<2.0a0|>=1.17.5,<2.0a0|>=1.16.6,<2.0a0|>=1.19.4,<2.0a0|>=1.23,<2|>=1.21,<2|>=1.19,<2|>=1.19.2,<2|>=1.21.2,<2|>=1.21.2,<2.0a0|>=1.14.6,<2.0a0|>=1.9.3,<2.0a0|>=1.9']
torchaudio -> numpy[version='>=1.11|>=1.21.2']
torchaudio -> pytorch==2.0.1 -> numpy[version='>=1.16.6,<2.0a0|>=1.17.5,<2.0a0|>=1.18.5,<2.0a0|>=1.19,<2|>=1.20.3,<2.0a0|>=1.21.5,<2.0a0|>=1.23.5,<2.0a0|>=1.22.4,<2.0a0|>=1.21.6,<2.0a0|>=1.23,<2|>=1.21,<2|>=1.19.5,<2.0a0|>=1.19.2,<2|>=1.21.2,<2|>=1.21.2,<2.0a0|>=1.19|>=1.19.4,<2.0a0']

Package readline conflicts for:
idna -> python[version='>=3.6'] -> readline[version='6.2.*|7.0|>=7.0,<8.0a0|>=8.0,<9.0a0|>=8.1,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0|7.*|7.0.*']
certifi -> python[version='>=3.7'] -> readline[version='6.2.*|7.0|>=7.0,<8.0a0|>=8.0,<9.0a0|>=8.1,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0|7.*|7.0.*']
python_abi -> python=3.11 -> readline[version='6.2.*|7.0|>=7.0,<8.0a0|>=8.0,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0|>=8.1,<9.0a0|7.*|7.0.*']
sqlite -> readline[version='6.2.*|7.0|7.0.*|>=7.0,<8.0a0|>=8.0,<9.0a0|>=8.1,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0']
pip -> python[version='>=3.7'] -> readline[version='6.2.*|7.0|>=7.0,<8.0a0|>=8.0,<9.0a0|>=8.1,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0|7.*|7.0.*']
pysocks -> python[version='>=3.8'] -> readline[version='6.2.*|7.0|>=7.0,<8.0a0|>=8.0,<9.0a0|>=8.1,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0|7.*|7.0.*']
pillow -> python[version='>=3.9,<3.10.0a0'] -> readline[version='6.2.*|7.0|>=7.0,<8.0a0|>=8.0,<9.0a0|>=8.1,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0|7.*|7.0.*']
wheel -> python[version='>=3.7'] -> readline[version='6.2.*|7.0|>=7.0,<8.0a0|>=8.0,<9.0a0|>=8.1,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0|7.0.*|7.*']
python=3.7.5 -> readline[version='>=7.0,<8.0a0|>=8.0,<9.0a0']
torchvision -> python[version='>=3.8,<3.9.0a0'] -> readline[version='6.2.*|7.0|>=7.0,<8.0a0|>=8.0,<9.0a0|>=8.1,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0|7.*|7.0.*']
charset-normalizer -> python[version='>=3.7'] -> readline[version='6.2.*|7.0|>=7.0,<8.0a0|>=8.0,<9.0a0|>=8.1,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0|7.*']
torchaudio -> python[version='>=3.9,<3.10.0a0'] -> readline[version='6.2.*|7.0|>=7.0,<8.0a0|>=8.0,<9.0a0|>=8.1,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0|7.*']
setuptools -> python[version='>=3.7'] -> readline[version='6.2.*|7.0|>=7.0,<8.0a0|>=8.0,<9.0a0|>=8.1,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0|7.*|7.0.*']
pytorch -> python[version='>=3.9,<3.10.0a0'] -> readline[version='6.2.*|7.0|>=7.0,<8.0a0|>=8.0,<9.0a0|>=8.1,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0|7.*|7.0.*']
numpy -> python[version='>=3.9,<3.10.0a0'] -> readline[version='6.2.*|7.0|>=7.0,<8.0a0|>=8.0,<9.0a0|>=8.1,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0|7.*|7.0.*']
requests -> python[version='>=3.7'] -> readline[version='6.2.*|7.0|>=7.0,<8.0a0|>=8.0,<9.0a0|>=8.1,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0|7.*|7.0.*']
python=3.7.5 -> sqlite[version='>=3.34.0,<4.0a0'] -> readline[version='>=8.1,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0']
typing_extensions -> python[version='>=3.7'] -> readline[version='6.2.*|7.0|>=7.0,<8.0a0|>=8.0,<9.0a0|>=8.1,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0|7.*|7.0.*']
urllib3 -> python[version='>=3.7'] -> readline[version='6.2.*|7.0|>=7.0,<8.0a0|>=8.0,<9.0a0|>=8.1,<9.0a0|>=8.1.2,<9.0a0|>=8.2,<9.0a0|7.0.*|7.*']

Package certifi conflicts for:
pytorch -> setuptools -> certifi[version='>=2016.09|>=2016.9.26']
wheel -> setuptools -> certifi[version='>=2016.09|>=2016.9.26']
requests -> certifi[version='>=2017.4.17']
requests -> urllib3[version='>=1.21.1,<3'] -> certifi
pip -> setuptools -> certifi[version='>=2016.09|>=2016.9.26']
setuptools -> certifi[version='>=2016.09|>=2016.9.26']
torchvision -> requests -> certifi[version='>=2016.09|>=2016.9.26|>=2017.4.17']
urllib3 -> certifi

Package intel-openmp conflicts for:
mkl -> intel-openmp[version='2021.*|2022.*|2023.*']
torchaudio -> pytorch==2.0.1 -> intel-openmp[version='>=2021.4.0,<2022.0a0|>=2023.1.0,<2024.0a0']
numpy -> mkl[version='>=2023.1.0,<2024.0a0'] -> intel-openmp[version='2021.*|2023.*|2022.*']
blas -> mkl -> intel-openmp[version='2021.*|2022.*|2023.*']
mkl-devel -> mkl==2020.2=256 -> intel-openmp[version='2021.*|2022.*|2023.*']
pytorch -> intel-openmp[version='>=2021.4.0,<2022.0a0|>=2023.1.0,<2024.0a0']
pytorch -> mkl[version='>=2018'] -> intel-openmp[version='2018.0.3.*|2019.*|2021.*|2022.*|2023.*']
blas-devel -> mkl[version='>=2022.1.0,<2023.0a0'] -> intel-openmp[version='2021.*|2022.*']
torchvision -> pytorch==2.0.1 -> intel-openmp[version='>=2021.4.0,<2022.0a0|>=2023.1.0,<2024.0a0']
libblas -> mkl[version='>=2022.1.0,<2023.0a0'] -> intel-openmp[version='2021.*|2022.*']

Package zlib conflicts for:
idna -> python[version='>=3.6'] -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|1.2.8|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0|1.2.11.*']
setuptools -> python[version='>=3.7'] -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0|1.2.8|1.2.11.*']
lcms2 -> libtiff[version='>=4.5.0,<4.6.0a0'] -> zlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
llvm-openmp -> zstd[version='>=1.5.2,<1.6.0a0'] -> zlib[version='>=1.2.13,<1.3.0a0']
sqlite -> zlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.13,<2.0a0']
freetype -> libpng[version='>=1.6.37,<1.7.0a0'] -> zlib[version='1.2.8|>=1.2.12,<1.3.0a0']
_openmp_mutex -> llvm-openmp[version='>=9.0.1'] -> zlib[version='>=1.2.12,<1.3.0a0']
openh264 -> zlib[version='>=1.2.11,<1.3.0a0']
zstd -> zlib[version='>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0']
python_abi -> python=3.11 -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0|1.2.8|1.2.11.*']
pillow -> pypy3.9[version='>=7.3.11'] -> zlib
pytorch -> python[version='>=3.9,<3.10.0a0'] -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0|1.2.8|>=1.2.13,<1.2.14|1.2.11.*']
blas -> llvm-openmp[version='>=14.0.4'] -> zlib[version='>=1.2.12,<1.3.0a0']
freetype -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0']
openjpeg -> libpng[version='>=1.6.39,<1.7.0a0'] -> zlib[version='>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
python=3.7.5 -> sqlite[version='>=3.34.0,<4.0a0'] -> zlib[version='>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.13,<2.0a0']
wheel -> python[version='>=3.7'] -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0|1.2.8|1.2.11.*']
libpng -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|1.2.8|>=1.2.13,<1.3.0a0']
libxml2 -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
charset-normalizer -> python[version='>=3.7'] -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0|1.2.8']
numpy -> pypy3.9[version='>=7.3.11'] -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0|1.2.8|1.2.11.*']
ffmpeg -> freetype[version='>=2.10.2,<3.0a0'] -> zlib[version='1.2.8|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
python=3.7.5 -> zlib[version='>=1.2.11,<1.3.0a0']
mkl -> llvm-openmp[version='>=14.0.3'] -> zlib[version='>=1.2.12,<1.3.0a0|>=1.2.13,<1.2.14|>=1.2.13,<1.3.0a0']
libtiff -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|1.2.8|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0']
ffmpeg -> zlib[version='1.2.*|1.2.11|1.2.11.*|>=1.2.11,<1.3.0a0']
pillow -> zlib[version='1.2.*|1.2.11|1.2.11.*|>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|1.2.8|>=1.2.13,<1.3.0a0']
pysocks -> python[version='>=3.8'] -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0|1.2.8|1.2.11.*']
torchaudio -> python[version='>=3.9,<3.10.0a0'] -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0|1.2.8']
openjpeg -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|1.2.8']
pip -> python[version='>=3.7'] -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0|1.2.8|1.2.11.*']
urllib3 -> python[version='>=3.7'] -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0|1.2.8|1.2.11.*']
libhwloc -> libxml2[version='>=2.10.3,<2.11.0a0'] -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
certifi -> python[version='>=3.7'] -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0|1.2.8|1.2.11.*']
llvm-openmp -> zlib[version='>=1.2.12,<1.3.0a0']
typing_extensions -> python[version='>=3.7'] -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0|1.2.8|1.2.11.*']
requests -> python[version='>=3.7'] -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0|1.2.8|1.2.11.*']
gnutls -> zlib[version='1.2.11|>=1.2.11,<1.3.0a0|1.2.8']
torchvision -> ffmpeg[version='>=4.2'] -> zlib[version='1.2.*|1.2.11|>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|1.2.8|>=1.2.13,<1.3.0a0|1.2.11.*']

Package libblas conflicts for:
liblapacke -> libcblas=3.9.0 -> libblas[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0',build='4_blis|7_blis|8_blis|13_blis|15_blis|0_blis|1_blis|3_blis|4_blis|6_blis|8_blis|11_linux64_blis|12_linux64_blis|14_linux64_blis|16_linux64_blis|17_linux64_blis|18_linux64_blis|15_linux64_blis|13_linux64_blis|10_blis|9_blis|7_blis|5_blis|2_blis|16_blis|14_blis|12_blis|11_blis|10_blis|9_blis|6_blis|5_blis']
torchaudio -> numpy[version='>=1.11'] -> libblas[version='*|>=3.8.0,<4.0a0|>=3.9.0,<4.0a0',build=*_mkl]
pytorch -> libblas[version='*|>=3.9.0,<4.0a0|>=3.8.0,<4.0a0',build=*_mkl]
liblapack -> libblas[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0.*|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0.*',build='4_mkl|5_openblas|6_openblas|6_mkl|7_openblas|8_mkl|9_openblas|12_openblas|12_mkl|14_mkl|15_mkl|17_openblas|18_mkl|19_mkl|3_openblas|4_mkl|5_openblas|6_openblas|7_openblas|8_mkl|9_openblas|11_linux64_openblas|11_linux64_mkl|12_linux64_openblas|13_linux64_openblas|13_linux64_mkl|14_linux64_openblas|15_linux64_openblas|16_linux64_openblas|18_linux64_openblas|17_linux64_openblas|16_linux64_mkl|15_linux64_mkl|14_linux64_mkl|12_linux64_mkl|10_mkl|10_openblas|9_mkl|8_openblas|7_mkl|6_mkl|5_mkl|4_openblas|2_openblas|1_openblas|0_openblas|21_mkl|20_mkl|16_mkl|16_openblas|15_openblas|14_openblas|13_openblas|13_mkl|11_mkl|11_openblas|10_mkl|10_openblas|9_mkl|8_openblas|7_mkl|5_mkl|4_openblas']
blas-devel -> libblas[version='3.8.0|3.9.0',build='7_h6e990d7_netlib|0_h86c2bf4_netlib|7_blis|7_openblas|8_blis|8_openblas|10_blis|10_openblas|11_linux64_blis|11_linux64_mkl|12_linux64_blis|12_linux64_openblas|13_linux64_mkl|14_linux64_mkl|15_linux64_openblas|16_linux64_openblas|17_linux64_openblas|18_linux64_openblas|18_linux64_blis|17_linux64_blis|16_linux64_mkl|16_linux64_blis|15_linux64_mkl|15_linux64_blis|14_linux64_openblas|14_linux64_blis|13_linux64_openblas|13_linux64_blis|12_linux64_mkl|11_linux64_openblas|10_mkl|9_mkl|9_openblas|9_blis|8_mkl|7_mkl|5_h92ddd45_netlib']
torchvision -> numpy[version='>=1.11'] -> libblas[version='*|>=3.8.0,<4.0a0|>=3.9.0,<4.0a0',build=*_mkl]
blas-devel -> liblapack==3.9.0[build=*netlib] -> libblas[version='3.8.0.*|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0.*|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0',build='14_mkl|15_blis|16_openblas|17_openblas|18_mkl|19_mkl|0_blis|0_openblas|3_blis|3_openblas|4_blis|4_mkl|5_openblas|6_blis|6_mkl|6_openblas|5_mkl|5_blis|4_openblas|2_openblas|2_blis|0_h6e990d7_netlib|21_mkl|20_mkl|16_mkl|16_blis|15_openblas|15_mkl|14_openblas|14_blis']
blas -> libblas[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0',build='0_blis|3_blis|3_openblas|4_mkl|4_h6e990d7_netlib|5_openblas|6_openblas|6_mkl|6_h6e990d7_netlib|7_blis|7_openblas|8_blis|8_openblas|8_h6e990d7_netlib|9_openblas|10_h86c2bf4_netlib|11_blis|12_openblas|12_mkl|14_mkl|15_blis|16_openblas|16_blis|17_openblas|18_mkl|19_mkl|5_openblas|6_mkl|7_blis|7_openblas|8_blis|8_openblas|9_openblas|9_mkl|10_blis|10_mkl|11_linux64_blis|11_linux64_openblas|11_linux64_mkl|12_linux64_openblas|12_linux64_blis|13_linux64_openblas|13_linux64_mkl|14_linux64_openblas|14_linux64_mkl|15_linux64_openblas|16_linux64_openblas|17_linux64_openblas|18_linux64_openblas|18_linux64_blis|17_linux64_blis|16_linux64_mkl|16_linux64_blis|15_linux64_mkl|15_linux64_blis|14_linux64_blis|13_linux64_blis|12_linux64_mkl|10_openblas|9_blis|8_mkl|7_mkl|6_openblas|6_blis|5_h92ddd45_netlib|5_mkl|5_blis|4_h92ddd45_netlib|3_h92ddd45_netlib|21_mkl|20_mkl|16_mkl|15_openblas|15_mkl|14_openblas|14_blis|13_mkl|13_openblas|13_blis|12_blis|11_h86c2bf4_netlib|11_mkl|11_openblas|10_mkl|10_openblas|10_blis|9_mkl|9_blis|8_mkl|7_h6e990d7_netlib|7_mkl|6_blis|5_mkl|5_blis|5_h6e990d7_netlib|4_openblas|4_blis|2_openblas|2_blis|1_h6e990d7_netlib|0_openblas|0_h6e990d7_netlib']
blas -> liblapack==3.9.0[build=*netlib] -> libblas[version='3.8.0.*|3.9.0.*']
libcblas -> libblas[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0.*|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0.*',build='4_mkl|5_openblas|6_blis|6_mkl|7_openblas|8_blis|8_mkl|9_openblas|10_mkl|11_blis|11_openblas|12_openblas|12_mkl|14_mkl|15_blis|15_openblas|18_mkl|19_mkl|0_blis|0_openblas|1_openblas|3_blis|3_openblas|4_mkl|5_openblas|6_blis|6_openblas|6_mkl|7_blis|7_openblas|8_blis|8_openblas|8_mkl|9_openblas|11_linux64_blis|11_linux64_openblas|11_linux64_mkl|12_linux64_blis|13_linux64_mkl|14_linux64_mkl|15_linux64_openblas|16_linux64_openblas|17_linux64_openblas|18_linux64_openblas|18_linux64_blis|17_linux64_blis|16_linux64_mkl|16_linux64_blis|15_linux64_mkl|15_linux64_blis|14_linux64_openblas|14_linux64_blis|13_linux64_openblas|13_linux64_blis|12_linux64_mkl|12_linux64_openblas|10_mkl|10_openblas|10_blis|9_mkl|9_blis|7_mkl|5_mkl|5_blis|4_openblas|4_blis|2_blis|2_openblas|1_blis|21_mkl|20_mkl|17_openblas|16_mkl|16_blis|16_openblas|15_mkl|14_blis|14_openblas|13_blis|13_openblas|13_mkl|12_blis|11_mkl|10_openblas|10_blis|9_mkl|9_blis|8_openblas|7_mkl|7_blis|6_openblas|5_mkl|5_blis|4_openblas|4_blis']
numpy -> libcblas[version='>=3.9.0,<4.0a0'] -> libblas[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0.*|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0.*',build='4_mkl|5_openblas|6_blis|6_mkl|7_openblas|8_blis|8_mkl|9_openblas|10_mkl|11_blis|11_openblas|12_openblas|12_mkl|14_mkl|15_blis|15_openblas|18_mkl|19_mkl|0_blis|0_openblas|1_openblas|3_blis|3_openblas|4_mkl|5_openblas|6_blis|6_openblas|6_mkl|7_blis|7_openblas|8_blis|8_openblas|8_mkl|9_openblas|11_linux64_blis|11_linux64_openblas|11_linux64_mkl|12_linux64_blis|13_linux64_mkl|14_linux64_mkl|15_linux64_openblas|16_linux64_openblas|17_linux64_openblas|18_linux64_openblas|18_linux64_blis|17_linux64_blis|16_linux64_mkl|16_linux64_blis|15_linux64_mkl|15_linux64_blis|14_linux64_openblas|14_linux64_blis|13_linux64_openblas|13_linux64_blis|12_linux64_mkl|12_linux64_openblas|10_mkl|10_openblas|10_blis|9_mkl|9_blis|7_mkl|5_mkl|5_blis|4_openblas|4_blis|2_blis|2_openblas|1_blis|21_mkl|20_mkl|17_openblas|16_mkl|16_blis|16_openblas|15_mkl|14_blis|14_openblas|13_blis|13_openblas|13_mkl|12_blis|11_mkl|10_openblas|10_blis|9_mkl|9_blis|8_openblas|7_mkl|7_blis|6_openblas|5_mkl|5_blis|4_openblas|4_blis']
liblapacke -> libblas[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0.*|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0.*',build='4_mkl|5_openblas|6_openblas|6_mkl|7_openblas|8_mkl|9_openblas|12_openblas|12_mkl|14_mkl|15_mkl|17_openblas|18_mkl|19_mkl|3_openblas|4_mkl|5_openblas|6_openblas|7_openblas|8_mkl|9_openblas|11_linux64_openblas|11_linux64_mkl|12_linux64_openblas|13_linux64_openblas|13_linux64_mkl|14_linux64_openblas|15_linux64_openblas|16_linux64_openblas|18_linux64_openblas|17_linux64_openblas|16_linux64_mkl|15_linux64_mkl|14_linux64_mkl|12_linux64_mkl|10_mkl|10_openblas|9_mkl|8_openblas|7_mkl|6_mkl|5_mkl|4_openblas|2_openblas|1_openblas|0_openblas|21_mkl|20_mkl|16_mkl|16_openblas|15_openblas|14_openblas|13_openblas|13_mkl|11_mkl|11_openblas|10_mkl|10_openblas|9_mkl|8_openblas|7_mkl|5_mkl|4_openblas']
pytorch -> blas=[build=mkl] -> libblas[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0.*|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0',build='5_openblas|6_openblas|7_openblas|9_openblas|12_openblas|16_openblas|0_blis|1_blis|3_blis|3_openblas|4_mkl|5_blis|5_openblas|6_openblas|7_blis|7_openblas|8_blis|8_openblas|9_openblas|11_linux64_blis|11_linux64_openblas|12_linux64_openblas|12_linux64_blis|15_linux64_openblas|16_linux64_openblas|17_linux64_blis|18_linux64_openblas|4_mkl|6_mkl|8_mkl|10_mkl|12_mkl|14_mkl|18_mkl|19_mkl|8_mkl|10_mkl|11_linux64_mkl|12_linux64_mkl|13_linux64_mkl|14_linux64_mkl|16_linux64_mkl|15_linux64_mkl|9_mkl|7_mkl|6_mkl|5_mkl|21_mkl|20_mkl|16_mkl|15_mkl|13_mkl|11_mkl|9_mkl|7_mkl|5_mkl|18_linux64_blis|17_linux64_openblas|16_linux64_blis|15_linux64_blis|14_linux64_openblas|14_linux64_blis|13_linux64_openblas|13_linux64_blis|10_openblas|10_blis|9_blis|6_blis|4_openblas|4_blis|2_blis|2_openblas|1_openblas|0_openblas|17_openblas|15_openblas|14_openblas|13_openblas|11_openblas|10_openblas|8_openblas|4_openblas']
mkl-devel -> blas=[build=mkl] -> libblas[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0',build='4_mkl|6_mkl|8_mkl|10_mkl|12_mkl|14_mkl|18_mkl|19_mkl|8_mkl|10_mkl|11_linux64_mkl|12_linux64_mkl|13_linux64_mkl|14_linux64_mkl|16_linux64_mkl|15_linux64_mkl|9_mkl|7_mkl|6_mkl|5_mkl|21_mkl|20_mkl|16_mkl|15_mkl|13_mkl|11_mkl|9_mkl|7_mkl|5_mkl']
numpy -> libblas[version='>=3.8.0,<4.0a0|>=3.9.0,<4.0a0']

Package llvm-openmp conflicts for:
blas -> openblas -> llvm-openmp[version='>=10.0.1|>=16.0.1|>=15.0.7|>=15.0.6|>=14.0.3']
blas-devel -> openblas=0.3.24 -> llvm-openmp[version='>=10.0.0|>=10.0.1|>=11.0.0|>=11.1.0|>=12.0.1|>=13.0.1|>=14.0.3|>=15.0.6|>=16.0.1|>=16.0.6|>=14.0.4|>=9.0.1']
blas -> llvm-openmp[version='>=10.0.0|>=11.0.0|>=11.0.1|>=11.1.0|>=12.0.1|>=13.0.1|>=14.0.4|>=16.0.5|>=16.0.6|>=9.0.1']
mkl -> llvm-openmp[version='>=10.0.0|>=11.0.0|>=11.1.0|>=12.0.1|>=14.0.3|>=15.0.6|>=15.0.7|>=16.0.1|>=16.0.6|>=9.0.1']
pytorch -> blas=[build=mkl] -> llvm-openmp[version='>=10.0.0|>=11.0.0|>=11.0.1|>=11.1.0|>=12.0.1|>=13.0.1|>=14.0.4|>=16.0.6|>=16.0.1|>=15.0.7|>=15.0.6|>=14.0.3|>=9.0.1|>=16.0.5|>=10.0.1']
numpy -> openblas[version='>=0.2.15'] -> llvm-openmp[version='>=10.0.0|>=10.0.1|>=11.0.0|>=11.1.0|>=12.0.1|>=13.0.1|>=14.0.4|>=16.0.1|>=16.0.6|>=9.0.1|>=16.0.5|>=11.0.1|>=15.0.7|>=15.0.6|>=14.0.3']
libblas -> libopenblas[version='>=0.3.24,<0.3.25.0a0'] -> llvm-openmp[version='>=10.0.0|>=11.0.0|>=11.1.0|>=12.0.1|>=13.0.1|>=14.0.3|>=15.0.6|>=16.0.1|>=16.0.6|>=14.0.4|>=9.0.1|>=10.0.1']
libgcc-ng -> _openmp_mutex[version='>=4.5'] -> llvm-openmp[version='>=9.0.1']
_openmp_mutex -> llvm-openmp[version='>=9.0.1']
mkl-devel -> mkl==2023.2.0=h84fe81f_49572 -> llvm-openmp[version='>=10.0.0|>=11.0.0|>=11.1.0|>=12.0.1|>=14.0.3|>=15.0.6|>=15.0.7|>=16.0.1|>=16.0.6|>=9.0.1|>=14.0.4|>=13.0.1|>=11.0.1']

Package xz conflicts for:
lcms2 -> libtiff[version='>=4.6.0,<4.7.0a0'] -> xz[version='>=5.2.10,<6.0a0|>=5.2.6,<6.0a0|>=5.2.4,<6.0a0|>=5.2.8,<6.0a0|>=5.2.6,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0.0a0']
idna -> python[version='>=3.6'] -> xz[version='5.0.*|5.2.*|>=5.2.3,<6.0.0a0|>=5.2.4,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.6,<5.3.0a0|>=5.2.6,<6.0a0|>=5.2.6,<6.0.0a0|>=5.4.2,<6.0a0|>=5.2.10,<6.0a0|>=5.2.8,<6.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0a0|>=5.2.3,<6.0a0']
zstd -> xz[version='>=5.2.10,<6.0a0|>=5.2.4,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0a0']
libtiff -> xz[version='5.0.*|5.2.*|>=5.2.3,<6.0.0a0|>=5.2.4,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.6,<6.0.0a0|>=5.2.6,<6.0a0|>=5.2.10,<6.0a0|>=5.2.4,<6.0a0|>=5.2.8,<6.0a0|>=5.2.5,<6.0a0|>=5.2.3,<6.0a0']
typing_extensions -> python[version='>=3.7'] -> xz[version='5.0.*|5.2.*|>=5.2.10,<6.0a0|>=5.2.3,<6.0.0a0|>=5.2.4,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.6,<5.3.0a0|>=5.2.6,<6.0a0|>=5.2.6,<6.0.0a0|>=5.4.2,<6.0a0|>=5.2.8,<6.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0a0|>=5.2.3,<6.0a0']
pillow -> libtiff[version='>=4.5.1,<4.6.0a0'] -> xz[version='5.0.*|5.2.*|>=5.2.10,<6.0a0|>=5.2.6,<6.0a0|>=5.2.4,<6.0a0|>=5.2.5,<6.0.0a0|>=5.4.2,<6.0a0|>=5.2.8,<6.0a0|>=5.2.5,<6.0a0|>=5.2.6,<5.3.0a0|>=5.2.4,<6.0.0a0|>=5.2.6,<6.0.0a0|>=5.2.3,<6.0.0a0|>=5.2.3,<6.0a0']
setuptools -> python[version='>=3.7'] -> xz[version='5.0.*|5.2.*|>=5.2.10,<6.0a0|>=5.2.3,<6.0.0a0|>=5.2.4,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.6,<5.3.0a0|>=5.2.6,<6.0a0|>=5.2.6,<6.0.0a0|>=5.4.2,<6.0a0|>=5.2.8,<6.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0a0|>=5.2.3,<6.0a0']
pytorch -> python[version='>=3.9,<3.10.0a0'] -> xz[version='5.0.*|5.2.*|>=5.2.10,<6.0a0|>=5.2.5,<6.0.0a0|>=5.2.6,<6.0a0|>=5.4.2,<6.0a0|>=5.2.8,<6.0a0|>=5.2.5,<6.0a0|>=5.2.6,<6.0.0a0|>=5.2.6,<5.3.0a0|>=5.2.4,<6.0.0a0|>=5.2.4,<6.0a0|>=5.2.3,<6.0.0a0|>=5.2.3,<6.0a0']
charset-normalizer -> python[version='>=3.7'] -> xz[version='5.0.*|5.2.*|>=5.2.10,<6.0a0|>=5.2.3,<6.0.0a0|>=5.2.4,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.6,<5.3.0a0|>=5.2.6,<6.0a0|>=5.2.6,<6.0.0a0|>=5.4.2,<6.0a0|>=5.2.8,<6.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0a0|>=5.2.3,<6.0a0']
pysocks -> python[version='>=3.8'] -> xz[version='5.0.*|5.2.*|>=5.2.10,<6.0a0|>=5.2.4,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.6,<5.3.0a0|>=5.2.6,<6.0a0|>=5.2.6,<6.0.0a0|>=5.4.2,<6.0a0|>=5.2.8,<6.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0a0|>=5.2.3,<6.0.0a0|>=5.2.3,<6.0a0']
numpy -> pypy3.9[version='>=7.3.11'] -> xz[version='5.0.*|5.2.*|>=5.2.10,<6.0a0|>=5.2.5,<6.0.0a0|>=5.2.6,<6.0a0|>=5.4.2,<6.0a0|>=5.2.8,<6.0a0|>=5.2.5,<6.0a0|>=5.2.6,<5.3.0a0|>=5.2.6,<6.0.0a0|>=5.2.4,<6.0.0a0|>=5.2.4,<6.0a0|>=5.2.3,<6.0.0a0|>=5.2.3,<6.0a0']
torchvision -> python[version='>=3.8,<3.9.0a0'] -> xz[version='5.0.*|5.2.*|>=5.2.10,<6.0a0|>=5.2.4,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.6,<6.0a0|>=5.4.2,<6.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0a0|>=5.2.8,<6.0a0|>=5.2.6,<5.3.0a0|>=5.2.6,<6.0.0a0|>=5.2.3,<6.0.0a0|>=5.2.3,<6.0a0']
llvm-openmp -> zstd[version='>=1.5.2,<1.6.0a0'] -> xz[version='>=5.2.10,<6.0a0|>=5.2.5,<6.0.0a0|>=5.2.5,<6.0a0']
torchaudio -> python[version='>=3.9,<3.10.0a0'] -> xz[version='5.0.*|5.2.*|>=5.2.10,<6.0a0|>=5.2.5,<6.0.0a0|>=5.2.6,<6.0a0|>=5.4.2,<6.0a0|>=5.2.8,<6.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0.0a0|>=5.2.4,<6.0a0|>=5.2.6,<6.0.0a0|>=5.2.6,<5.3.0a0|>=5.2.3,<6.0.0a0|>=5.2.3,<6.0a0']
requests -> python[version='>=3.7'] -> xz[version='5.0.*|5.2.*|>=5.2.10,<6.0a0|>=5.2.3,<6.0.0a0|>=5.2.4,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.6,<5.3.0a0|>=5.2.6,<6.0a0|>=5.2.6,<6.0.0a0|>=5.4.2,<6.0a0|>=5.2.8,<6.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0a0|>=5.2.3,<6.0a0']
libxml2 -> xz[version='5.0.*|5.2.*|>=5.2.3,<6.0.0a0|>=5.2.4,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.6,<6.0.0a0|>=5.2.6,<6.0a0|>=5.4.2,<6.0a0|>=5.2.10,<6.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0a0|>=5.2.3,<6.0a0']
ffmpeg -> libxml2[version='>=2.11.5,<2.12.0a0'] -> xz[version='>=5.2.10,<6.0a0|>=5.2.6,<6.0a0|>=5.4.2,<6.0a0|>=5.2.6,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.5,<6.0a0']
wheel -> python[version='>=3.7'] -> xz[version='5.0.*|5.2.*|>=5.2.10,<6.0a0|>=5.2.3,<6.0.0a0|>=5.2.4,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.6,<5.3.0a0|>=5.2.6,<6.0a0|>=5.2.6,<6.0.0a0|>=5.4.2,<6.0a0|>=5.2.8,<6.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0a0|>=5.2.3,<6.0a0']
urllib3 -> python[version='>=3.7'] -> xz[version='5.0.*|5.2.*|>=5.2.10,<6.0a0|>=5.2.3,<6.0.0a0|>=5.2.4,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.6,<5.3.0a0|>=5.2.6,<6.0a0|>=5.2.6,<6.0.0a0|>=5.4.2,<6.0a0|>=5.2.8,<6.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0a0|>=5.2.3,<6.0a0']
python_abi -> python=3.11 -> xz[version='5.0.*|5.2.*|>=5.2.10,<6.0a0|>=5.2.6,<5.3.0a0|>=5.2.6,<6.0a0|>=5.4.2,<6.0a0|>=5.2.8,<6.0a0|>=5.2.6,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0.0a0|>=5.2.4,<6.0a0|>=5.2.3,<6.0.0a0|>=5.2.3,<6.0a0']
python=3.7.5 -> xz[version='>=5.2.4,<6.0a0|>=5.2.5,<6.0.0a0']
certifi -> python[version='>=3.7'] -> xz[version='5.0.*|5.2.*|>=5.2.10,<6.0a0|>=5.2.3,<6.0.0a0|>=5.2.4,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.6,<5.3.0a0|>=5.2.6,<6.0a0|>=5.2.6,<6.0.0a0|>=5.4.2,<6.0a0|>=5.2.8,<6.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0a0|>=5.2.3,<6.0a0']
pip -> python[version='>=3.7'] -> xz[version='5.0.*|5.2.*|>=5.2.10,<6.0a0|>=5.2.3,<6.0.0a0|>=5.2.4,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.6,<5.3.0a0|>=5.2.6,<6.0a0|>=5.2.6,<6.0.0a0|>=5.4.2,<6.0a0|>=5.2.8,<6.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0a0|>=5.2.3,<6.0a0']
openjpeg -> libtiff[version='>=4.5.0,<4.6.0a0'] -> xz[version='5.0.*|5.2.*|>=5.2.10,<6.0a0|>=5.2.6,<6.0a0|>=5.2.4,<6.0a0|>=5.2.8,<6.0a0|>=5.2.6,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0.0a0|>=5.2.3,<6.0.0a0|>=5.2.3,<6.0a0']
libhwloc -> libxml2[version='>=2.11.5,<2.12.0a0'] -> xz[version='5.0.*|5.2.*|>=5.2.10,<6.0a0|>=5.2.6,<6.0a0|>=5.4.2,<6.0a0|>=5.2.6,<6.0.0a0|>=5.2.5,<6.0.0a0|>=5.2.5,<6.0a0|>=5.2.4,<6.0.0a0|>=5.2.4,<6.0a0|>=5.2.3,<6.0.0a0|>=5.2.3,<6.0a0']

Package _libgcc_mutex conflicts for:
liblapacke -> libgcc-ng[version='>=9.3.0'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
libzlib -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
sqlite -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
libsqlite -> libgcc-ng[version='>=12'] -> _libgcc_mutex==0.1=conda_forge
mkl -> _openmp_mutex=[build=*_llvm] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
xorg-libxau -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
zstd -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
libdeflate -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
libgcc-ng -> _libgcc_mutex[version='*|0.1|0.1',build='main|conda_forge|main']
libcurand -> libgcc-ng[version='>=12'] -> _libgcc_mutex==0.1=conda_forge
libwebp-base -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
_openmp_mutex -> _libgcc_mutex==0.1[build='conda_forge|main']
libcufile -> libgcc-ng[version='>=12'] -> _libgcc_mutex==0.1=conda_forge
torchvision -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1|0.1',build='main|conda_forge|main']
libxcb -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
libgomp -> _libgcc_mutex==0.1[build='conda_forge|main']
zlib -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
libcublas -> libgcc-ng[version='>=12'] -> _libgcc_mutex==0.1=conda_forge
readline -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
libblas -> libgcc-ng[version='>=9.3.0'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
libbrotlienc -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
xorg-libxdmcp -> libgcc-ng[version='>=9.3.0'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
pthread-stubs -> libgcc-ng[version='>=7.5.0'] -> _libgcc_mutex[version='*|0.1|0.1',build='main|conda_forge|main']
libffi -> libgcc-ng[version='>=9.4.0'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
cuda-nvrtc -> libgcc-ng[version='>=12'] -> _libgcc_mutex==0.1=conda_forge
gmp -> libgcc-ng[version='>=7.5.0'] -> _libgcc_mutex[version='*|0.1|0.1',build='main|conda_forge|main']
bzip2 -> libgcc-ng[version='>=9.3.0'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
gnutls -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1|0.1',build='main|conda_forge|main']
xz -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1|0.1',build='main|conda_forge|main']
libhwloc -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1|0.1',build='main|conda_forge|main']
ffmpeg -> libgcc-ng[version='>=7.3.0'] -> _libgcc_mutex[version='*|0.1|0.1',build='main|conda_forge|main']
cudatoolkit=11.1 -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
libcufft -> libgcc-ng[version='>=12'] -> _libgcc_mutex==0.1=conda_forge
brotli -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
lerc -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
libcusparse -> libgcc-ng[version='>=12'] -> _libgcc_mutex==0.1=conda_forge
libpng -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1|0.1',build='main|conda_forge|main']
libnpp -> libgcc-ng[version='>=12'] -> _libgcc_mutex==0.1=conda_forge
libxml2 -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
libiconv -> libgcc-ng[version='>=10.3.0'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
lame -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
cuda-cupti -> libgcc-ng[version='>=12'] -> _libgcc_mutex==0.1=conda_forge
blas -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
openh264 -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
tbb -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
pillow -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
lcms2 -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
liblapack -> libgcc-ng[version='>=9.3.0'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
ncurses -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
libtiff -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
python=3.7.5 -> libgcc-ng[version='>=9.3.0'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
cuda-nvtx -> libgcc-ng[version='>=12'] -> _libgcc_mutex==0.1=conda_forge
libnvjpeg -> libgcc-ng[version='>=12'] -> _libgcc_mutex==0.1=conda_forge
freetype -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
llvm-openmp -> libgcc-ng[version='>=7.3.0'] -> _libgcc_mutex[version='*|0.1|0.1',build='main|conda_forge|main']
nettle -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
pytorch -> _openmp_mutex[version='>=4.5'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
jpeg -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
cuda-cudart -> libgcc-ng[version='>=12'] -> _libgcc_mutex==0.1=conda_forge
libcblas -> libgcc-ng[version='>=9.3.0'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
brotli-bin -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
libcusolver -> libgcc-ng[version='>=12'] -> _libgcc_mutex==0.1=conda_forge
icu -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
openjpeg -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
libbrotlicommon -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
numpy -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
openssl -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']
libbrotlidec -> libgcc-ng[version='>=12'] -> _libgcc_mutex[version='*|0.1',build='main|conda_forge|main']

Package liblapack conflicts for:
blas-devel -> liblapack[version='3.8.0|3.9.0',build='7_h6e990d7_netlib|0_h86c2bf4_netlib|7_openblas|10_mkl|11_linux64_openblas|11_linux64_mkl|13_linux64_mkl|14_linux64_openblas|14_linux64_mkl|15_linux64_openblas|16_linux64_openblas|18_linux64_openblas|*netlib|17_linux64_openblas|16_linux64_mkl|15_linux64_mkl|13_linux64_openblas|12_linux64_mkl|12_linux64_openblas|10_openblas|9_mkl|9_openblas|8_mkl|8_openblas|7_mkl|5_h92ddd45_netlib']
numpy -> blas=[build=openblas] -> liblapack[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0',build='4_mkl|10_mkl|12_mkl|13_mkl|18_mkl|19_mkl|8_mkl|11_linux64_mkl|12_linux64_mkl|13_linux64_mkl|14_linux64_mkl|0_openblas|3_openblas|6_openblas|7_openblas|12_openblas|16_openblas|17_openblas|5_openblas|6_openblas|7_openblas|8_openblas|9_openblas|12_linux64_openblas|14_linux64_openblas|15_linux64_openblas|16_linux64_openblas|18_linux64_openblas|17_linux64_openblas|13_linux64_openblas|11_linux64_openblas|10_openblas|15_openblas|14_openblas|13_openblas|11_openblas|10_openblas|9_openblas|8_openblas|5_openblas|4_openblas|2_openblas|16_linux64_mkl|15_linux64_mkl|10_mkl|9_mkl|7_mkl|6_mkl|5_mkl|21_mkl|20_mkl|16_mkl|15_mkl|14_mkl|11_mkl|9_mkl|8_mkl|7_mkl|6_mkl|5_mkl']
mkl-devel -> blas=[build=mkl] -> liblapack[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0',build='4_mkl|6_mkl|8_mkl|10_mkl|12_mkl|14_mkl|18_mkl|19_mkl|8_mkl|10_mkl|11_linux64_mkl|12_linux64_mkl|13_linux64_mkl|14_linux64_mkl|16_linux64_mkl|15_linux64_mkl|9_mkl|7_mkl|6_mkl|5_mkl|21_mkl|20_mkl|16_mkl|15_mkl|13_mkl|11_mkl|9_mkl|7_mkl|5_mkl']
torchaudio -> numpy[version='>=1.11'] -> liblapack[version='>=3.8.0,<4.0.0a0|>=3.8.0,<4.0a0|>=3.9.0,<4.0a0']
torchvision -> numpy[version='>=1.11'] -> liblapack[version='>=3.8.0,<4.0.0a0|>=3.8.0,<4.0a0|>=3.9.0,<4.0a0']
pytorch -> blas=[build=mkl] -> liblapack[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|>=3.8.0,<4.0a0|>=3.8.0,<4.0.0a0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0',build='3_openblas|5_openblas|7_openblas|8_openblas|9_openblas|12_openblas|16_openblas|5_openblas|7_openblas|8_openblas|11_linux64_openblas|15_linux64_openblas|16_linux64_openblas|18_linux64_openblas|4_mkl|6_mkl|8_mkl|10_mkl|12_mkl|14_mkl|18_mkl|19_mkl|8_mkl|10_mkl|11_linux64_mkl|12_linux64_mkl|13_linux64_mkl|14_linux64_mkl|16_linux64_mkl|15_linux64_mkl|9_mkl|7_mkl|6_mkl|5_mkl|21_mkl|20_mkl|16_mkl|15_mkl|13_mkl|11_mkl|9_mkl|7_mkl|5_mkl|17_linux64_openblas|14_linux64_openblas|13_linux64_openblas|12_linux64_openblas|10_openblas|9_openblas|6_openblas|17_openblas|15_openblas|14_openblas|13_openblas|11_openblas|10_openblas|6_openblas|4_openblas|2_openblas|0_openblas']
blas -> liblapacke==3.9.0[build=*netlib] -> liblapack[version='3.8.0.*|3.9.0.*']
blas -> liblapack[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0',build='0_openblas|3_openblas|4_mkl|5_openblas|6_openblas|6_mkl|6_h6e990d7_netlib|7_openblas|8_openblas|8_mkl|9_openblas|9_mkl|10_openblas|10_mkl|10_h86c2bf4_netlib|11_openblas|12_openblas|12_mkl|14_mkl|*netlib|17_openblas|18_mkl|19_mkl|4_h92ddd45_netlib|5_openblas|5_h92ddd45_netlib|6_openblas|6_mkl|7_openblas|10_mkl|11_linux64_openblas|11_linux64_mkl|13_linux64_mkl|14_linux64_openblas|14_linux64_mkl|15_linux64_openblas|16_linux64_openblas|18_linux64_openblas|*netlib|17_linux64_openblas|16_linux64_mkl|15_linux64_mkl|13_linux64_openblas|12_linux64_mkl|12_linux64_openblas|10_openblas|9_mkl|9_openblas|8_mkl|8_openblas|7_mkl|5_mkl|3_h92ddd45_netlib|21_mkl|20_mkl|16_mkl|16_openblas|15_openblas|15_mkl|14_openblas|13_mkl|13_openblas|11_h86c2bf4_netlib|11_mkl|8_h6e990d7_netlib|7_h6e990d7_netlib|7_mkl|5_mkl|5_h6e990d7_netlib|4_h6e990d7_netlib|4_openblas|2_openblas|1_h6e990d7_netlib|0_h6e990d7_netlib']
liblapacke -> liblapack[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0.*|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0.*',build='4_mkl|5_openblas|6_openblas|6_mkl|7_openblas|8_mkl|9_openblas|12_openblas|12_mkl|14_mkl|15_mkl|17_openblas|18_mkl|19_mkl|3_openblas|4_mkl|5_openblas|6_openblas|7_openblas|8_mkl|9_openblas|11_linux64_openblas|11_linux64_mkl|12_linux64_openblas|13_linux64_openblas|13_linux64_mkl|14_linux64_openblas|15_linux64_openblas|16_linux64_openblas|18_linux64_openblas|17_linux64_openblas|16_linux64_mkl|15_linux64_mkl|14_linux64_mkl|12_linux64_mkl|10_mkl|10_openblas|9_mkl|8_openblas|7_mkl|6_mkl|5_mkl|4_openblas|2_openblas|1_openblas|0_openblas|21_mkl|20_mkl|16_mkl|16_openblas|15_openblas|14_openblas|13_openblas|13_mkl|11_mkl|11_openblas|10_mkl|10_openblas|9_mkl|8_openblas|7_mkl|5_mkl|4_openblas']
blas-devel -> liblapacke==3.9.0[build=*netlib] -> liblapack[version='3.8.0.*|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0.*|3.9.0|3.9.0|3.9.0|3.9.0',build='16_openblas|18_mkl|19_mkl|0_openblas|3_openblas|4_mkl|*netlib|5_openblas|6_mkl|6_openblas|5_mkl|4_openblas|2_openblas|0_h6e990d7_netlib|21_mkl|20_mkl|17_openblas|16_mkl|15_openblas|15_mkl|14_mkl|14_openblas']
pytorch -> liblapack[version='>=3.9.0,<4.0a0']
numpy -> liblapack[version='>=3.8.0,<4.0.0a0|>=3.8.0,<4.0a0|>=3.9.0,<4.0a0']

Package tk conflicts for:
pillow -> tk[version='8.6.*|>=8.6.10,<8.7.0a0|>=8.6.11,<8.7.0a0|>=8.6.12,<8.7.0a0|>=8.6.9,<8.7.0a0|>=8.6.8,<8.7.0a0|>=8.6.7,<8.7.0a0']
wheel -> python[version='>=3.7'] -> tk[version='8.5.*|8.6.*|>=8.6.10,<8.7.0a0|>=8.6.11,<8.7.0a0|>=8.6.12,<8.7.0a0|>=8.6.9,<8.7.0a0|>=8.6.8,<8.7.0a0|>=8.6.7,<8.7.0a0']
pysocks -> python[version='>=3.8'] -> tk[version='8.5.*|8.6.*|>=8.6.10,<8.7.0a0|>=8.6.11,<8.7.0a0|>=8.6.12,<8.7.0a0|>=8.6.9,<8.7.0a0|>=8.6.8,<8.7.0a0|>=8.6.7,<8.7.0a0']
python_abi -> python=3.11 -> tk[version='8.5.*|8.6.*|>=8.6.10,<8.7.0a0|>=8.6.11,<8.7.0a0|>=8.6.12,<8.7.0a0|>=8.6.9,<8.7.0a0|>=8.6.8,<8.7.0a0|>=8.6.7,<8.7.0a0']
setuptools -> python[version='>=3.7'] -> tk[version='8.5.*|8.6.*|>=8.6.10,<8.7.0a0|>=8.6.11,<8.7.0a0|>=8.6.12,<8.7.0a0|>=8.6.9,<8.7.0a0|>=8.6.8,<8.7.0a0|>=8.6.7,<8.7.0a0']
charset-normalizer -> python[version='>=3.7'] -> tk[version='8.5.*|8.6.*|>=8.6.10,<8.7.0a0|>=8.6.11,<8.7.0a0|>=8.6.12,<8.7.0a0|>=8.6.9,<8.7.0a0|>=8.6.8,<8.7.0a0|>=8.6.7,<8.7.0a0']
python=3.7.5 -> tk[version='>=8.6.10,<8.7.0a0|>=8.6.8,<8.7.0a0']
idna -> python[version='>=3.6'] -> tk[version='8.5.*|8.6.*|>=8.6.10,<8.7.0a0|>=8.6.11,<8.7.0a0|>=8.6.12,<8.7.0a0|>=8.6.9,<8.7.0a0|>=8.6.8,<8.7.0a0|>=8.6.7,<8.7.0a0']
pytorch -> python[version='>=3.9,<3.10.0a0'] -> tk[version='8.5.*|8.6.*|>=8.6.10,<8.7.0a0|>=8.6.11,<8.7.0a0|>=8.6.12,<8.7.0a0|>=8.6.9,<8.7.0a0|>=8.6.8,<8.7.0a0|>=8.6.7,<8.7.0a0']
typing_extensions -> python[version='>=3.7'] -> tk[version='8.5.*|8.6.*|>=8.6.10,<8.7.0a0|>=8.6.11,<8.7.0a0|>=8.6.12,<8.7.0a0|>=8.6.9,<8.7.0a0|>=8.6.8,<8.7.0a0|>=8.6.7,<8.7.0a0']
pillow -> python[version='>=3.6,<3.7.0a0'] -> tk=8.5
numpy -> pypy3.9[version='>=7.3.11'] -> tk[version='8.5.*|8.6.*|>=8.6.10,<8.7.0a0|>=8.6.11,<8.7.0a0|>=8.6.12,<8.7.0a0|>=8.6.9,<8.7.0a0|>=8.6.8,<8.7.0a0|>=8.6.7,<8.7.0a0']
urllib3 -> python[version='>=3.7'] -> tk[version='8.5.*|8.6.*|>=8.6.10,<8.7.0a0|>=8.6.11,<8.7.0a0|>=8.6.12,<8.7.0a0|>=8.6.9,<8.7.0a0|>=8.6.8,<8.7.0a0|>=8.6.7,<8.7.0a0']
torchvision -> pillow[version='>=5.3.0,!=8.3.*'] -> tk[version='8.5.*|8.6.*|>=8.6.10,<8.7.0a0|>=8.6.11,<8.7.0a0|>=8.6.12,<8.7.0a0|>=8.6.9,<8.7.0a0|>=8.6.8,<8.7.0a0|>=8.6.7,<8.7.0a0']
certifi -> python[version='>=3.7'] -> tk[version='8.5.*|8.6.*|>=8.6.10,<8.7.0a0|>=8.6.11,<8.7.0a0|>=8.6.12,<8.7.0a0|>=8.6.9,<8.7.0a0|>=8.6.8,<8.7.0a0|>=8.6.7,<8.7.0a0']
torchaudio -> python[version='>=3.9,<3.10.0a0'] -> tk[version='8.5.*|8.6.*|>=8.6.10,<8.7.0a0|>=8.6.11,<8.7.0a0|>=8.6.12,<8.7.0a0|>=8.6.9,<8.7.0a0|>=8.6.8,<8.7.0a0|>=8.6.7,<8.7.0a0']
requests -> python[version='>=3.7'] -> tk[version='8.5.*|8.6.*|>=8.6.10,<8.7.0a0|>=8.6.11,<8.7.0a0|>=8.6.12,<8.7.0a0|>=8.6.9,<8.7.0a0|>=8.6.8,<8.7.0a0|>=8.6.7,<8.7.0a0']
pip -> python[version='>=3.7'] -> tk[version='8.5.*|8.6.*|>=8.6.10,<8.7.0a0|>=8.6.11,<8.7.0a0|>=8.6.12,<8.7.0a0|>=8.6.9,<8.7.0a0|>=8.6.8,<8.7.0a0|>=8.6.7,<8.7.0a0']

Package libzlib conflicts for:
setuptools -> python[version='>=3.7'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
gnutls -> zlib[version='>=1.2.11,<1.3.0a0'] -> libzlib[version='1.2.11|1.2.11|1.2.11|1.2.12|1.2.12|1.2.12|1.2.12|1.2.12|1.2.13',build='h166bdaf_1014|h166bdaf_0|h166bdaf_2|hd590300_5|h166bdaf_4|h166bdaf_4|h166bdaf_3|h166bdaf_1|h36c2ea0_1013|h36c2ea0_1012']
libhwloc -> libxml2[version='>=2.11.5,<2.12.0a0'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
certifi -> python[version='>=3.7'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
openjpeg -> zlib[version='>=1.2.11,<1.3.0a0'] -> libzlib[version='1.2.11|1.2.11|1.2.11|1.2.12|1.2.12|1.2.12|1.2.12|1.2.12|1.2.13',build='h166bdaf_1014|h166bdaf_0|h166bdaf_2|hd590300_5|h166bdaf_4|h166bdaf_4|h166bdaf_3|h166bdaf_1|h36c2ea0_1013|h36c2ea0_1012']
zlib -> libzlib[version='1.2.11|1.2.11|1.2.11|1.2.12|1.2.12|1.2.12|1.2.12|1.2.12|1.2.13',build='h166bdaf_1014|h166bdaf_0|h166bdaf_2|hd590300_5|h166bdaf_4|h166bdaf_4|h166bdaf_3|h166bdaf_1|h36c2ea0_1013|h36c2ea0_1012']
libpng -> zlib[version='>=1.2.12,<1.3.0a0'] -> libzlib[version='1.2.11|1.2.11|1.2.11|1.2.12|1.2.12|1.2.12|1.2.12|1.2.12|1.2.13',build='h166bdaf_1014|h166bdaf_0|h166bdaf_2|hd590300_5|h166bdaf_4|h166bdaf_4|h166bdaf_3|h166bdaf_1|h36c2ea0_1013|h36c2ea0_1012']
libxml2 -> zlib -> libzlib[version='1.2.11|1.2.11|1.2.11|1.2.12|1.2.12|1.2.12|1.2.12|1.2.12|1.2.13',build='h166bdaf_1014|h166bdaf_0|h166bdaf_2|hd590300_5|h166bdaf_4|h166bdaf_4|h166bdaf_3|h166bdaf_1|h36c2ea0_1013|h36c2ea0_1012']
openh264 -> zlib[version='>=1.2.11,<1.3.0a0'] -> libzlib[version='1.2.11|1.2.11|1.2.11|1.2.12|1.2.12|1.2.12|1.2.12|1.2.12|1.2.13',build='h166bdaf_1014|h166bdaf_0|h166bdaf_2|hd590300_5|h166bdaf_4|h166bdaf_4|h166bdaf_3|h166bdaf_1|h36c2ea0_1013|h36c2ea0_1012']
python_abi -> python=3.11 -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
blas -> llvm-openmp[version='>=16.0.6'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0']
requests -> python[version='>=3.7'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
_openmp_mutex -> llvm-openmp[version='>=9.0.1'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0']
torchaudio -> python[version='>=3.9,<3.10.0a0'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0']
ffmpeg -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
libsqlite -> libzlib[version='>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
zstd -> zlib[version='>=1.2.11,<1.3.0a0'] -> libzlib[version='1.2.11|1.2.11|1.2.11|1.2.12|1.2.12|1.2.12|1.2.12|1.2.12|1.2.13',build='h166bdaf_1014|h166bdaf_0|h166bdaf_2|hd590300_5|h166bdaf_4|h166bdaf_4|h166bdaf_3|h166bdaf_1|h36c2ea0_1013|h36c2ea0_1012']
llvm-openmp -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0']
libtiff -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
openh264 -> libzlib[version='>=1.2.12,<1.3.0a0']
sqlite -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
numpy -> pypy3.9[version='>=7.3.11'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0']
pillow -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
libxml2 -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
python=3.7.5 -> sqlite[version='>=3.34.0,<4.0a0'] -> libzlib[version='1.2.11|1.2.11|1.2.11|1.2.12|1.2.12|1.2.12|1.2.12|1.2.12|1.2.13|1.2.13|>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0',build='h166bdaf_1014|h166bdaf_0|h166bdaf_2|hd590300_5|h166bdaf_4|h166bdaf_4|h166bdaf_3|h166bdaf_1|h36c2ea0_1013|h36c2ea0_1012']
libtiff -> zlib[version='>=1.2.11,<1.3.0a0'] -> libzlib[version='1.2.11|1.2.11|1.2.11|1.2.12|1.2.12|1.2.12|1.2.12|1.2.12|1.2.13',build='h166bdaf_1014|h166bdaf_0|h166bdaf_2|hd590300_5|h166bdaf_4|h166bdaf_4|h166bdaf_3|h166bdaf_1|h36c2ea0_1013|h36c2ea0_1012']
pip -> python[version='>=3.7'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
torchvision -> ffmpeg[version='>=4.2'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
urllib3 -> python[version='>=3.7'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
openjpeg -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
mkl -> llvm-openmp[version='>=16.0.6'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0']
zstd -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
pillow -> zlib[version='>=1.2.12,<1.3.0a0'] -> libzlib[version='1.2.11|1.2.11|1.2.11|1.2.12|1.2.12|1.2.12|1.2.12|1.2.12|1.2.13',build='h166bdaf_1014|h166bdaf_0|h166bdaf_2|hd590300_5|h166bdaf_4|h166bdaf_4|h166bdaf_3|h166bdaf_1|h36c2ea0_1013|h36c2ea0_1012']
ffmpeg -> zlib[version='>=1.2.11,<1.3.0a0'] -> libzlib[version='1.2.11|1.2.11|1.2.11|1.2.12|1.2.12|1.2.12|1.2.12|1.2.12|1.2.13',build='h166bdaf_1014|h166bdaf_0|h166bdaf_2|hd590300_5|h166bdaf_4|h166bdaf_4|h166bdaf_3|h166bdaf_1|h36c2ea0_1013|h36c2ea0_1012']
pytorch -> python[version='>=3.9,<3.10.0a0'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.13,<1.3.0a0|>=1.2.12,<1.3.0a0']
lcms2 -> libtiff[version='>=4.6.0,<4.7.0a0'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
idna -> python[version='>=3.6'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
wheel -> python[version='>=3.7'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
charset-normalizer -> python[version='>=3.7'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
pysocks -> python[version='>=3.8'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
libpng -> libzlib[version='>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
typing_extensions -> python[version='>=3.7'] -> libzlib[version='>=1.2.11,<1.3.0a0|>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
freetype -> libzlib[version='>=1.2.12,<1.3.0a0|>=1.2.13,<1.3.0a0']
freetype -> zlib[version='>=1.2.11,<1.3.0a0'] -> libzlib[version='1.2.11|1.2.11|1.2.11|1.2.12|1.2.12|1.2.12|1.2.12|1.2.12|1.2.13',build='h166bdaf_1014|h166bdaf_0|h166bdaf_2|hd590300_5|h166bdaf_4|h166bdaf_4|h166bdaf_3|h166bdaf_1|h36c2ea0_1013|h36c2ea0_1012']
sqlite -> zlib[version='>=1.2.12,<1.3.0a0'] -> libzlib[version='1.2.11|1.2.11|1.2.11|1.2.12|1.2.12|1.2.12|1.2.12|1.2.12|1.2.13',build='h166bdaf_1014|h166bdaf_0|h166bdaf_2|hd590300_5|h166bdaf_4|h166bdaf_4|h166bdaf_3|h166bdaf_1|h36c2ea0_1013|h36c2ea0_1012']
llvm-openmp -> zstd[version='>=1.5.2,<1.6.0a0'] -> libzlib[version='1.2.12|1.2.12|1.2.12|1.2.12|1.2.12|1.2.13|1.2.13|>=1.2.12,<1.3.0a0',build='h166bdaf_0|h166bdaf_2|hd590300_5|h166bdaf_4|h166bdaf_4|h166bdaf_3|h166bdaf_1']

Package libpng conflicts for:
freetype -> libpng[version='1.6.*|>=1.6.21,<1.7|>=1.6.22,<1.6.31|>=1.6.32,<1.6.35|>=1.6.34,<1.7.0a0|>=1.6.35,<1.7.0a0|>=1.6.37,<1.7.0a0|>=1.6.39,<1.7.0a0|>=1.6.28,<1.7|>=1.6.23,<1.7|>=1.6.32,<1.7.0a0']
ffmpeg -> libpng[version='>=1.6.37,<1.7.0a0']
pillow -> freetype[version='>=2.12.1,<3.0a0'] -> libpng[version='1.6.*|>=1.6.21,<1.7|>=1.6.22,<1.6.31|>=1.6.32,<1.6.35|>=1.6.32,<1.7.0a0|>=1.6.34,<1.7.0a0|>=1.6.35,<1.7.0a0|>=1.6.37,<1.7.0a0|>=1.6.39,<1.7.0a0|>=1.6.28,<1.7|>=1.6.23,<1.7']
torchvision -> libpng[version='>=1.6.37,<1.7.0a0|>=1.6.39,<1.7.0a0']
libtiff -> libwebp -> libpng[version='>=1.6.32,<1.7.0a0|>=1.6.34,<1.7.0a0|>=1.6.35,<1.7.0a0|>=1.6.37,<1.7.0a0|>=1.6.39,<1.7.0a0']
openjpeg -> libpng[version='1.6.*|>=1.6.21,<1.7|>=1.6.22,<1.6.31|>=1.6.32,<1.6.35|>=1.6.34,<1.7.0a0|>=1.6.35,<1.7.0a0|>=1.6.37,<1.7.0a0|>=1.6.39,<1.7.0a0|>=1.6.28,<1.7|>=1.6.23,<1.7|>=1.6.32,<1.7.0a0']
ffmpeg -> freetype[version='>=2.10.2,<3.0a0'] -> libpng[version='>=1.6.32,<1.6.35|>=1.6.34,<1.7.0a0|>=1.6.35,<1.7.0a0|>=1.6.39,<1.7.0a0|>=1.6.32,<1.7.0a0']

Package pypy3.8 conflicts for:
requests -> certifi[version='>=2017.4.17'] -> pypy3.8[version='7.3.11.*|>=7.3.8|>=7.3.9|7.3.9.*|7.3.8.*']
pysocks -> pypy3.8[version='>=7.3.8']
pysocks -> python[version='>=3.8'] -> pypy3.8[version='7.3.*|7.3.11.*|7.3.9.*|7.3.8.*']
setuptools -> python[version='>=3.7'] -> pypy3.8[version='7.3.*|7.3.11.*|7.3.9.*|7.3.8.*']
setuptools -> pypy3.8[version='>=7.3.8|>=7.3.9']
certifi -> pypy3.8[version='>=7.3.8|>=7.3.9']
certifi -> python[version='>=3.7'] -> pypy3.8[version='7.3.*|7.3.11.*|7.3.9.*|7.3.8.*']
wheel -> python[version='>=3.7'] -> pypy3.8[version='7.3.11.*|7.3.9.*|7.3.8.*|>=7.3.9|>=7.3.8']
pytorch -> sympy -> pypy3.8[version='7.3.11.*|>=7.3.9|7.3.9.*|7.3.8.*|>=7.3.11|>=7.3.8']
torchaudio -> numpy[version='>=1.11'] -> pypy3.8[version='7.3.11.*|>=7.3.11|>=7.3.9|>=7.3.8|7.3.9.*|7.3.8.*']
pillow -> pypy3.8[version='>=7.3.11|>=7.3.9']
typing_extensions -> python[version='>=3.7'] -> pypy3.8[version='7.3.11.*|7.3.9.*|7.3.8.*']
python_abi -> pypy3.8=7.3
pillow -> python[version='>=3.8,<3.9.0a0'] -> pypy3.8[version='7.3.*|7.3.11.*|7.3.9.*|7.3.8.*']
charset-normalizer -> python[version='>=3.7'] -> pypy3.8[version='7.3.11.*|7.3.9.*|7.3.8.*']
torchvision -> numpy[version='>=1.11'] -> pypy3.8[version='7.3.11.*|>=7.3.11|>=7.3.9|>=7.3.8|7.3.9.*|7.3.8.*']
python_abi -> python=3.8 -> pypy3.8[version='7.3.11.*|7.3.9.*|7.3.8.*']
idna -> python[version='>=3.6'] -> pypy3.8[version='7.3.11.*|7.3.9.*|7.3.8.*']
numpy -> pypy3.8[version='>=7.3.11|>=7.3.9|>=7.3.8']
urllib3 -> brotli-python[version='>=1.0.9'] -> pypy3.8[version='7.3.11.*|>=7.3.11|>=7.3.9|>=7.3.8|7.3.9.*|7.3.8.*']
pip -> python[version='>=3.7'] -> pypy3.8[version='7.3.11.*|7.3.9.*|7.3.8.*|>=7.3.9|>=7.3.8']
numpy -> python[version='>=3.8,<3.9.0a0'] -> pypy3.8[version='7.3.*|7.3.11.*|7.3.9.*|7.3.8.*']
zstd -> lz4 -> pypy3.8[version='>=7.3.11|>=7.3.9|>=7.3.8']

Package packaging conflicts for:
wheel -> packaging[version='>=20.2']
pip -> wheel -> packaging[version='>=20.2']

Package cuda-version conflicts for:
libcusparse -> cuda-version[version='>=12.0.0,<12.1.0a0']
cuda-nvrtc -> cuda-version[version='>=12.0,<12.1.0a0']
libhwloc -> cuda-version[version='>=12.0,<13']
libcurand -> cuda-version[version='>=12.0.0,<12.1.0a0']
cuda-libraries -> cuda-cudart=12.0.107 -> cuda-version[version='>=12.0,<12.1.0a0|>=12.0.0,<12.1.0a0']
libcusolver -> cuda-version[version='>=12.0.0,<12.1.0a0']
libcufft -> cuda-version[version='>=12.0.0,<12.1.0a0']
libnvjpeg -> cuda-version[version='>=12.0,<12.1.0a0']
libcusolver -> libcublas[version='>=12.0.1.189,<12.1.0a0'] -> cuda-version[version='>=12.0,<12.1.0a0']
pytorch -> cudnn[version='>=8.8.0.121,<9.0a0'] -> cuda-version[version='>=11.0,<12.0a0|>=12.0,<13.0a0|>=12.0,<13|>=11.8,<12.0a0|>=11.2,<12.0a0|>=11.1,<12.0a0']
torchvision -> cudnn[version='>=8.8.0.121,<9.0a0'] -> cuda-version[version='>=11.0,<12.0a0|>=12.0,<13.0a0']
cuda-nvtx -> cuda-version[version='>=12.0,<12.1.0a0']
libcufile -> cuda-version[version='>=12.0,<12.1.0a0']
libcublas -> cuda-version[version='>=12.0,<12.1.0a0|>=12.0.0,<12.1.0a0']
libnpp -> cuda-version[version='>=12.0,<12.1.0a0']
tbb -> libhwloc[version='>=2.9.2,<2.9.3.0a0'] -> cuda-version[version='>=12.0,<13']
cuda-cupti -> cuda-version[version='>=12.0,<12.1.0a0']
cuda-cudart -> cuda-version[version='>=12.0,<12.1.0a0']

Package cuda-libraries conflicts for:
cuda-runtime -> cuda-libraries[version='12.0.0.*|>=11.8.0']
pytorch-cuda=11.8 -> cuda-runtime[version='>=11.8,<12.0'] -> cuda-libraries[version='>=11.8.0']
torchaudio -> pytorch-cuda=11.8 -> cuda-libraries[version='>=11.7,<11.8|>=11.8,<12.0']
torchvision -> pytorch-cuda=11.8 -> cuda-libraries[version='>=11.7,<11.8|>=11.8,<12.0']
pytorch-cuda=11.8 -> cuda-libraries[version='>=11.8,<12.0']
pytorch -> pytorch-cuda[version='>=11.8,<11.9'] -> cuda-libraries[version='>=11.7,<11.8|>=11.8,<12.0']

Package libnvjpeg conflicts for:
pytorch -> pytorch-cuda[version='>=11.8,<11.9'] -> libnvjpeg[version='>=11.7.2.34,<11.9.0.86|>=11.9.0.86,<12.0.0.28']
cuda-runtime -> cuda-libraries=12.0.0 -> libnvjpeg[version='12.0.0.28.*|>=11.9.0.86']
pytorch-cuda=11.8 -> libnvjpeg[version='>=11.9.0.86,<12.0.0.28']
torchaudio -> pytorch-cuda=11.8 -> libnvjpeg[version='>=11.7.2.34,<11.9.0.86|>=11.9.0.86,<12.0.0.28']
torchvision -> pytorch-cuda=11.8 -> libnvjpeg[version='>=11.7.2.34,<11.9.0.86|>=11.9.0.86,<12.0.0.28']
cuda-libraries -> libnvjpeg[version='12.0.0.28.*|>=11.9.0.86']
pytorch-cuda=11.8 -> cuda-libraries[version='>=11.8,<12.0'] -> libnvjpeg[version='>=11.9.0.86']

Package graalpy conflicts for:
setuptools -> python[version='>=3.7'] -> graalpy[version='>=22.3.0,<22.3.1.0a0|>=23.0.0,<23.0.1.0a0']
numpy -> python[version='>=3.10,<3.11.0a0'] -> graalpy[version='>=22.3.0,<22.3.1.0a0|>=23.0.0,<23.0.1.0a0']
charset-normalizer -> python[version='>=3.7'] -> graalpy[version='>=22.3.0,<22.3.1.0a0|>=23.0.0,<23.0.1.0a0']
wheel -> python[version='>=3.7'] -> graalpy[version='>=22.3.0,<22.3.1.0a0|>=23.0.0,<23.0.1.0a0']
requests -> python[version='>=3.7'] -> graalpy[version='>=22.3.0,<22.3.1.0a0|>=23.0.0,<23.0.1.0a0']
certifi -> python[version='>=3.7'] -> graalpy[version='>=22.3.0,<22.3.1.0a0|>=23.0.0,<23.0.1.0a0']
urllib3 -> python[version='>=3.7'] -> graalpy[version='>=22.3.0,<22.3.1.0a0|>=23.0.0,<23.0.1.0a0']
idna -> python[version='>=3.6'] -> graalpy[version='>=22.3.0,<22.3.1.0a0|>=23.0.0,<23.0.1.0a0']
pillow -> python[version='>=3.8,<3.9.0a0'] -> graalpy[version='>=22.3.0,<22.3.1.0a0|>=23.0.0,<23.0.1.0a0']
pytorch -> python[version='>=3.10,<3.11.0a0'] -> graalpy[version='>=22.3.0,<22.3.1.0a0|>=23.0.0,<23.0.1.0a0']
pip -> python[version='>=3.7'] -> graalpy[version='>=22.3.0,<22.3.1.0a0|>=23.0.0,<23.0.1.0a0']
pysocks -> python[version='>=3.8'] -> graalpy[version='>=22.3.0,<22.3.1.0a0|>=23.0.0,<23.0.1.0a0']
python_abi -> python=3.10 -> graalpy[version='>=22.3.0,<22.3.1.0a0|>=23.0.0,<23.0.1.0a0']
torchvision -> python[version='>=3.8,<3.9.0a0'] -> graalpy[version='>=22.3.0,<22.3.1.0a0|>=23.0.0,<23.0.1.0a0']
torchaudio -> python[version='>=3.8,<3.9.0a0'] -> graalpy[version='>=22.3.0,<22.3.1.0a0|>=23.0.0,<23.0.1.0a0']
typing_extensions -> python[version='>=3.7'] -> graalpy[version='>=22.3.0,<22.3.1.0a0|>=23.0.0,<23.0.1.0a0']

Package libgfortran4 conflicts for:
mkl-devel -> blas=[build=mkl] -> libgfortran4[version='>=7.5.0']
blas-devel -> liblapack==3.9.0[build=*netlib] -> libgfortran4[version='>=7.5.0']
numpy -> libblas[version='>=3.9.0,<4.0a0'] -> libgfortran4[version='7.5.0.*|>=7.5.0']
blas -> libgfortran4[version='>=7.5.0']
libcblas -> libgfortran4[version='>=7.5.0']
blas -> libgfortran-ng -> libgfortran4=7.5.0
libblas -> libgfortran-ng -> libgfortran4=7.5.0
liblapack -> libgfortran4[version='>=7.5.0']
liblapacke -> libgfortran-ng -> libgfortran4=7.5.0
libgfortran-ng -> libgfortran4=7.5.0
liblapack -> libgfortran-ng -> libgfortran4=7.5.0
pytorch -> blas=[build=mkl] -> libgfortran4[version='>=7.5.0']
liblapacke -> libgfortran4[version='>=7.5.0']
libcblas -> libgfortran-ng -> libgfortran4=7.5.0
libblas -> libgfortran4[version='>=7.5.0']

Package libuuid conflicts for:
requests -> python[version='>=3.7'] -> libuuid[version='>=1.0.3,<2.0a0|>=1.41.5,<2.0a0|>=2.32.1,<3.0a0|>=2.38.1,<3.0a0']
pip -> python[version='>=3.7'] -> libuuid[version='>=1.0.3,<2.0a0|>=1.41.5,<2.0a0|>=2.32.1,<3.0a0|>=2.38.1,<3.0a0']
idna -> python[version='>=3.6'] -> libuuid[version='>=1.0.3,<2.0a0|>=1.41.5,<2.0a0|>=2.32.1,<3.0a0|>=2.38.1,<3.0a0']
pytorch -> python[version='>=3.9,<3.10.0a0'] -> libuuid[version='>=1.0.3,<2.0a0|>=1.41.5,<2.0a0|>=2.32.1,<3.0a0|>=2.38.1,<3.0a0']
wheel -> python[version='>=3.7'] -> libuuid[version='>=1.0.3,<2.0a0|>=1.41.5,<2.0a0|>=2.32.1,<3.0a0|>=2.38.1,<3.0a0']
typing_extensions -> python[version='>=3.7'] -> libuuid[version='>=1.0.3,<2.0a0|>=1.41.5,<2.0a0|>=2.32.1,<3.0a0|>=2.38.1,<3.0a0']
python_abi -> python=3.11 -> libuuid[version='>=1.0.3,<2.0a0|>=1.41.5,<2.0a0|>=2.32.1,<3.0a0|>=2.38.1,<3.0a0']
torchaudio -> python[version='>=3.9,<3.10.0a0'] -> libuuid[version='>=1.0.3,<2.0a0|>=1.41.5,<2.0a0|>=2.32.1,<3.0a0|>=2.38.1,<3.0a0']
urllib3 -> python[version='>=3.7'] -> libuuid[version='>=1.0.3,<2.0a0|>=1.41.5,<2.0a0|>=2.32.1,<3.0a0|>=2.38.1,<3.0a0']
ffmpeg -> fontconfig[version='>=2.14.2,<3.0a0'] -> libuuid[version='>=1.41.5,<2.0a0|>=2.32.1,<3.0a0']
torchvision -> python[version='>=3.8,<3.9.0a0'] -> libuuid[version='>=1.0.3,<2.0a0|>=1.41.5,<2.0a0|>=2.32.1,<3.0a0|>=2.38.1,<3.0a0']
setuptools -> python[version='>=3.7'] -> libuuid[version='>=1.0.3,<2.0a0|>=1.41.5,<2.0a0|>=2.32.1,<3.0a0|>=2.38.1,<3.0a0']
pysocks -> python[version='>=3.8'] -> libuuid[version='>=1.0.3,<2.0a0|>=1.41.5,<2.0a0|>=2.32.1,<3.0a0|>=2.38.1,<3.0a0']
charset-normalizer -> python[version='>=3.7'] -> libuuid[version='>=1.0.3,<2.0a0|>=1.41.5,<2.0a0|>=2.32.1,<3.0a0|>=2.38.1,<3.0a0']
pillow -> python[version='>=3.9,<3.10.0a0'] -> libuuid[version='>=1.0.3,<2.0a0|>=1.41.5,<2.0a0|>=2.32.1,<3.0a0|>=2.38.1,<3.0a0']
certifi -> python[version='>=3.7'] -> libuuid[version='>=1.0.3,<2.0a0|>=1.41.5,<2.0a0|>=2.32.1,<3.0a0|>=2.38.1,<3.0a0']
numpy -> python[version='>=3.9,<3.10.0a0'] -> libuuid[version='>=1.0.3,<2.0a0|>=1.41.5,<2.0a0|>=2.32.1,<3.0a0|>=2.38.1,<3.0a0']

Package libcblas conflicts for:
blas -> libcblas[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0',build='0_blis|3_blis|3_openblas|4_mkl|4_h6e990d7_netlib|5_openblas|6_openblas|6_mkl|6_h6e990d7_netlib|7_blis|7_openblas|8_blis|8_openblas|8_h6e990d7_netlib|9_openblas|10_h86c2bf4_netlib|11_blis|12_openblas|12_mkl|14_mkl|15_blis|16_openblas|16_blis|17_openblas|18_mkl|19_mkl|5_openblas|6_mkl|7_blis|7_openblas|8_blis|8_openblas|9_openblas|9_mkl|10_blis|10_mkl|11_linux64_blis|11_linux64_openblas|11_linux64_mkl|12_linux64_openblas|12_linux64_blis|13_linux64_openblas|13_linux64_mkl|14_linux64_openblas|14_linux64_mkl|15_linux64_openblas|16_linux64_openblas|17_linux64_openblas|18_linux64_openblas|18_linux64_blis|17_linux64_blis|16_linux64_mkl|16_linux64_blis|15_linux64_mkl|15_linux64_blis|14_linux64_blis|13_linux64_blis|12_linux64_mkl|10_openblas|9_blis|8_mkl|7_mkl|6_openblas|6_blis|5_h92ddd45_netlib|5_mkl|5_blis|4_h92ddd45_netlib|3_h92ddd45_netlib|21_mkl|20_mkl|16_mkl|15_openblas|15_mkl|14_openblas|14_blis|13_mkl|13_openblas|13_blis|12_blis|11_h86c2bf4_netlib|11_mkl|11_openblas|10_mkl|10_openblas|10_blis|9_mkl|9_blis|8_mkl|7_h6e990d7_netlib|7_mkl|6_blis|5_mkl|5_blis|5_h6e990d7_netlib|4_openblas|4_blis|2_openblas|2_blis|1_h6e990d7_netlib|0_openblas|0_h6e990d7_netlib']
pytorch -> libcblas[version='>=3.9.0,<4.0a0']
blas-devel -> libcblas[version='3.8.0|3.9.0',build='7_h6e990d7_netlib|0_h86c2bf4_netlib|7_blis|7_openblas|8_blis|8_openblas|10_blis|10_openblas|11_linux64_blis|11_linux64_mkl|12_linux64_blis|12_linux64_openblas|13_linux64_mkl|14_linux64_mkl|15_linux64_openblas|16_linux64_openblas|17_linux64_openblas|18_linux64_openblas|18_linux64_blis|17_linux64_blis|16_linux64_mkl|16_linux64_blis|15_linux64_mkl|15_linux64_blis|14_linux64_openblas|14_linux64_blis|13_linux64_openblas|13_linux64_blis|12_linux64_mkl|11_linux64_openblas|10_mkl|9_mkl|9_openblas|9_blis|8_mkl|7_mkl|5_h92ddd45_netlib']
mkl-devel -> blas=[build=mkl] -> libcblas[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0',build='4_mkl|6_mkl|8_mkl|10_mkl|12_mkl|14_mkl|18_mkl|19_mkl|8_mkl|10_mkl|11_linux64_mkl|12_linux64_mkl|13_linux64_mkl|14_linux64_mkl|16_linux64_mkl|15_linux64_mkl|9_mkl|7_mkl|6_mkl|5_mkl|21_mkl|20_mkl|16_mkl|15_mkl|13_mkl|11_mkl|9_mkl|7_mkl|5_mkl']
numpy -> libcblas[version='>=3.8.0,<4.0a0|>=3.9.0,<4.0a0']
blas-devel -> liblapacke==3.9.0[build=*netlib] -> libcblas[version='3.8.0.*|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0.*|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0',build='14_mkl|15_blis|16_openblas|17_openblas|18_mkl|19_mkl|0_blis|0_openblas|3_blis|3_openblas|4_blis|4_mkl|5_openblas|6_blis|6_mkl|6_openblas|5_mkl|5_blis|4_openblas|2_openblas|2_blis|0_h6e990d7_netlib|21_mkl|20_mkl|16_mkl|16_blis|15_openblas|15_mkl|14_openblas|14_blis']
torchaudio -> numpy[version='>=1.11'] -> libcblas[version='>=3.8.0,<4.0a0|>=3.9.0,<4.0a0']
blas -> liblapacke==3.9.0[build=*netlib] -> libcblas[version='3.8.0.*|3.9.0.*']
liblapacke -> libcblas[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0.*|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0.*',build='4_mkl|5_openblas|6_openblas|6_mkl|7_openblas|8_mkl|9_openblas|12_openblas|12_mkl|14_mkl|15_mkl|17_openblas|18_mkl|19_mkl|3_openblas|4_mkl|5_openblas|6_openblas|7_openblas|8_mkl|9_openblas|11_linux64_openblas|11_linux64_mkl|12_linux64_openblas|13_linux64_openblas|13_linux64_mkl|14_linux64_openblas|15_linux64_openblas|16_linux64_openblas|18_linux64_openblas|17_linux64_openblas|16_linux64_mkl|15_linux64_mkl|14_linux64_mkl|12_linux64_mkl|10_mkl|10_openblas|9_mkl|8_openblas|7_mkl|6_mkl|5_mkl|4_openblas|2_openblas|1_openblas|0_openblas|21_mkl|20_mkl|16_mkl|16_openblas|15_openblas|14_openblas|13_openblas|13_mkl|11_mkl|11_openblas|10_mkl|10_openblas|9_mkl|8_openblas|7_mkl|5_mkl|4_openblas']
numpy -> blas=[build=openblas] -> libcblas[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0',build='4_mkl|10_mkl|12_mkl|13_mkl|18_mkl|19_mkl|8_mkl|11_linux64_mkl|12_linux64_mkl|13_linux64_mkl|14_linux64_mkl|0_openblas|3_openblas|6_openblas|7_openblas|12_openblas|16_openblas|17_openblas|5_openblas|6_openblas|7_openblas|8_openblas|9_openblas|12_linux64_openblas|14_linux64_openblas|15_linux64_openblas|16_linux64_openblas|18_linux64_openblas|17_linux64_openblas|13_linux64_openblas|11_linux64_openblas|10_openblas|15_openblas|14_openblas|13_openblas|11_openblas|10_openblas|9_openblas|8_openblas|5_openblas|4_openblas|2_openblas|16_linux64_mkl|15_linux64_mkl|10_mkl|9_mkl|7_mkl|6_mkl|5_mkl|21_mkl|20_mkl|16_mkl|15_mkl|14_mkl|11_mkl|9_mkl|8_mkl|7_mkl|6_mkl|5_mkl']
torchvision -> numpy[version='>=1.11'] -> libcblas[version='>=3.8.0,<4.0a0|>=3.9.0,<4.0a0']
pytorch -> blas=[build=mkl] -> libcblas[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|>=3.8.0,<4.0a0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0',build='3_openblas|5_openblas|7_openblas|8_openblas|9_openblas|12_openblas|16_openblas|5_openblas|7_openblas|8_openblas|11_linux64_openblas|15_linux64_openblas|16_linux64_openblas|18_linux64_openblas|4_mkl|6_mkl|8_mkl|10_mkl|12_mkl|14_mkl|18_mkl|19_mkl|8_mkl|10_mkl|11_linux64_mkl|12_linux64_mkl|13_linux64_mkl|14_linux64_mkl|16_linux64_mkl|15_linux64_mkl|9_mkl|7_mkl|6_mkl|5_mkl|21_mkl|20_mkl|16_mkl|15_mkl|13_mkl|11_mkl|9_mkl|7_mkl|5_mkl|17_linux64_openblas|14_linux64_openblas|13_linux64_openblas|12_linux64_openblas|10_openblas|9_openblas|6_openblas|17_openblas|15_openblas|14_openblas|13_openblas|11_openblas|10_openblas|6_openblas|4_openblas|2_openblas|0_openblas']

Package freetype conflicts for:
ffmpeg -> freetype[version='2.8.1|2.8.1.*|>=2.10.2,<3.0a0|>=2.10.3,<3.0a0|>=2.12.1,<3.0a0|>=2.10.4,<3.0a0|>=2.9.1,<3.0a0|>=2.8.1,<2.9.0a0|>=2.8.1,<2.8.2.0a0|>=2.8,<2.9.0a0']
pillow -> freetype[version='2.5.*|2.6.*|2.7|2.7.*|2.7|2.8.*|2.8.1|2.8.1.*|>=2.10.4,<3.0a0|>=2.12.1,<3.0a0|>=2.9.1,<3.0a0|>=2.8.1,<2.9.0a0|>=2.10.3,<3.0a0|>=2.8,<2.9.0a0']
torchvision -> ffmpeg[version='>=4.2'] -> freetype[version='2.7|2.7.*|2.7|2.8.*|2.8.1|2.8.1.*|>=2.10.2,<3.0a0|>=2.10.3,<3.0a0|>=2.12.1,<3.0a0|>=2.10.4,<3.0a0|>=2.9.1,<3.0a0|>=2.8.1,<2.9.0a0|>=2.8,<2.9.0a0']

Package libcufft conflicts for:
torchaudio -> pytorch-cuda=11.8 -> libcufft[version='>=10.7.2.50,<10.9.0.58|>=10.9.0.58,<11.0.0.21']
pytorch-cuda=11.8 -> cuda-libraries[version='>=11.8,<12.0'] -> libcufft[version='>=10.9.0.58']
cuda-runtime -> cuda-libraries=12.0.0 -> libcufft[version='11.0.0.21.*|>=10.9.0.58']
torchvision -> pytorch-cuda=11.8 -> libcufft[version='>=10.7.2.50,<10.9.0.58|>=10.9.0.58,<11.0.0.21']
pytorch -> pytorch-cuda[version='>=11.8,<11.9'] -> libcufft[version='>=10.7.2.50,<10.9.0.58|>=10.9.0.58,<11.0.0.21']
pytorch-cuda=11.8 -> libcufft[version='>=10.9.0.58,<11.0.0.21']
cuda-libraries -> libcufft[version='11.0.0.21.*|>=10.9.0.58']

Package bzip2 conflicts for:
idna -> python[version='>=3.6'] -> bzip2[version='>=1.0.6,<2.0a0|>=1.0.8,<2.0a0']
numpy -> pypy3.9[version='>=7.3.11'] -> bzip2[version='>=1.0.6,<2.0a0|>=1.0.8,<2.0a0']
pytorch -> python[version='>=3.9,<3.10.0a0'] -> bzip2[version='>=1.0.6,<2.0a0|>=1.0.8,<2.0a0']
typing_extensions -> python[version='>=3.7'] -> bzip2[version='>=1.0.6,<2.0a0|>=1.0.8,<2.0a0']
certifi -> python[version='>=3.7'] -> bzip2[version='>=1.0.6,<2.0a0|>=1.0.8,<2.0a0']
ffmpeg -> bzip2[version='1.0.*|>=1.0.6,<1.1.0a0|>=1.0.6,<2.0a0|>=1.0.8,<2.0a0']
pip -> python[version='>=3.7'] -> bzip2[version='>=1.0.6,<2.0a0|>=1.0.8,<2.0a0']
pillow -> pypy3.9[version='>=7.3.11'] -> bzip2[version='>=1.0.6,<2.0a0|>=1.0.8,<2.0a0']
pysocks -> python[version='>=3.8'] -> bzip2[version='>=1.0.6,<2.0a0|>=1.0.8,<2.0a0']
setuptools -> python[version='>=3.7'] -> bzip2[version='>=1.0.6,<2.0a0|>=1.0.8,<2.0a0']
urllib3 -> python[version='>=3.7'] -> bzip2[version='>=1.0.6,<2.0a0|>=1.0.8,<2.0a0']
charset-normalizer -> python[version='>=3.7'] -> bzip2[version='>=1.0.6,<2.0a0|>=1.0.8,<2.0a0']
torchvision -> ffmpeg[version='>=4.2'] -> bzip2[version='>=1.0.6,<2.0a0|>=1.0.8,<2.0a0']
torchaudio -> python[version='>=3.9,<3.10.0a0'] -> bzip2[version='>=1.0.6,<2.0a0|>=1.0.8,<2.0a0']
wheel -> python[version='>=3.7'] -> bzip2[version='>=1.0.6,<2.0a0|>=1.0.8,<2.0a0']
requests -> python[version='>=3.7'] -> bzip2[version='>=1.0.6,<2.0a0|>=1.0.8,<2.0a0']
python_abi -> python=3.11 -> bzip2[version='>=1.0.6,<2.0a0|>=1.0.8,<2.0a0']

Package liblapacke conflicts for:
numpy -> blas=[build=openblas] -> liblapacke[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0',build='4_mkl|10_mkl|12_mkl|13_mkl|18_mkl|19_mkl|8_mkl|11_linux64_mkl|12_linux64_mkl|13_linux64_mkl|14_linux64_mkl|0_openblas|3_openblas|6_openblas|7_openblas|12_openblas|16_openblas|17_openblas|5_openblas|6_openblas|7_openblas|8_openblas|9_openblas|12_linux64_openblas|14_linux64_openblas|15_linux64_openblas|16_linux64_openblas|18_linux64_openblas|17_linux64_openblas|13_linux64_openblas|11_linux64_openblas|10_openblas|15_openblas|14_openblas|13_openblas|11_openblas|10_openblas|9_openblas|8_openblas|5_openblas|4_openblas|2_openblas|16_linux64_mkl|15_linux64_mkl|10_mkl|9_mkl|7_mkl|6_mkl|5_mkl|21_mkl|20_mkl|16_mkl|15_mkl|14_mkl|11_mkl|9_mkl|8_mkl|7_mkl|6_mkl|5_mkl']
blas-devel -> liblapacke[version='3.8.0|3.9.0',build='7_h6e990d7_netlib|0_h86c2bf4_netlib|7_openblas|10_mkl|11_linux64_openblas|11_linux64_mkl|13_linux64_mkl|14_linux64_openblas|14_linux64_mkl|15_linux64_openblas|16_linux64_openblas|18_linux64_openblas|*netlib|17_linux64_openblas|16_linux64_mkl|15_linux64_mkl|13_linux64_openblas|12_linux64_mkl|12_linux64_openblas|10_openblas|9_mkl|9_openblas|8_mkl|8_openblas|7_mkl|5_h92ddd45_netlib']
blas -> liblapacke[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0',build='0_openblas|3_openblas|4_mkl|5_openblas|6_openblas|6_mkl|6_h6e990d7_netlib|7_openblas|8_openblas|8_mkl|9_openblas|9_mkl|10_openblas|10_mkl|10_h86c2bf4_netlib|11_openblas|12_openblas|12_mkl|14_mkl|*netlib|17_openblas|18_mkl|19_mkl|4_h92ddd45_netlib|5_openblas|5_h92ddd45_netlib|6_openblas|6_mkl|7_openblas|10_mkl|11_linux64_openblas|11_linux64_mkl|13_linux64_mkl|14_linux64_openblas|14_linux64_mkl|15_linux64_openblas|16_linux64_openblas|18_linux64_openblas|*netlib|17_linux64_openblas|16_linux64_mkl|15_linux64_mkl|13_linux64_openblas|12_linux64_mkl|12_linux64_openblas|10_openblas|9_mkl|9_openblas|8_mkl|8_openblas|7_mkl|5_mkl|3_h92ddd45_netlib|21_mkl|20_mkl|16_mkl|16_openblas|15_openblas|15_mkl|14_openblas|13_mkl|13_openblas|11_h86c2bf4_netlib|11_mkl|8_h6e990d7_netlib|7_h6e990d7_netlib|7_mkl|5_mkl|5_h6e990d7_netlib|4_h6e990d7_netlib|4_openblas|2_openblas|1_h6e990d7_netlib|0_h6e990d7_netlib']
mkl-devel -> blas=[build=mkl] -> liblapacke[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0',build='4_mkl|6_mkl|8_mkl|10_mkl|12_mkl|14_mkl|18_mkl|19_mkl|8_mkl|10_mkl|11_linux64_mkl|12_linux64_mkl|13_linux64_mkl|14_linux64_mkl|16_linux64_mkl|15_linux64_mkl|9_mkl|7_mkl|6_mkl|5_mkl|21_mkl|20_mkl|16_mkl|15_mkl|13_mkl|11_mkl|9_mkl|7_mkl|5_mkl']
blas-devel -> blas==2.106=mkl -> liblapacke[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0',build='16_openblas|18_mkl|19_mkl|0_openblas|3_openblas|4_mkl|*netlib|5_openblas|6_mkl|6_openblas|5_mkl|4_openblas|2_openblas|0_h6e990d7_netlib|21_mkl|20_mkl|17_openblas|16_mkl|15_openblas|15_mkl|14_mkl|14_openblas']
pytorch -> blas=[build=mkl] -> liblapacke[version='3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.8.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0|3.9.0',build='3_openblas|5_openblas|7_openblas|8_openblas|9_openblas|12_openblas|16_openblas|5_openblas|7_openblas|8_openblas|11_linux64_openblas|15_linux64_openblas|16_linux64_openblas|18_linux64_openblas|4_mkl|6_mkl|8_mkl|10_mkl|12_mkl|14_mkl|18_mkl|19_mkl|8_mkl|10_mkl|11_linux64_mkl|12_linux64_mkl|13_linux64_mkl|14_linux64_mkl|16_linux64_mkl|15_linux64_mkl|9_mkl|7_mkl|6_mkl|5_mkl|21_mkl|20_mkl|16_mkl|15_mkl|13_mkl|11_mkl|9_mkl|7_mkl|5_mkl|17_linux64_openblas|14_linux64_openblas|13_linux64_openblas|12_linux64_openblas|10_openblas|9_openblas|6_openblas|17_openblas|15_openblas|14_openblas|13_openblas|11_openblas|10_openblas|6_openblas|4_openblas|2_openblas|0_openblas']

Package ncurses conflicts for:
urllib3 -> python[version='>=3.7'] -> ncurses[version='5.9.*|5.9|>=6.1,<7.0.0a0|>=6.2,<6.3.0a0|>=6.3,<7.0a0|>=6.4,<7.0a0|>=6.2,<7.0.0a0|>=6.2,<7.0a0|>=6.1,<7.0a0|>=6.0,<7.0a0|6.0.*']
sqlite -> readline[version='>=8.0,<9.0a0'] -> ncurses[version='6.0.*|>=6.0,<7.0a0|>=6.1,<7.0a0']
setuptools -> python[version='>=3.7'] -> ncurses[version='5.9.*|5.9|>=6.1,<7.0.0a0|>=6.2,<6.3.0a0|>=6.3,<7.0a0|>=6.4,<7.0a0|>=6.2,<7.0.0a0|>=6.2,<7.0a0|>=6.1,<7.0a0|>=6.0,<7.0a0|6.0.*']
python=3.7.5 -> ncurses[version='>=6.1,<7.0a0|>=6.2,<7.0.0a0']
pytorch -> python[version='>=3.9,<3.10.0a0'] -> ncurses[version='5.9.*|5.9|>=6.1,<7.0.0a0|>=6.2,<6.3.0a0|>=6.2,<7.0.0a0|>=6.3,<7.0a0|>=6.4,<7.0a0|>=6.2,<7.0a0|>=6.1,<7.0a0|>=6.0,<7.0a0|6.0.*']
sqlite -> ncurses[version='5.9|5.9.*|>=6.1,<7.0.0a0|>=6.2,<7.0.0a0|>=6.3,<7.0a0|>=6.4,<7.0a0|>=6.2,<7.0a0']
charset-normalizer -> python[version='>=3.7'] -> ncurses[version='5.9.*|5.9|>=6.1,<7.0.0a0|>=6.2,<6.3.0a0|>=6.3,<7.0a0|>=6.4,<7.0a0|>=6.2,<7.0.0a0|>=6.2,<7.0a0|>=6.1,<7.0a0|>=6.0,<7.0a0|6.0.*']
wheel -> python[version='>=3.7'] -> ncurses[version='5.9.*|5.9|>=6.1,<7.0.0a0|>=6.2,<6.3.0a0|>=6.3,<7.0a0|>=6.4,<7.0a0|>=6.2,<7.0.0a0|>=6.2,<7.0a0|>=6.1,<7.0a0|>=6.0,<7.0a0|6.0.*']
readline -> ncurses[version='5.9.*|>=6.1,<7.0.0a0|>=6.2,<7.0.0a0|>=6.3,<7.0a0|>=6.2,<7.0a0|>=6.1,<7.0a0|>=6.0,<7.0a0|6.0.*']
typing_extensions -> python[version='>=3.7'] -> ncurses[version='5.9.*|5.9|>=6.1,<7.0.0a0|>=6.2,<6.3.0a0|>=6.3,<7.0a0|>=6.4,<7.0a0|>=6.2,<7.0.0a0|>=6.2,<7.0a0|>=6.1,<7.0a0|>=6.0,<7.0a0|6.0.*']
python=3.7.5 -> readline[version='>=8.0,<9.0a0'] -> ncurses[version='5.9.*|>=6.1,<7.0.0a0|>=6.3,<7.0a0|>=6.2,<7.0a0|>=6.4,<7.0a0|>=6.0,<7.0a0|6.0.*']
requests -> python[version='>=3.7'] -> ncurses[version='5.9.*|5.9|>=6.1,<7.0.0a0|>=6.2,<6.3.0a0|>=6.3,<7.0a0|>=6.4,<7.0a0|>=6.2,<7.0.0a0|>=6.2,<7.0a0|>=6.1,<7.0a0|>=6.0,<7.0a0|6.0.*']
certifi -> python[version='>=3.7'] -> ncurses[version='5.9.*|5.9|>=6.1,<7.0.0a0|>=6.2,<6.3.0a0|>=6.3,<7.0a0|>=6.4,<7.0a0|>=6.2,<7.0.0a0|>=6.2,<7.0a0|>=6.1,<7.0a0|>=6.0,<7.0a0|6.0.*']
python_abi -> python=3.11 -> ncurses[version='5.9.*|5.9|>=6.1,<7.0.0a0|>=6.2,<6.3.0a0|>=6.3,<7.0a0|>=6.4,<7.0a0|>=6.2,<7.0.0a0|>=6.2,<7.0a0|>=6.1,<7.0a0|>=6.0,<7.0a0|6.0.*']
torchaudio -> python[version='>=3.9,<3.10.0a0'] -> ncurses[version='5.9.*|5.9|>=6.1,<7.0.0a0|>=6.2,<7.0.0a0|>=6.3,<7.0a0|>=6.4,<7.0a0|>=6.2,<7.0a0|>=6.1,<7.0a0|>=6.2,<6.3.0a0|>=6.0,<7.0a0|6.0.*']
numpy -> pypy3.9[version='>=7.3.11'] -> ncurses[version='5.9.*|5.9|>=6.1,<7.0.0a0|>=6.2,<6.3.0a0|>=6.2,<7.0.0a0|>=6.3,<7.0a0|>=6.4,<7.0a0|>=6.2,<7.0a0|>=6.1,<7.0a0|>=6.0,<7.0a0|6.0.*']
pillow -> pypy3.9[version='>=7.3.11'] -> ncurses[version='5.9.*|5.9|>=6.1,<7.0.0a0|>=6.2,<7.0.0a0|>=6.3,<7.0a0|>=6.4,<7.0a0|>=6.2,<7.0a0|>=6.1,<7.0a0|>=6.2,<6.3.0a0|>=6.0,<7.0a0|6.0.*']
idna -> python[version='>=3.6'] -> ncurses[version='5.9.*|5.9|>=6.1,<7.0.0a0|>=6.2,<6.3.0a0|>=6.3,<7.0a0|>=6.4,<7.0a0|>=6.2,<7.0.0a0|>=6.2,<7.0a0|>=6.1,<7.0a0|>=6.0,<7.0a0|6.0.*']
torchvision -> python[version='>=3.8,<3.9.0a0'] -> ncurses[version='5.9.*|5.9|>=6.1,<7.0.0a0|>=6.2,<7.0.0a0|>=6.3,<7.0a0|>=6.4,<7.0a0|>=6.2,<7.0a0|>=6.1,<7.0a0|>=6.2,<6.3.0a0|>=6.0,<7.0a0|6.0.*']
pip -> python[version='>=3.7'] -> ncurses[version='5.9.*|5.9|>=6.1,<7.0.0a0|>=6.2,<6.3.0a0|>=6.3,<7.0a0|>=6.4,<7.0a0|>=6.2,<7.0.0a0|>=6.2,<7.0a0|>=6.1,<7.0a0|>=6.0,<7.0a0|6.0.*']
pysocks -> python[version='>=3.8'] -> ncurses[version='5.9.*|5.9|>=6.1,<7.0.0a0|>=6.2,<6.3.0a0|>=6.3,<7.0a0|>=6.4,<7.0a0|>=6.2,<7.0.0a0|>=6.2,<7.0a0|>=6.1,<7.0a0|>=6.0,<7.0a0|6.0.*']

Package libxml2 conflicts for:
tbb -> libhwloc[version='>=2.9.2,<2.9.3.0a0'] -> libxml2[version='>=2.10.3,<2.11.0a0|>=2.11.4,<2.12.0a0|>=2.11.5,<2.12.0a0|>=2.9.14,<2.11.0a0']
ffmpeg -> libxml2[version='>=2.10.3,<2.11.0a0|>=2.10.4,<2.11.0a0|>=2.11.3,<2.12.0a0|>=2.11.4,<2.12.0a0|>=2.11.5,<2.12.0a0|>=2.9.14,<2.11.0a0|>=2.9.13,<2.11.0a0|>=2.9.12,<2.11.0a0']
libhwloc -> libxml2[version='2.9.*|>=2.10.3,<2.11.0a0|>=2.11.4,<2.12.0a0|>=2.11.5,<2.12.0a0|>=2.9.14,<2.11.0a0|>=2.9.12,<2.11.0a0|>=2.9.10,<2.11.0a0|>=2.9.9,<2.11.0a0|>=2.9.8,<2.11.0a0|>=2.10.4,<2.11.0a0|2.9.3']
torchvision -> ffmpeg[version='>=4.2'] -> libxml2[version='>=2.10.3,<2.11.0a0|>=2.10.4,<2.11.0a0|>=2.11.3,<2.12.0a0|>=2.11.4,<2.12.0a0|>=2.11.5,<2.12.0a0|>=2.9.14,<2.11.0a0|>=2.9.13,<2.11.0a0|>=2.9.12,<2.11.0a0']
ffmpeg -> fontconfig[version='>=2.14.1,<3.0a0'] -> libxml2[version='>=2.9.14,<2.10.0a0']

Package python_abi conflicts for:
ffmpeg -> libxml2[version='>=2.11.3,<2.12.0a0'] -> python_abi=3.10[build=*_cp310]
certifi -> python[version='>=3.7'] -> python_abi[version='3.10.*|3.8.*',build='*_graalpy230_310_native|*_graalpy223_38_native']
idna -> python[version='>=3.6'] -> python_abi[version='3.10.*|3.9|3.8|3.8.*|3.7|3.6',build='*_graalpy223_38_native|*_graalpy230_310_native|*_pypy39_pp73|*_pypy38_pp73|*_pypy37_pp73|*_pypy36_pp73']
charset-normalizer -> python[version='>=3.7'] -> python_abi[version='3.10.*|3.9|3.8|3.8.*|3.7|3.6',build='*_graalpy223_38_native|*_graalpy230_310_native|*_pypy39_pp73|*_pypy38_pp73|*_pypy37_pp73|*_pypy36_pp73']
torchvision -> python_abi[version='3.10.*|3.7.*|3.9.*|3.8.*|3.11.*|3.6.*',build='*_cp36m|*_cp311|*_cp310|*_cp38|*_cp39|*_cp37m']
setuptools -> python[version='>=3.7'] -> python_abi[version='2.7.*|3.10.*|3.8.*',build='*_graalpy230_310_native|*_graalpy223_38_native|*_cp27mu']
typing_extensions -> python[version='>=3.7'] -> python_abi[version='3.10.*|3.9|3.8|3.8.*|3.7|3.9.*',build='*_cp39|*_graalpy223_38_native|*_graalpy230_310_native|*_pypy39_pp73|*_pypy38_pp73|*_pypy37_pp73']
pysocks -> python_abi[version='2.7.*|3.10.*|3.7.*|3.8.*|3.9|3.8|3.9.*|3.7|3.6.*|3.6',build='*_cp36m|*_cp39|*_cp310|*_pypy39_pp73|*_cp38|*_cp37m|*_pypy38_pp73|*_pypy37_pp73|*_pypy36_pp73|*_cp27mu']
urllib3 -> python_abi[version='2.7.*|3.8.*|3.6.*|3.6|3.7.*',build='*_pypy36_pp73|*_cp38|*_cp27mu|*_cp36m|*_cp37m']
torchvision -> numpy[version='>=1.11'] -> python_abi[version='2.7.*|3.6|3.7|3.8|3.9|3.8.*|3.10.*',build='*_graalpy230_310_native|*_cp27mu|*_graalpy223_38_native|*_pypy39_pp73|*_pypy38_pp73|*_pypy37_pp73|*_pypy36_pp73']
certifi -> python_abi[version='2.7.*|3.10.*|3.7.*|3.8|3.8.*|3.9.*|3.9|3.7|3.6.*|3.6',build='*_cp36m|*_cp39|*_cp38|*_pypy38_pp73|*_cp37m|*_cp310|*_pypy39_pp73|*_pypy37_pp73|*_pypy36_pp73|*_cp27mu']
urllib3 -> brotli-python[version='>=1.0.9'] -> python_abi[version='3.10.*|3.10.*|3.11.*|3.8|3.9|3.9.*|3.7|3.8.*',build='*_graalpy223_38_native|*_graalpy230_310_native|*_cp310|*_cp39|*_cp311|*_pypy39_pp73|*_pypy38_pp73|*_pypy37_pp73']
requests -> certifi[version='>=2017.4.17'] -> python_abi[version='3.10.*|3.10.*|3.8|3.9.*|3.9|3.7|3.8.*',build='*_graalpy230_310_native|*_cp39|*_cp310|*_pypy38_pp73|*_pypy39_pp73|*_pypy37_pp73|*_graalpy223_38_native']
pillow -> python[version='>=3.8,<3.9.0a0'] -> python_abi[version='3.10.*|3.8.*',build='*_graalpy230_310_native|*_graalpy223_38_native']
requests -> python_abi[version='2.7.*|3.6.*|3.6|3.8.*|3.7.*',build='*_cp36m|*_cp38|*_pypy36_pp73|*_cp37m|*_cp27mu']
wheel -> python[version='>=3.7'] -> python_abi[version='3.10.*|3.10.*|3.9|3.8|3.8.*|3.7|3.6|3.9.*|3.7.*|3.8.*|3.11.*|3.6.*',build='*_cp311|*_cp310|*_cp39|*_graalpy223_38_native|*_graalpy230_310_native|*_pypy39_pp73|*_pypy38_pp73|*_pypy37_pp73|*_pypy36_pp73|*_cp37m|*_cp38|*_cp36m']
pillow -> python_abi[version='3.10.*|3.11.*|3.9|3.8.*|3.8|3.9.*|3.7.*|3.7|3.6.*|3.6',build='*_cp310|*_cp39|*_pypy38_pp73|*_cp311|*_pypy39_pp73|*_cp38|*_cp37m|*_pypy37_pp73|*_cp36m|*_pypy36_pp73']
torchaudio -> numpy[version='>=1.11'] -> python_abi[version='3.10.*|3.10.*|3.11.*|3.9|3.8|3.8.*|3.7.*|3.7|3.6.*|3.6|3.8.*',build='*_graalpy230_310_native|*_cp38|*_cp311|*_pypy39_pp73|*_cp310|*_pypy38_pp73|*_cp37m|*_pypy37_pp73|*_cp36m|*_pypy36_pp73|*_graalpy223_38_native']
pip -> python[version='>=3.7'] -> python_abi[version='3.10.*|3.10.*|3.9|3.8|3.8.*|3.7|3.9.*|3.7.*|3.8.*|3.11.*|3.6.*|3.6',build='*_pypy36_pp73|*_cp311|*_cp38|*_cp310|*_cp37m|*_cp39|*_graalpy223_38_native|*_graalpy230_310_native|*_pypy39_pp73|*_pypy38_pp73|*_pypy37_pp73|*_cp36m']
libhwloc -> libxml2 -> python_abi=3.10[build=*_cp310]
numpy -> python[version='>=3.10,<3.11.0a0'] -> python_abi[version='3.10.*|3.8.*',build='*_graalpy230_310_native|*_graalpy223_38_native']
numpy -> python_abi[version='3.10.*|3.11.*|3.9|3.9.*|3.8|3.8.*|3.7.*|3.7|3.6.*|3.6',build='*_cp38|*_pypy38_pp73|*_cp39|*_cp311|*_pypy39_pp73|*_cp310|*_cp37m|*_pypy37_pp73|*_cp36m|*_pypy36_pp73']
pytorch -> python_abi[version='3.10.*|3.9.*|3.8.*|3.11.*|3.7.*|3.6.*',build='*_cp36m|*_cp311|*_cp38|*_cp39|*_cp310|*_cp37m']
pysocks -> python[version='>=3.8'] -> python_abi[version='3.10.*|3.8.*',build='*_graalpy230_310_native|*_graalpy223_38_native']
zstd -> lz4 -> python_abi[version='3.10.*|3.11.*|3.9|3.8.*|3.8|3.9.*|3.7.*|3.7|3.6|3.6.*',build='*_cp39|*_pypy39_pp73|*_cp311|*_cp310|*_cp38|*_pypy38_pp73|*_cp37m|*_pypy37_pp73|*_pypy36_pp73|*_cp36m']
setuptools -> python_abi[version='3.10.*|3.7.*|3.9.*|3.9|3.8.*|3.8|3.7|3.11.*|3.6.*|3.6',build='*_pypy36_pp73|*_cp311|*_pypy39_pp73|*_cp310|*_cp39|*_cp37m|*_cp38|*_pypy38_pp73|*_pypy37_pp73|*_cp36m']
pytorch -> python[version='>=3.9,<3.10.0a0'] -> python_abi[version='2.7.*|3.6|3.7|3.8|3.9|3.10.*|3.8.*',build='*_graalpy223_38_native|*_graalpy230_310_native|*_pypy39_pp73|*_pypy38_pp73|*_pypy37_pp73|*_pypy36_pp73|*_cp27mu']
typing_extensions -> python_abi[version='2.7.*|3.6.*|3.6|3.8.*|3.7.*',build='*_cp36m|*_cp38|*_pypy36_pp73|*_cp37m|*_cp27mu']
libxml2 -> python_abi=3.10[build=*_cp310]
torchaudio -> python_abi=3.9[build=*_cp39]

Package openjpeg conflicts for:
pillow -> openjpeg[version='>=2.3.0,<3.0a0|>=2.4.0,<3.0.0a0|>=2.5.0,<2.6.0a0|>=2.5.0,<3.0a0|>=2.4.0,<3.0a0']
torchvision -> pillow[version='>=5.3.0,!=8.3.*'] -> openjpeg[version='>=2.3.0,<3.0a0|>=2.4.0,<3.0.0a0|>=2.5.0,<2.6.0a0|>=2.5.0,<3.0a0|>=2.4.0,<3.0a0']

Package libcublas conflicts for:
pytorch-cuda=11.8 -> cuda-libraries[version='>=11.8,<12.0'] -> libcublas[version='>=11.11.3.6']
cuda-libraries -> libcusolver=11.4.2.57 -> libcublas[version='>=12.0.1.189,<12.1.0a0']
pytorch-cuda=11.8 -> libcublas[version='>=11.11.3.6,<12.0.1.189']
pytorch -> pytorch-cuda[version='>=11.8,<11.9'] -> libcublas[version='>=11.10.1.25,<11.11.3.6|>=11.11.3.6,<12.0.1.189|>=12.0.1.189,<13.0a0']
cuda-libraries -> libcublas[version='12.0.1.189.*|>=11.11.3.6']
cuda-runtime -> cuda-libraries=12.0.0 -> libcublas[version='12.0.1.189.*|>=11.11.3.6']
libcusolver -> libcublas[version='>=12.0.1.189,<12.1.0a0']
torchaudio -> pytorch-cuda=11.8 -> libcublas[version='>=11.10.1.25,<11.11.3.6|>=11.11.3.6,<12.0.1.189']
torchvision -> pytorch-cuda=11.8 -> libcublas[version='>=11.10.1.25,<11.11.3.6|>=11.11.3.6,<12.0.1.189']

Package mkl conflicts for:
blas -> mkl
torchvision -> numpy[version='>=1.11'] -> mkl[version='2019.*|2020.*|2021.*|2021.*.*|2023.*.*|>=2018|>=2018.0.0,<2019.0a0|>=2018.0.1,<2019.0a0|>=2018.0.2,<2019.0a0|>=2018.0.3,<2019.0a0|>=2019.1,<2021.0a0|>=2019.3,<2021.0a0|>=2019.4,<2021.0a0|>=2021.2.0,<2022.0a0|>=2021.3.0,<2022.0a0|>=2021.4.0,<2022.0a0|>=2023.1.0,<2024.0a0|>=2019.4,<2020.0a0|>=2022.2.1,<2023.0a0|>=2022.1.0,<2023.0a0|2022.*|>=2022.0.1,<2023.0a0|>=2020.4,<2021.0a0|>=2020.2,<2021.0a0']
blas-devel -> mkl-devel=2022.1 -> mkl[version='2017.0.4|2018.0.0|2018.0.1|2018.0.2|2018.0.3|2019.0|2019.0|2019.1|2019.3|2019.4|2019.5|2020.0|2020.1|2020.1|2020.2|2020.2|2020.4|2021.1.1|2021.2.0|2021.3.0|2021.4.0|2022.0.1|2022.0.1|2022.1.0|2023.2.0|2023.2.0|2023.1.0|2023.1.0|2023.0.0|2023.0.0|2022.2.1|2022.2.1|2023.1.0|2023.1.0|2023.0.0|2021.4.0|2021.3.0|2021.2.0',build='h4c4d0af_0|hb491cac_4|h19d6760_4|199|h06a4308_640|h213fc3f_46343|256|ha770c72_256|h726a3e6_304|h726a3e6_389|h84fe81f_16996|h84fe81f_16997|h84fe81f_25396|h84fe81f_26648|h84fe81f_46349|h84fe81f_33|h06a4308_117|h8d4b97c_803|h84fe81f_915|hc2b9512_224|hc2b9512_223|h84fe81f_49572|h84fe81f_48680|h8d4b97c_729|h726a3e6_557|h726a3e6_79|219|217|166|281|h6d00ec8_46342|h6d00ec8_25399|h06a4308_520|h06a4308_296|243|144|118|117|1|1']
pytorch -> mkl[version='2019.*|2020.*|2021.*.*|2021.*|2022.*|>=2018|>=2022.2.1,<2023.0a0|>=2022.1.0,<2023.0a0|>=2022.0.1,<2023.0a0|>=2021.4.0,<2022.0a0|>=2021.3.0,<2022.0a0|>=2020.4,<2021.0a0|2023.*.*|>=2023.1.0,<2024.0a0|>=2020.2,<2021.0a0|>=2019.4,<2021.0a0|>=2019.1,<2021.0a0|>=2018.0.3,<2019.0a0|>=2018.0.2,<2019.0a0']
pytorch -> blas=[build=mkl] -> mkl[version='2019.1.*|2023.*|>=2018.0.0,<2019.0a0|>=2018.0.1,<2019.0a0|>=2019.3,<2021.0a0|>=2021.2.0,<2022.0a0|>=2019.4,<2020.0a0|>=2020.0,<2021.0a0|>=2019.0,<2020.0a0|>=2019.3,<2020.0a0']
mkl-devel -> mkl[version='2017.0.4|2018.0.0|2018.0.1|2018.0.2|2018.0.3|2019.0|2019.0|2019.1|2019.3|2019.4|2019.5|2020.0|2020.1|2020.1|2020.2|2020.2|2020.4|2021.1.1|2021.2.0|2021.3.0|2021.4.0|2022.0.1|2022.1.0|2022.2.1|2022.2.1|2023.0.0|2023.0.0|2023.1.0|2023.1.0|2023.2.0|2023.1.0|2023.1.0|2023.0.0|2022.1.0|2022.1.0|2022.0.1|2021.4.0|2021.3.0|2021.2.0',build='h4c4d0af_0|hb491cac_4|199|h06a4308_296|h06a4308_640|hc2b9512_224|h213fc3f_46343|ha770c72_256|h726a3e6_304|h8d4b97c_729|h8d4b97c_803|h84fe81f_915|h84fe81f_16996|h84fe81f_16997|h84fe81f_25396|h84fe81f_26648|h84fe81f_49572|h84fe81f_33|h84fe81f_48680|h84fe81f_46349|h726a3e6_557|h726a3e6_389|h726a3e6_79|256|219|217|166|281|h6d00ec8_46342|h6d00ec8_25399|hc2b9512_223|h06a4308_117|h06a4308_520|243|144|118|117|1|1|h19d6760_4']
libcblas -> libblas==3.9.0=16_linux64_mkl -> mkl[version='2019.1.*|>=2019.0,<2020.0a0|>=2020.0,<2021.0a0|>=2020.4,<2021.0a0|>=2021.2.0,<2022.0a0|>=2021.3.0,<2022.0a0|>=2021.4.0,<2022.0a0|>=2022.0.1,<2023.0a0|>=2022.1.0,<2023.0a0']
torchaudio -> numpy[version='>=1.11'] -> mkl[version='2020.*|2021.*|2021.*.*|2023.*.*|>=2018|>=2018.0.0,<2019.0a0|>=2018.0.1,<2019.0a0|>=2018.0.2,<2019.0a0|>=2018.0.3,<2019.0a0|>=2019.1,<2021.0a0|>=2019.3,<2021.0a0|>=2019.4,<2021.0a0|>=2021.2.0,<2022.0a0|>=2021.3.0,<2022.0a0|>=2021.4.0,<2022.0a0|>=2023.1.0,<2024.0a0|>=2019.4,<2020.0a0|>=2022.2.1,<2023.0a0|>=2022.1.0,<2023.0a0|2022.*|>=2022.0.1,<2023.0a0|>=2020.4,<2021.0a0|>=2020.2,<2021.0a0']
liblapack -> libblas==3.9.0=16_linux64_mkl -> mkl[version='2019.1.*|>=2019.0,<2020.0a0|>=2020.0,<2021.0a0|>=2020.4,<2021.0a0|>=2021.2.0,<2022.0a0|>=2021.3.0,<2022.0a0|>=2021.4.0,<2022.0a0|>=2022.0.1,<2023.0a0|>=2022.1.0,<2023.0a0']
liblapacke -> libblas==3.9.0=16_linux64_mkl -> mkl[version='2019.1.*|>=2019.0,<2020.0a0|>=2020.0,<2021.0a0|>=2020.4,<2021.0a0|>=2021.2.0,<2022.0a0|>=2021.3.0,<2022.0a0|>=2021.4.0,<2022.0a0|>=2022.0.1,<2023.0a0|>=2022.1.0,<2023.0a0']
numpy -> libblas[version='>=3.9.0,<4.0a0'] -> mkl[version='2019.1.*|>=2019.0,<2020.0a0|>=2020.0,<2021.0a0|>=2020.4,<2021.0a0|>=2022.0.1,<2023.0a0|>=2022.1.0,<2023.0a0|>=2020.2,<2021.0a0|>=2022.2.1,<2023.0a0|>=2019.3,<2020.0a0|>=2019.1,<2020.0a0|>=2020.1,<2021.0a0']
libblas -> mkl[version='2019.1.*|>=2019.0,<2020.0a0|>=2020.0,<2021.0a0|>=2020.4,<2021.0a0|>=2021.2.0,<2022.0a0|>=2021.3.0,<2022.0a0|>=2021.4.0,<2022.0a0|>=2022.0.1,<2023.0a0|>=2022.1.0,<2023.0a0']
blas-devel -> mkl[version='>=2020.4,<2021.0a0|>=2021.2.0,<2022.0a0|>=2021.3.0,<2022.0a0|>=2021.4.0,<2022.0a0|>=2022.0.1,<2023.0a0|>=2022.1.0,<2023.0a0']
blas -> blas-devel==3.9.0=16_linux64_mkl -> mkl[version='2019.1.*|>=2019.0,<2020.0a0|>=2020.0,<2021.0a0|>=2020.4,<2021.0a0|>=2021.2.0,<2022.0a0|>=2021.3.0,<2022.0a0|>=2021.4.0,<2022.0a0|>=2022.0.1,<2023.0a0|>=2022.1.0,<2023.0a0']
numpy -> mkl[version='>=2018.0.0,<2019.0a0|>=2018.0.1,<2019.0a0|>=2018.0.2,<2019.0a0|>=2018.0.3,<2019.0a0|>=2019.1,<2021.0a0|>=2019.3,<2021.0a0|>=2019.4,<2021.0a0|>=2021.2.0,<2022.0a0|>=2021.3.0,<2022.0a0|>=2021.4.0,<2022.0a0|>=2023.1.0,<2024.0a0|>=2019.4,<2020.0a0']

Package libiconv conflicts for:
ffmpeg -> libiconv[version='1.15|1.15.*|>=1.15,<2.0.0a0|>=1.16,<2.0.0a0']
libhwloc -> libxml2[version='>=2.11.5,<2.12.0a0'] -> libiconv[version='1.15|>=1.15,<2.0.0a0|>=1.16,<2.0.0a0|>=1.17,<2.0.0a0|>=1.17,<2.0a0']
gnutls -> libidn11 -> libiconv[version='>=1.15,<2.0.0a0']
torchvision -> ffmpeg[version='>=4.2'] -> libiconv[version='>=1.15,<2.0.0a0|>=1.16,<2.0.0a0']
libxml2 -> libiconv[version='1.15|>=1.15,<2.0.0a0|>=1.16,<2.0.0a0|>=1.17,<2.0.0a0|>=1.17,<2.0a0']
ffmpeg -> libxml2[version='>=2.11.5,<2.12.0a0'] -> libiconv[version='>=1.17,<2.0.0a0|>=1.17,<2.0a0']

Package cudatoolkit conflicts for:
tbb -> libhwloc[version='>=2.9.2,<2.9.3.0a0'] -> cudatoolkit[version='10.2|10.2.*|11.0|11.0.*|11.1|11.1.*|>=11.2,<12']
libhwloc -> cudatoolkit[version='10.2|10.2.*|11.0|11.0.*|11.1|11.1.*|>=11.2,<12']

Package libtiff conflicts for:
pillow -> libtiff[version='4.*|4.0.*|>=4.0.10,<4.4.0a0|>=4.1.0,<4.4.0a0|>=4.2.0,<4.4.0a0|>=4.3.0,<4.4.0a0|>=4.3.0,<4.5.0a0|>=4.4.0,<4.5.0a0|>=4.5.0,<4.6.0a0|>=4.5.1,<4.6.0a0|>=4.0.9,<4.4.0a0|>=4.0.8,<4.0.10|>=4.0.3,<4.0.8|4.0.6|>=4.2.0,<5.0a0|>=4.1.0,<5.0a0|>=4.0.10,<5.0a0|>=4.0.9,<5.0a0|>=4.0.8,<5.0a0']
torchvision -> pillow[version='>=5.3.0,!=8.3.*'] -> libtiff[version='4.0.*|>=4.0.10,<4.4.0a0|>=4.1.0,<4.4.0a0|>=4.2.0,<4.4.0a0|>=4.3.0,<4.4.0a0|>=4.3.0,<4.5.0a0|>=4.4.0,<4.5.0a0|>=4.5.0,<4.6.0a0|>=4.5.1,<4.6.0a0|>=4.0.9,<4.4.0a0|>=4.2.0,<5.0a0|>=4.1.0,<5.0a0|>=4.0.10,<5.0a0|>=4.0.9,<5.0a0|>=4.0.8,<4.0.10|>=4.0.3,<4.0.8|>=4.0.8,<5.0a0']
pillow -> lcms2[version='>=2.15,<3.0a0'] -> libtiff[version='>=4.0.10,<4.5.0a0|>=4.1.0,<4.5.0a0|>=4.2.0,<4.5.0a0|>=4.6.0,<4.7.0a0|>=4.0.9,<4.5.0a0']
openjpeg -> libtiff[version='4.*|4.0.*|>=4.0.10,<4.5.0a0|>=4.1.0,<4.5.0a0|>=4.2.0,<4.5.0a0|>=4.3.0,<4.5.0a0|>=4.4.0,<4.5.0a0|>=4.5.0,<4.6.0a0|>=4.0.9,<4.5.0a0|>=4.0.8,<4.0.10|>=4.0.3,<4.0.8|4.0.6|>=4.1.0,<5.0a0|>=4.0.9,<5.0a0|>=4.0.8,<5.0a0']
lcms2 -> libtiff[version='>=4.0.10,<4.5.0a0|>=4.1.0,<4.5.0a0|>=4.2.0,<4.5.0a0|>=4.4.0,<4.5.0a0|>=4.5.0,<4.6.0a0|>=4.6.0,<4.7.0a0|>=4.1.0,<5.0a0']

Package libgfortran-ng conflicts for:
libcblas -> libgfortran-ng[version='>=7,<8.0a0']
blas-devel -> liblapack==3.9.0[build=*netlib] -> libgfortran-ng[version='>=4.9|>=7,<8.0a0']
torchaudio -> numpy[version='>=1.11'] -> libgfortran-ng[version='>=4.9|>=7,<8.0a0|>=7.2.0,<8.0a0']
torchvision -> numpy[version='>=1.11'] -> libgfortran-ng[version='>=4.9|>=7,<8.0a0|>=7.2.0,<8.0a0']
numpy -> libgfortran-ng[version='>=4.9|>=7,<8.0a0|>=7.2.0,<8.0a0']
libblas -> libgfortran-ng[version='>=7,<8.0a0']
mkl-devel -> blas=[build=mkl] -> libgfortran-ng[version='>=7,<8.0a0']
blas -> openblas -> libgfortran-ng[version='>=4.9']
liblapack -> libgfortran-ng[version='>=7,<8.0a0']
numpy -> libopenblas[version='>=0.3.2,<0.3.3.0a0'] -> libgfortran-ng[version='>=8,<9.0a0']
liblapacke -> libgfortran-ng[version='>=7,<8.0a0']
pytorch -> blas=[build=mkl] -> libgfortran-ng[version='>=4.9|>=7,<8.0a0|>=7.2.0,<8.0a0|>=8,<9.0a0']
blas -> libgfortran-ng[version='>=7,<8.0a0']

Package libffi conflicts for:
certifi -> python[version='>=3.7'] -> libffi[version='3.2.*|>=3.2.1,<3.3.0a0|>=3.3,<3.4.0a0|>=3.4,<4.0a0|>=3.4.2,<3.5.0a0|>=3.4,<3.5|>=3.2.1,<3.3a0']
python=3.7.5 -> libffi[version='>=3.2.1,<3.3a0|>=3.3,<3.4.0a0']
pillow -> pypy3.9[version='>=7.3.11'] -> libffi[version='3.2.*|>=3.2.1,<3.3.0a0|>=3.3,<3.4.0a0|>=3.4,<4.0a0|>=3.4.2,<3.5.0a0|>=3.4,<3.5|>=3.2.1,<3.3a0']
requests -> python[version='>=3.7'] -> libffi[version='3.2.*|>=3.2.1,<3.3.0a0|>=3.3,<3.4.0a0|>=3.4,<4.0a0|>=3.4.2,<3.5.0a0|>=3.4,<3.5|>=3.2.1,<3.3a0']
torchvision -> python[version='>=3.8,<3.9.0a0'] -> libffi[version='3.2.*|>=3.2.1,<3.3.0a0|>=3.3,<3.4.0a0|>=3.4,<4.0a0|>=3.4.2,<3.5.0a0|>=3.4,<3.5|>=3.2.1,<3.3a0']
torchaudio -> python[version='>=3.9,<3.10.0a0'] -> libffi[version='3.2.*|>=3.2.1,<3.3.0a0|>=3.3,<3.4.0a0|>=3.4,<4.0a0|>=3.4.2,<3.5.0a0|>=3.4,<3.5|>=3.2.1,<3.3a0']
pytorch -> python[version='>=3.9,<3.10.0a0'] -> libffi[version='3.2.*|>=3.2.1,<3.3.0a0|>=3.3,<3.4.0a0|>=3.4,<4.0a0|>=3.4.2,<3.5.0a0|>=3.4,<3.5|>=3.2.1,<3.3a0|<3.3.0.a0|>=3.3']
python_abi -> python=3.11 -> libffi[version='3.2.*|>=3.2.1,<3.3.0a0|>=3.3,<3.4.0a0|>=3.4,<3.5|>=3.4,<4.0a0|>=3.4.2,<3.5.0a0|>=3.2.1,<3.3a0']
pip -> python[version='>=3.7'] -> libffi[version='3.2.*|>=3.2.1,<3.3.0a0|>=3.3,<3.4.0a0|>=3.4,<4.0a0|>=3.4.2,<3.5.0a0|>=3.4,<3.5|>=3.2.1,<3.3a0']
urllib3 -> python[version='>=3.7'] -> libffi[version='3.2.*|>=3.2.1,<3.3.0a0|>=3.3,<3.4.0a0|>=3.4,<4.0a0|>=3.4.2,<3.5.0a0|>=3.4,<3.5|>=3.2.1,<3.3a0']
numpy -> pypy3.9[version='>=7.3.11'] -> libffi[version='3.2.*|>=3.2.1,<3.3.0a0|>=3.3,<3.4.0a0|>=3.4,<4.0a0|>=3.4.2,<3.5.0a0|>=3.4,<3.5|>=3.2.1,<3.3a0']
gnutls -> p11-kit[version='>=0.24.1,<0.25.0a0'] -> libffi[version='>=3.2.1,<3.3.0a0|>=3.3,<3.4.0a0|>=3.4.2,<3.5.0a0']
mkl -> intel-openmp=2023 -> libffi[version='>=3.4,<3.5|>=3.4,<4.0a0']
idna -> python[version='>=3.6'] -> libffi[version='3.2.*|>=3.2.1,<3.3.0a0|>=3.3,<3.4.0a0|>=3.4,<4.0a0|>=3.4.2,<3.5.0a0|>=3.4,<3.5|>=3.2.1,<3.3a0']
wheel -> python[version='>=3.7'] -> libffi[version='3.2.*|>=3.2.1,<3.3.0a0|>=3.3,<3.4.0a0|>=3.4,<4.0a0|>=3.4.2,<3.5.0a0|>=3.4,<3.5|>=3.2.1,<3.3a0']
charset-normalizer -> python[version='>=3.7'] -> libffi[version='3.2.*|>=3.2.1,<3.3.0a0|>=3.3,<3.4.0a0|>=3.4,<4.0a0|>=3.4.2,<3.5.0a0|>=3.4,<3.5|>=3.2.1,<3.3a0']
pysocks -> python[version='>=3.8'] -> libffi[version='3.2.*|>=3.2.1,<3.3.0a0|>=3.3,<3.4.0a0|>=3.4,<4.0a0|>=3.4.2,<3.5.0a0|>=3.4,<3.5|>=3.2.1,<3.3a0']
typing_extensions -> python[version='>=3.7'] -> libffi[version='3.2.*|>=3.2.1,<3.3.0a0|>=3.3,<3.4.0a0|>=3.4,<4.0a0|>=3.4.2,<3.5.0a0|>=3.4,<3.5|>=3.2.1,<3.3a0']
setuptools -> python[version='>=3.7'] -> libffi[version='3.2.*|>=3.2.1,<3.3.0a0|>=3.3,<3.4.0a0|>=3.4,<4.0a0|>=3.4.2,<3.5.0a0|>=3.4,<3.5|>=3.2.1,<3.3a0']

Package libgomp conflicts for:
libgcc-ng -> _openmp_mutex[version='>=4.5'] -> libgomp[version='>=7.3.0|>=7.5.0']
pytorch -> _openmp_mutex[version='>=4.5'] -> libgomp[version='>=7.3.0|>=7.5.0']
mkl -> _openmp_mutex[version='>=4.5'] -> libgomp[version='>=7.3.0|>=7.5.0']
_openmp_mutex -> libgomp[version='>=7.3.0|>=7.5.0']
blas -> _openmp_mutex[version='>=4.5'] -> libgomp[version='>=7.3.0|>=7.5.0']

Package xorg-libx11 conflicts for:
ffmpeg -> libva[version='>=2.19.0,<3.0a0'] -> xorg-libx11[version='>=1.8.4,<2.0a0|>=1.8.6,<2.0a0']
certifi -> pypy3.8[version='>=7.3.9'] -> xorg-libx11[version='>=1.8.4,<2.0a0|>=1.8.6,<2.0a0']
numpy -> pypy3.9[version='>=7.3.11'] -> xorg-libx11[version='>=1.8.4,<2.0a0|>=1.8.6,<2.0a0']
python_abi -> pypy3.9=7.3 -> xorg-libx11[version='>=1.8.4,<2.0a0|>=1.8.6,<2.0a0']
setuptools -> pypy3.9[version='>=7.3.9'] -> xorg-libx11[version='>=1.8.4,<2.0a0|>=1.8.6,<2.0a0']
pysocks -> pypy3.9[version='>=7.3.8'] -> xorg-libx11[version='>=1.8.4,<2.0a0|>=1.8.6,<2.0a0']
pillow -> pypy3.9[version='>=7.3.11'] -> xorg-libx11[version='>=1.8.4,<2.0a0|>=1.8.6,<2.0a0']

Package libnpp conflicts for:
pytorch-cuda=11.8 -> cuda-libraries[version='>=11.8,<12.0'] -> libnpp[version='>=11.8.0.86']
cuda-runtime -> cuda-libraries=12.0.0 -> libnpp[version='12.0.0.30.*|>=11.8.0.86']
pytorch-cuda=11.8 -> libnpp[version='>=11.8.0.86,<12.0.0.30']
torchaudio -> pytorch-cuda=11.8 -> libnpp[version='>=11.7.3.21,<11.8.0.86|>=11.8.0.86,<12.0.0.30']
torchvision -> pytorch-cuda=11.8 -> libnpp[version='>=11.7.3.21,<11.8.0.86|>=11.8.0.86,<12.0.0.30']
cuda-libraries -> libnpp[version='12.0.0.30.*|>=11.8.0.86']
pytorch -> pytorch-cuda[version='>=11.8,<11.9'] -> libnpp[version='>=11.7.3.21,<11.8.0.86|>=11.8.0.86,<12.0.0.30']

Package rocm-smi conflicts for:
tbb -> libhwloc[version='>=2.9.2,<2.9.3.0a0'] -> rocm-smi[version='>=5.6.0,<5.7.0a0']
libhwloc -> rocm-smi[version='>=5.6.0,<5.7.0a0|>=5.6.1,<5.7.0a0']

Package libgfortran conflicts for:
numpy -> libgfortran[version='>=3.0']
torchaudio -> numpy[version='>=1.11'] -> libgfortran[version='>=3.0']
numpy -> openblas[version='>=0.2.20,<0.2.21.0a0'] -> libgfortran
pytorch -> numpy[version='>=1.11'] -> libgfortran[version='>=3.0']
torchvision -> numpy[version='>=1.11'] -> libgfortran[version='>=3.0']
blas -> openblas -> libgfortran[version='>=3.0']
blas-devel -> openblas -> libgfortran[version='>=3.0']

Package libsqlite conflicts for:
pillow -> pypy3.9[version='>=7.3.11'] -> libsqlite[version='>=3.39.2,<4.0a0|>=3.39.4,<4.0a0|>=3.40.0,<4.0a0|>=3.41.2,<4.0a0|>=3.43.0,<4.0a0|>=3.42.0,<4.0a0']
setuptools -> python[version='>=3.7'] -> libsqlite[version='>=3.39.2,<4.0a0|>=3.39.4,<4.0a0|>=3.40.0,<4.0a0|>=3.42.0,<4.0a0|>=3.43.0,<4.0a0|>=3.41.2,<4.0a0']
idna -> python[version='>=3.6'] -> libsqlite[version='>=3.39.2,<4.0a0|>=3.39.4,<4.0a0|>=3.40.0,<4.0a0|>=3.42.0,<4.0a0|>=3.43.0,<4.0a0|>=3.41.2,<4.0a0']
sqlite -> libsqlite[version='3.39.2|3.39.3|3.39.4|3.40.0|3.40.0|3.41.2|3.42.0|3.43.0',build='h753d276_0|h753d276_0|h753d276_0|h2797004_0|h2797004_1|h753d276_1|h753d276_1']
torchaudio -> python[version='>=3.9,<3.10.0a0'] -> libsqlite[version='>=3.39.2,<4.0a0|>=3.40.0,<4.0a0|>=3.42.0,<4.0a0|>=3.43.0,<4.0a0|>=3.41.2,<4.0a0|>=3.39.4,<4.0a0']
pip -> python[version='>=3.7'] -> libsqlite[version='>=3.39.2,<4.0a0|>=3.39.4,<4.0a0|>=3.40.0,<4.0a0|>=3.42.0,<4.0a0|>=3.43.0,<4.0a0|>=3.41.2,<4.0a0']
torchvision -> python[version='>=3.8,<3.9.0a0'] -> libsqlite[version='>=3.39.2,<4.0a0|>=3.39.4,<4.0a0|>=3.40.0,<4.0a0|>=3.42.0,<4.0a0|>=3.43.0,<4.0a0|>=3.41.2,<4.0a0']
urllib3 -> python[version='>=3.7'] -> libsqlite[version='>=3.39.2,<4.0a0|>=3.39.4,<4.0a0|>=3.40.0,<4.0a0|>=3.42.0,<4.0a0|>=3.43.0,<4.0a0|>=3.41.2,<4.0a0']
pytorch -> python[version='>=3.9,<3.10.0a0'] -> libsqlite[version='>=3.39.2,<4.0a0|>=3.40.0,<4.0a0|>=3.42.0,<4.0a0|>=3.43.0,<4.0a0|>=3.41.2,<4.0a0|>=3.39.4,<4.0a0']
charset-normalizer -> python[version='>=3.7'] -> libsqlite[version='>=3.39.2,<4.0a0|>=3.39.4,<4.0a0|>=3.40.0,<4.0a0|>=3.42.0,<4.0a0|>=3.43.0,<4.0a0|>=3.41.2,<4.0a0']
wheel -> python[version='>=3.7'] -> libsqlite[version='>=3.39.2,<4.0a0|>=3.39.4,<4.0a0|>=3.40.0,<4.0a0|>=3.42.0,<4.0a0|>=3.43.0,<4.0a0|>=3.41.2,<4.0a0']
requests -> python[version='>=3.7'] -> libsqlite[version='>=3.39.2,<4.0a0|>=3.39.4,<4.0a0|>=3.40.0,<4.0a0|>=3.42.0,<4.0a0|>=3.43.0,<4.0a0|>=3.41.2,<4.0a0']
certifi -> python[version='>=3.7'] -> libsqlite[version='>=3.39.2,<4.0a0|>=3.39.4,<4.0a0|>=3.40.0,<4.0a0|>=3.42.0,<4.0a0|>=3.43.0,<4.0a0|>=3.41.2,<4.0a0']
numpy -> pypy3.9[version='>=7.3.11'] -> libsqlite[version='>=3.39.2,<4.0a0|>=3.39.4,<4.0a0|>=3.40.0,<4.0a0|>=3.41.2,<4.0a0|>=3.43.0,<4.0a0|>=3.42.0,<4.0a0']
pysocks -> python[version='>=3.8'] -> libsqlite[version='>=3.39.2,<4.0a0|>=3.39.4,<4.0a0|>=3.40.0,<4.0a0|>=3.42.0,<4.0a0|>=3.43.0,<4.0a0|>=3.41.2,<4.0a0']
python=3.7.5 -> sqlite[version='>=3.34.0,<4.0a0'] -> libsqlite[version='3.39.2|3.39.3|3.39.4|3.40.0|3.40.0|3.41.2|3.42.0|3.43.0',build='h753d276_0|h753d276_0|h753d276_0|h2797004_0|h2797004_1|h753d276_1|h753d276_1']
python_abi -> python=3.11 -> libsqlite[version='>=3.39.2,<4.0a0|>=3.39.4,<4.0a0|>=3.40.0,<4.0a0|>=3.42.0,<4.0a0|>=3.43.0,<4.0a0|>=3.41.2,<4.0a0']
typing_extensions -> python[version='>=3.7'] -> libsqlite[version='>=3.39.2,<4.0a0|>=3.39.4,<4.0a0|>=3.40.0,<4.0a0|>=3.42.0,<4.0a0|>=3.43.0,<4.0a0|>=3.41.2,<4.0a0']

Package gnutls conflicts for:
ffmpeg -> gnutls[version='3.5.*|>=3.5.19,<3.6.0a0|>=3.6.13,<3.7.0a0|>=3.6.5,<3.7.0a0|>=3.7.8,<3.8.0a0|>=3.7.7,<3.8.0a0|>=3.7.6,<3.8.0a0']
torchvision -> ffmpeg[version='>=4.2'] -> gnutls[version='>=3.6.13,<3.7.0a0|>=3.6.5,<3.7.0a0|>=3.7.8,<3.8.0a0|>=3.7.7,<3.8.0a0|>=3.7.6,<3.8.0a0']

Package sqlite conflicts for:
pip -> python[version='>=3.7'] -> sqlite[version='3.13.*|3.20.*|>=3.24.0,<4.0a0|>=3.25.1,<4.0a0|>=3.25.2,<4.0a0|>=3.25.3,<4.0a0|>=3.26.0,<4.0a0|>=3.28.0,<4.0a0|>=3.30.1,<4.0a0|>=3.32.3,<4.0a0|>=3.33.0,<4.0a0|>=3.34.0,<4.0a0|>=3.35.5,<4.0a0|>=3.36.0,<4.0a0|>=3.37.0,<4.0a0|>=3.37.1,<4.0a0|>=3.38.5,<4.0a0|>=3.41.2,<4.0a0|>=3.41.1,<4.0a0|>=3.40.1,<4.0a0|>=3.40.0,<4.0a0|>=3.39.3,<4.0a0|>=3.38.0,<4.0a0|>=3.37.2,<4.0a0|>=3.39.2,<4.0a0|>=3.38.3,<4.0a0|>=3.38.2,<4.0a0|>=3.35.4,<4.0a0|>=3.31.1,<4.0a0|>=3.30.0,<4.0a0|>=3.29.0,<4.0a0|>=3.27.2,<4.0a0|>=3.23.1,<4.0a0|>=3.22.0,<4.0a0|>=3.20.1,<4.0a0|3.9.*']
torchvision -> python[version='>=3.8,<3.9.0a0'] -> sqlite[version='3.13.*|3.20.*|>=3.24.0,<4.0a0|>=3.25.1,<4.0a0|>=3.25.2,<4.0a0|>=3.25.3,<4.0a0|>=3.26.0,<4.0a0|>=3.28.0,<4.0a0|>=3.30.0,<4.0a0|>=3.30.1,<4.0a0|>=3.32.3,<4.0a0|>=3.33.0,<4.0a0|>=3.34.0,<4.0a0|>=3.35.5,<4.0a0|>=3.36.0,<4.0a0|>=3.37.0,<4.0a0|>=3.37.1,<4.0a0|>=3.41.2,<4.0a0|>=3.40.1,<4.0a0|>=3.40.0,<4.0a0|>=3.39.3,<4.0a0|>=3.38.0,<4.0a0|>=3.35.4,<4.0a0|>=3.31.1,<4.0a0|>=3.38.5,<4.0a0|>=3.39.2,<4.0a0|>=3.38.3,<4.0a0|>=3.38.2,<4.0a0|>=3.41.1,<4.0a0|>=3.37.2,<4.0a0|>=3.29.0,<4.0a0|>=3.27.2,<4.0a0|>=3.23.1,<4.0a0|>=3.22.0,<4.0a0|>=3.20.1,<4.0a0|3.9.*']
python=3.7.5 -> sqlite[version='>=3.30.1,<4.0a0|>=3.34.0,<4.0a0']
charset-normalizer -> python[version='>=3.7'] -> sqlite[version='3.13.*|3.20.*|>=3.24.0,<4.0a0|>=3.25.1,<4.0a0|>=3.25.2,<4.0a0|>=3.25.3,<4.0a0|>=3.26.0,<4.0a0|>=3.28.0,<4.0a0|>=3.30.1,<4.0a0|>=3.32.3,<4.0a0|>=3.33.0,<4.0a0|>=3.34.0,<4.0a0|>=3.35.5,<4.0a0|>=3.36.0,<4.0a0|>=3.37.0,<4.0a0|>=3.37.1,<4.0a0|>=3.38.5,<4.0a0|>=3.41.2,<4.0a0|>=3.41.1,<4.0a0|>=3.40.1,<4.0a0|>=3.40.0,<4.0a0|>=3.39.3,<4.0a0|>=3.38.0,<4.0a0|>=3.37.2,<4.0a0|>=3.39.2,<4.0a0|>=3.38.3,<4.0a0|>=3.38.2,<4.0a0|>=3.35.4,<4.0a0|>=3.31.1,<4.0a0|>=3.30.0,<4.0a0|>=3.29.0,<4.0a0|>=3.27.2,<4.0a0|>=3.23.1,<4.0a0|>=3.22.0,<4.0a0|>=3.20.1,<4.0a0|3.9.*']
idna -> python[version='>=3.6'] -> sqlite[version='3.13.*|3.20.*|>=3.24.0,<4.0a0|>=3.25.1,<4.0a0|>=3.25.2,<4.0a0|>=3.25.3,<4.0a0|>=3.26.0,<4.0a0|>=3.28.0,<4.0a0|>=3.30.1,<4.0a0|>=3.32.3,<4.0a0|>=3.33.0,<4.0a0|>=3.34.0,<4.0a0|>=3.35.5,<4.0a0|>=3.36.0,<4.0a0|>=3.37.0,<4.0a0|>=3.37.1,<4.0a0|>=3.38.5,<4.0a0|>=3.41.2,<4.0a0|>=3.41.1,<4.0a0|>=3.40.1,<4.0a0|>=3.40.0,<4.0a0|>=3.39.3,<4.0a0|>=3.38.0,<4.0a0|>=3.37.2,<4.0a0|>=3.39.2,<4.0a0|>=3.38.3,<4.0a0|>=3.38.2,<4.0a0|>=3.35.4,<4.0a0|>=3.31.1,<4.0a0|>=3.30.0,<4.0a0|>=3.29.0,<4.0a0|>=3.27.2,<4.0a0|>=3.23.1,<4.0a0|>=3.22.0,<4.0a0|>=3.20.1,<4.0a0|3.9.*']
urllib3 -> python[version='>=3.7'] -> sqlite[version='3.13.*|3.20.*|>=3.24.0,<4.0a0|>=3.25.1,<4.0a0|>=3.25.2,<4.0a0|>=3.25.3,<4.0a0|>=3.26.0,<4.0a0|>=3.28.0,<4.0a0|>=3.30.1,<4.0a0|>=3.32.3,<4.0a0|>=3.33.0,<4.0a0|>=3.34.0,<4.0a0|>=3.35.5,<4.0a0|>=3.36.0,<4.0a0|>=3.37.0,<4.0a0|>=3.37.1,<4.0a0|>=3.38.5,<4.0a0|>=3.41.2,<4.0a0|>=3.41.1,<4.0a0|>=3.40.1,<4.0a0|>=3.40.0,<4.0a0|>=3.39.3,<4.0a0|>=3.38.0,<4.0a0|>=3.37.2,<4.0a0|>=3.39.2,<4.0a0|>=3.38.3,<4.0a0|>=3.38.2,<4.0a0|>=3.35.4,<4.0a0|>=3.31.1,<4.0a0|>=3.30.0,<4.0a0|>=3.29.0,<4.0a0|>=3.27.2,<4.0a0|3.9.*|>=3.23.1,<4.0a0|>=3.22.0,<4.0a0|>=3.20.1,<4.0a0']
pytorch -> python[version='>=3.9,<3.10.0a0'] -> sqlite[version='3.13.*|3.20.*|>=3.24.0,<4.0a0|>=3.25.1,<4.0a0|>=3.25.2,<4.0a0|>=3.25.3,<4.0a0|>=3.26.0,<4.0a0|>=3.28.0,<4.0a0|>=3.30.0,<4.0a0|>=3.30.1,<4.0a0|>=3.32.3,<4.0a0|>=3.33.0,<4.0a0|>=3.34.0,<4.0a0|>=3.35.5,<4.0a0|>=3.36.0,<4.0a0|>=3.37.0,<4.0a0|>=3.37.1,<4.0a0|>=3.38.5,<4.0a0|>=3.41.2,<4.0a0|>=3.40.1,<4.0a0|>=3.40.0,<4.0a0|>=3.39.3,<4.0a0|>=3.39.2,<4.0a0|>=3.38.3,<4.0a0|>=3.38.2,<4.0a0|>=3.38.0,<4.0a0|>=3.35.4,<4.0a0|>=3.41.1,<4.0a0|>=3.37.2,<4.0a0|>=3.31.1,<4.0a0|>=3.29.0,<4.0a0|>=3.27.2,<4.0a0|>=3.23.1,<4.0a0|>=3.22.0,<4.0a0|>=3.20.1,<4.0a0|3.9.*']
setuptools -> python[version='>=3.7'] -> sqlite[version='3.13.*|3.20.*|>=3.24.0,<4.0a0|>=3.25.1,<4.0a0|>=3.25.2,<4.0a0|>=3.25.3,<4.0a0|>=3.26.0,<4.0a0|>=3.28.0,<4.0a0|>=3.30.1,<4.0a0|>=3.32.3,<4.0a0|>=3.33.0,<4.0a0|>=3.34.0,<4.0a0|>=3.35.5,<4.0a0|>=3.36.0,<4.0a0|>=3.37.0,<4.0a0|>=3.37.1,<4.0a0|>=3.38.5,<4.0a0|>=3.41.2,<4.0a0|>=3.41.1,<4.0a0|>=3.40.1,<4.0a0|>=3.40.0,<4.0a0|>=3.39.3,<4.0a0|>=3.38.0,<4.0a0|>=3.37.2,<4.0a0|>=3.39.2,<4.0a0|>=3.38.3,<4.0a0|>=3.38.2,<4.0a0|>=3.35.4,<4.0a0|>=3.31.1,<4.0a0|>=3.30.0,<4.0a0|>=3.29.0,<4.0a0|>=3.27.2,<4.0a0|>=3.39.1,<4.0a0|>=3.23.1,<4.0a0|>=3.22.0,<4.0a0|>=3.20.1,<4.0a0|3.9.*']
pysocks -> python[version='>=3.8'] -> sqlite[version='3.13.*|3.20.*|>=3.24.0,<4.0a0|>=3.25.1,<4.0a0|>=3.25.2,<4.0a0|>=3.25.3,<4.0a0|>=3.26.0,<4.0a0|>=3.28.0,<4.0a0|>=3.30.0,<4.0a0|>=3.30.1,<4.0a0|>=3.32.3,<4.0a0|>=3.33.0,<4.0a0|>=3.34.0,<4.0a0|>=3.35.5,<4.0a0|>=3.36.0,<4.0a0|>=3.37.0,<4.0a0|>=3.37.1,<4.0a0|>=3.38.5,<4.0a0|>=3.41.2,<4.0a0|>=3.41.1,<4.0a0|>=3.40.1,<4.0a0|>=3.40.0,<4.0a0|>=3.39.3,<4.0a0|>=3.38.0,<4.0a0|>=3.37.2,<4.0a0|>=3.39.2,<4.0a0|>=3.38.3,<4.0a0|>=3.38.2,<4.0a0|>=3.35.4,<4.0a0|>=3.31.1,<4.0a0|>=3.29.0,<4.0a0|>=3.27.2,<4.0a0|>=3.39.1,<4.0a0|>=3.23.1,<4.0a0|>=3.22.0,<4.0a0|>=3.20.1,<4.0a0|3.9.*']
requests -> python[version='>=3.7'] -> sqlite[version='3.13.*|3.20.*|>=3.24.0,<4.0a0|>=3.25.1,<4.0a0|>=3.25.2,<4.0a0|>=3.25.3,<4.0a0|>=3.26.0,<4.0a0|>=3.28.0,<4.0a0|>=3.30.1,<4.0a0|>=3.32.3,<4.0a0|>=3.33.0,<4.0a0|>=3.34.0,<4.0a0|>=3.35.5,<4.0a0|>=3.36.0,<4.0a0|>=3.37.0,<4.0a0|>=3.37.1,<4.0a0|>=3.38.5,<4.0a0|>=3.41.2,<4.0a0|>=3.41.1,<4.0a0|>=3.40.1,<4.0a0|>=3.40.0,<4.0a0|>=3.39.3,<4.0a0|>=3.38.0,<4.0a0|>=3.37.2,<4.0a0|>=3.39.2,<4.0a0|>=3.38.3,<4.0a0|>=3.38.2,<4.0a0|>=3.35.4,<4.0a0|>=3.31.1,<4.0a0|>=3.30.0,<4.0a0|>=3.29.0,<4.0a0|>=3.27.2,<4.0a0|>=3.23.1,<4.0a0|>=3.22.0,<4.0a0|>=3.20.1,<4.0a0|3.9.*']
wheel -> python[version='>=3.7'] -> sqlite[version='3.13.*|3.20.*|>=3.24.0,<4.0a0|>=3.25.1,<4.0a0|>=3.25.2,<4.0a0|>=3.25.3,<4.0a0|>=3.26.0,<4.0a0|>=3.28.0,<4.0a0|>=3.30.1,<4.0a0|>=3.32.3,<4.0a0|>=3.33.0,<4.0a0|>=3.34.0,<4.0a0|>=3.35.5,<4.0a0|>=3.36.0,<4.0a0|>=3.37.0,<4.0a0|>=3.37.1,<4.0a0|>=3.38.5,<4.0a0|>=3.41.2,<4.0a0|>=3.41.1,<4.0a0|>=3.40.1,<4.0a0|>=3.40.0,<4.0a0|>=3.39.3,<4.0a0|>=3.38.0,<4.0a0|>=3.37.2,<4.0a0|>=3.39.2,<4.0a0|>=3.38.3,<4.0a0|>=3.38.2,<4.0a0|>=3.35.4,<4.0a0|>=3.31.1,<4.0a0|>=3.30.0,<4.0a0|>=3.29.0,<4.0a0|>=3.27.2,<4.0a0|3.9.*|>=3.23.1,<4.0a0|>=3.22.0,<4.0a0|>=3.20.1,<4.0a0']
numpy -> pypy3.9[version='>=7.3.11'] -> sqlite[version='3.13.*|3.20.*|>=3.24.0,<4.0a0|>=3.25.1,<4.0a0|>=3.25.2,<4.0a0|>=3.25.3,<4.0a0|>=3.26.0,<4.0a0|>=3.28.0,<4.0a0|>=3.30.0,<4.0a0|>=3.30.1,<4.0a0|>=3.32.3,<4.0a0|>=3.33.0,<4.0a0|>=3.34.0,<4.0a0|>=3.35.5,<4.0a0|>=3.36.0,<4.0a0|>=3.37.0,<4.0a0|>=3.37.1,<4.0a0|>=3.38.5,<4.0a0|>=3.41.2,<4.0a0|>=3.40.1,<4.0a0|>=3.40.0,<4.0a0|>=3.39.3,<4.0a0|>=3.39.2,<4.0a0|>=3.38.3,<4.0a0|>=3.38.2,<4.0a0|>=3.38.0,<4.0a0|>=3.35.4,<4.0a0|>=3.41.1,<4.0a0|>=3.37.2,<4.0a0|>=3.31.1,<4.0a0|>=3.39.1,<4.0a0|>=3.29.0,<4.0a0|>=3.27.2,<4.0a0|>=3.23.1,<4.0a0|>=3.22.0,<4.0a0|>=3.20.1,<4.0a0|3.9.*']
torchaudio -> python[version='>=3.9,<3.10.0a0'] -> sqlite[version='3.13.*|3.20.*|>=3.24.0,<4.0a0|>=3.25.1,<4.0a0|>=3.25.2,<4.0a0|>=3.25.3,<4.0a0|>=3.26.0,<4.0a0|>=3.28.0,<4.0a0|>=3.30.0,<4.0a0|>=3.30.1,<4.0a0|>=3.32.3,<4.0a0|>=3.33.0,<4.0a0|>=3.34.0,<4.0a0|>=3.35.5,<4.0a0|>=3.36.0,<4.0a0|>=3.37.0,<4.0a0|>=3.37.1,<4.0a0|>=3.38.5,<4.0a0|>=3.41.2,<4.0a0|>=3.40.1,<4.0a0|>=3.40.0,<4.0a0|>=3.39.3,<4.0a0|>=3.39.2,<4.0a0|>=3.38.3,<4.0a0|>=3.38.2,<4.0a0|>=3.38.0,<4.0a0|>=3.35.4,<4.0a0|>=3.31.1,<4.0a0|>=3.41.1,<4.0a0|>=3.37.2,<4.0a0|>=3.29.0,<4.0a0|>=3.27.2,<4.0a0|>=3.23.1,<4.0a0|>=3.22.0,<4.0a0|>=3.20.1,<4.0a0|3.9.*']
python_abi -> python=3.11 -> sqlite[version='3.13.*|3.20.*|>=3.24.0,<4.0a0|>=3.25.1,<4.0a0|>=3.25.2,<4.0a0|>=3.25.3,<4.0a0|>=3.26.0,<4.0a0|>=3.28.0,<4.0a0|>=3.30.0,<4.0a0|>=3.30.1,<4.0a0|>=3.32.3,<4.0a0|>=3.33.0,<4.0a0|>=3.34.0,<4.0a0|>=3.35.5,<4.0a0|>=3.36.0,<4.0a0|>=3.37.0,<4.0a0|>=3.37.1,<4.0a0|>=3.38.5,<4.0a0|>=3.40.1,<4.0a0|>=3.41.1,<4.0a0|>=3.41.2,<4.0a0|>=3.40.0,<4.0a0|>=3.39.3,<4.0a0|>=3.38.0,<4.0a0|>=3.37.2,<4.0a0|>=3.39.2,<4.0a0|>=3.39.1,<4.0a0|>=3.38.2,<4.0a0|>=3.38.3,<4.0a0|>=3.35.4,<4.0a0|>=3.31.1,<4.0a0|>=3.29.0,<4.0a0|>=3.27.2,<4.0a0|>=3.23.1,<4.0a0|>=3.22.0,<4.0a0|>=3.20.1,<4.0a0|3.9.*']
certifi -> python[version='>=3.7'] -> sqlite[version='3.13.*|3.20.*|>=3.24.0,<4.0a0|>=3.25.1,<4.0a0|>=3.25.2,<4.0a0|>=3.25.3,<4.0a0|>=3.26.0,<4.0a0|>=3.28.0,<4.0a0|>=3.30.1,<4.0a0|>=3.32.3,<4.0a0|>=3.33.0,<4.0a0|>=3.34.0,<4.0a0|>=3.35.5,<4.0a0|>=3.36.0,<4.0a0|>=3.37.0,<4.0a0|>=3.37.1,<4.0a0|>=3.38.5,<4.0a0|>=3.41.2,<4.0a0|>=3.41.1,<4.0a0|>=3.40.1,<4.0a0|>=3.40.0,<4.0a0|>=3.39.3,<4.0a0|>=3.38.0,<4.0a0|>=3.37.2,<4.0a0|>=3.39.2,<4.0a0|>=3.38.3,<4.0a0|>=3.38.2,<4.0a0|>=3.35.4,<4.0a0|>=3.31.1,<4.0a0|>=3.30.0,<4.0a0|>=3.29.0,<4.0a0|>=3.27.2,<4.0a0|>=3.39.1,<4.0a0|>=3.23.1,<4.0a0|>=3.22.0,<4.0a0|>=3.20.1,<4.0a0|3.9.*']
typing_extensions -> python[version='>=3.7'] -> sqlite[version='3.13.*|3.20.*|>=3.24.0,<4.0a0|>=3.25.1,<4.0a0|>=3.25.2,<4.0a0|>=3.25.3,<4.0a0|>=3.26.0,<4.0a0|>=3.28.0,<4.0a0|>=3.30.1,<4.0a0|>=3.32.3,<4.0a0|>=3.33.0,<4.0a0|>=3.34.0,<4.0a0|>=3.35.5,<4.0a0|>=3.36.0,<4.0a0|>=3.37.0,<4.0a0|>=3.37.1,<4.0a0|>=3.38.5,<4.0a0|>=3.41.2,<4.0a0|>=3.41.1,<4.0a0|>=3.40.1,<4.0a0|>=3.40.0,<4.0a0|>=3.39.3,<4.0a0|>=3.38.0,<4.0a0|>=3.37.2,<4.0a0|>=3.39.2,<4.0a0|>=3.38.3,<4.0a0|>=3.38.2,<4.0a0|>=3.35.4,<4.0a0|>=3.31.1,<4.0a0|>=3.30.0,<4.0a0|>=3.29.0,<4.0a0|>=3.27.2,<4.0a0|>=3.23.1,<4.0a0|>=3.22.0,<4.0a0|>=3.20.1,<4.0a0|3.9.*']
pillow -> pypy3.9[version='>=7.3.11'] -> sqlite[version='3.13.*|3.20.*|>=3.24.0,<4.0a0|>=3.25.1,<4.0a0|>=3.25.2,<4.0a0|>=3.25.3,<4.0a0|>=3.26.0,<4.0a0|>=3.28.0,<4.0a0|>=3.30.0,<4.0a0|>=3.30.1,<4.0a0|>=3.32.3,<4.0a0|>=3.33.0,<4.0a0|>=3.34.0,<4.0a0|>=3.35.5,<4.0a0|>=3.36.0,<4.0a0|>=3.37.0,<4.0a0|>=3.37.1,<4.0a0|>=3.38.5,<4.0a0|>=3.41.2,<4.0a0|>=3.40.1,<4.0a0|>=3.40.0,<4.0a0|>=3.39.3,<4.0a0|>=3.39.2,<4.0a0|>=3.38.3,<4.0a0|>=3.38.2,<4.0a0|>=3.38.0,<4.0a0|>=3.35.4,<4.0a0|>=3.41.1,<4.0a0|>=3.31.1,<4.0a0|>=3.37.2,<4.0a0|>=3.39.1,<4.0a0|>=3.29.0,<4.0a0|>=3.27.2,<4.0a0|>=3.23.1,<4.0a0|>=3.22.0,<4.0a0|>=3.20.1,<4.0a0|3.9.*']

Package setuptools conflicts for:
wheel -> setuptools
pip -> setuptools
python=3.7.5 -> pip -> setuptools
torchaudio -> pytorch==1.13.1 -> setuptools[version='<59.6']
torchvision -> pytorch==1.10.2 -> setuptools[version='<59.6']
zstd -> lz4 -> setuptools
pytorch -> setuptools[version='<59.6']
torchvision -> setuptools

Package gmp conflicts for:
gnutls -> gmp[version='6.1.*|>=6.1.2,<7.0a0|>=6.1.2']
ffmpeg -> gmp[version='>=6.1.2,<7.0a0|>=6.1.2|>=6.2.1,<7.0a0|>=6.2.0,<7.0a0']
ffmpeg -> gnutls=3.5 -> gmp=6.1
nettle -> gmp[version='6.1.*|>=6.1.2,<7.0a0|>=6.1.2']
torchvision -> ffmpeg[version='>=4.2'] -> gmp[version='>=6.1.2,<7.0a0|>=6.1.2|>=6.2.1,<7.0a0|>=6.2.0,<7.0a0']
pytorch -> libgcc -> gmp[version='>=4.2']

Package jpeg conflicts for:
torchvision -> pillow[version='>=5.3.0,!=8.3.*'] -> jpeg[version='9.*|>=9c,<10a']
libtiff -> libwebp -> jpeg
openjpeg -> libtiff[version='>=4.5.0,<4.6.0a0'] -> jpeg[version='9.*|>=9b,<10a|>=9d,<10a|>=9e,<10a|>=9c,<10a']
libtiff -> jpeg[version='9.*|>=9b,<10a|>=9c,<10a|>=9d,<10a|>=9e,<10a']
lcms2 -> jpeg[version='>=9b,<10a|>=9c,<10a|>=9d,<10a|>=9e,<10a']
pillow -> jpeg[version='8.*|9.*|>=9c,<10a|>=9d,<10a|>=9e,<10a|>=9b,<10a']
torchvision -> jpeg[version='<=9b|>=9e,<10a|>=9d,<10a|>=9b,<10a']

Package nomkl conflicts for:
blas -> openblas -> nomkl==3.0=0
numpy -> openblas[version='>=0.3.3,<0.3.4.0a0'] -> nomkl==3.0=0
torchaudio -> pytorch==2.0.0 -> nomkl
pytorch -> nomkl
blas-devel -> openblas=0.3.21 -> nomkl==3.0=0
libblas -> openblas[version='>=0.3.6,<0.3.7.0a0'] -> nomkl==3.0=0
torchvision -> pytorch==2.0.0 -> nomkl

Package ld_impl_linux-64 conflicts for:
urllib3 -> python[version='>=3.7'] -> ld_impl_linux-64[version='>=2.34|>=2.36.1|>=2.35.1']
pysocks -> python[version='>=3.8'] -> ld_impl_linux-64[version='>=2.34|>=2.36.1|>=2.35.1']
requests -> python[version='>=3.7'] -> ld_impl_linux-64[version='>=2.34|>=2.36.1|>=2.35.1']
torchaudio -> python[version='>=3.9,<3.10.0a0'] -> ld_impl_linux-64[version='>=2.34|>=2.36.1|>=2.35.1']
pytorch -> python[version='>=3.9,<3.10.0a0'] -> ld_impl_linux-64[version='>=2.34|>=2.35.1|>=2.36.1']
python=3.7.5 -> ld_impl_linux-64[version='>=2.34']
pip -> python[version='>=3.7'] -> ld_impl_linux-64[version='>=2.34|>=2.36.1|>=2.35.1']
typing_extensions -> python[version='>=3.7'] -> ld_impl_linux-64[version='>=2.34|>=2.36.1|>=2.35.1']
python_abi -> python=3.11 -> ld_impl_linux-64[version='>=2.34|>=2.35.1|>=2.36.1']
numpy -> python[version='>=3.9,<3.10.0a0'] -> ld_impl_linux-64[version='>=2.34|>=2.35.1|>=2.36.1']
idna -> python[version='>=3.6'] -> ld_impl_linux-64[version='>=2.34|>=2.36.1|>=2.35.1']
pillow -> python[version='>=3.9,<3.10.0a0'] -> ld_impl_linux-64[version='>=2.34|>=2.35.1|>=2.36.1']
setuptools -> python[version='>=3.7'] -> ld_impl_linux-64[version='>=2.34|>=2.36.1|>=2.35.1']
charset-normalizer -> python[version='>=3.7'] -> ld_impl_linux-64[version='>=2.34|>=2.36.1|>=2.35.1']
wheel -> python[version='>=3.7'] -> ld_impl_linux-64[version='>=2.34|>=2.36.1|>=2.35.1']
certifi -> python[version='>=3.7'] -> ld_impl_linux-64[version='>=2.34|>=2.36.1|>=2.35.1']
torchvision -> python[version='>=3.8,<3.9.0a0'] -> ld_impl_linux-64[version='>=2.34|>=2.36.1|>=2.35.1']

Package cuda-cudart conflicts for:
pytorch-cuda=11.8 -> cuda-libraries[version='>=11.8,<12.0'] -> cuda-cudart[version='>=11.8.89']
cuda-libraries -> cuda-cudart[version='12.0.107.*|>=11.8.89']
pytorch-cuda=11.8 -> cuda-cudart[version='>=11.8,<12.0']
torchaudio -> pytorch-cuda=11.8 -> cuda-cudart[version='>=11.7,<11.8|>=11.8,<12.0']
pytorch -> pytorch-cuda[version='>=11.8,<11.9'] -> cuda-cudart[version='>=11.7,<11.8|>=11.8,<12.0|>=12.0.107,<13.0a0']
torchvision -> pytorch-cuda=11.8 -> cuda-cudart[version='>=11.7,<11.8|>=11.8,<12.0']
cuda-runtime -> cuda-libraries=12.0.0 -> cuda-cudart[version='12.0.107.*|>=11.8.89']

Package cuda-nvrtc conflicts for:
torchvision -> pytorch-cuda=11.8 -> cuda-nvrtc[version='>=11.7,<11.8|>=11.8,<12.0']
cuda-libraries -> cuda-nvrtc[version='12.0.76.*|>=11.8.89']
cuda-runtime -> cuda-libraries=12.0.0 -> cuda-nvrtc[version='12.0.76.*|>=11.8.89']
pytorch-cuda=11.8 -> cuda-libraries[version='>=11.8,<12.0'] -> cuda-nvrtc[version='>=11.8.89']
torchaudio -> pytorch-cuda=11.8 -> cuda-nvrtc[version='>=11.7,<11.8|>=11.8,<12.0']
pytorch-cuda=11.8 -> cuda-nvrtc[version='>=11.8,<12.0']
libcusolver -> libcublas[version='>=12.0.1.189,<12.1.0a0'] -> cuda-nvrtc
cuda-libraries -> libcublas=12.0.1.189 -> cuda-nvrtc
pytorch -> pytorch-cuda[version='>=11.8,<11.9'] -> cuda-nvrtc[version='>=11.7,<11.8|>=11.8,<12.0']
libcublas -> cuda-nvrtc

Package brotli-bin conflicts for:
urllib3 -> brotli[version='>=1.0.9'] -> brotli-bin[version='1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.1.0',build='h5eee18b_7|h7f98852_6|h166bdaf_8|h166bdaf_9|hd590300_0|h166bdaf_7|h7f98852_5']
brotli -> brotli-bin[version='1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.1.0',build='h5eee18b_7|h7f98852_6|h166bdaf_8|h166bdaf_9|hd590300_0|h166bdaf_7|h7f98852_5']

Package flit-core conflicts for:
typing_extensions -> flit-core[version='>=3.6,<4']
torchvision -> typing_extensions -> flit-core[version='>=3.6,<4']
pytorch -> typing_extensions -> flit-core[version='>=3.6,<4']

Package gdbm conflicts for:
setuptools -> pypy3.9[version='>=7.3.9'] -> gdbm[version='>=1.18,<1.19.0a0']
python_abi -> pypy3.9=7.3 -> gdbm[version='>=1.18,<1.19.0a0']
pysocks -> pypy3.9[version='>=7.3.8'] -> gdbm[version='>=1.18,<1.19.0a0']
numpy -> pypy3.9[version='>=7.3.11'] -> gdbm[version='>=1.18,<1.19.0a0']
certifi -> pypy3.8[version='>=7.3.9'] -> gdbm[version='>=1.18,<1.19.0a0']
pillow -> pypy3.9[version='>=7.3.11'] -> gdbm[version='>=1.18,<1.19.0a0']

Package libopenblas conflicts for:
torchaudio -> numpy[version='>=1.11'] -> libopenblas[version='>=0.2.20,<0.2.21.0a0|>=0.3.2,<0.3.3.0a0|>=0.3.20,<1.0a0|>=0.3.21,<1.0a0|>=0.3.3,<1.0a0']
numpy -> libopenblas[version='>=0.2.20,<0.2.21.0a0|>=0.3.2,<0.3.3.0a0|>=0.3.20,<1.0a0|>=0.3.21,<1.0a0|>=0.3.3,<1.0a0']
blas -> libblas==3.9.0=18_linux64_openblas -> libopenblas[version='0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.12|0.3.12|0.3.12|0.3.12|0.3.12|0.3.12|0.3.12|0.3.12|0.3.13|0.3.13|0.3.15|0.3.15|0.3.15|0.3.15|0.3.16|0.3.16|0.3.17|0.3.17|0.3.17|0.3.17|0.3.18|0.3.18|0.3.20|0.3.20|0.3.20|0.3.20|0.3.21|0.3.21|0.3.21|0.3.21|0.3.21|0.3.21|0.3.21|0.3.23|0.3.23|0.3.24|0.3.24|>=0.3.10,<0.3.11.0a0|>=0.3.12,<0.3.13.0a0|>=0.3.15,<0.3.16.0a0|>=0.3.17,<0.3.18.0a0|>=0.3.18,<0.3.19.0a0|>=0.3.20,<0.3.21.0a0|>=0.3.21,<0.3.22.0a0|>=0.3.23,<0.3.24.0a0|>=0.3.24,<0.3.25.0a0|>=0.3.24,<1.0a0|>=0.3.23,<1.0a0|>=0.3.21,<1.0a0|>=0.3.20,<1.0a0|>=0.3.18,<1.0a0|>=0.3.17,<1.0a0|>=0.3.15,<1.0a0|>=0.3.12,<1.0a0|>=0.3.10,<1.0a0|>=0.3.9,<0.3.10.0a0|>=0.3.9,<1.0a0|>=0.3.8,<0.3.9.0a0|>=0.3.8,<1.0a0|>=0.3.7,<0.3.8.0a0|>=0.3.7,<1.0a0|>=0.3.6,<0.3.7.0a0|>=0.3.6,<1.0a0|0.3.9|0.3.8|0.3.7|0.3.7|0.3.7|0.3.7|0.3.7|0.3.7|0.3.7|0.3.7|0.3.6|0.3.6|0.3.6|0.3.6|0.3.21|0.3.20|0.3.20|0.3.18|0.3.17|0.3.13|0.3.6|0.3.6|0.3.6|0.3.3|0.3.3|0.3.3|>=0.3.2,<0.3.3.0a0|>=0.2.20,<0.2.21.0a0',build='h5a2b251_1|h5a2b251_2|h5a2b251_3|h5a2b251_1|h5a2b251_2|hf726d26_1|h043d6bf_1|h6e990d7_3|h6e990d7_4|h6e990d7_5|h6e990d7_0|h6e990d7_2|h6e990d7_3|h5ec1e0e_5|h5ec1e0e_6|h5ec1e0e_0|pthreads_hb3c22a3_2|openmp_h709eae2_3|openmp_h709eae2_4|openmp_h59f9010_5|pthreads_hb3c22a3_0|openmp_h709eae2_0|openmp_h709eae2_1|openmp_h59f9010_1|openmp_h3d5035f_0|openmp_h3d5035f_0|openmp_h3d5035f_0|openmp_h3d5035f_0|pthreads_h8fe5266_0|pthreads_h8fe5266_1|openmp_h3d5035f_1|openmp_h3d5035f_0|openmp_h74cd887_0|openmp_h74cd887_1|openmp_h74cd887_0|pthreads_h78a6416_2|openmp_h74cd887_2|pthreads_h78a6416_3|pthreads_h80387f5_0|pthreads_h413a1c8_0|openmp_h2e9423c_0|openmp_h2a4e791_0|openmp_h74cd887_3|pthreads_h78a6416_1|pthreads_h78a6416_0|pthreads_h78a6416_1|pthreads_h78a6416_0|pthreads_h8fe5266_0|pthreads_h8fe5266_0|pthreads_h8fe5266_1|openmp_h3d5035f_1|pthreads_h8fe5266_0|pthreads_h8fe5266_0|pthreads_h4812303_1|pthreads_hb3c22a3_1|pthreads_h4812303_0|openmp_h59f9010_0|openmp_h709eae2_5|pthreads_hb3c22a3_5|pthreads_h4812303_5|pthreads_hb3c22a3_4|pthreads_hb3c22a3_3|openmp_h709eae2_2|pthreads_hb3c22a3_1|openmp_h709eae2_1|h5ec1e0e_0|h5ec1e0e_0|h5ec1e0e_7|h5ec1e0e_4|h6e990d7_1|h6e990d7_6|h043d6bf_0|h043d6bf_0|hf726d26_0|h4367d64_0|h5a2b251_0|h5a2b251_0']
liblapack -> libblas==3.9.0=18_linux64_openblas -> libopenblas[version='>=0.3.10,<0.3.11.0a0|>=0.3.12,<0.3.13.0a0|>=0.3.15,<0.3.16.0a0|>=0.3.17,<0.3.18.0a0|>=0.3.18,<0.3.19.0a0|>=0.3.20,<0.3.21.0a0|>=0.3.21,<0.3.22.0a0|>=0.3.23,<0.3.24.0a0|>=0.3.24,<0.3.25.0a0|>=0.3.24,<1.0a0|>=0.3.23,<1.0a0|>=0.3.21,<1.0a0|>=0.3.20,<1.0a0|>=0.3.18,<1.0a0|>=0.3.17,<1.0a0|>=0.3.15,<1.0a0|>=0.3.12,<1.0a0|>=0.3.10,<1.0a0|>=0.3.9,<0.3.10.0a0|>=0.3.9,<1.0a0|>=0.3.8,<0.3.9.0a0|>=0.3.8,<1.0a0|>=0.3.7,<0.3.8.0a0|>=0.3.7,<1.0a0|>=0.3.6,<0.3.7.0a0|>=0.3.6,<1.0a0']
blas-devel -> libblas==3.9.0=18_linux64_openblas -> libopenblas[version='0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.12|0.3.12|0.3.12|0.3.12|0.3.12|0.3.12|0.3.12|0.3.12|0.3.13|0.3.13|0.3.15|0.3.15|0.3.15|0.3.15|0.3.16|0.3.16|0.3.17|0.3.17|0.3.17|0.3.17|0.3.18|0.3.18|0.3.18|0.3.20|0.3.20|0.3.20|0.3.20|0.3.20|0.3.20|0.3.21|0.3.21|0.3.21|0.3.21|0.3.21|0.3.21|0.3.21|0.3.21|0.3.23|0.3.23|0.3.24|0.3.24|>=0.3.24,<0.3.25.0a0|>=0.3.24,<1.0a0|>=0.3.23,<0.3.24.0a0|>=0.3.23,<1.0a0|>=0.3.21,<0.3.22.0a0|>=0.3.21,<1.0a0|>=0.3.20,<0.3.21.0a0|>=0.3.20,<1.0a0|>=0.3.18,<0.3.19.0a0|>=0.3.18,<1.0a0|0.3.9|0.3.8|0.3.7|0.3.7|0.3.7|0.3.7|0.3.7|0.3.7|0.3.7|0.3.7|0.3.6|0.3.6|0.3.6|0.3.6|0.3.17|0.3.13|0.3.6|0.3.6|0.3.6|0.3.3|0.3.3|0.3.3|>=0.3.2,<0.3.3.0a0|>=0.2.20,<0.2.21.0a0|>=0.3.17,<0.3.18.0a0|>=0.3.17,<1.0a0|>=0.3.15,<0.3.16.0a0|>=0.3.15,<1.0a0|>=0.3.12,<0.3.13.0a0|>=0.3.12,<1.0a0',build='h5a2b251_1|h5a2b251_2|h5a2b251_3|h5a2b251_1|h5a2b251_2|h6e990d7_3|h6e990d7_4|h6e990d7_5|h6e990d7_0|h6e990d7_1|h6e990d7_2|h6e990d7_3|h5ec1e0e_5|h5ec1e0e_6|h5ec1e0e_0|openmp_h709eae2_1|pthreads_hb3c22a3_2|pthreads_hb3c22a3_3|openmp_h709eae2_3|pthreads_hb3c22a3_0|openmp_h709eae2_1|openmp_h59f9010_1|openmp_h3d5035f_0|openmp_h3d5035f_0|pthreads_h8fe5266_1|openmp_h3d5035f_0|openmp_h3d5035f_0|pthreads_h8fe5266_1|openmp_h3d5035f_1|openmp_h3d5035f_0|h043d6bf_1|openmp_h74cd887_0|openmp_h74cd887_1|openmp_h74cd887_0|pthreads_h78a6416_2|openmp_h74cd887_2|pthreads_h78a6416_3|pthreads_h80387f5_0|pthreads_h413a1c8_0|openmp_h2e9423c_0|openmp_h2a4e791_0|openmp_h74cd887_3|pthreads_h78a6416_1|pthreads_h78a6416_0|h043d6bf_0|pthreads_h78a6416_1|pthreads_h78a6416_0|h043d6bf_0|pthreads_h8fe5266_0|hf726d26_0|pthreads_h8fe5266_0|pthreads_h8fe5266_0|openmp_h3d5035f_1|pthreads_h8fe5266_0|pthreads_h8fe5266_0|pthreads_h4812303_1|pthreads_hb3c22a3_1|openmp_h709eae2_0|pthreads_h4812303_0|openmp_h59f9010_0|openmp_h709eae2_5|pthreads_hb3c22a3_5|pthreads_h4812303_5|openmp_h59f9010_5|openmp_h709eae2_4|pthreads_hb3c22a3_4|openmp_h709eae2_2|pthreads_hb3c22a3_1|h5ec1e0e_0|h5ec1e0e_0|h5ec1e0e_7|h5ec1e0e_4|h6e990d7_6|hf726d26_1|h4367d64_0|h5a2b251_0|h5a2b251_0']
libblas -> openblas[version='>=0.3.6,<0.3.7.0a0'] -> libopenblas==0.3.6[build='h5a2b251_2|h6e990d7_3|h6e990d7_4|h6e990d7_5|h6e990d7_6|h5a2b251_1|h5a2b251_0']
libcblas -> libblas==3.9.0=18_linux64_openblas -> libopenblas[version='>=0.3.10,<0.3.11.0a0|>=0.3.12,<0.3.13.0a0|>=0.3.15,<0.3.16.0a0|>=0.3.17,<0.3.18.0a0|>=0.3.18,<0.3.19.0a0|>=0.3.20,<0.3.21.0a0|>=0.3.21,<0.3.22.0a0|>=0.3.23,<0.3.24.0a0|>=0.3.24,<0.3.25.0a0|>=0.3.24,<1.0a0|>=0.3.23,<1.0a0|>=0.3.21,<1.0a0|>=0.3.20,<1.0a0|>=0.3.18,<1.0a0|>=0.3.17,<1.0a0|>=0.3.15,<1.0a0|>=0.3.12,<1.0a0|>=0.3.10,<1.0a0|>=0.3.9,<0.3.10.0a0|>=0.3.9,<1.0a0|>=0.3.8,<0.3.9.0a0|>=0.3.8,<1.0a0|>=0.3.7,<0.3.8.0a0|>=0.3.7,<1.0a0|>=0.3.6,<0.3.7.0a0|>=0.3.6,<1.0a0']
numpy -> libblas[version='>=3.9.0,<4.0a0'] -> libopenblas[version='0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.10|0.3.12|0.3.12|0.3.12|0.3.12|0.3.12|0.3.12|0.3.12|0.3.12|0.3.13|0.3.13|0.3.15|0.3.15|0.3.15|0.3.15|0.3.16|0.3.16|0.3.17|0.3.17|0.3.17|0.3.17|0.3.18|0.3.18|0.3.20|0.3.20|0.3.20|0.3.20|0.3.21|0.3.21|0.3.21|0.3.21|0.3.21|0.3.21|0.3.21|0.3.23|0.3.23|0.3.24|0.3.24|0.3.3|0.3.3|0.3.3|>=0.3.10,<0.3.11.0a0|>=0.3.12,<0.3.13.0a0|>=0.3.15,<0.3.16.0a0|>=0.3.17,<0.3.18.0a0|>=0.3.18,<0.3.19.0a0|>=0.3.20,<0.3.21.0a0|>=0.3.21,<0.3.22.0a0|>=0.3.23,<0.3.24.0a0|>=0.3.24,<0.3.25.0a0|>=0.3.24,<1.0a0|>=0.3.23,<1.0a0|>=0.3.18,<1.0a0|>=0.3.17,<1.0a0|>=0.3.15,<1.0a0|>=0.3.12,<1.0a0|>=0.3.10,<1.0a0|>=0.3.9,<0.3.10.0a0|>=0.3.9,<1.0a0|>=0.3.8,<0.3.9.0a0|>=0.3.8,<1.0a0|>=0.3.7,<0.3.8.0a0|>=0.3.7,<1.0a0|>=0.3.6,<0.3.7.0a0|>=0.3.6,<1.0a0|0.3.9|0.3.8|0.3.7|0.3.7|0.3.7|0.3.7|0.3.7|0.3.7|0.3.7|0.3.7|0.3.6|0.3.6|0.3.6|0.3.6|0.3.21|0.3.20|0.3.20|0.3.18|0.3.17|0.3.13|0.3.6|0.3.6|0.3.6',build='h5a2b251_1|h5a2b251_2|hf726d26_0|h043d6bf_1|h6e990d7_3|h6e990d7_5|h6e990d7_1|h6e990d7_2|h6e990d7_3|h5ec1e0e_5|h5ec1e0e_6|pthreads_hb3c22a3_2|openmp_h709eae2_3|openmp_h59f9010_0|pthreads_h4812303_0|pthreads_hb3c22a3_0|openmp_h709eae2_0|openmp_h709eae2_1|openmp_h59f9010_1|openmp_h3d5035f_0|pthreads_h8fe5266_0|openmp_h3d5035f_0|openmp_h3d5035f_0|openmp_h3d5035f_0|pthreads_h8fe5266_0|openmp_h3d5035f_0|openmp_h74cd887_0|openmp_h74cd887_1|openmp_h74cd887_0|pthreads_h78a6416_2|openmp_h74cd887_2|pthreads_h78a6416_3|h5a2b251_1|h5a2b251_2|h5a2b251_3|pthreads_h413a1c8_0|openmp_h2e9423c_0|pthreads_h80387f5_0|openmp_h2a4e791_0|openmp_h74cd887_3|pthreads_h78a6416_1|pthreads_h78a6416_0|pthreads_h78a6416_1|pthreads_h78a6416_0|pthreads_h8fe5266_0|openmp_h3d5035f_1|pthreads_h8fe5266_1|pthreads_h8fe5266_0|pthreads_h8fe5266_1|openmp_h3d5035f_1|pthreads_h8fe5266_0|pthreads_h4812303_1|pthreads_hb3c22a3_1|openmp_h709eae2_5|pthreads_hb3c22a3_5|pthreads_h4812303_5|openmp_h59f9010_5|openmp_h709eae2_4|pthreads_hb3c22a3_4|pthreads_hb3c22a3_3|openmp_h709eae2_2|pthreads_hb3c22a3_1|openmp_h709eae2_1|h5ec1e0e_0|h5ec1e0e_0|h5ec1e0e_0|h5ec1e0e_7|h5ec1e0e_4|h6e990d7_0|h6e990d7_6|h6e990d7_4|h043d6bf_0|h043d6bf_0|hf726d26_1|h4367d64_0|h5a2b251_0|h5a2b251_0']
torchvision -> numpy[version='>=1.11'] -> libopenblas[version='>=0.2.20,<0.2.21.0a0|>=0.3.2,<0.3.3.0a0|>=0.3.20,<1.0a0|>=0.3.21,<1.0a0|>=0.3.3,<1.0a0']
liblapacke -> libblas==3.9.0=18_linux64_openblas -> libopenblas[version='>=0.3.10,<0.3.11.0a0|>=0.3.12,<0.3.13.0a0|>=0.3.15,<0.3.16.0a0|>=0.3.17,<0.3.18.0a0|>=0.3.18,<0.3.19.0a0|>=0.3.20,<0.3.21.0a0|>=0.3.21,<0.3.22.0a0|>=0.3.23,<0.3.24.0a0|>=0.3.24,<0.3.25.0a0|>=0.3.24,<1.0a0|>=0.3.23,<1.0a0|>=0.3.21,<1.0a0|>=0.3.20,<1.0a0|>=0.3.18,<1.0a0|>=0.3.17,<1.0a0|>=0.3.15,<1.0a0|>=0.3.12,<1.0a0|>=0.3.10,<1.0a0|>=0.3.9,<0.3.10.0a0|>=0.3.9,<1.0a0|>=0.3.8,<0.3.9.0a0|>=0.3.8,<1.0a0|>=0.3.7,<0.3.8.0a0|>=0.3.7,<1.0a0|>=0.3.6,<0.3.7.0a0|>=0.3.6,<1.0a0']
pytorch -> numpy[version='>=1.19'] -> libopenblas[version='>=0.2.20,<0.2.21.0a0|>=0.3.2,<0.3.3.0a0|>=0.3.20,<1.0a0|>=0.3.21,<1.0a0|>=0.3.3,<1.0a0|>=0.3.24,<0.3.25.0a0|>=0.3.24,<1.0a0|>=0.3.23,<0.3.24.0a0|>=0.3.23,<1.0a0|>=0.3.21,<0.3.22.0a0|>=0.3.20,<0.3.21.0a0|>=0.3.18,<0.3.19.0a0|>=0.3.18,<1.0a0|>=0.3.17,<0.3.18.0a0|>=0.3.17,<1.0a0|>=0.3.15,<0.3.16.0a0|>=0.3.15,<1.0a0|>=0.3.12,<0.3.13.0a0|>=0.3.12,<1.0a0|>=0.3.10,<0.3.11.0a0|>=0.3.10,<1.0a0|>=0.3.9,<0.3.10.0a0|>=0.3.9,<1.0a0|>=0.3.8,<0.3.9.0a0|>=0.3.8,<1.0a0|>=0.3.7,<0.3.8.0a0|>=0.3.7,<1.0a0|>=0.3.6,<0.3.7.0a0|>=0.3.6,<1.0a0']
pytorch -> libopenblas
libblas -> libopenblas[version='>=0.3.10,<0.3.11.0a0|>=0.3.12,<0.3.13.0a0|>=0.3.15,<0.3.16.0a0|>=0.3.17,<0.3.18.0a0|>=0.3.18,<0.3.19.0a0|>=0.3.20,<0.3.21.0a0|>=0.3.21,<0.3.22.0a0|>=0.3.23,<0.3.24.0a0|>=0.3.24,<0.3.25.0a0|>=0.3.24,<1.0a0|>=0.3.23,<1.0a0|>=0.3.21,<1.0a0|>=0.3.20,<1.0a0|>=0.3.18,<1.0a0|>=0.3.17,<1.0a0|>=0.3.15,<1.0a0|>=0.3.12,<1.0a0|>=0.3.10,<1.0a0|>=0.3.9,<0.3.10.0a0|>=0.3.9,<1.0a0|>=0.3.8,<0.3.9.0a0|>=0.3.8,<1.0a0|>=0.3.7,<0.3.8.0a0|>=0.3.7,<1.0a0|>=0.3.6,<0.3.7.0a0|>=0.3.6,<1.0a0']

Package tbb conflicts for:
libblas -> mkl[version='>=2022.1.0,<2023.0a0'] -> tbb=2021
mkl -> tbb=2021
blas-devel -> mkl[version='>=2022.1.0,<2023.0a0'] -> tbb=2021
mkl-devel -> mkl==2023.2.0=h84fe81f_49572 -> tbb=2021
blas -> mkl -> tbb=2021
numpy -> mkl[version='>=2023.1.0,<2024.0a0'] -> tbb=2021
pytorch -> mkl[version='>=2018'] -> tbb=2021

Package ca-certificates conflicts for:
numpy -> python[version='>=2.7,<2.8.0a0'] -> ca-certificates
torchvision -> python[version='>=2.7,<2.8.0a0'] -> ca-certificates
pytorch -> python[version='>=2.7,<2.8.0a0'] -> ca-certificates
certifi -> python[version='>=2.7,<2.8.0a0'] -> ca-certificates
gnutls -> ca-certificates
typing_extensions -> python[version='>=2.7,<2.8.0a0'] -> ca-certificates
ffmpeg -> gnutls[version='>=3.6.5,<3.7.0a0'] -> ca-certificates
idna -> python -> ca-certificates
wheel -> python[version='!=3.0,!=3.1,!=3.2,!=3.3,!=3.4'] -> ca-certificates
pip -> python -> ca-certificates
python_abi -> python=2.7 -> ca-certificates
requests -> python -> ca-certificates
python=3.7.5 -> openssl[version='>=1.1.1i,<1.1.2a'] -> ca-certificates
pillow -> python[version='>=2.7,<2.8.0a0'] -> ca-certificates
urllib3 -> python[version='<4.0'] -> ca-certificates
openssl -> ca-certificates
setuptools -> python[version='>=2.7,<2.8.0a0'] -> ca-certificates
pysocks -> python[version='>=2.7,<2.8.0a0'] -> ca-certificates

Package libnvjitlink conflicts for:
cuda-libraries -> libnvjitlink=12.0.76
cuda-runtime -> cuda-libraries=12.0.0 -> libnvjitlink=12.0.76
libcusparse -> libnvjitlink[version='>=12.0.76,<12.1.0a0']
cuda-libraries -> libcusolver=11.4.2.57 -> libnvjitlink[version='>=12.0.76,<12.1.0a0']
libcusolver -> libnvjitlink[version='>=12.0.76,<12.1.0a0']

Package fribidi conflicts for:
pillow -> fribidi[version='>=1.0.10,<2.0a0']
torchvision -> pillow[version='>=5.3.0,!=8.3.*'] -> fribidi[version='>=1.0.10,<2.0a0']
ffmpeg -> libass[version='>=0.17.1,<0.17.2.0a0'] -> fribidi[version='>=1.0.10,<2.0a0']

Package pip conflicts for:
idna -> python[version='>=3.6'] -> pip
requests -> python[version='>=3.7'] -> pip
typing_extensions -> python[version='>=3.7'] -> pip
urllib3 -> python[version='>=3.7'] -> pip
pysocks -> python[version='>=3.8'] -> pip
pytorch -> python[version='>=3.9,<3.10.0a0'] -> pip
torchaudio -> python[version='>=3.9,<3.10.0a0'] -> pip
pillow -> python[version='>=3.9,<3.10.0a0'] -> pip
python_abi -> python=3.11 -> pip
torchvision -> python[version='>=3.8,<3.9.0a0'] -> pip
python=3.7.5 -> pip
setuptools -> python[version='>=3.7'] -> pip
wheel -> python[version='>=3.7'] -> pip
numpy -> python[version='>=3.9,<3.10.0a0'] -> pip
charset-normalizer -> python[version='>=3.7'] -> pip
certifi -> python[version='>=3.7'] -> pip

Package libgfortran5 conflicts for:
liblapack -> libgfortran-ng -> libgfortran5[version='10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.4.0|10.4.0|10.4.0|10.4.0|11.1.0|11.1.0|11.1.0|11.1.0|11.1.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.3.0|11.3.0|11.3.0|11.3.0|11.4.0|12.1.0|12.1.0|12.2.0|12.2.0|12.3.0|13.1.0|13.2.0|9.5.0|9.5.0|9.5.0|9.5.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.3.0.*|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.4.0.*|11.2.0.*',build='h0ffbd86_9|h0ffbd86_13|h0ffbd86_16|h42c683c_19|h62347ff_7|h62347ff_8|h62347ff_11|h62347ff_12|h62347ff_13|h62347ff_14|h6e911d1_16|h6e911d1_17|hab08dfb_18|hab08dfb_19|hb56cab1_9|hb56cab1_11|he3294f5_16|he3294f5_17|h6c583b3_7|h6c583b3_8|h5c6108e_9|h5c6108e_13|h5c6108e_14|h5c6108e_16|h6a973e8_17|h39d6296_19|hdcd56e2_16|h337968e_18|ha4646dd_0|h15d22d2_0|hc57166a_0|h337968e_19|hdcd56e2_17|h2c0dd1a_0|h39d6296_18|h6a973e8_16|h5c6108e_15|h5c6108e_12|h5c6108e_11|h5c6108e_10|h5c6108e_8|h6c583b3_6|h6c583b3_5|h6c583b3_4|hfbd5096_19|hfbd5096_18|hb56cab1_16|hb56cab1_15|hb56cab1_14|hb56cab1_13|hb56cab1_12|hb56cab1_10|hb56cab1_8|hb56cab1_7|hb56cab1_6|hb56cab1_5|hb56cab1_4|h62347ff_16|h62347ff_15|h62347ff_10|h62347ff_9|h62347ff_6|h62347ff_5|h62347ff_4|h42c683c_18|h0ffbd86_17|h0ffbd86_15|h0ffbd86_14|h0ffbd86_12|h0ffbd86_11|h0ffbd86_10|h0ffbd86_8']
numpy -> libgfortran5[version='>=11.2.0']
liblapacke -> libgfortran-ng -> libgfortran5[version='10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.4.0|10.4.0|10.4.0|10.4.0|11.1.0|11.1.0|11.1.0|11.1.0|11.1.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.3.0|11.3.0|11.3.0|11.3.0|11.4.0|12.1.0|12.1.0|12.2.0|12.2.0|12.3.0|13.1.0|13.2.0|9.5.0|9.5.0|9.5.0|9.5.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.3.0.*|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.4.0.*|11.2.0.*',build='h0ffbd86_9|h0ffbd86_13|h0ffbd86_16|h42c683c_19|h62347ff_7|h62347ff_8|h62347ff_11|h62347ff_12|h62347ff_13|h62347ff_14|h6e911d1_16|h6e911d1_17|hab08dfb_18|hab08dfb_19|hb56cab1_9|hb56cab1_11|he3294f5_16|he3294f5_17|h6c583b3_7|h6c583b3_8|h5c6108e_9|h5c6108e_13|h5c6108e_14|h5c6108e_16|h6a973e8_17|h39d6296_19|hdcd56e2_16|h337968e_18|ha4646dd_0|h15d22d2_0|hc57166a_0|h337968e_19|hdcd56e2_17|h2c0dd1a_0|h39d6296_18|h6a973e8_16|h5c6108e_15|h5c6108e_12|h5c6108e_11|h5c6108e_10|h5c6108e_8|h6c583b3_6|h6c583b3_5|h6c583b3_4|hfbd5096_19|hfbd5096_18|hb56cab1_16|hb56cab1_15|hb56cab1_14|hb56cab1_13|hb56cab1_12|hb56cab1_10|hb56cab1_8|hb56cab1_7|hb56cab1_6|hb56cab1_5|hb56cab1_4|h62347ff_16|h62347ff_15|h62347ff_10|h62347ff_9|h62347ff_6|h62347ff_5|h62347ff_4|h42c683c_18|h0ffbd86_17|h0ffbd86_15|h0ffbd86_14|h0ffbd86_12|h0ffbd86_11|h0ffbd86_10|h0ffbd86_8']
libcblas -> libgfortran5[version='>=9.3.0']
libblas -> libopenblas[version='>=0.3.24,<0.3.25.0a0'] -> libgfortran5[version='10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.4.0|10.4.0|10.4.0|10.4.0|11.1.0|11.1.0|11.1.0|11.1.0|11.1.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.3.0|11.3.0|11.3.0|11.3.0|11.4.0|12.1.0|12.1.0|12.2.0|12.2.0|12.3.0|13.1.0|13.2.0|>=10.3.0|>=10.4.0|>=11.3.0|>=12.3.0|>=11.2.0|>=9.4.0|9.5.0|9.5.0|9.5.0|9.5.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.3.0.*|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.4.0.*|11.2.0.*',build='h0ffbd86_9|h0ffbd86_13|h0ffbd86_16|h42c683c_19|h62347ff_7|h62347ff_8|h62347ff_11|h62347ff_12|h62347ff_13|h62347ff_14|h6e911d1_16|h6e911d1_17|hab08dfb_18|hab08dfb_19|hb56cab1_9|hb56cab1_11|he3294f5_16|he3294f5_17|h6c583b3_7|h6c583b3_8|h5c6108e_9|h5c6108e_13|h5c6108e_14|h5c6108e_16|h6a973e8_17|h39d6296_19|hdcd56e2_16|h337968e_18|ha4646dd_0|h15d22d2_0|hc57166a_0|h337968e_19|hdcd56e2_17|h2c0dd1a_0|h39d6296_18|h6a973e8_16|h5c6108e_15|h5c6108e_12|h5c6108e_11|h5c6108e_10|h5c6108e_8|h6c583b3_6|h6c583b3_5|h6c583b3_4|hfbd5096_19|hfbd5096_18|hb56cab1_16|hb56cab1_15|hb56cab1_14|hb56cab1_13|hb56cab1_12|hb56cab1_10|hb56cab1_8|hb56cab1_7|hb56cab1_6|hb56cab1_5|hb56cab1_4|h62347ff_16|h62347ff_15|h62347ff_10|h62347ff_9|h62347ff_6|h62347ff_5|h62347ff_4|h42c683c_18|h0ffbd86_17|h0ffbd86_15|h0ffbd86_14|h0ffbd86_12|h0ffbd86_11|h0ffbd86_10|h0ffbd86_8']
blas -> libgfortran5[version='>=10.3.0|>=10.4.0|>=12.2.0|>=12.3.0|>=9.4.0|>=9.3.0']
blas -> libgfortran-ng -> libgfortran5[version='10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.4.0|10.4.0|10.4.0|10.4.0|11.1.0|11.1.0|11.1.0|11.1.0|11.1.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.3.0|11.3.0|11.3.0|11.3.0|11.4.0|12.1.0|12.1.0|12.2.0|12.2.0|12.3.0|13.1.0|13.2.0|9.5.0|9.5.0|9.5.0|9.5.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.3.0.*|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.4.0.*|11.2.0.*|>=11.3.0',build='h0ffbd86_9|h0ffbd86_13|h0ffbd86_16|h42c683c_19|h62347ff_7|h62347ff_8|h62347ff_11|h62347ff_12|h62347ff_13|h62347ff_14|h6e911d1_16|h6e911d1_17|hab08dfb_18|hab08dfb_19|hb56cab1_9|hb56cab1_11|he3294f5_16|he3294f5_17|h6c583b3_7|h6c583b3_8|h5c6108e_9|h5c6108e_13|h5c6108e_14|h5c6108e_16|h6a973e8_17|h39d6296_19|hdcd56e2_16|h337968e_18|ha4646dd_0|h15d22d2_0|hc57166a_0|h337968e_19|hdcd56e2_17|h2c0dd1a_0|h39d6296_18|h6a973e8_16|h5c6108e_15|h5c6108e_12|h5c6108e_11|h5c6108e_10|h5c6108e_8|h6c583b3_6|h6c583b3_5|h6c583b3_4|hfbd5096_19|hfbd5096_18|hb56cab1_16|hb56cab1_15|hb56cab1_14|hb56cab1_13|hb56cab1_12|hb56cab1_10|hb56cab1_8|hb56cab1_7|hb56cab1_6|hb56cab1_5|hb56cab1_4|h62347ff_16|h62347ff_15|h62347ff_10|h62347ff_9|h62347ff_6|h62347ff_5|h62347ff_4|h42c683c_18|h0ffbd86_17|h0ffbd86_15|h0ffbd86_14|h0ffbd86_12|h0ffbd86_11|h0ffbd86_10|h0ffbd86_8']
numpy -> libblas[version='>=3.9.0,<4.0a0'] -> libgfortran5[version='10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.4.0|10.4.0|10.4.0|10.4.0|11.1.0|11.1.0|11.1.0|11.1.0|11.1.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.3.0|11.3.0|11.3.0|11.3.0|11.4.0|12.1.0|12.1.0|12.2.0|12.2.0|12.3.0|13.1.0|13.2.0|>=9.3.0|9.5.0|9.5.0|9.5.0|9.5.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.3.0.*|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.4.0.*|11.2.0.*|>=12.3.0|>=11.3.0|>=10.4.0|>=10.3.0|>=9.4.0|>=12.2.0',build='h0ffbd86_9|h0ffbd86_13|h0ffbd86_16|h42c683c_19|h62347ff_7|h62347ff_8|h62347ff_11|h62347ff_12|h62347ff_13|h62347ff_14|h6e911d1_16|h6e911d1_17|hab08dfb_18|hab08dfb_19|hb56cab1_9|hb56cab1_11|he3294f5_16|he3294f5_17|h6c583b3_7|h6c583b3_8|h5c6108e_9|h5c6108e_13|h5c6108e_14|h5c6108e_16|h6a973e8_17|h39d6296_19|hdcd56e2_16|h337968e_18|ha4646dd_0|h15d22d2_0|hc57166a_0|h337968e_19|hdcd56e2_17|h2c0dd1a_0|h39d6296_18|h6a973e8_16|h5c6108e_15|h5c6108e_12|h5c6108e_11|h5c6108e_10|h5c6108e_8|h6c583b3_6|h6c583b3_5|h6c583b3_4|hfbd5096_19|hfbd5096_18|hb56cab1_16|hb56cab1_15|hb56cab1_14|hb56cab1_13|hb56cab1_12|hb56cab1_10|hb56cab1_8|hb56cab1_7|hb56cab1_6|hb56cab1_5|hb56cab1_4|h62347ff_16|h62347ff_15|h62347ff_10|h62347ff_9|h62347ff_6|h62347ff_5|h62347ff_4|h42c683c_18|h0ffbd86_17|h0ffbd86_15|h0ffbd86_14|h0ffbd86_12|h0ffbd86_11|h0ffbd86_10|h0ffbd86_8']
blas-devel -> liblapack==3.9.0[build=*netlib] -> libgfortran5[version='>=10.3.0|>=10.4.0|>=11.3.0|>=12.3.0|>=9.3.0|>=9.4.0']
torchaudio -> numpy[version='>=1.11'] -> libgfortran5[version='>=11.2.0']
libblas -> libgfortran5[version='>=9.3.0']
torchvision -> numpy[version='>=1.11'] -> libgfortran5[version='>=11.2.0']
liblapack -> libgfortran5[version='>=9.3.0']
libgfortran-ng -> libgfortran5[version='10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.4.0|10.4.0|10.4.0|10.4.0|11.1.0|11.1.0|11.1.0|11.1.0|11.1.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.3.0|11.3.0|11.3.0|11.3.0|11.4.0|12.1.0|12.1.0|12.2.0|12.2.0|12.3.0|13.1.0|13.2.0|9.5.0|9.5.0|9.5.0|9.5.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.3.0.*|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.4.0.*|11.2.0.*',build='h0ffbd86_9|h0ffbd86_13|h0ffbd86_16|h42c683c_19|h62347ff_7|h62347ff_8|h62347ff_11|h62347ff_12|h62347ff_13|h62347ff_14|h6e911d1_16|h6e911d1_17|hab08dfb_18|hab08dfb_19|hb56cab1_9|hb56cab1_11|he3294f5_16|he3294f5_17|h6c583b3_7|h6c583b3_8|h5c6108e_9|h5c6108e_13|h5c6108e_14|h5c6108e_16|h6a973e8_17|h39d6296_19|hdcd56e2_16|h337968e_18|ha4646dd_0|h15d22d2_0|hc57166a_0|h337968e_19|hdcd56e2_17|h2c0dd1a_0|h39d6296_18|h6a973e8_16|h5c6108e_15|h5c6108e_12|h5c6108e_11|h5c6108e_10|h5c6108e_8|h6c583b3_6|h6c583b3_5|h6c583b3_4|hfbd5096_19|hfbd5096_18|hb56cab1_16|hb56cab1_15|hb56cab1_14|hb56cab1_13|hb56cab1_12|hb56cab1_10|hb56cab1_8|hb56cab1_7|hb56cab1_6|hb56cab1_5|hb56cab1_4|h62347ff_16|h62347ff_15|h62347ff_10|h62347ff_9|h62347ff_6|h62347ff_5|h62347ff_4|h42c683c_18|h0ffbd86_17|h0ffbd86_15|h0ffbd86_14|h0ffbd86_12|h0ffbd86_11|h0ffbd86_10|h0ffbd86_8']
pytorch -> blas=[build=mkl] -> libgfortran5[version='>=10.3.0|>=10.4.0|>=9.4.0|>=9.3.0|>=11.2.0|>=12.3.0|>=12.2.0|>=11.3.0']
mkl-devel -> blas=[build=mkl] -> libgfortran5[version='>=10.3.0|>=10.4.0|>=9.4.0|>=9.3.0']
libcblas -> libgfortran-ng -> libgfortran5[version='10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.3.0|10.4.0|10.4.0|10.4.0|10.4.0|11.1.0|11.1.0|11.1.0|11.1.0|11.1.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.2.0|11.3.0|11.3.0|11.3.0|11.3.0|11.4.0|12.1.0|12.1.0|12.2.0|12.2.0|12.3.0|13.1.0|13.2.0|9.5.0|9.5.0|9.5.0|9.5.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.4.0|9.3.0.*|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.5.0|8.4.0.*|11.2.0.*',build='h0ffbd86_9|h0ffbd86_13|h0ffbd86_16|h42c683c_19|h62347ff_7|h62347ff_8|h62347ff_11|h62347ff_12|h62347ff_13|h62347ff_14|h6e911d1_16|h6e911d1_17|hab08dfb_18|hab08dfb_19|hb56cab1_9|hb56cab1_11|he3294f5_16|he3294f5_17|h6c583b3_7|h6c583b3_8|h5c6108e_9|h5c6108e_13|h5c6108e_14|h5c6108e_16|h6a973e8_17|h39d6296_19|hdcd56e2_16|h337968e_18|ha4646dd_0|h15d22d2_0|hc57166a_0|h337968e_19|hdcd56e2_17|h2c0dd1a_0|h39d6296_18|h6a973e8_16|h5c6108e_15|h5c6108e_12|h5c6108e_11|h5c6108e_10|h5c6108e_8|h6c583b3_6|h6c583b3_5|h6c583b3_4|hfbd5096_19|hfbd5096_18|hb56cab1_16|hb56cab1_15|hb56cab1_14|hb56cab1_13|hb56cab1_12|hb56cab1_10|hb56cab1_8|hb56cab1_7|hb56cab1_6|hb56cab1_5|hb56cab1_4|h62347ff_16|h62347ff_15|h62347ff_10|h62347ff_9|h62347ff_6|h62347ff_5|h62347ff_4|h42c683c_18|h0ffbd86_17|h0ffbd86_15|h0ffbd86_14|h0ffbd86_12|h0ffbd86_11|h0ffbd86_10|h0ffbd86_8']
liblapacke -> libgfortran5[version='>=9.3.0']

Package libhwloc conflicts for:
mkl -> tbb=2021 -> libhwloc[version='>=2.8.0,<2.8.1.0a0|>=2.9.0,<2.9.1.0a0|>=2.9.1,<2.9.2.0a0|>=2.9.2,<2.9.3.0a0']
tbb -> libhwloc[version='>=2.8.0,<2.8.1.0a0|>=2.9.0,<2.9.1.0a0|>=2.9.1,<2.9.2.0a0|>=2.9.2,<2.9.3.0a0']

Package blis conflicts for:
blas-devel -> libblas==3.9.0=18_linux64_blis -> blis[version='>=0.8.0,<0.8.1.0a0|>=0.8.1,<0.8.2.0a0|>=0.9.0,<0.9.1.0a0']
numpy -> libblas[version='>=3.9.0,<4.0a0'] -> blis[version='0.5.1.*|>=0.5.2,<0.5.3.0a0|>=0.6.0,<0.6.1.0a0|>=0.6.1,<0.6.2.0a0|>=0.7.0,<0.7.1.0a0|>=0.8.0,<0.8.1.0a0|>=0.8.1,<0.8.2.0a0|>=0.9.0,<0.9.1.0a0']
libcblas -> libblas==3.9.0=18_linux64_blis -> blis[version='0.5.1.*|>=0.5.2,<0.5.3.0a0|>=0.6.0,<0.6.1.0a0|>=0.6.1,<0.6.2.0a0|>=0.7.0,<0.7.1.0a0|>=0.8.0,<0.8.1.0a0|>=0.8.1,<0.8.2.0a0|>=0.9.0,<0.9.1.0a0']
libblas -> blis[version='0.5.1.*|>=0.5.2,<0.5.3.0a0|>=0.6.0,<0.6.1.0a0|>=0.6.1,<0.6.2.0a0|>=0.7.0,<0.7.1.0a0|>=0.8.0,<0.8.1.0a0|>=0.8.1,<0.8.2.0a0|>=0.9.0,<0.9.1.0a0']
blas -> libblas==3.9.0=18_linux64_blis -> blis[version='0.5.1.*|>=0.5.2,<0.5.3.0a0|>=0.6.0,<0.6.1.0a0|>=0.6.1,<0.6.2.0a0|>=0.7.0,<0.7.1.0a0|>=0.8.0,<0.8.1.0a0|>=0.8.1,<0.8.2.0a0|>=0.9.0,<0.9.1.0a0']
liblapack -> libblas=3.9.0 -> blis[version='0.5.1.*|>=0.5.2,<0.5.3.0a0|>=0.6.0,<0.6.1.0a0|>=0.6.1,<0.6.2.0a0|>=0.7.0,<0.7.1.0a0|>=0.8.0,<0.8.1.0a0|>=0.8.1,<0.8.2.0a0|>=0.9.0,<0.9.1.0a0']
liblapacke -> libblas=3.9.0 -> blis[version='0.5.1.*|>=0.5.2,<0.5.3.0a0|>=0.6.0,<0.6.1.0a0|>=0.6.1,<0.6.2.0a0|>=0.7.0,<0.7.1.0a0|>=0.8.0,<0.8.1.0a0|>=0.8.1,<0.8.2.0a0|>=0.9.0,<0.9.1.0a0']
pytorch -> libblas[version='>=3.9.0,<4.0a0'] -> blis[version='0.5.1.*|>=0.5.2,<0.5.3.0a0|>=0.6.0,<0.6.1.0a0|>=0.6.1,<0.6.2.0a0|>=0.7.0,<0.7.1.0a0|>=0.8.0,<0.8.1.0a0|>=0.8.1,<0.8.2.0a0|>=0.9.0,<0.9.1.0a0']

Package libedit conflicts for:
sqlite -> libedit[version='>=3.1.20170329,<3.2.0a0|>=3.1.20181209,<3.2.0a0|>=3.1.20191231,<3.2.0a0']
python=3.7.5 -> sqlite[version='>=3.30.1,<4.0a0'] -> libedit[version='>=3.1.20181209,<3.2.0a0|>=3.1.20191231,<3.2.0a0']

Package libcusparse conflicts for:
torchvision -> pytorch-cuda=11.8 -> libcusparse[version='>=11.7.3.50,<11.7.5.86|>=11.7.5.86,<12.0.0.76']
pytorch -> pytorch-cuda[version='>=11.8,<11.9'] -> libcusparse[version='>=11.7.3.50,<11.7.5.86|>=11.7.5.86,<12.0.0.76|>=12.0.0.76,<13.0a0']
cuda-runtime -> cuda-libraries=12.0.0 -> libcusparse[version='12.0.0.76.*|>=11.7.5.86']
torchaudio -> pytorch-cuda=11.8 -> libcusparse[version='>=11.7.3.50,<11.7.5.86|>=11.7.5.86,<12.0.0.76']
pytorch-cuda=11.8 -> cuda-libraries[version='>=11.8,<12.0'] -> libcusparse[version='>=11.7.5.86']
pytorch-cuda=11.8 -> libcusparse[version='>=11.7.5.86,<12.0.0.76']
cuda-libraries -> libcusparse[version='12.0.0.76.*|>=11.7.5.86']

Package lz4 conflicts for:
libtiff -> zstd[version='>=1.3.7,<1.3.8.0a0'] -> lz4
zstd -> lz4

Package p11-kit conflicts for:
ffmpeg -> gnutls[version='>=3.7.8,<3.8.0a0'] -> p11-kit[version='>=0.23.21,<0.24.0a0|>=0.24.1,<0.25.0a0']
gnutls -> p11-kit[version='>=0.23.21,<0.24.0a0|>=0.24.1,<0.25.0a0']

Package libcusolver conflicts for:
pytorch-cuda=11.8 -> cuda-libraries[version='>=11.8,<12.0'] -> libcusolver[version='>=11.4.1.48']
torchaudio -> pytorch-cuda=11.8 -> libcusolver[version='>=11.3.5.50,<11.4.1.48|>=11.4.1.48,<11.4.2.57']
pytorch -> pytorch-cuda[version='>=11.8,<11.9'] -> libcusolver[version='>=11.3.5.50,<11.4.1.48|>=11.4.1.48,<11.4.2.57']
cuda-runtime -> cuda-libraries=12.0.0 -> libcusolver[version='11.4.2.57.*|>=11.4.1.48']
cuda-libraries -> libcusolver[version='11.4.2.57.*|>=11.4.1.48']
torchvision -> pytorch-cuda=11.8 -> libcusolver[version='>=11.3.5.50,<11.4.1.48|>=11.4.1.48,<11.4.2.57']
pytorch-cuda=11.8 -> libcusolver[version='>=11.4.1.48,<11.4.2.57']

Package giflib conflicts for:
libtiff -> libwebp -> giflib[version='>=5.1.4,<5.2.0a0|>=5.1.7,<5.1.8.0a0|>=5.2.1,<5.3.0a0']
pillow -> libwebp -> giflib[version='>=5.1.4,<5.2.0a0|>=5.1.7,<5.1.8.0a0|>=5.2.1,<5.3.0a0']

Package libbrotlidec conflicts for:
brotli-bin -> libbrotlidec[version='1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.1.0',build='h5eee18b_7|h7f98852_6|h166bdaf_8|h166bdaf_9|hd590300_0|h166bdaf_7|h7f98852_5']
urllib3 -> brotli[version='>=1.0.9'] -> libbrotlidec[version='1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.1.0',build='h5eee18b_7|h7f98852_6|h166bdaf_8|h166bdaf_9|hd590300_0|h166bdaf_7|h7f98852_5']
brotli -> libbrotlidec[version='1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.1.0',build='h5eee18b_7|h7f98852_6|h166bdaf_8|h166bdaf_9|hd590300_0|h166bdaf_7|h7f98852_5']

Package blas conflicts for:
pytorch -> blas[version='*|1.0',build='mkl|mkl|openblas']
pytorch -> numpy[version='>=1.11'] -> blas[version='1.0|1.1',build=openblas]
blas-devel -> blas[version='2.0|2.0|2.0|2.1|2.1|2.106|2.5|2.5|2.5|2.4|2.4|2.4|2.3|2.3|2.2|2.2|2.21|2.20|2.19|2.18|2.17|2.16|2.16|2.16|2.15|2.15|2.15|2.14|2.14|2.14|2.7',build='netlib|mkl|blis|mkl|openblas|mkl|mkl|openblas|mkl|blis|mkl|mkl|openblas|blis|openblas|openblas|blis|openblas|blis|blis|openblas|blis|openblas|blis|netlib|mkl|mkl|mkl|blis|openblas|openblas|openblas|blis']
numpy -> blas[version='*|*|1.0|1.1|1.0',build='mkl|openblas|mkl|openblas|openblas']
mkl-devel -> blas=[build=mkl]
torchvision -> numpy[version='>=1.11'] -> blas[version='*|*|1.0|1.1|1.0',build='mkl|openblas|mkl|openblas|openblas']
blas-devel -> mkl-devel=2022.1 -> blas[version='*|1.0',build='mkl|openblas']
libblas -> openblas[version='>=0.3.6,<0.3.7.0a0'] -> blas==1.0=openblas
torchaudio -> numpy[version='>=1.11'] -> blas[version='*|*|1.0|1.1|1.0',build='mkl|openblas|mkl|openblas|openblas']

Package libdeflate conflicts for:
pillow -> libtiff[version='>=4.5.1,<4.6.0a0'] -> libdeflate[version='>=1.10,<1.11.0a0|>=1.12,<1.13.0a0|>=1.13,<1.14.0a0|>=1.14,<1.15.0a0|>=1.16,<1.17.0a0|>=1.17,<1.18.0a0|>=1.18,<1.19.0a0|>=1.8,<1.9.0a0|>=1.7,<1.8.0a0']
openjpeg -> libtiff[version='>=4.5.0,<4.6.0a0'] -> libdeflate[version='>=1.10,<1.11.0a0|>=1.12,<1.13.0a0|>=1.13,<1.14.0a0|>=1.14,<1.15.0a0|>=1.16,<1.17.0a0|>=1.17,<1.18.0a0|>=1.18,<1.19.0a0|>=1.8,<1.9.0a0|>=1.7,<1.8.0a0']
lcms2 -> libtiff[version='>=4.6.0,<4.7.0a0'] -> libdeflate[version='>=1.10,<1.11.0a0|>=1.12,<1.13.0a0|>=1.13,<1.14.0a0|>=1.14,<1.15.0a0|>=1.16,<1.17.0a0|>=1.17,<1.18.0a0|>=1.18,<1.19.0a0|>=1.8,<1.9.0a0|>=1.7,<1.8.0a0']
libtiff -> libdeflate[version='>=1.10,<1.11.0a0|>=1.12,<1.13.0a0|>=1.13,<1.14.0a0|>=1.14,<1.15.0a0|>=1.16,<1.17.0a0|>=1.17,<1.18.0a0|>=1.18,<1.19.0a0|>=1.8,<1.9.0a0|>=1.7,<1.8.0a0']

Package urllib3 conflicts for:
torchvision -> requests -> urllib3[version='>=1.21.1,<1.22|>=1.21.1,<1.23|>=1.21.1,<1.24|>=1.21.1,<1.25|>=1.21.1,<1.26,!=1.25.0,!=1.25.1|>=1.21.1,<1.27|>=1.21.1,<3|>=1.21.1,<2']
requests -> urllib3[version='>=1.21.1,<1.22|>=1.21.1,<1.23|>=1.21.1,<1.24|>=1.21.1,<1.25|>=1.21.1,<1.26,!=1.25.0,!=1.25.1|>=1.21.1,<1.27|>=1.21.1,<3|>=1.21.1,<2']

Package nettle conflicts for:
gnutls -> nettle[version='3.3.*|3.3|3.3.*|>=3.3,<3.4.0a0|>=3.4.1,<3.5.0a0|>=3.4.1|>=3.7,<3.8.0a0|>=3.8,<3.9.0a0|>=3.8.1,<3.9.0a0|>=3.6,<3.7.0a0|>=3.7.2,<3.8.0a0']
ffmpeg -> nettle[version='>=3.4.1,<3.5.0a0']
torchvision -> ffmpeg[version='>=4.2'] -> nettle[version='>=3.4.1,<3.5.0a0']
ffmpeg -> gnutls[version='>=3.6.5,<3.7.0a0'] -> nettle[version='3.3.*|3.3|3.3.*|>=3.3,<3.4.0a0|>=3.4.1|>=3.6,<3.7.0a0|>=3.7.2,<3.8.0a0|>=3.8.1,<3.9.0a0|>=3.8,<3.9.0a0|>=3.7,<3.8.0a0']

Package zstd conflicts for:
blas -> llvm-openmp[version='>=16.0.6'] -> zstd[version='>=1.5.2,<1.6.0a0']
_openmp_mutex -> llvm-openmp[version='>=9.0.1'] -> zstd[version='>=1.5.2,<1.6.0a0']
openjpeg -> libtiff[version='>=4.5.0,<4.6.0a0'] -> zstd[version='>=1.3.3,<1.3.4.0a0|>=1.3.7,<1.3.8.0a0|>=1.4.4,<1.5.0a0|>=1.4|>=1.4.3,<1.5.0.0a0|>=1.4.4,<1.5.0.0a0|>=1.4.5,<1.5.0a0|>=1.4.9,<1.5.0a0|>=1.5.0,<1.6.0a0|>=1.5.2,<1.6.0a0|>=1.4.0,<1.5.0.0a0|>=1.5.5,<1.6.0a0']
lcms2 -> libtiff[version='>=4.6.0,<4.7.0a0'] -> zstd[version='>=1.3.3,<1.3.4.0a0|>=1.3.7,<1.3.8.0a0|>=1.4.4,<1.5.0a0|>=1.4|>=1.4.3,<1.5.0.0a0|>=1.4.4,<1.5.0.0a0|>=1.4.5,<1.5.0a0|>=1.4.9,<1.5.0a0|>=1.5.0,<1.6.0a0|>=1.5.2,<1.6.0a0|>=1.5.5,<1.6.0a0|>=1.4.0,<1.5.0.0a0']
pillow -> libtiff[version='>=4.5.1,<4.6.0a0'] -> zstd[version='>=1.3.3,<1.3.4.0a0|>=1.3.7,<1.3.8.0a0|>=1.4.4,<1.5.0a0|>=1.4|>=1.4.3,<1.5.0.0a0|>=1.4.4,<1.5.0.0a0|>=1.4.5,<1.5.0a0|>=1.4.9,<1.5.0a0|>=1.5.0,<1.6.0a0|>=1.5.2,<1.6.0a0|>=1.4.0,<1.5.0.0a0|>=1.5.5,<1.6.0a0']
llvm-openmp -> zstd[version='>=1.5.2,<1.6.0a0']
mkl -> llvm-openmp[version='>=16.0.6'] -> zstd[version='>=1.5.2,<1.6.0a0']
libtiff -> zstd[version='>=1.3.3,<1.3.4.0a0|>=1.4.0,<1.5.0.0a0|>=1.4.3,<1.5.0.0a0|>=1.4.4,<1.5.0.0a0|>=1.4.5,<1.5.0a0|>=1.4.9,<1.5.0a0|>=1.5.0,<1.6.0a0|>=1.5.2,<1.6.0a0|>=1.5.5,<1.6.0a0|>=1.4|>=1.4.4,<1.5.0a0|>=1.3.7,<1.3.8.0a0']

Package mkl-include conflicts for:
mkl-devel -> mkl-include[version='2017.0.4|2018.0.0|2018.0.1|2018.0.2|2018.0.3|2019.0|2019.0|2019.1|2019.3|2019.4|2019.5|2020.0|2020.1|2020.1|2020.2|2020.2|2020.4|2021.1.1|2021.2.0|2021.3.0|2021.4.0|2022.0.1|2022.1.0|2022.2.1|2022.2.1|2023.0.0|2023.0.0|2023.1.0|2023.1.0|2023.2.0|2023.1.0|2023.1.0|2023.0.0|2022.1.0|2022.1.0|2022.0.1|2021.4.0|2021.3.0|2021.2.0',build='h15fc484_2|117|144|199|h06a4308_296|h06a4308_520|h06a4308_640|h06a4308_117|h06a4308_46343|ha770c72_256|h726a3e6_304|h8d4b97c_729|h8d4b97c_803|h84fe81f_915|h84fe81f_16996|h84fe81f_16997|h84fe81f_25396|h84fe81f_26648|h84fe81f_49572|h84fe81f_33|h84fe81f_48680|h84fe81f_46349|h726a3e6_557|h726a3e6_389|h726a3e6_79|256|219|217|166|281|h06a4308_46342|h06a4308_25399|h06a4308_224|h06a4308_223|243|118|1|1|hc7b2577_4|hf7c01fb_0']
blas-devel -> mkl-devel=2022.1 -> mkl-include[version='2017.0.4|2018.0.0|2018.0.1|2018.0.2|2018.0.3|2019.0|2019.0|2019.1|2019.3|2019.4|2019.5|2020.0|2020.1|2020.1|2020.2|2020.2|2020.4|2021.1.1|2021.2.0|2021.3.0|2021.4.0|2022.0.1|2022.0.1|2022.1.0|2023.2.0|2023.2.0|2023.1.0|2023.1.0|2023.0.0|2023.0.0|2022.2.1|2022.2.1|2023.1.0|2023.1.0|2023.0.0|2021.4.0|2021.3.0|2021.2.0',build='h15fc484_2|1|117|199|h06a4308_296|h06a4308_640|h06a4308_46343|281|166|ha770c72_256|h726a3e6_304|h726a3e6_389|h8d4b97c_729|h84fe81f_16996|h84fe81f_16997|h84fe81f_25396|h84fe81f_26648|h84fe81f_46349|h84fe81f_33|h06a4308_117|h84fe81f_915|h06a4308_224|h06a4308_223|h8d4b97c_803|h84fe81f_49572|h84fe81f_48680|h726a3e6_557|h726a3e6_79|256|219|217|h06a4308_46342|h06a4308_25399|h06a4308_520|243|144|118|1|hc7b2577_4|hf7c01fb_0']

Package jbig conflicts for:
pillow -> libtiff[version='>=4.3.0,<4.5.0a0'] -> jbig
openjpeg -> libtiff[version='>=4.3.0,<4.5.0a0'] -> jbig
libtiff -> jbig
lcms2 -> libtiff[version='>=4.2.0,<4.5.0a0'] -> jbig

Package six conflicts for:
numpy -> mkl-service[version='>=2.3.0,<3.0a0'] -> six
torchvision -> six
urllib3 -> cryptography[version='>=1.3.4'] -> six[version='>=1.4.1|>=1.5.2']
wheel -> packaging[version='>=20.2'] -> six
pytorch -> mkl-service[version='>=2.3.0,<3.0a0'] -> six

Package lcms2 conflicts for:
torchvision -> pillow[version='>=5.3.0,!=8.3.*'] -> lcms2[version='>=2.11,<3.0a0|>=2.12,<3.0a0|>=2.14,<3.0a0|>=2.15,<3.0a0']
pillow -> lcms2[version='>=2.11,<3.0a0|>=2.12,<3.0a0|>=2.14,<3.0a0|>=2.15,<3.0a0']

Package cuda-opencl conflicts for:
cuda-libraries -> cuda-opencl=12.0.76
cuda-runtime -> cuda-libraries=12.0.0 -> cuda-opencl=12.0.76

Package cuda-runtime conflicts for:
torchaudio -> pytorch-cuda=11.8 -> cuda-runtime[version='>=11.7,<11.8|>=11.8,<12.0']
pytorch -> pytorch-cuda[version='>=11.8,<11.9'] -> cuda-runtime[version='>=11.7,<11.8|>=11.8,<12.0']
pytorch-cuda=11.8 -> cuda-runtime[version='>=11.8,<12.0']
torchvision -> pytorch-cuda=11.8 -> cuda-runtime[version='>=11.7,<11.8|>=11.8,<12.0']

Package lame conflicts for:
ffmpeg -> lame[version='>=3.100,<3.101.0a0']
torchvision -> ffmpeg[version='>=4.2'] -> lame[version='>=3.100,<3.101.0a0']

Package cuda-cupti conflicts for:
pytorch-cuda=11.8 -> cuda-cupti[version='>=11.8,<12.0']
torchaudio -> pytorch-cuda=11.8 -> cuda-cupti[version='>=11.7,<11.8|>=11.8,<12.0']
pytorch -> pytorch-cuda[version='>=11.8,<11.9'] -> cuda-cupti[version='>=11.7,<11.8|>=11.8,<12.0']
torchvision -> pytorch-cuda=11.8 -> cuda-cupti[version='>=11.7,<11.8|>=11.8,<12.0']

Package blas-devel conflicts for:
blas -> blas-devel==3.9.0[build='5_netlib|7_blis|7_openblas|8_blis|8_openblas|9_openblas|9_mkl|10_blis|10_mkl|11_linux64_blis|11_linux64_openblas|11_linux64_mkl|12_linux64_openblas|12_linux64_blis|13_linux64_openblas|13_linux64_mkl|14_linux64_openblas|14_linux64_mkl|15_linux64_openblas|16_linux64_openblas|17_linux64_openblas|18_linux64_openblas|18_linux64_blis|17_linux64_blis|16_linux64_mkl|16_linux64_blis|15_linux64_mkl|15_linux64_blis|14_linux64_blis|13_linux64_blis|12_linux64_mkl|10_openblas|9_blis|8_mkl|7_mkl']
mkl-devel -> blas=[build=mkl] -> blas-devel==3.9.0[build='8_mkl|10_mkl|11_linux64_mkl|12_linux64_mkl|13_linux64_mkl|14_linux64_mkl|16_linux64_mkl|15_linux64_mkl|9_mkl|7_mkl']
numpy -> blas=[build=openblas] -> blas-devel==3.9.0[build='8_mkl|9_mkl|10_mkl|11_linux64_mkl|13_linux64_mkl|14_linux64_mkl|16_linux64_mkl|7_openblas|8_openblas|9_openblas|12_linux64_openblas|14_linux64_openblas|15_linux64_openblas|16_linux64_openblas|18_linux64_openblas|17_linux64_openblas|13_linux64_openblas|11_linux64_openblas|10_openblas|15_linux64_mkl|12_linux64_mkl|7_mkl']
pytorch -> blas=[build=mkl] -> blas-devel==3.9.0[build='7_openblas|9_openblas|11_linux64_openblas|12_linux64_openblas|14_linux64_openblas|15_linux64_openblas|16_linux64_openblas|18_linux64_openblas|8_mkl|10_mkl|11_linux64_mkl|12_linux64_mkl|13_linux64_mkl|14_linux64_mkl|16_linux64_mkl|15_linux64_mkl|9_mkl|7_mkl|17_linux64_openblas|13_linux64_openblas|10_openblas|8_openblas']

Package libcurand conflicts for:
cuda-libraries -> libcurand[version='10.3.1.50.*|>=10.3.0.86']
pytorch-cuda=11.8 -> cuda-libraries[version='>=11.8,<12.0'] -> libcurand[version='>=10.3.0.86']
cuda-runtime -> cuda-libraries=12.0.0 -> libcurand[version='10.3.1.50.*|>=10.3.0.86']

Package openh264 conflicts for:
ffmpeg -> openh264[version='1.7.*|>=1.8.0,<1.9.0a0|>=2.1.0,<2.2.0a0|>=2.3.1,<2.3.2.0a0|>=2.3.0,<2.3.1.0a0|>=2.2.0,<2.3.0a0|>=2.1.1,<2.2.0a0']
torchvision -> ffmpeg[version='>=4.2'] -> openh264[version='>=1.8.0,<1.9.0a0|>=2.1.0,<2.2.0a0|>=2.3.1,<2.3.2.0a0|>=2.3.0,<2.3.1.0a0|>=2.2.0,<2.3.0a0|>=2.1.1,<2.2.0a0']

Package mkl-devel conflicts for:
blas-devel -> mkl-devel[version='2022.0.*|2022.1.*']
blas -> blas-devel==3.9.0=16_linux64_mkl -> mkl-devel[version='2022.0.*|2022.1.*']

Package openblas-devel conflicts for:
numpy -> openblas[version='>=0.3.3,<0.3.4.0a0'] -> openblas-devel[version='0.3.10|0.3.13|0.3.17|0.3.18|0.3.20|0.3.20|0.3.21|0.3.3|>=0.2.20,<0.2.21.0a0|0.3.6|0.3.6|0.3.6|>=0.3.2,<0.3.3.0a0',build='0|0|h06a4308_0|h06a4308_1|h06a4308_0|3|2|1|h06a4308_0|h06a4308_1|h06a4308_0|2|1']
libblas -> openblas[version='>=0.3.6,<0.3.7.0a0'] -> openblas-devel==0.3.6[build='1|2|0']
blas -> openblas -> openblas-devel[version='0.3.10|0.3.13|0.3.17|0.3.18|0.3.20|0.3.20|0.3.21|0.3.6|0.3.6|0.3.6|0.3.3|0.3.3|0.3.3|>=0.3.2,<0.3.3.0a0|>=0.2.20,<0.2.21.0a0',build='1|0|0|h06a4308_1|h06a4308_0|h06a4308_0|h06a4308_0|h06a4308_1|h06a4308_0|2|1|3|2']
blas-devel -> openblas=0.3.21 -> openblas-devel[version='0.3.10|0.3.13|0.3.17|0.3.18|0.3.20|0.3.20|0.3.21|0.3.6|0.3.6|0.3.6|0.3.3|0.3.3|0.3.3|>=0.3.2,<0.3.3.0a0|>=0.2.20,<0.2.21.0a0',build='1|0|0|h06a4308_1|h06a4308_0|h06a4308_0|h06a4308_0|h06a4308_1|h06a4308_0|2|1|3|2']

Package typing_extensions conflicts for:
torchvision -> typing_extensions
torchaudio -> pytorch==2.0.1 -> typing_extensions
pytorch -> typing-extensions -> typing_extensions[version='3.10.0.0|3.10.0.0|3.10.0.1|3.10.0.2|4.0.0|4.0.1|4.1.1|4.2.0|4.2.0|4.3.0|4.4.0|4.5.0|4.6.0|4.6.1|4.6.2|4.6.3|4.7.0|4.7.1|3.7.4.3|3.7.4.2|3.7.4.1|3.7.4.1|3.7.4.1|3.7.4.1|3.7.4|3.7.2|3.6.6|3.6.6|3.6.5|4.7.1|4.7.1|4.7.1|4.7.1|4.6.3|4.6.3|4.6.3|4.6.3|4.5.0|4.5.0|4.5.0|4.5.0|4.4.0|4.4.0|4.4.0|4.4.0|4.4.0|4.3.0|4.3.0|4.3.0|4.3.0|4.1.1|3.10.0.2|3.7.4.3|3.7.4',build='py36_0|pyh06a4308_0|pyh06a4308_0|pyh06a4308_0|pyh06a4308_0|py38h06a4308_0|py39h06a4308_0|py37h06a4308_0|py38h06a4308_0|py37h06a4308_0|py38h06a4308_0|py39h06a4308_0|py38h06a4308_0|py37_0|py38_0|py37hc8dfbb8_2|py_0|py_0|pyha770c72_0|pyha770c72_0|pyha770c72_0|pyha770c72_0|pyha770c72_0|pyha770c72_0|pyha770c72_1|pyha770c72_0|pyha770c72_0|py36h9f0ad1d_3|py27h8c360ce_1|py37_1000|py37_1000|py36_0|py36_0|py310h06a4308_0|py311h06a4308_0|py310h06a4308_0|py38h06a4308_0|py39h06a4308_0|py311h06a4308_0|py39h06a4308_0|py311h06a4308_0|py310h06a4308_0|py311h06a4308_0|py310h06a4308_0|py39h06a4308_0|py310h06a4308_0']
pytorch -> typing_extensions

Package lerc conflicts for:
lcms2 -> libtiff[version='>=4.6.0,<4.7.0a0'] -> lerc[version='>=2.2.1,<3.0a0|>=3.0,<4.0a0|>=4.0.0,<5.0a0']
libtiff -> lerc[version='>=2.2.1,<3.0a0|>=3.0,<4.0a0|>=4.0.0,<5.0a0']
pillow -> libtiff[version='>=4.5.1,<4.6.0a0'] -> lerc[version='>=2.2.1,<3.0a0|>=3.0,<4.0a0|>=4.0.0,<5.0a0']
openjpeg -> libtiff[version='>=4.5.0,<4.6.0a0'] -> lerc[version='>=2.2.1,<3.0a0|>=3.0,<4.0a0|>=4.0.0,<5.0a0']

Package icu conflicts for:
libhwloc -> libxml2[version='>=2.11.5,<2.12.0a0'] -> icu[version='56.*|58.*|69.*|>=58.2,<59.0a0|>=70.1,<71.0a0|>=72.1,<73.0a0|>=73.2,<74.0a0|>=73.1,<74.0a0|>=69.1,<70.0a0|>=68.1,<69.0a0|>=67.1,<68.0a0|>=64.2,<65.0a0']
libxml2 -> icu[version='56.*|58.*|69.*|>=70.1,<71.0a0|>=72.1,<73.0a0|>=73.2,<74.0a0|>=69.1,<70.0a0|>=68.1,<69.0a0|>=67.1,<68.0a0|>=64.2,<65.0a0|>=58.2,<59.0a0|>=73.1,<74.0a0']
ffmpeg -> libxml2[version='>=2.11.5,<2.12.0a0'] -> icu[version='69.*|>=58.2,<59.0a0|>=72.1,<73.0a0|>=73.2,<74.0a0|>=73.1,<74.0a0|>=70.1,<71.0a0|>=69.1,<70.0a0|>=68.1,<69.0a0']

Package libxcb conflicts for:
pillow -> libxcb[version='>=1.13,<1.14.0a0|>=1.15,<1.16.0a0']
torchvision -> pillow[version='>=5.3.0,!=8.3.*'] -> libxcb[version='>=1.13,<1.14.0a0|>=1.15,<1.16.0a0']

Package libbrotlienc conflicts for:
brotli-bin -> libbrotlienc[version='1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.1.0',build='h5eee18b_7|h7f98852_6|h166bdaf_8|h166bdaf_9|hd590300_0|h166bdaf_7|h7f98852_5']
brotli -> libbrotlienc[version='1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.1.0',build='h5eee18b_7|h7f98852_6|h166bdaf_8|h166bdaf_9|hd590300_0|h166bdaf_7|h7f98852_5']
urllib3 -> brotli[version='>=1.0.9'] -> libbrotlienc[version='1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.1.0',build='h5eee18b_7|h7f98852_6|h166bdaf_8|h166bdaf_9|hd590300_0|h166bdaf_7|h7f98852_5']

Package xorg-libxau conflicts for:
libxcb -> xorg-libxau[version='>=1.0.11,<2.0a0']
pillow -> libxcb[version='>=1.15,<1.16.0a0'] -> xorg-libxau

Package cryptography conflicts for:
requests -> urllib3[version='>=1.21.1,<3'] -> cryptography[version='>=1.3.4']
urllib3 -> pyopenssl[version='>=0.14'] -> cryptography[version='>=1.3|>=1.9|>=2.1.4|>=2.2.1|>=2.8|>=3.2|>=3.3|>=35.0,<39|>=38.0.0,<39|>=38.0.0,<40|>=38.0.0,<41|>=38.0.0,<42,!=40.0.0,!=40.0.1|>=35.0']
urllib3 -> cryptography[version='>=1.3.4']

Package libgcc conflicts for:
pytorch -> libgcc
torchvision -> pytorch -> libgcc

Package lz4-c conflicts for:
llvm-openmp -> zstd[version='>=1.5.2,<1.6.0a0'] -> lz4-c[version='>=1.9.3,<1.10.0a0|>=1.9.3,<1.9.4.0a0|>=1.9.4,<1.10.0a0']
zstd -> lz4 -> lz4-c[version='1.8.1.*|>=1.8.1.2,<1.9.0a0']
zstd -> lz4-c[version='>=1.8.1.2,<1.8.2.0a0|>=1.8.3,<1.8.4.0a0|>=1.9.2,<1.9.3.0a0|>=1.9.3,<1.10.0a0|>=1.9.3,<1.9.4.0a0|>=1.9.4,<1.10.0a0|>=1.9.2,<1.10.0a0']
libtiff -> zstd[version='>=1.5.5,<1.6.0a0'] -> lz4-c[version='>=1.8.3,<1.8.4.0a0|>=1.9.2,<1.10.0a0|>=1.9.2,<1.9.3.0a0|>=1.9.3,<1.10.0a0|>=1.9.4,<1.10.0a0|>=1.9.3,<1.9.4.0a0']

Package pytorch-mutex conflicts for:
torchvision -> pytorch-mutex==1.0[build='cpu|cuda']
pytorch -> pytorch-mutex==1.0[build='cpu|cuda']
torchaudio -> pytorch-mutex==1.0[build='cpu|cuda']

Package libwebp-base conflicts for:
pillow -> libtiff[version='>=4.5.0,<4.6.0a0'] -> libwebp-base[version='1.1.0|1.1.0.*|1.2.0.*|1.2.1.*|1.2.2.*|1.2.3.*|1.2.4.*|1.3.0.*|1.3.1.*|>=1.2.3,<2.0a0|>=1.1.0,<1.2.0a0',build=2]
pillow -> libwebp-base[version='>=1.2.2,<2.0a0|>=1.2.4,<2.0a0|>=1.3.0,<2.0a0|>=1.3.1,<2.0a0']
torchvision -> pillow[version='>=5.3.0,!=8.3.*'] -> libwebp-base[version='>=1.2.2,<2.0a0|>=1.2.4,<2.0a0|>=1.3.0,<2.0a0|>=1.3.1,<2.0a0']
libtiff -> libwebp-base[version='>=1.1.0,<1.2.0a0|>=1.2.3,<2.0a0|>=1.2.4,<2.0a0|>=1.3.0,<2.0a0|>=1.3.1,<2.0a0']
lcms2 -> libtiff[version='>=4.6.0,<4.7.0a0'] -> libwebp-base[version='>=1.1.0,<1.2.0a0|>=1.2.3,<2.0a0|>=1.2.4,<2.0a0|>=1.3.0,<2.0a0|>=1.3.1,<2.0a0']
libtiff -> libwebp -> libwebp-base[version='1.1.0|1.1.0.*|1.2.0.*|1.2.1.*|1.2.2.*|1.2.3.*|1.2.4.*|1.3.0.*|1.3.1.*',build=2]
openjpeg -> libtiff[version='>=4.5.0,<4.6.0a0'] -> libwebp-base[version='>=1.1.0,<1.2.0a0|>=1.2.3,<2.0a0|>=1.2.4,<2.0a0|>=1.3.0,<2.0a0|>=1.3.1,<2.0a0']

Package libcufile conflicts for:
pytorch-cuda=11.8 -> cuda-libraries[version='>=11.8,<12.0'] -> libcufile[version='>=1.4.0.31']
cuda-runtime -> cuda-libraries=12.0.0 -> libcufile[version='1.5.0.59.*|>=1.4.0.31']
cuda-libraries -> libcufile[version='1.5.0.59.*|>=1.4.0.31']

Package cuda-nvtx conflicts for:
torchaudio -> pytorch-cuda=11.8 -> cuda-nvtx[version='>=11.7,<11.8|>=11.8,<12.0']
torchvision -> pytorch-cuda=11.8 -> cuda-nvtx[version='>=11.7,<11.8|>=11.8,<12.0']
pytorch -> pytorch-cuda[version='>=11.8,<11.9'] -> cuda-nvtx[version='>=11.7,<11.8|>=11.8,<12.0']
pytorch-cuda=11.8 -> cuda-nvtx[version='>=11.8,<12.0']

Package typing conflicts for:
pytorch -> typing_extensions -> typing[version='>=3.6.2|>=3.7.4']
pytorch -> typing

Package libbrotlicommon conflicts for:
brotli -> libbrotlidec==1.1.0=hd590300_0 -> libbrotlicommon[version='1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.1.0',build='h5eee18b_7|h7f98852_6|h166bdaf_8|h166bdaf_9|hd590300_0|h166bdaf_7|h7f98852_5']
libbrotlienc -> libbrotlicommon[version='1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.1.0',build='h5eee18b_7|h7f98852_6|h166bdaf_8|h166bdaf_9|hd590300_0|h166bdaf_7|h7f98852_5']
libbrotlidec -> libbrotlicommon[version='1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.1.0',build='h5eee18b_7|h7f98852_6|h166bdaf_8|h166bdaf_9|hd590300_0|h166bdaf_7|h7f98852_5']
brotli-bin -> libbrotlidec==1.1.0=hd590300_0 -> libbrotlicommon[version='1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.0.9|1.1.0',build='h5eee18b_7|h7f98852_6|h166bdaf_8|h166bdaf_9|hd590300_0|h166bdaf_7|h7f98852_5']

Package brotli conflicts for:
requests -> urllib3[version='>=1.21.1,<3'] -> brotli[version='>=1.0.9']
urllib3 -> brotli[version='>=1.0.9']

Package cffi conflicts for:
pytorch -> cffi
torchaudio -> pytorch==2.0.1 -> cffi
urllib3 -> brotlipy[version='>=0.6.0'] -> cffi[version='!=1.11.3,>=1.8|>=1.0.0|>=1.12|>=1.8,!=1.11.3|>=1.7|>=1.8']
torchvision -> pytorch==2.0.1 -> cffi

Package charset-normalizer conflicts for:
torchvision -> requests -> charset-normalizer[version='>=2,<3|>=2,<4|>=2.0.0,<2.1|>=2.0.0,<2.0.1|>=2.0.0,<3|>=2.0.0,<2.1.0']
requests -> charset-normalizer[version='>=2,<3|>=2,<4|>=2.0.0,<2.1|>=2.0.0,<2.0.1|>=2.0.0,<3|>=2.0.0,<2.1.0']

Package pysocks conflicts for:
requests -> urllib3[version='>=1.21.1,<3'] -> pysocks[version='>=1.5.6,<2.0,!=1.5.7']
urllib3 -> pysocks[version='>=1.5.6,<2.0,!=1.5.7']

Package xorg-libxdmcp conflicts for:
pillow -> libxcb[version='>=1.15,<1.16.0a0'] -> xorg-libxdmcp
libxcb -> xorg-libxdmcp

Package wheel conflicts for:
pip -> wheel
python=3.7.5 -> pip -> wheel

Package pthread-stubs conflicts for:
libxcb -> pthread-stubs
pillow -> libxcb[version='>=1.15,<1.16.0a0'] -> pthread-stubs

Package cuda-cudart_linux-64 conflicts for:
cuda-libraries -> cuda-cudart=12.0.107 -> cuda-cudart_linux-64==12.0.107[build='h59595ed_2|h59595ed_6|h59595ed_5']
cuda-cudart -> cuda-cudart_linux-64==12.0.107[build='h59595ed_2|h59595ed_6|h59595ed_5']The following specifications were found to be incompatible with your system:

  - feature:/linux-64::__cuda==12.2=0
  - feature:/linux-64::__glibc==2.35=0
  - feature:/linux-64::__unix==0=0
  - feature:|@/linux-64::__cuda==12.2=0
  - feature:|@/linux-64::__glibc==2.35=0
  - feature:|@/linux-64::__unix==0=0
  - blas -> libgfortran-ng -> __glibc[version='>=2.17']
  - brotli -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - brotli-bin -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - bzip2 -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - cuda-cudart -> __glibc[version='>=2.17,<3.0.a0']
  - cuda-libraries -> cuda-cudart=12.0.107 -> __glibc[version='>=2.17,<3.0.a0']
  - cuda-nvrtc -> __glibc[version='>=2.17,<3.0.a0']
  - cudatoolkit=11.1 -> __glibc[version='>=2.17,<3.0.a0']
  - cudatoolkit=11.1 -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - ffmpeg -> libgcc-ng[version='>=7.3.0'] -> __glibc[version='>=2.17']
  - freetype -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - gmp -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - gnutls -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - icu -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - jpeg -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - lame -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - lcms2 -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - lerc -> libgcc-ng[version='>=9.4.0'] -> __glibc[version='>=2.17']
  - libblas -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libbrotlicommon -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - libbrotlidec -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - libbrotlienc -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - libcblas -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libcublas -> __glibc[version='>=2.17,<3.0.a0']
  - libcufft -> __glibc[version='>=2.17,<3.0.a0']
  - libcufile -> __glibc[version='>=2.17,<3.0.a0']
  - libcurand -> __glibc[version='>=2.17,<3.0.a0']
  - libcusolver -> __glibc[version='>=2.17,<3.0.a0']
  - libcusparse -> __glibc[version='>=2.17,<3.0.a0']
  - libdeflate -> libgcc-ng[version='>=9.4.0'] -> __glibc[version='>=2.17']
  - libffi -> libgcc-ng[version='>=9.4.0'] -> __glibc[version='>=2.17']
  - libgcc-ng -> __glibc[version='>=2.17']
  - libgfortran-ng -> __glibc[version='>=2.17']
  - libhwloc -> __cuda
  - libhwloc -> __glibc[version='>=2.17']
  - libhwloc -> cudatoolkit[version='>=11.2,<12'] -> __glibc[version='>=2.17,<3.0.a0']
  - libiconv -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - liblapack -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - liblapacke -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - libnpp -> __glibc[version='>=2.17,<3.0.a0']
  - libpng -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - libstdcxx-ng -> __glibc[version='>=2.17']
  - libtiff -> libgcc-ng[version='>=9.4.0'] -> __glibc[version='>=2.17']
  - libwebp-base -> libgcc-ng[version='>=9.4.0'] -> __glibc[version='>=2.17']
  - libxcb -> libgcc-ng[version='>=9.4.0'] -> __glibc[version='>=2.17']
  - libxml2 -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - libzlib -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - llvm-openmp -> libgcc-ng[version='>=7.3.0'] -> __glibc[version='>=2.17']
  - mkl -> libgcc-ng[version='>=11.2.0'] -> __glibc[version='>=2.17']
  - ncurses -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - nettle -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - numpy -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - openh264 -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - openjpeg -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - openssl -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - pillow -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - pthread-stubs -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - pysocks -> __unix
  - pysocks -> __win
  - python=3.7.5 -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - pytorch -> __cuda[version='>=11.8']
  - pytorch -> __glibc[version='>=2.17|>=2.17,<3.0.a0']
  - pytorch -> nccl[version='>=2.14.3.1,<3.0a0'] -> __cuda[version='10.2|10.2.*|11.0|11.0.*|>=11.2,<12|11.1|11.1.*']
  - pytorch -> sympy -> __unix
  - readline -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - sqlite -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - tbb -> libhwloc[version='>=2.9.2,<2.9.3.0a0'] -> __cuda
  - tbb -> libhwloc[version='>=2.9.2,<2.9.3.0a0'] -> __glibc[version='>=2.17']
  - torchaudio -> pytorch==2.0.0 -> __glibc[version='>=2.17|>=2.17,<3.0.a0']
  - torchaudio -> pytorch==2.0.1 -> __cuda[version='>=11.8']
  - torchvision -> __glibc[version='>=2.17|>=2.17,<3.0.a0']
  - torchvision -> pytorch==2.0.1 -> __cuda[version='>=11.8']
  - urllib3 -> pysocks[version='>=1.5.6,<2.0,!=1.5.7'] -> __unix
  - urllib3 -> pysocks[version='>=1.5.6,<2.0,!=1.5.7'] -> __win
  - xorg-libxau -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - xorg-libxdmcp -> libgcc-ng[version='>=9.3.0'] -> __glibc[version='>=2.17']
  - xz -> libgcc-ng[version='>=7.5.0'] -> __glibc[version='>=2.17']
  - zlib -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']
  - zstd -> libgcc-ng[version='>=10.3.0'] -> __glibc[version='>=2.17']

Your installed version is: 2.35

Note that strict channel priority may have removed packages required for satisfiability.
