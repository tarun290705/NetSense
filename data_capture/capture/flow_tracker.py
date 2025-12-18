import time
from collections import defaultdict

flows = defaultdict(lambda: {
    "start_time": time.time(),
    "spkts": 0,
    "dpkts": 0,
    "sbytes": 0,
    "dbytes": 0
})

def update_flow(src, dst, proto, length):
    key = (src, dst, proto)
    flow = flows[key]

    flow["spkts"] += 1
    flow["sbytes"] += length

    return key, flow

def finalize_flow(key):
    flow = flows[key]
    duration = time.time() - flow["start_time"]

    features = {
        "dur": round(duration, 3),
        "spkts": flow["spkts"],
        "dpkts": flow["dpkts"],
        "sbytes": flow["sbytes"],
        "dbytes": flow["dbytes"]
    }

    del flows[key]
    return features
