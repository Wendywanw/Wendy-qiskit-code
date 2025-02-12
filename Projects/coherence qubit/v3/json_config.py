import json
from qiskit_metal import Dict
from typing import Union, Any

def dict_to_lists(input_dict: dict, num_repeats: int) -> dict:
    """Convert nested dictionary values to lists"""
    if isinstance(input_dict, dict):
        return {k: dict_to_lists(v, num_repeats) for k, v in input_dict.items()}
    elif isinstance(input_dict, (list, tuple)):
        return [dict_to_lists(item, num_repeats) for item in input_dict]
    else:
        return [input_dict] * num_repeats

def save_config(data: dict, filepath: str) -> None:
    """Save configuration to JSON file"""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def load_config(filepath: str, index: int = None) -> Dict:
    """Load configuration from JSON file"""
    with open(filepath, 'r') as f:
        data = json.load(f)
    if index is not None:
        data = extract_index(data, index)
    return Dict(data)

def extract_index(data: dict, index: int) -> dict:
    """Extract specific index from nested lists"""
    if isinstance(data, dict):
        return {k: extract_index(v, index) for k, v in data.items()}
    elif isinstance(data, list):
        return data[index]
    return data

def update_nested(data: dict, key_path: str, value: Any, index: int = None) -> dict:
    """Update nested dictionary at path"""
    keys = key_path.split('.')
    current = data
    for key in keys[:-1]:
        current = current.setdefault(key, {})
    
    if index is not None:
        if not isinstance(current[keys[-1]], list):
            current[keys[-1]] = [current[keys[-1]]] * 3
        current[keys[-1]][index] = value
    else:
        current[keys[-1]] = value
    return data

def update_config(json_file: str, updates: dict, qubit_index: int = None) -> Dict:
    """Update JSON configuration"""
    config = load_config(json_file)
    for path, value in updates.items():
        config = update_nested(config, path, value, qubit_index)
    save_config(config, json_file)
    return Dict(config)
