import os

from django import forms

from pages.models import Object


class DateInput(forms.DateInput):
    input_type = 'date'


class DependentForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput, label='Дата укладення')

    class Meta:
        model = Object
        fields = ('so', 'department', 'date')
        widgets = {'date': DateInput()}
        labels = {'so': 'Назва СО',
                  'department': 'Дільниця',
                  }
        widgets['so'] = forms.Select(attrs={'class': 'select-white', 'style': 'width: 215px; margin-bottom: 0'})
        widgets['department'] = forms.Select(attrs={'class': 'select-white', 'style': 'width: 215px; margin-bottom: 0'})


SCHEMA_CHOICES = [(i[2], '/static/pages/media/schemes/' + i) for i in os.listdir('static/pages/media/schemes')]


class SchemaForm(forms.ModelForm):
    schema = forms.ChoiceField(choices=SCHEMA_CHOICES, widget=forms.RadioSelect, required=True)

    class Meta:
        model = Object
        fields = ('schema',)


class Page3Schema1Form(forms.ModelForm):
    class Meta:
        model = Object
        fields = ['tp_num', 'line_num', 'fider_num', 'resistance_num', 'full_trans_power', 'substation_name',
                  'line_type',
                  'line_length', 'active_line_resistance', 'reactive_line_resistance', 'power', 'work_mode',
                  'voltage_level', 'shield', 'stream_av', 'line_mark', 'section_numbers', 'initial_indicators',
                  'counter_type', 'counter_serial_num', 'counter_nominal', 'quarter', 'reliability_category']

        widgets = {name: forms.TextInput(attrs={'class': 'input-tech-left'}) for name in fields}
        widgets['line_type'] = forms.Select(choices=(('', ''), ('КЛ', 'КЛ'), ('ПЛ', 'ПЛ'), ('ПЛІ', 'ПЛІ')),
                                            attrs={'class': 'select-white'})
        widgets['voltage_level'] = forms.Select(choices=(('', ''), ('0,22', '0,22'), ('0,38', '0,38')),
                                                attrs={'class': 'select-white'})
        widgets['reliability_category'] = forms.Select(choices=(('', ''), ('I', 'I'), ('II', 'II'), ('III', 'III')),
                                                       attrs={'class': 'select-white'})
        widgets['shield'] = forms.Select(choices=(('', ''), ('ЗКО', 'ЗКО'), ('ВРЩ', 'ВРЩ')),
                                         attrs={'class': 'select-white'})

        input_tech_right = {'resistance_num': forms.TextInput(attrs={'class': 'input-tech-right'}),
                            'full_trans_power': forms.TextInput(attrs={'class': 'input-tech-right'}),
                            'substation_name': forms.TextInput(attrs={'class': 'input-tech-right',
                                                                      'style': "width: 250px; margin-right: 0; margin-left: 20px"}),
                            }
        input_tech_right_m_list = ['line_mark', 'section_numbers', 'initial_indicators', 'counter_type',
                                   'counter_serial_num', 'counter_nominal', 'quarter']

        input_tech_right_m = {name: forms.TextInput(attrs={'class': 'input-tech-right-m'}) for name in
                              input_tech_right_m_list}
        widgets.update(input_tech_right)
        widgets.update(input_tech_right_m)


class Page3Schema2Form(Page3Schema1Form):
    class Meta(Page3Schema1Form.Meta):
        fields = Page3Schema1Form.Meta.fields
        fields.extend(['fider_type', 'av_num', 'av_num_vrs'])
        exclude = ('full_trans_power',)
        fields = Page3Schema1Form.Meta.fields + ['full_power_t1', 'full_power_t2', 'os_section_numbers', 'os_line_mark',
                                                 'os_line_type', 'os_line_length', 'cutter_num_VRSH',
                                                 'auth_person_position']
        widgets = Page3Schema1Form.Meta.widgets

        small_input = ['tp_num', 'line_num', 'fider_num', 'fider_type', 'full_power_t1', 'full_power_t2',
                       'os_line_type', 'os_line_length', 'av_num', 'av_num_vrs']
        medium_input = ['os_section_numbers', 'os_line_mark']
        widgets.update({i: forms.TextInput(attrs={'class': 'input-tech-right-m'}) for i in medium_input})
        widgets.update({i: forms.TextInput(attrs={'class': 'input-tech-left'}) for i in small_input})
        widgets['cutter_num_VRSH'] = forms.TextInput(
            attrs={'class': 'input-tech-left', 'style': 'margin-top: 8px; width'})
        widgets['auth_person_position'] = forms.Textarea(attrs={"rows": "1", 'cols': '29', 'style': 'width: 230px'})


class Page3Schema3Form(Page3Schema1Form):
    class Meta(Page3Schema1Form.Meta):
        model = Object
        fields = Page3Schema1Form.Meta.fields
        fields.extend(['av_stream_ru_04'])

        widgets = Page3Schema1Form.Meta.widgets
        widgets['av_stream_ru_04'] = forms.TextInput(attrs={'class': 'input-tech-left'})
        widgets['fider_type'] = forms.TextInput(attrs={'class': 'input-tech-right'})


class Page4Schema1Form(forms.ModelForm):
    class Meta:
        model = Object
        fields = ['object_type', 'contract_num', 'eis_code', 'position_pib', 'full_cons_name', 'activity_document',
                  'abbreviated_full_name', 'consumer_pib', 'index_legal_address', 'index_circulation_address',
                  'actual_address']

        widgets = {name: forms.Textarea(attrs={"rows": "2", 'cols': '29', 'style': 'width: 230px'}) for name in
                   fields}

        add_widgets = {'object_type': forms.TextInput(attrs={'style': 'width: 105px'}),
                       'contract_num': forms.TextInput(attrs={'style': 'width: 105px'}),
                       'eis_code': forms.TextInput(attrs={'style': 'width: 230px'}),
                       'abbreviated_full_name': forms.TextInput(attrs={'style': 'width: 230px'}),
                       'consumer_pib': forms.TextInput(attrs={'style': 'width: 230px'}),
                       }
        widgets.update(add_widgets)


class Page4Schema2Form(Page4Schema1Form):
    class Meta(Page4Schema1Form.Meta):
        fields = Page4Schema1Form.Meta.fields
        widgets = Page4Schema1Form.Meta.widgets

        fields.extend(['general_consumer_pib', 'general_consumer_abbreviated', 'general_full_name'])
        widgets['general_consumer_abbreviated'] = forms.Textarea(
            attrs={"rows": "2", 'cols': '29', 'style': 'width: 230px'})

        widgets['general_full_name'] = forms.Textarea(
            attrs={"rows": "2", 'cols': '29', 'style': 'width: 230px'})


class Page4Schema3Form(Page4Schema1Form):
    class Meta(Page4Schema1Form.Meta):
        pass
