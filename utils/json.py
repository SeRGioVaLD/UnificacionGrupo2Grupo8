from sqlalchemy.orm import class_mapper

def model_to_dict(obj):
    data = {}
    for column in class_mapper(obj.__class__).mapped_table.columns:
        data[column.name] = getattr(obj, column.name)
    return data