from covid import Covid

covid=Covid()
india=covid.get_status_by_country_name("india")
data = {
    key : india[key]
    for key in india.keys() and {'confirmed',
                                 'active',
                                 'deaths',
                                 'recovered'}
}
print(data)