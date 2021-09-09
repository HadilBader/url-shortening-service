import numpy


# TODO: consider using get_current_site(request) from from django.contrib.sites.models import Site instead
def encode_url(host_address, url_id):
    base36_id = numpy.base_repr(url_id, 36)
    return f'{host_address}{base36_id}'
