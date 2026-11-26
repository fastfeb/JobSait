import os



def company_logo_upload_path(instance, filename):
    return os.path.join('company_logos/', str(instance.owner.id), filename )