def get_all_file_inside(path):
    from pathlib import Path

    return [str(x) for x in Path(path).glob("**/*") if x.is_file()]


def makedirs_parent(path):
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True)


def thang_tqdm(iterator, is_vanilla=True):
    if is_vanilla:
        from tqdm import tqdm
    else:
        from tqdm.rich import tqdm
    return tqdm(iterator, total=len(iterator))


def thang_update_tqdm_i(progress_bar, dict_content):
    progress_bar.set_postfix(dict_content)


def open_as_json(path):
    import json

    return json.load(open(path))


def save_as_json(obj, path=""):
    import json

    if path == "":
        path = "tmp.json"
    with open(path, "w") as f:
        json.dump(obj, f, indent=4)


def re_search(string, pattern, group=0):
    # if group = 0, return the whole match.
    """
    match_object = re.match(r'(\w+)@(\w+)\.(\w+)', 'username@geekforgeeks.org')

     w in above pattern stands for alphabetical character
        + is used to match a consecutive set of characters
        satisfying a given condition
        so w+ will match a consecutive set of alphabetical characters

    # for entire match
    print(match_object.group())
    # also print(match_object.group(0)) can be used

    # for the first parenthesized subgroup
    print(match_object.group(1))

    # for the second parenthesized subgroup
    print(match_object.group(2))

    # for the third parenthesized subgroup
    print(match_object.group(3))

    # for a tuple of all matched subgroups
    print(match_object.group(1, 2, 3))

    username@geekforgeeks.org
    username
    geekforgeeks
    org
    ('username', 'geekforgeeks', 'org')
    """

    import re

    if match_object := re.search(pattern, string):
        return match_object.group(group)
    else:
        return "Not Found!"


def give_quick_stat_of_this_list(a):
    import numpy as np

    # Convert lengths to a numpy array
    a_array = np.array(a)

    # Calculate statistics
    max_length = np.max(a_array)
    min_length = np.min(a_array)
    quartiles = np.percentile(a_array, [25, 50, 75])

    # Print statistics
    print(f"Max: {max_length}")
    print(f"Min: {min_length}")
    print(f"Mean: {a_array.mean()}")
    print(f"25th percentile (Q1): {quartiles[0]}")
    print(f"50th percentile (Median): {quartiles[1]}")
    print(f"75th percentile (Q3): {quartiles[2]}")


def give_a_number_between_0_1_uniform():
    import random

    return random.random()


def split_train_test(train_ratio):
    import random

    return "train" if random.random() < train_ratio else "test"


def remove_dup_item(list_item):
    return list(set(list_item))


def copy_to_directory(path1, dir_path):
    import os
    import shutil

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    shutil.copy(path1, dir_path)


def copy_to_new_path(path1, path2):
    import shutil

    shutil.copy(path1, path2)


def os_makedirs_exist_ok(path):
    import os

    os.makedirs(path, exist_ok=True)


def get_infinite_dict():
    from collections import defaultdict

    return defaultdict(lambda: defaultdict(dict))


def read_text_from_file_strip_merge(path):
    return "".join([x.strip() for x in open(path).readlines()])


def get_infinite_dict_list():
    """For when you need nested dicts that default to lists

    Example:
    data = get_infinite_dict_list()
    data['patients']['john']['symptoms'].append('fever')
    data['patients']['jane']['symptoms'].append('cough')
    # No KeyError, automatically creates nested structure
    """
    from collections import defaultdict

    return defaultdict(lambda: defaultdict(list))


def get_infinite_dict_set():
    """For when you need nested dicts that default to sets

    Example:
    tags = get_infinite_dict_set()
    tags['medical']['ct_scans'].add('lung')
    tags['medical']['ct_scans'].add('heart')
    tags['medical']['ct_scans'].add('lung')  # Duplicate ignored
    # Result: tags['medical']['ct_scans'] = {'lung', 'heart'}
    """
    from collections import defaultdict

    return defaultdict(lambda: defaultdict(set))


def get_infinite_dict_counter():
    """For when you need nested dicts that default to counters

    Example:
    counts = get_infinite_dict_counter()
    counts['md1']['recording1']['slice_thickness'][1.0] += 1
    counts['md1']['recording1']['slice_thickness'][1.25] += 1
    counts['md1']['recording1']['slice_thickness'][1.0] += 1
    # Result: counts['md1']['recording1']['slice_thickness'] = Counter({1.0: 2, 1.25: 1})
    """
    from collections import Counter, defaultdict

    return defaultdict(lambda: defaultdict(Counter))


def safe_get(dictionary, *keys, default=None):
    """Safely get nested dictionary values without KeyError

    Example:
    data = {'md1': {'recording1': {'series1': {'thickness': 1.0}}}}

    # Instead of this (which might raise KeyError):
    # thickness = data['md1']['recording1']['series1']['thickness']

    # Use this (safe):
    thickness = safe_get(data, 'md1', 'recording1', 'series1', 'thickness', default=0.0)
    missing = safe_get(data, 'md1', 'recording999', 'series1', default='Not found')
    """
    for key in keys:
        if isinstance(dictionary, dict) and key in dictionary:
            dictionary = dictionary[key]
        else:
            return default
    return dictionary


