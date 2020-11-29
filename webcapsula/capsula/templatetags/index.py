from django import template
register = template.Library()

@register.filter
def getitem(abouts, i):
    return abouts[int(i)]

@register.filter
def getattr(obj, attr):
    if attr == "image":
        return obj.image.url
    elif attr == "title":
        return obj.title
    elif attr == "subtitle":
        return obj.subtitle
    elif attr == "description":
        return obj.description
    elif attr == "name":
        return obj.name
    elif attr == "linkedin":
        return obj.linkedin
    elif attr == "facebook":
        return obj.facebook
    elif attr == "github":
        return obj.github
    elif attr == "project_name":
        return obj.project_name
    elif attr == "project_data":
        return obj.project_data
    elif attr == "project_date":
        return obj.project_date
    elif attr == "project_image":
        return obj.project_image.url
    elif attr == "project_description":
        return obj.project_description
    elif attr == "project_client":
        return obj.project_client
    elif attr == "project_category":
        return obj.project_category
