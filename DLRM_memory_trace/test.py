import pandas as pd
import numpy as np
import torch
import torch.nn as nn

# 假设数据集如下：
data = {
    'user_id': [1, 2, 3, 1, 2],
    'item_id': [5, 6, 7, 5, 8]
}

# 创建DataFrame
df = pd.DataFrame(data)

# 计算唯一的用户和商品数量
num_unique_users = df['user_id'].nunique()
num_unique_items = df['item_id'].nunique()

# 嵌入向量的维度（通常是一个超参数，需要根据实际情况调整）
embedding_dim = 5

# 创建嵌入层
user_embedding_layer = nn.Embedding(num_embeddings=num_unique_users, embedding_dim=embedding_dim)
item_embedding_layer = nn.Embedding(num_embeddings=num_unique_items, embedding_dim=embedding_dim)

# 将用户ID和商品ID转换为嵌入向量
user_ids = torch.LongTensor(df['user_id'].values)  # 假设用户ID从1开始
item_ids = torch.LongTensor(df['item_id'].values)  # 假设商品ID从5开始

print(user_ids, item_ids)

# 由于实际的索引是从0开始的，我们需要调整ID
user_ids = user_ids - 1
item_ids = item_ids - 5

print(user_ids, item_ids)
# 查找嵌入向量
user_embeddings = user_embedding_layer(user_ids)
item_embeddings = item_embedding_layer(item_ids)

print(user_embedding_layer.weight, item_embedding_layer.weight)

# 显示嵌入向量
print("User Embeddings:")
print(user_embeddings)
print("\nItem Embeddings:")
print(item_embeddings)
