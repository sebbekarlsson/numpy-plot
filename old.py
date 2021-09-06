FILENAME = "result2.json"


# Rack upp handen nar ni har en liknande fil-struktur som jag

def generate_data():
    records = cases.get('records')
    dates = [record.get('dateRep') for record in records]
    dates_case = [datetime.datetime.strptime(d, '%d/%m/%Y') for d in dates]
    country_case = [d['geoId'] for d in records]
    records_vac = vaccine.get('records')
    dates_vac = [yearweek_to_date(record.get('YearWeekISO')) for record in records_vac]
    country_vac = [v['Region'] for v in records_vac]

    data_to_check0 = list(map(lambda dat: [dat[1], country_case[dat[0]]], enumerate(dates_case)))
    data_to_check = list(map(lambda dat: [dat[1], country_vac[dat[0]]], enumerate(dates_vac)))

    for i, d in enumerate(data_to_check0):
        indices = [d_i for d_i, dv in enumerate(data_to_check) if d[0] == dv[0] and d[1] == dv[1]]
        vaccines = [records_vac[r_i] for r_i in indices]
        records[i]['vaccines'] = vaccines

    with open('result2.json', mode='w+') as my_file:
        json.dump(records, my_file)



if not os.path.isfile(FILENAME):
    generate_data()


dataset = json.loads(open('result2.json').read())

sweden_data = list(filter(lambda case: case.get('geoId') == 'SE', dataset))
at_data = list(filter(lambda case: case.get('geoId') == 'AT', dataset))



def get_axises(data):
    xaxis = map(lambda case:
        sum(list(map(
            lambda vac:
            int(vac.get('NumberDosesReceived') or 0), case.get('vaccines')
        ))),
        data
    )

    yaxis = map(lambda case: case.get('deaths'), data)

    xaxis = np.array(list(xaxis))
    yaxis = np.array(list(yaxis))

    return xaxis, yaxis



xaxis, yaxis = get_axises(sweden_data)
xaxis2, yaxis2 = get_axises(at_data)



convolved_y = np.convolve(yaxis, yaxis2)

xaxis = range(convolved_y.size)

fig, ax = plt.subplots()
ax.scatter(xaxis, convolved_y)

ax.set(xlabel='Doses', ylabel='Deaths',
       title='Doses & Deaths')
ax.grid()

fig.savefig("test.png")
plt.show()
