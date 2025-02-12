wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh -u
source ~/.bashrc
conda create -n rwkv python=3.10
conda activate rwkv

pip install torch --upgrade --extra-index-url https://download.pytorch.org/whl/cu121
pip install pytorch-lightning==1.9.5 deepspeed wandb ninja --upgrade
pip install bitsandbytes einops triton rwkv-fla rwkv transformers GPUtil plotly gradio datasets
pip install pandas ujson