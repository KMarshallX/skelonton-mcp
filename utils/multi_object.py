"""Multi-object decomposition and merge helpers."""

from __future__ import annotations

from typing import List, Sequence, Tuple, cast

import numpy as np
from scipy import ndimage


_FULL_26_STRUCT = np.ones((3, 3, 3), dtype=np.uint8)


def decompose(volume: np.ndarray, min_size: int = 50) -> List[Tuple[int, np.ndarray]]:
    """Decompose volume into 26-connected components.

    Parameters
    ----------
    volume
        Fuzzy or binary input volume in `(z, y, x)` order.
    min_size
        Minimum voxel count required for a component to be kept.

    Returns
    -------
    list
        List of `(component_label, sub_mask)` tuples where `sub_mask` is a
        boolean mask in full-volume coordinates.
    """
    object_mask = np.asarray(volume) > 0
    labeled, num_components = cast(
        Tuple[np.ndarray, int], ndimage.label(object_mask, structure=_FULL_26_STRUCT)
    )

    components: List[Tuple[int, np.ndarray]] = []
    for component_label in range(1, num_components + 1):
        sub_mask = labeled == component_label
        if int(sub_mask.sum()) >= int(min_size):
            components.append((component_label, sub_mask))

    return components


def merge_skeletons(
    shape: Sequence[int],
    results: Sequence[Tuple[int, np.ndarray]],
    label_objects: bool = False,
) -> np.ndarray:
    """Merge per-object skeleton masks into a single volume.

    Parameters
    ----------
    shape
        Output array shape `(z, y, x)`.
    results
        Sequence of `(label, skeleton_mask)` tuples.
    label_objects
        If True, voxels get their object label value; otherwise they are set to 1.

    Returns
    -------
    np.ndarray
        Merged skeleton volume.
    """
    dtype = np.int32 if label_objects else np.uint8
    merged = np.zeros(shape, dtype=dtype)

    for label, skeleton_mask in results:
        mask = np.asarray(skeleton_mask, dtype=bool)
        if label_objects:
            merged[mask] = int(label)
        else:
            merged[mask] = 1

    return merged
