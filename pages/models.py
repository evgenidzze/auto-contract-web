from django.db import models
#
#
class So(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    document_num = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Назви СО'
#
#
class Department(models.Model):
    # id = models.IntegerField(primary_key=True)
    so = models.ForeignKey('So', on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.department


class Object(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    so = models.ForeignKey('So', on_delete=models.CASCADE, null=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True)
    schema = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True)
    # page 3
    tp_num = models.CharField(default='', blank=True, verbose_name='Номер ТП', max_length=20)
    line_num = models.CharField(default='', blank=True, verbose_name='Номер лінії', max_length=20)
    fider_num = models.CharField(default='', blank=True, verbose_name='Номер фідера', max_length=20)
    fider_type = models.CharField(max_length=10, default='', blank=True, verbose_name='Тип фідера')
    resistance_num = models.CharField(max_length=10, default='', blank=True, verbose_name='Номер опори')
    full_trans_power = models.CharField(default='', blank=True, verbose_name='Повна потужність трансформатора',
                                        max_length=20)
    substation_name = models.CharField(max_length=200, default='', blank=True, verbose_name='Назва підстанції')

    line_type = models.CharField(default='', max_length=20, blank=True, verbose_name='Тип лінії')
    line_length = models.CharField(default='', max_length=20, blank=True, verbose_name='Довжина лінії')
    active_line_resistance = models.CharField(default='', max_length=20, blank=True, verbose_name='Активний опір лінії')
    reactive_line_resistance = models.CharField(default='', max_length=20, blank=True,
                                                verbose_name='Реактивний опір лінії')
    power = models.CharField(default='', max_length=20, blank=True, verbose_name='Потужність')
    work_mode = models.CharField(default='', max_length=20, blank=True, verbose_name='Режим роботи')
    voltage_level = models.CharField(default='', max_length=20, blank=True, verbose_name='Ступінь напруги ТРЕЕ')
    shield = models.CharField(default='', max_length=20, blank=True, verbose_name='Щитова')
    stream_av = models.CharField(default='', max_length=20, blank=True, verbose_name='Струм АВ')

    line_mark = models.CharField(default='', max_length=100, blank=True, verbose_name='Марка лінії')
    section_numbers = models.CharField(default='', max_length=100, blank=True, verbose_name='Кількість х Переріз')
    initial_indicators = models.CharField(default='', max_length=100, blank=True, verbose_name='Початкові показники')
    counter_type = models.CharField(default='', max_length=100, blank=True, verbose_name='Тип лічильника')
    counter_serial_num = models.CharField(default='', max_length=100, blank=True,
                                          verbose_name='Серійний номер лічильника')
    counter_nominal = models.CharField(default='', max_length=100, blank=True, verbose_name='Номінал лічильника')
    quarter = models.CharField(default='', max_length=100, blank=True, verbose_name='Квартал та рік повірки')
    reliability_category = models.CharField(default='', max_length=100, blank=True,
                                            verbose_name='Категорія надійності струмоприймачів')
    av_stream_ru_04 = models.CharField(default='', max_length=100, blank=True, verbose_name='Струм АВ в РУ-0,4кВ')

    full_power_t1 = models.CharField(default='', max_length=100, blank=True, verbose_name='Повна потужність Т1')
    full_power_t2 = models.CharField(default='', max_length=100, blank=True, verbose_name='Повна потужність Т2')
    os_section_numbers = models.CharField(default='', max_length=100, blank=True,
                                          verbose_name='Кількість Х Переріз ліній на балансі ОС')
    os_line_mark = models.CharField(default='', max_length=100, blank=True, verbose_name='Марка лінії на балансі ОС')
    os_line_type = models.CharField(default='', max_length=100, blank=True, verbose_name='Тип лінії на балансі ОС')
    os_line_length = models.CharField(default='', max_length=100, blank=True,
                                      verbose_name='Довжина лінії на балансі ОС')
    cutter_num_VRSH = models.CharField(default='', max_length=100, blank=True,
                                       verbose_name='Номінал рубільника в ВРЩ ж/б')
    auth_person_position = models.CharField(default='', max_length=100, blank=True,
                                            verbose_name='Посада\nуповноваженої особи')

    object_type = models.CharField(default='', max_length=100, blank=True, verbose_name="Вид об'єкта")
    contract_num = models.CharField(default='', max_length=100, blank=True, verbose_name='Номер договору')
    eis_code = models.CharField(default='', max_length=100, blank=True, verbose_name='ЕІС-код')
    position_pib = models.CharField(default='', max_length=100, blank=True,
                                    verbose_name='Посада уповноваженої особи споживача, П.І.Б.')
    full_cons_name = models.CharField(default='', max_length=100, blank=True, verbose_name='Повна юр. назва споживача')
    activity_document = models.CharField(default='', max_length=100, blank=True,
                                         verbose_name='Документ за яким споживач здійснює діяльність')

    abbreviated_full_name = models.CharField(default='', max_length=100, blank=True,
                                             verbose_name='Скорочена повна юр. назва споживача')
    consumer_pib = models.CharField(default='', max_length=100, blank=True, verbose_name='П.І.Б. споживача')
    index_legal_address = models.CharField(default='', max_length=100, blank=True,
                                           verbose_name='Індекс, Юридична адреса')
    index_circulation_address = models.CharField(default='', max_length=100, blank=True,
                                                 verbose_name='Індекс, Адреса для документообігу')
    actual_address = models.CharField(default='', max_length=100, blank=True, verbose_name="Фактична адреса об'єкту")

    av_num = models.CharField(default='', max_length=100, blank=True, verbose_name="Номінал АВ")
    av_num_vrs = models.CharField(default='', max_length=100, blank=True, verbose_name="Номінал АВ в ВРЩ ж/б")

    general_consumer_pib = models.CharField(default='', max_length=100, blank=True,
                                            verbose_name="П.І.Б. основного споживача")
    general_consumer_abbreviated = models.CharField(default='', max_length=100, blank=True,
                                                    verbose_name="Скорочена повна юр. назва основного споживача")
    general_full_name = models.CharField(default='', max_length=100, blank=True,
                                         verbose_name="Повна юр. назва основного споживача")
    consumer_category = models.ForeignKey('ConsumerCategory', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.department)


class ConsumerCategory(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
