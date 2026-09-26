def generate_anchors(feature_size: int, image_size: float, scales: list[float], aspect_ratios: list[float]) -> list[list[float]]:
    """
    Returns a list of [x1, y1, x2, y2] anchor boxes.
    """
    # Write code here
    stride = image_size / feature_size
    anchor_boxes = []
    for i in range(feature_size):
        for j in range(feature_size):
            for s in scales:
                for r in aspect_ratios:
                    cx = (j + 0.5) * stride
                    cy = (i + 0.5) * stride
                    w = s * (r ** 0.5)
                    h = s / (r ** 0.5)
                    print(w,h)

                    box = [cx - w/2, cy - h/2, cx + w/2, cy + h/2]
                    anchor_boxes.append(box)
                    
    return anchor_boxes
                
                    