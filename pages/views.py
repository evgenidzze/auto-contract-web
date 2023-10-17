import datetime
import locale
import logging
import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from docxtpl import DocxTemplate
from six import BytesIO

from .forms import DependentForm, SchemaForm, Page4Schema1Form, Page3Schema3Form, Page3Schema1Form, Page3Schema2Form, \
    Page4Schema2Form, Page4Schema3Form
from .models import Department, Object, So, ConsumerCategory
from .utils import rod_months

locale.setlocale(locale.LC_ALL, 'uk_UA')
logger = logging.getLogger(__name__)


class Page1Create(LoginRequiredMixin, CreateView):
    form_class = DependentForm
    template_name = 'pages/page1.html'

    def get_queryset(self):
        contracts = Object.objects.all()
        return contracts

    # def form_valid(self, form):
    #     obj = form.save(commit=False)
    #     obj.consumer_category = self.request.user.consumer_category
    #     return super().form_valid(form)

    def get_success_url(self):
        last_id = Object.objects.filter().order_by('id').last().id
        if not last_id:
            last_id = 1
        return reverse_lazy('page2', kwargs={'pk': last_id})


class BaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Object

    def get_success_url(self):
        return reverse_lazy(self.next_page, kwargs={'pk': self.object.id})


class Page1Update(BaseUpdateView):
    form_class = DependentForm
    template_name = 'pages/page1.html'
    next_page = 'page2'


class Page2(BaseUpdateView):
    form_class = SchemaForm
    template_name = 'pages/page2.html'
    next_page = 'page3'


class Page3(BaseUpdateView):
    template_name = 'pages/page3.html'
    next_page = 'page4'

    def get_form_class(self):
        form_classes = [Page3Schema1Form, Page3Schema2Form, Page3Schema3Form]
        form_class = form_classes[int(self.object.schema) - 1]
        return form_class

    def get_template_names(self):
        template_names = ['page3.html', 'page3_schema2.html', 'page3_schema3.html']
        return f'pages/{template_names[int(self.object.schema) - 1]}'

    def form_valid(self, form):
        form.save()
        if 'save' in self.request.POST:
            url = reverse_lazy('page4', kwargs={'pk': self.object.id})
            response = HttpResponseRedirect(url)
        else:
            url = reverse_lazy('page2', kwargs={'pk': self.object.id})
            response = HttpResponseRedirect(url)
        return response


class Page4(BaseUpdateView):
    form_class = Page4Schema1Form
    template_name = 'pages/page4.html'

    def get_form_class(self):
        form_classes = [Page4Schema1Form, Page4Schema2Form, Page4Schema3Form]
        form_class = form_classes[int(self.object.schema) - 1]
        return form_class

    def get_template_names(self):
        template_names = ['page4.html', 'page4_schema2.html', 'page4_schema3.html']
        return f'pages/{template_names[int(self.object.schema) - 1]}'

    def form_valid(self, form):
        form.save()
        all_data = formated_data(self)
        if 'save' in self.request.POST:
            response = FileResponse(replace_data(document_num=self.object.schema, values_dict=all_data),
                                    as_attachment=True, filename=f'Document_{self.object.id}.docx')
        else:
            url = reverse_lazy('page3', kwargs={'pk': self.object.id})
            response = HttpResponseRedirect(url)
        return response


def get_departments(request):
    so_id = request.GET.get('so')
    if so_id == '':
        form = None
    else:
        form = Department.objects.filter(so_id=so_id).order_by('id')
    return render(request, 'pages/dropdown_list.html', {'form': form})


def replace_data(document_num, values_dict):
    dir_name = './static/pages/media/documents/'
    documents = [DocxTemplate(os.path.abspath(os.path.join(dir_name, file))) for file in os.listdir(dir_name)]
    doc = documents[document_num - 1]
    file_buffer = BytesIO()
    doc.render(values_dict)
    doc.save(file_buffer)
    file_buffer.seek(0)
    return file_buffer


def formated_data(self: Page4):
    all_data = self.object.__dict__
    department_data = self.object.department.__dict__
    so_data = self.object.so.__dict__

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    so_data['name'] = so_data['name'][4:-1]
    so_data['abbreviate_director'] = so_data['director'].split(', ')[1]
    so_data['full_director'] = so_data['director'].split(', ')[0]
    so_data['day'] = self.object.date.strftime("%d")
    so_data['month'] = self.object.date.strftime("%B")
    so_data['month_num'] = self.object.date.strftime("%m")
    so_data['year'] = self.object.date.strftime("%Y")
    so_data['month_rod'] = rod_months[so_data['month']]
    try:
        c_name = str(self.object.consumer_pib).split()
        so_data['ю4'] = f'{c_name[1][0]}. {c_name[2][0]}. {c_name[0]}'
    except Exception as error:

        logger.warning(
            f"[{formatted_time}] User: {self.request.user.username} - Entered value in 'c_name' variable: '{self.object.consumer_pib}'."
            f" Error Details: {error}"
        )
    try:
        general_consumer_pib_split = str(self.object.general_consumer_pib).split()
        so_data['к21'] = f'{general_consumer_pib_split[1][0]}. ' \
                         f'{general_consumer_pib_split[2][0]}. ' \
                         f'{general_consumer_pib_split[0]}'
    except Exception as error:
        logger.warning(
            f"[{formatted_time}] User: {self.request.user.username} - Entered value in 'general_consumer_pib' variable:"
            f" '{self.object.general_consumer_pib}'."
            f" Error Details: {error}"
        )

    if self.object.index_legal_address is None:
        self.object.index_legal_address = self.object.index_circulation_address
    if self.object.voltage_level == '0,22':
        all_data['т2_1'] = '1'
    elif self.object.voltage_level == '0,38':
        all_data['т2_1'] = '3'

    try:
        all_data['т12_1'] = str(int(self.object.line_length) / 1000).replace('.', ',')
    except Exception as error:
        logger.warning(
            f"[{formatted_time}] User: {self.request.user.username} - Entered value in 'line_length' variable:"
            f" '{self.object.line_length}'."
            f" Error Details: {error}"
        )

    if self.object.line_type == 'КЛ':
        all_data['т99'] = "в місці кріплення кабелю живлення"
    elif self.object.line_type in ('ПЛ', 'ПЛІ'):
        all_data['т99'] = "в місці кріплення проводів ЛЕП"

    all_data['activity_document_2'] = str(self.object.activity_document).split()

    del so_data['id'], department_data['id']
    all_data.update(so_data)
    all_data.update(department_data)
    return all_data


def redirect_view(request):
    response = redirect('page_1_create')
    return response
