
log_date = []
log_time = []
log_result = []

def write_log(result):
    """Запись в файл(excel)"""

    import datetime
    import pandas

    global log_time, log_date, log_result
    date = datetime.datetime.today()
    log_date.append(date.strftime("%d/%m/%Y"))
    log_time.append(date.strftime("%H:%M:%S"))
    log_result.append(result)
    df = pandas.DataFrame({'Дата': log_date,
                           'Время': log_time,
                           'Результат': log_result})
    df.to_excel('./log.xlsx', index=False)

count_run = []

def chart():
    """Функция построения диаграммы (Ось OX - степени депрессии, Ось OY - количество респондентов, с соответствующей степенью депрессии)"""

    import matplotlib.pyplot as plt
    import numpy as np

    global log_result, count_run

    nds_count = [0 <= x < 10 for x in log_result].count(True) #no depressive symptoms
    subd_count = [10 <= x < 16 for x in log_result].count(True) #subdepression
    moadd_count = [16 <= x < 20 for x in log_result].count(True) #moderate depression
    sevd_count = [20 <= x < 30 for x in log_result].count(True) #severe depression
    majd_count = [30 <= x < 64 for x in log_result].count(True) #major depression

    plt.style.use('_mpl-gallery')

    fig, ax = plt.subplots(figsize=(5, 2), layout='constrained')
    categories = ['ОДС', 'ЛД', 'УД', 'ВДСТ', 'ТД']

    ax.bar(categories, np.array([nds_count, subd_count, moadd_count, sevd_count, majd_count]))

    ax.set(xticks=np.arange(-1, 6), yticks=np.arange(0, 11))

    count_run.append(len(count_run))
    number_png = count_run[-1] + 1
    plt.savefig(f'figure/Figure {number_png}')

    plt.show()