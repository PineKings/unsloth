
#模型下载
from modelscope import snapshot_download

# 下载模型到本地路径
model_dir = snapshot_download('Qwen/Qwen3.5-0.8B',local_dir='./checkpoints/Qwen/Qwen3.5-0.8B')