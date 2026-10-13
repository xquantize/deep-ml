import numpy as np

def non_maximum_suppression(boxes, scores, iou_threshold):
    """
    Apply Non-Maximum Suppression (NMS) to bounding boxes.
    
    Args:
        boxes: Array-like of shape (N, 4) with boxes in format [x1, y1, x2, y2]
        scores: Array-like of shape (N,) with confidence scores
        iou_threshold: float, IoU threshold for suppression (0 to 1)
    
    Returns:
        List of indices of kept boxes, ordered by descending score
        Returns -1 for invalid inputs
    """
    if not isinstance(iou_threshold, (int, float)) or not (0 <= iou_threshold <= 1):
        return -1

    try:
        boxes = np.array(boxes, dtype=float)
        scores = np.array(scores, dtype=float)
    except (ValueError, TypeError):
        return -1

    if boxes.size == 0 and scores.size == 0:
        return []

    if boxes.ndim != 2 or boxes.shape[1] != 4 or scores.ndim != 1:
        return -1

    if boxes.shape[0] != scores.shape[0]:
        return -1

    x1, y1, x2, y2 = boxes[:, 0], boxes[:, 1], boxes[:, 2], boxes[:, 3]
    areas = np.maximum(0, x2 - x1) * np.maximum(0, y2 - y1)

    order = np.argsort(-scores, kind='stable')
    keep = []

    while order.size > 0:
        i = order[0]
        keep.append(int(i))
        rest = order[1:]

        ix1 = np.maximum(x1[i], x1[rest])
        iy1 = np.maximum(y1[i], y1[rest])
        ix2 = np.minimum(x2[i], x2[rest])
        iy2 = np.minimum(y2[i], y2[rest])
        inter = np.maximum(0, ix2 - ix1) * np.maximum(0, iy2 - iy1)

        union = areas[i] + areas[rest] - inter
        iou = np.where(union > 0, inter / np.where(union > 0, union, 1), 0)

        order = rest[iou <= iou_threshold]

    return keep    
