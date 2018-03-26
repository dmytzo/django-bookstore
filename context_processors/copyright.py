from django.template.context_processors import request


def site_copyright(request):
    return {
        "copyright_start": "2017",
        "copyright_end": "2018"
    }