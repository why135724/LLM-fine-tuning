import json,os
# CUDA_VISIBLE_DEVICES=2 python create_humaneval.py
# 示例数据，通常你会有自己的数据生成或处理逻辑
# cd /mnt/data/train/LLM-FineTune-final/
# CUDA_VISIBLE_DEVICES=2 python create_humaneval.py
# 读取大模型预测结果
import json
# conda activate hywunew
import json
# 打开jsonl文件

base_dir = os.path.dirname(os.path.abspath(__file__)) # 脚本工程文件根目录, xx/LLM-Finetune/


data = []
with open('human-eval-v2-20210705.jsonl', 'r', encoding='utf-8') as file:
    for line in file:
        # 尝试解析每一行的JSON数据
        temp = json.loads(line)
        # 打印或处理解析后的数据
        array = {}
        print(temp)
        array['text'] = temp['prompt']
        array['category'] = ['0', '1']
        array['output'] = temp['canonical_solution']
        data.append(array)

with open(os.path.join(base_dir, 'data/train_humaneval.jsonl'), 'w', encoding='utf-8') as file:
    for item in data:
        # 将每个字典对象转换为JSON字符串，并写入文件
        json.dump(item, file, ensure_ascii=False)
        # 每个JSON对象后面跟一个换行符
        file.write('\n')