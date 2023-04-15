from typing import Mapping, List, Dict, Tuple
import re


KEY_VAL_CELL_PATTERN = r'"(?P<key>\w+)":\s+"(?P<value>\w+)"'


def key_val_to_cell(key: str, val: str) -> str:
    return f'"{str(key)}": "{str(val)}"'


def cell_to_key_val(cell: str) -> Tuple[str, str]:
    match = re.search(KEY_VAL_CELL_PATTERN, cell)
    if match:
        return match.group('key'), match.group('value')
    else:
        raise ValueError('Could not extract key-value pair from cell.')


def doc_to_row(doc: Mapping) -> List[str]:
    row = []
    for key, val in doc.items():
        row.append(key_val_to_cell(str(key), str(val)))
    return row


def row_to_doc(row: List[str]) -> Dict[str, str]:
    doc = {}
    for cell in row:
        key, val = cell_to_key_val(cell)
        doc[key] = val
    return doc
