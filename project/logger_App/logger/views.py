from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from .models import User,Customer,Product,Sale,Repair
from datetime import datetime, timedelta, time
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView
#Login required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.urls import reverse
from django.http import HttpResponseRedirect
import csv
# Create your views here.


#View for main app
@login_required
def index(request):

    '''
    Retrive index view
    '''

    #check if request user is Authenticated
    if request.user.is_superuser:
        return HttpResponseRedirect('/admin')
    elif request.user.is_staff:
        notebook_today = 0
        notebook_week = 0
        notebook_month = 0
        notebook_stats = []
        today = datetime.now().date()
        customer_unrepaired_notebooks = Product.objects.none
        #Retrive Notebooks
        if Product.objects.filter(product_type='Notebook').exists():
            customer_notebooks = Product.objects.filter(product_type='Notebook')
            number_of_notebooks = len(customer_notebooks)

            for notebook in customer_notebooks:
                if notebook.created_at.day == today.day:
                    notebook_today=notebook_today+1
                if notebook.created_at.isocalendar()[1] is today.isocalendar()[1]:
                    notebook_week= notebook_week+1
                if notebook.created_at.month is today.month:
                    notebook_month = notebook_month +1

            notebook_stats.append(notebook_today)
            notebook_stats.append(notebook_week)
            notebook_stats.append(notebook_month)
            #Retrive Unrepaired Notebooks
            if Product.objects.filter(product_type='Notebook',repaired=False).exists():
                customer_unrepaired_notebooks = Product.objects.filter(product_type='Notebook',repaired=False)
                notebook_percentage = int((1 - len(customer_unrepaired_notebooks)/number_of_notebooks)*100)
            else:
                customer_unrepaired_notebooks = Product.objects.none
                notebook_percentage=int(100)
        else:
            notebook_stats.append(notebook_today)
            notebook_stats.append(notebook_week)
            notebook_stats.append(notebook_month)
            notebook_percentage=int(0)

        smartphone_today = 0
        smartphone_week = 0
        smartphone_month = 0
        smartphone_stats = []
        customer_unrepaired_smartphones = Product.objects.none
        #Retrive Smartphones
        if Product.objects.filter(product_type='Smartphone').exists():
            customer_smartphones = Product.objects.filter(product_type='Smartphone')
            number_of_smartphones = len(customer_smartphones)

            for smartphone in customer_smartphones:
                if smartphone.created_at.day == today.day:
                    smartphone_today=smartphone_today+1
                if smartphone.created_at.isocalendar()[1] is today.isocalendar()[1]:
                    smartphone_week= smartphone_week+1
                if smartphone.created_at.month is today.month:
                    smartphone_month = smartphone_month +1

            smartphone_stats.append(smartphone_today)
            smartphone_stats.append(smartphone_week)
            smartphone_stats.append(smartphone_month)
            #Retrive Unrepaired Notebooks
            if Product.objects.filter(product_type='Smartphone',repaired=False).exists():
                customer_unrepaired_smartphones = Product.objects.filter(product_type='Smartphone',repaired=False)
                smartphone_percentage = int((1 - len(customer_unrepaired_smartphones)/number_of_smartphones)*100)
            else:
                customer_unrepaired_smartphones = Product.objects.none
                smartphone_percentage=int(100)

        else:
            smartphone_stats.append(smartphone_today)
            smartphone_stats.append(smartphone_week)
            smartphone_stats.append(smartphone_month)
            smartphone_percentage=int(0)

        tablet_today = 0
        tablet_week = 0
        tablet_month = 0
        tablet_stats = []
        customer_unrepaired_tablets = Product.objects.none
        #Retrive Tablets
        if Product.objects.filter(product_type='Tablet').exists():
            customer_tablets = Product.objects.filter(product_type='Tablet')


            number_of_tablet = len(customer_tablets)

            for tablet in customer_tablets:
                if tablet.created_at.day == today.day:
                    tablet_today=tablet_today+1
                if tablet.created_at.isocalendar()[1] is today.isocalendar()[1]:
                    tablet_week= tablet_week+1
                if tablet.created_at.month is today.month:
                    tablet_month = tablet_month +1

            tablet_stats.append(tablet_today)
            tablet_stats.append(tablet_week)
            tablet_stats.append(tablet_month)

            #Retrive Unrepaired Tablets
            if Product.objects.filter(product_type='Tablet',repaired=False).exists():
                customer_unrepaired_tablets = Product.objects.filter(product_type='Tablet',repaired=False)
                tablet_percentage = int((1 - len(customer_unrepaired_tablets)/number_of_tablet)*100)
            else:
                customer_unrepaired_tablets = Product.objects.none
                tablet_percentage=int(100)


        else:
            tablet_stats.append(tablet_today)
            tablet_stats.append(tablet_week)
            tablet_stats.append(tablet_month)
            tablet_percentage=int(0)



    elif request.user.is_customer:

        user = User.objects.get(username=request.user)
        customer = Customer.objects.get(account=user)
        customer_unrepaired_notebooks = Product.objects.none
        notebook_today = 0
        notebook_week = 0
        notebook_month = 0
        notebook_stats = []
        today = datetime.now().date()
        #Retrive Notebooks
        if Product.objects.filter(customer =customer,product_type='Notebook').exists():
            customer_notebooks = Product.objects.filter(customer =customer,product_type='Notebook')
            number_of_notebooks = len(customer_notebooks)

            for notebook in customer_notebooks:
                if notebook.created_at.day == today.day:
                    notebook_today=notebook_today+1
                if notebook.created_at.isocalendar()[1] is today.isocalendar()[1]:
                    notebook_week= notebook_week+1
                if notebook.created_at.month is today.month:
                    notebook_month = notebook_month +1

            notebook_stats.append(notebook_today)
            notebook_stats.append(notebook_week)
            notebook_stats.append(notebook_month)
            #Retrive Unrepaired Notebooks
            if Product.objects.filter(customer =customer,product_type='Notebook',repaired=False).exists():
                customer_unrepaired_notebooks = Product.objects.filter(customer =customer,product_type='Notebook',repaired=False)
                notebook_percentage = int((1 - len(customer_unrepaired_notebooks)/number_of_notebooks)*100)
            else:
                customer_unrepaired_notebooks = Product.objects.none
                notebook_percentage=int(100)
        else:
            notebook_stats.append(notebook_today)
            notebook_stats.append(notebook_week)
            notebook_stats.append(notebook_month)
            notebook_percentage=int(0)

        smartphone_today = 0
        smartphone_week = 0
        smartphone_month = 0
        smartphone_stats = []
        customer_unrepaired_smartphones = Product.objects.none
        #Retrive Smartphones
        if Product.objects.filter(customer =customer,product_type='Smartphone').exists():
            customer_smartphones = Product.objects.filter(customer =customer,product_type='Smartphone')
            number_of_smartphones = len(customer_smartphones)

            for smartphone in customer_smartphones:
                if smartphone.created_at.day == today.day:
                    smartphone_today=smartphone_today+1
                if smartphone.created_at.isocalendar()[1] is today.isocalendar()[1]:
                    smartphone_week= smartphone_week+1
                if smartphone.created_at.month is today.month:
                    smartphone_month = smartphone_month +1

            smartphone_stats.append(smartphone_today)
            smartphone_stats.append(smartphone_week)
            smartphone_stats.append(smartphone_month)
            #Retrive Unrepaired Notebooks
            if Product.objects.filter(customer =customer,product_type='Smartphone',repaired=False).exists():
                customer_unrepaired_smartphones = Product.objects.filter(customer =customer,product_type='Smartphone',repaired=False)
                smartphone_percentage = int((1 - len(customer_unrepaired_smartphones)/number_of_smartphones)*100)
            else:
                customer_unrepaired_smartphones = Product.objects.none
                smartphone_percentage=int(100)

        else:
            smartphone_stats.append(smartphone_today)
            smartphone_stats.append(smartphone_week)
            smartphone_stats.append(smartphone_month)
            smartphone_percentage=int(0)

        tablet_today = 0
        tablet_week = 0
        tablet_month = 0
        tablet_stats = []
        customer_unrepaired_tablets = Product.objects.none
        #Retrive Tablets
        if Product.objects.filter(customer =customer,product_type='Tablet').exists():
            customer_tablets = Product.objects.filter(customer =customer,product_type='Tablet')
            number_of_tablet = len(customer_tablets)

            for tablet in customer_tablets:
                if tablet.created_at.day == today.day:
                    tablet_today=tablet_today+1
                if tablet.created_at.isocalendar()[1] is today.isocalendar()[1]:
                    tablet_week= tablet_week+1
                if tablet.created_at.month is today.month:
                    tablet_month = tablet_month +1

            tablet_stats.append(tablet_today)
            tablet_stats.append(tablet_week)
            tablet_stats.append(tablet_month)

            #Retrive Unrepaired Tablets
            if Product.objects.filter(customer =customer,product_type='Tablet',repaired=False).exists():
                customer_unrepaired_tablets = Product.objects.filter(customer =customer,product_type='Tablet',repaired=False)
                tablet_percentage = int((1 - len(customer_unrepaired_tablets)/number_of_tablet)*100)
            else:
                customer_unrepaired_tablets = Product.objects.none
                tablet_percentage=int(100)


        else:
            tablet_stats.append(tablet_today)
            tablet_stats.append(tablet_week)
            tablet_stats.append(tablet_month)
            tablet_percentage=int(0)


    else:
        return render(request,'logger/page-notfound.html')


    context = {


        'notebook_percentage':notebook_percentage,
        'notebook_stats': notebook_stats,
        'smartphone_percentage':smartphone_percentage,
        'smartphone_stats': smartphone_stats,
        'tablet_percentage':tablet_percentage,
        'tablet_stats': tablet_stats,
        'customer_unrepaired_notebooks':customer_unrepaired_notebooks,
        'customer_unrepaired_smartphones':customer_unrepaired_smartphones,
        'customer_unrepaired_tablets':customer_unrepaired_tablets,

    }
    return render(request, 'logger/index.html', context)


