def list_input(msg, items, default):
    answer = raw_input(msg + " [" + '/'.join(items)+ "]: ")
    while answer and answer not in items:
        answer = raw_input(msg + " [" + '/'.join(items)+ "]: ")
    if not answer:
        answer = default
    return answer
