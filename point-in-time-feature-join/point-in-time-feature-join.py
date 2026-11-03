def point_in_time_join(events: list, feature_rows: list, ttl: int) -> list:
    """
    Returns one dictionary per event with the feature value that was known at that time.
    """
    output = []
    for i, event in enumerate(events):
        candidates = []
        entity_out = {"entity_id": event["entity_id"], "timestamp": event["timestamp"], "value": None}
        for feat in feature_rows:
            if event["entity_id"] == feat["entity_id"]:
                if feat["timestamp"] <= event["timestamp"] and (event["timestamp"] - feat["timestamp"]) <= ttl :
                    candidates.append(feat["timestamp"])
                    entity_out["entity_id"] = event["entity_id"]
                    entity_out["timestamp"] = event["timestamp"]
                    entity_out["value"] = next((ft["value"] for ft in feature_rows if ft["timestamp"] == max(candidates)), None)
                elif not entity_out:
                    entity_out["entity_id"] = event["entity_id"]
                    entity_out["timestamp"] = event["timestamp"]
                    entity_out["value"] = None

    
        output.append(entity_out)
        
    return output
        