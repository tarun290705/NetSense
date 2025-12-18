def build_feature_payload(packet, flow_features):
    src_ip = packet["IP"].src
    dst_ip = packet["IP"].dst
    protocol = packet["IP"].proto
    length = len(packet)

    proto_map = {6: "tcp", 17: "udp", 1: "icmp"}
    proto_name = proto_map.get(protocol, "other")

    return {
        "src_ip": src_ip,
        "dst_ip": dst_ip,
        "protocol": proto_name,
        "length": length,
        "features": flow_features
    }
