#!/bin/python3
import sys


def transform_ip(block: str) -> str:
    """
    Returns the transformed filters from a list of IPs.

    >>> transform_ip("localhost:65535,udp")
    '(host localhost and port 65535 and (udp))'
    >>> transform_ip("10.28.24.100:65535")
    '(host 10.28.24.100 and port 65535)'
    >>> transform_ip("*:80,tcp")
    '(port 80 and (tcp))'
    """
    if "," in block:
        addr, other_filters = block.split(",")
    else:
        addr = block
        other_filters = None
    host, port = addr.split(":")
    and_filters = f" and ({other_filters})" if other_filters is not None else ""
    if host == "*":
        return f"(port {port}{and_filters})"
    if port == "*":
        return f"(host {host}{and_filters})"
    return f"(host {host} and port {port}{and_filters})"


if __name__ == "__main__":
    lines = list(map(transform_ip, [line.strip("\n") for line in sys.stdin]))
    print(
        ("(" if len(lines) > 1 else "")
        + f"{' or '.join(lines)}"
        + (")" if len(lines) > 1 else "")
    )
