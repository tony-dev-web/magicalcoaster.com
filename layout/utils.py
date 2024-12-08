from layout.models import LayoutModel

def LayoutUtils(lang=None):
    return LayoutModel.objects.get(lang=lang)