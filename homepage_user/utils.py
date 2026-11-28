


def filtered_objects_with_filter_type(objects, filter_type):

    if filter_type == 'part_time':
        objects = objects.filter(employment_type='part_time')

    elif filter_type == 'full_time':   
        objects = objects.filter(employment_type='full_time')

    elif filter_type == 'internship':
        objects = objects.filter(employment_type='internship')

    elif filter_type == 'remote':
        objects = objects.filter(employment_type='remote')

    elif filter_type == 'contract':
        objects = objects.filter(employment_type='contract')

    return objects










    