@method_decorator(login_required,name='dispatch')
class SaleListView(ListView):

    template_name = 'logger/sales.html'
    def get_queryset(self):
        user = User.objects.get(username=self.request.user)
        if user.is_staff:
            return Sale.objects.all()
        elif user.is_customer:
            customer = Customer.objects.get(account=user)
            return Sale.objects.filter(customer=customer)

@method_decorator(login_required,name='dispatch')
class SaleCreate(CreateView):
    model = Sale
    fields = ['customer','product_name','supplier','serial_number','invoice_no', 'price','comments','warranty']
    template_name = 'logger/add_new_sale_form.html'
    #form_class = ActionForm




@method_decorator(login_required,name='dispatch')
class ProductListView(ListView):

    template_name = 'logger/object_list.html'
    def get_queryset(self):
        user = User.objects.get(username=self.request.user)
        if user.is_staff:
            return Product.objects.filter(product_type=self.kwargs['type'])
        elif user.is_customer:
            customer = Customer.objects.get(account=user)
            return Product.objects.filter(customer=customer,product_type=self.kwargs['type'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = self.kwargs['type']
        return context

@method_decorator(login_required,name='dispatch')
class ProductDetailView(DetailView):

    template_name = 'logger/object_detail.html'

    def get_queryset(self):
        user = User.objects.get(username=self.request.user)
        customer = Customer.objects.get(account=user)
        return Product.objects.filter(id=self.kwargs['pk'],product_type=self.kwargs['type'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = self.kwargs['type']
        return context

class ProductEditView(UpdateView):
    model = Product
    fields = ['customer','product_type','device_model', 'serial_number', 'issue','comment','cost']
    template_name = 'logger/add_new_item_form.html'

    def get_queryset(self):
        user = User.objects.get(username=self.request.user)
        customer = Customer.objects.get(account=user)
        return Product.objects.filter(id=self.kwargs['pk'],product_type=self.kwargs['type'])


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = self.kwargs['type']
        return context


@login_required
def update_product_field(request,type,pk,field):

    user = User.objects.get(username=request.user)
    customer = Customer.objects.get(account=user)
    if Product.objects.filter(id=pk,product_type=type).exists():
        product = Product.objects.get(id=pk,product_type=type)
        if field == 'repaired':
            if product.repaired is True:
                product.repaired = False
                product.save()
            else:
                product.repaired = True
                product.save()
        elif field == 'payed':
            if product.payed is True:
                product.payed = False
                product.save()
            else:
                product.payed = True
                product.save()
        elif field == 'canceled':
            if product.canceled is True:
                product.canceled = False
                product.save()
            else:
                product.canceled = True
                product.save()
        #else:
            #return render(request,'logger/page-notfound.html')
    else:
        return render(request,'logger/page-notfound.html')

    return HttpResponseRedirect(reverse('logger:product-detail', kwargs={'type': product.product_type ,'pk':product.pk}))

# Form for create new product
@method_decorator(login_required,name='dispatch')
class ProductCreate(CreateView):
    model = Product
    fields = ['customer','product_type','device_model', 'serial_number', 'issue','comment','cost']
    template_name = 'logger/add_new_item_form.html'
    #form_class = ActionForm


@login_required
def backup_product_csv(request,type):

    user = User.objects.get(username=request.user)
    customer = Customer.objects.get(account=user)
    if Product.objects.filter(product_type=type).exists():
        product_list = Product.objects.filter(product_type=type)

        response = HttpResponse(content_type ='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Backup.csv"'

        writer = csv.writer(response)
        writer.writerow(['Id','Customer' , 'Date Inc','Product Type','Model','Serial_number','Issue','Comments','Warranty','Damage Descriptions' ,'Cost','Repaired','Payed','Canceled'])

        for product in product_list:
            writer.writerow([product.id,
                            str(product.customer.first_name)+ str(product.customer.last_name),
                            product.created_at,
                            product.product_type,
                            product.device_model,
                            product.serial_number,
                            product.Repairs(),
                            product.comment,
                            product.Warranty(),
                            product.damage_description,
                            product.cost,
                            product.repaired,
                            product.payed,
                            product.canceled
                            ])

    return response


@method_decorator(login_required,name='dispatch')
class CustomerListView(ListView):
    model = Customer
    template_name = 'logger/customers.html'



# Form for create new customer
@method_decorator(login_required,name='dispatch')
class CustomerCreate(CreateView):
    model = Customer
    fields = ['first_name','last_name','e_mail','customer_type','telephone', 'vat_id', 'address',]
    template_name = 'logger/add_new_customer_form.html'
