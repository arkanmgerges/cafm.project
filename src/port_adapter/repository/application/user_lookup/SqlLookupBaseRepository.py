class SqlLookupBaseRepository:
    def _constructFiltering(self, filters):
        filterData = ""
        if filters is not None:
            filterData = ""
            filterItems = []

            for item in filters:
                operator = item.get("operator", "=")
                valueSplit = item["value"].split("|")
                if len(valueSplit) == 2:
                    operator = valueSplit[0]
                    item["value"] = valueSplit[1]
                filterItems.append(f'{item["key"]} {operator} "{item["value"]}"')

            if len(filterItems) > 0:
                filterData = "WHERE " + 'AND '.join(filterItems)
        return filterData