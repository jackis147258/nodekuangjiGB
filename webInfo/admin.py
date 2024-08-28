from django.contrib import admin
from app1.models import webInfo
# Register your models here.

# from import_export.admin import ExportActionModelAdmin
from django.http import HttpResponse, JsonResponse
# from simplepro.dialog import ModalDialog
from simpleui.admin import AjaxAdmin



@admin.register(webInfo) 
class T_webInfoAdmin(AjaxAdmin):    
     #    列表部分
    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     accUser = request.user 
    #     # 在此处添加任何过滤逻辑
    #     queryset = queryset.filter(uid=accUser.id)
    #     return queryset
    
    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         # 如果是创建新的对象，为 uid 字段设置当前登录的用户
    #         obj.uid = request.user
    #     super().save_model(request, obj, form, change)
    
    
    #    列表部分  'status',
    
    # list_display = ('TRADE_TOKEN_ADDRESS','buyPrice', 'sellPrice','taskLog', 'get_run','taskClose',
    #                   'USDT_TOKEN_ADDRESS', 'WBNB_ADDRESS', 'LP_ymiiUsdt_ADDRESS', 'Tools_lpPrice_ADDRESS', 
    #                  'PANCAKE_ROUTER_ADDRESS', 'Bnb_TokenGas', 'buyNumberTotal',  'coinsRecharge', 'AmountBuy0', 'AmountBuy1',
    #                  'AmountSell0', 'AmountSell1', 'Token_Transaction_Time', 'PercentBuy','PercenttSell',
    #                 )
    
    list_display = ('webName','status', 'cn_memo', 'created_at')
    
    # list_editable = ('buyPrice','sellPrice',)
    
    date_hierarchy = 'created_at'
    
    list_per_page = 15
    
    # actions = ('layer_input','layer_close',perform_check_all)
    
    # actions = [export_excel ]
     
    
       
    # def taskLog(self, obj):
        
    #     parameter_str = '{}'.format(str(obj.id) )
    #     btn_str = '<a class="btn btn-xs btn-danger" target="_blank" href="{}">' \
    #               '<input name="查看明细"' \
    #               'type="button" id="passButton" ' \
    #               'title="passButton" value="查看明细">' \
    #               '</a>'
    #     return format_html(btn_str, '/app1/showlog/{}/'.format(parameter_str))
    # taskLog.short_description = '明细'

   
    
    