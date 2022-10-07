from admin_section.models import *
# h = header.objects.filter(id=1).first()
# f = site_footer.objects.filter(id=1).first()
# m = menus.objects.filter(menu_type='main', menu_status=True).first()

def header_renderer(request):
    h1 = ''
    f1 = ''
    m1 = ''
    try:
        h_dict = []
        f_dict = []
        m=menus.objects.filter(menu_type='main', menu_status=True).first(),
        ml = menu_links.objects.filter(menu=m[0].id, link_status=True).order_by('sequence').all()
        for l in ml:
            sl = sub_menu_links.objects.filter(link_parent=l.id, link_status=True).order_by('sequence').all()
            h_dict.append({'menu':l,'sub_links':sl})
        return {
            'h': header.objects.filter(id=1).first(),
            'f': site_footer.objects.filter(id=1).first(),
            'm': h_dict,
        }
    except Exception as e:
        print(e)
        return {
            'h': h1,
            'f': f1,
            'm': m1,
        }

# def mains(request):
#     CLP=''
#     try:
#         CLP=Category.objects.get(category_name="CLP")
#         return {'mains': Main_Course.objects.filter(category_name=CLP)}
#     except Exception as e:
#         print(e)
#         return {'mains': CLP}

# def dlp_course(request):
#     DLP=''
#     try:
#         DLP=Category.objects.get(category_name="DLP")
#         return {'dlp_course': Main_Course.objects.filter(category_name=DLP)}
#     except Exception as e:
#         print(e)  
#         return {'dlp_course': DLP}  
    


# def aits_course(request):
#     AITS=''
#     try:
#         AITS=Category.objects.get(category_name="AITS")
#         return {'aits_course': Main_Course.objects.filter(category_name=AITS)}
#     except Exception as e:
#         print(e)
#         return {'aits_course': AITS }

# def allmess(request):
#     allmess=''
#     try:
#         return {'allmess':message_from.objects.all()}
#     except Exception as e:
#         print(e)
#         return {'allmess': allmess}

# def PopupImage(request):
#     popups=''
#     try:
#         return {'popups':PopupImage.objects.all()}
#     except Exception as e:
#         print(e)
#         return {'popups': popups}