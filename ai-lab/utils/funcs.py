"""
Utility functions
"""


def build_path(node):
    """
    Builds a path going backward from a node

    Args:
        node: node to start from

    Returns:
        path from root to ``node``
    """
    path = []
    while node.parent is not None:
        path.append(node.state)
        node = node.parent
    return tuple(reversed(path))
