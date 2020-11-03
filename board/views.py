from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic
from board.models import Account, Location, WorkOrder, Labor
from datetime import date



# Create your views here.
def index(request):
    """View function for home page of site."""

    # Open Work Orders (status = 'i')
    open_work_orders = WorkOrder.objects.filter(status__contains='i')

    # Today's Applied Labor
    todays_labor = Labor.objects.filter(start_time__date=date.today())

    context = {
        "open_work_orders": open_work_orders,
        "todays_labor": todays_labor,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)



class WorkOrdersInProgressListView(ListView):
    model = WorkOrder
    context_object_name = 'work_orders_in_progress'
    queryset = WorkOrder.objects.filter(status__contains='i')
    template_name = 'work-orders-in-progress.html'


class LaborTodayListView(ListView):
    model = Labor
    context_object_name = 'labor_today'
    queryset = Labor.objects.filter(start_time__date=date.today())
    template_name = 'labor-today.html'


# class WorkOrderListView(ListView):
#     def __init__(self, work_order_number):
#         self.work_order_number = work_order_number
# 
#     model = WorkOrder
#     context_object_name = f'{self.work_order_number}'
#     queryset = WorkOrder.objects.filter(number__contains=f'self.work_order_number')


        
