from dataclasses import dataclass
from pathlib import Path


@dataclass()
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    unzip_dir: Path
    local_data_file:Path



@dataclass
class PrepareBaseModelConfig:
    root_dir: Path
    base_model: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
