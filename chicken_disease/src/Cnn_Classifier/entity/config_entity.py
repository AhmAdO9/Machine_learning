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



@dataclass
class PrepareCallbacksConfig:
    root_dir: Path
    checkpoint_model_filepath: Path



@dataclass
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmented: bool
    params_image_size: list
