"""
Contains functionality for creating PyTorch DataLoaders for 
cow weight image data.
"""

import pandas as pd
from datasets import Dataset, Image as CImage
import torch
from torchvision import transforms
from torch.utils.data import DataLoader


IMG_DIR = ""
TRANSFORM_IMG = transforms.Compose([transforms.Resize((224,224)),
                                     transforms.ToTensor()])

def prepare_data(csv_addr):
    df = pd.read_csv(csv_addr)

    df["sku"] = df["sku"].apply(lambda x: f"{IMG_DIR}/{x}/{x}_0.jpg")
    min_weight = min(df['weight_in_kg'])
    max_weight = max(df['weight_in_kg'])
    # weight minmax normalization
    df['weight_in_kg'] = df['weight_in_kg'].apply(lambda x: (x-min_weight)/(max_weight-min_weight))
    return df


def huggingface_dataset(df):
    image_name = df['sku']
    cow_weight = df['weight_in_kg']
    ds = Dataset.from_dict({"image":image_name, 
                            "weights":cow_weight})
    #convert img address to Image type
    ds = ds.cast_column('image', CImage())
    return ds

def collate_fn(batch):
    """
    batch making function
    """
    images = torch.stack([TRANSFORM_IMG(item["image"]) for item in batch]) 
    weights = torch.tensor([item["weights"] for item in batch],
                            dtype=torch.float32)
    return images, weights


def get_loaders(ds):

    dataloader_train = DataLoader(ds['train'], collate_fn=collate_fn, batch_size=64, shuffle=True)

    dataloader_val = DataLoader(ds['test'], collate_fn=collate_fn, batch_size=64, shuffle=True)
    
    return dataloader_train, dataloader_val



