from modelscope import snapshot_download
import os
base_dir = os.path.dirname(os.path.abspath(__file__)) # xx/LLM-Finetune/

#  qwen -- codeqwen1.5-7b-chat / Qwen2-7b / Qwen2.5-7B-Instruct / qwen2.5-coder-7b-instruct
#  swift -- llava-1.5-7b-hf
model_id = snapshot_download('qwen/qwen2.5-coder-7b-instruct', local_dir=os.path.join(base_dir, 
                                    'PretrainModels/qwen2.5-coder-7b-instruct/'))


# model_dir = snapshot_download('skyline2006/llama-7b')
