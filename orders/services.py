import uuid


def generate_order_number():

    return f"ORD-{str(uuid.uuid4())[:8].upper()}"