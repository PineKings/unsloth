
#模型下载
from modelscope import snapshot_download

# 下载模型到本地路径
model_dir = snapshot_download('google/gemma-4-E2B-it',local_dir='./checkpoints/google/gemma-4-E2B-it')