def safe_set(dictionary, *keys, value):
    """Safely set nested dictionary values, creating intermediate dicts

    Example:
    data = {}
    # Instead of manually creating nested structure:
    # data['md1'] = {}
    # data['md1']['recording1'] = {}
    # data['md1']['recording1']['series1'] = {}
    # data['md1']['recording1']['series1']['thickness'] = 1.0

    # Use this:
    safe_set(data, 'md1', 'recording1', 'series1', 'thickness', 1.0)
    # Result: data = {'md1': {'recording1': {'series1': {'thickness': 1.0}}}}
    """
    for key in keys[:-1]:
        if key not in dictionary:
            dictionary[key] = {}
        dictionary = dictionary[key]
    dictionary[keys[-1]] = value


def flatten_dict(d, parent_key="", sep="_"):
    """Flatten nested dictionary

    Example:
    nested = {
        'md1': {
            'recording1': {
                'series1': {'thickness': 1.0, 'slices': 100}
            }
        }
    }
    flat = flatten_dict(nested)
    # Result: {'md1_recording1_series1_thickness': 1.0, 'md1_recording1_series1_slices': 100}

    # Useful for pandas DataFrame creation or CSV export
    import pandas as pd
    df = pd.DataFrame([flat])
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def dict_to_namespace(d):
    """Convert dict to namespace for dot notation access

    Example:
    config = {
        'model': {
            'learning_rate': 0.001,
            'batch_size': 32
        },
        'data': {
            'path': '/home/data'
        }
    }

    ns = dict_to_namespace(config)
    # Now you can use dot notation:
    print(ns.model.learning_rate)  # 0.001
    print(ns.data.path)           # '/home/data'

    # Instead of:
    # print(config['model']['learning_rate'])
    """
    import types

    ns = types.SimpleNamespace()
    for key, value in d.items():
        if isinstance(value, dict):
            setattr(ns, key, dict_to_namespace(value))
        else:
            setattr(ns, key, value)
    return ns


def merge_dicts(*dicts):
    """Deep merge multiple dictionaries

    Example:
    base_config = {
        'model': {'lr': 0.001, 'epochs': 100},
        'data': {'batch_size': 32}
    }
    user_config = {
        'model': {'lr': 0.01},  # Override learning rate
        'logging': {'level': 'INFO'}  # Add new section
    }

    final_config = merge_dicts(base_config, user_config)
    # Result: {
    #     'model': {'lr': 0.01, 'epochs': 100},  # lr overridden, epochs kept
    #     'data': {'batch_size': 32},
    #     'logging': {'level': 'INFO'}
    # }
    """

    def _merge_two(dict1, dict2):
        result = dict1.copy()
        for key, value in dict2.items():
            if (
                key in result
                and isinstance(result[key], dict)
                and isinstance(value, dict)
            ):
                result[key] = _merge_two(result[key], value)
            else:
                result[key] = value
        return result

    result = {}
    for d in dicts:
        result = _merge_two(result, d)
    return result


def pretty_print_dict(d, indent=0):
    """Pretty print nested dictionary

    Example:
    data = {'md1': {'recording1': {'series1': {'thickness': 1.0, 'slices': 100}}}}
    pretty_print_dict(data)
    # Output:
    # md1:
    #   recording1:
    #     series1:
    #       thickness:
    #         1.0
    #       slices:
    #         100

    # Much more readable than: print(data)
    """
    for key, value in d.items():
        print("  " * indent + str(key) + ":")
        if isinstance(value, dict):
            pretty_print_dict(value, indent + 1)
        else:
            print("  " * (indent + 1) + str(value))


def get_dict_size(d):
    """Get total number of leaf values in nested dict

    Example:
    data = {
        'md1': {
            'rec1': {'s1': 1.0, 's2': 2.0},
            'rec2': {'s3': 3.0}
        },
        'md2': {
            'rec1': {'s1': 4.0}
        }
    }
    size = get_dict_size(data)  # Returns 4 (four leaf values)

    # Useful for progress bars or memory estimation
    """
    count = 0
    for value in d.values():
        if isinstance(value, dict):
            count += get_dict_size(value)
        else:
            count += 1
    return count


def ensure_list(item):
    """Ensure item is a list

    Example:
    # When processing user input that might be single item or list:
    def process_files(files):
        files = ensure_list(files)  # Now always a list
        for file in files:
            print(f"Processing {file}")

    process_files("single_file.txt")     # Works
    process_files(["file1.txt", "file2.txt"])  # Works
    process_files(None)                  # Returns []
    """
    if isinstance(item, list):
        return item
    elif item is None:
        return []
    else:
        return [item]


def chunk_list(lst, chunk_size):
    """Split list into chunks of specified size

    Example:
    # Process large file list in batches
    all_files = list(range(100))  # [0, 1, 2, ..., 99]

    for batch in chunk_list(all_files, 10):
        print(f"Processing batch: {batch}")
        # Process 10 files at a time

    # First batch: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Second batch: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    # ... and so on
    """
    return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]


def unique_preserve_order(lst):
    """Remove duplicates while preserving order

    Example:
    # Regular set() doesn't preserve order:
    original = ['apple', 'banana', 'apple', 'cherry', 'banana']

    # This preserves order:
    unique = unique_preserve_order(original)
    # Result: ['apple', 'banana', 'cherry']

    # Useful when order matters (like processing pipeline steps)
    processing_steps = ['preprocess', 'augment', 'preprocess', 'train']
    steps = unique_preserve_order(processing_steps)
    # Result: ['preprocess', 'augment', 'train']
    """
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]
