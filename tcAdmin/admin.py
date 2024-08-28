from django.contrib import admin
from django.contrib.admin import AdminSite
# Register your models here.
from django.template.response import TemplateResponse
from django.shortcuts import redirect,render




class tcAdminSite(AdminSite):
   

    # Text to put in each page's <h1>.
    site_header = "TcAdmin"
    # Text to put at the top of the admin index page.
    index_title = "TcAdmin"
    
    site_title="tcAdmin"    
    index_template="info.html"
    # index_title="sdafasfd" 
    def index(self, request, extra_context=None):

        if self.index_template=="info.html":

            return redirect('/')
        # return redirect('/info')
        

            # user_count =5
            # task_count = 6

            # userId=request.session.get('_auth_user_id')
        
            # context = { 'user_count': user_count, 'task_count': task_count }
            # return render(request, 'info.html',context)
        
        super().index(request, extra_context=None)


        # """
        # Display the main admin index page, which lists all of the installed
        # apps that have been registered in this site.
        # """
        # app_list = self.get_app_list(request)

        # context = {
        #     **self.each_context(request),
        #     "title": self.index_title,
        #     "subtitle": None,
        #     "app_list": app_list,
        #     **(extra_context or {}),
        #     "dk": "dkdk",
        # }

        # request.current_app = self.name

       

        # return TemplateResponse(
        #     request, self.index_template or "admin/index.html", context
        # )

tcAdmin_site=tcAdminSite(name="tcAdmin")








