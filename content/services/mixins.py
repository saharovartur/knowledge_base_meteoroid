# from django.contrib.auth.mixins import AccessMixin
# from django.contrib import messages
# from django.shortcuts import redirect
#
#
# class CompanyRequiredMixin(AccessMixin):
#     """Кастомный миксин для просмотра  статей компании"""
#
#     def dispatch(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return self.handle_no_permission()
#
#         if request.user.is_authenticated:
#             if not (request.profile.user == self.get_object().company):
#                 messages.info(request, 'Просмотр доступен только сотруднику компании')
#                 return redirect('')
#         return super().dispatch(request, *args, **kwargs)