"""
This module includes the utility function encode_url()
"""

import numpy

"""
Given that I limit the url_id to 8 digits, the number of urls that could 
be encoded is ZZZZZZZZ, which is around 78 billion in base 10. I believe 
base-36 is a good choice for this assignment, as it is between base 10
and base 62: it is more compact than base 10, but also does not include 
both uppercase and lowercase letters, unlike base 62, which makes the encoded 
URLs slightly more convenient.
"""


# TODO: consider using get_current_site(request) from from django.contrib.sites.models import Site instead
# TODO: consider generalizing the function
def encode_url(host_address, url_id):
    """
    :host_address: protocol + FQDN. E.g., http://localhost:8000/
    :url_id: base-10 number to encode. E.g., 35
    :returns: host_address concatenated to base 36 representation of url_id. E.g, http://localhost:8000/Z
    """
    base36_id = numpy.base_repr(url_id, 36)
    return f'{host_address}{base36_id}'

