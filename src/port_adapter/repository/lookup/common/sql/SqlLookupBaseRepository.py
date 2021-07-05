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

    def _constructFilterItemByKeyword(self, filterItem, keyword, keywordReplacementInKey = None):
        key = filterItem["key"]
        if (key.find(keyword) != -1 and keyword != "") or (keyword == "" and key != "" and key.find(".") == -1):
            value = filterItem["value"]
            valueTypeFound = False
            try:
                if value is float(value):
                    value = float(value)
                    valueTypeFound = True
            except: pass

            try:
                if value is int(value):
                    value = int(value)
                    valueTypeFound = True
            except: pass

            if keywordReplacementInKey is not None:
                key = key.replace(keyword, keywordReplacementInKey)
            if not valueTypeFound:
                return f'{key} = "{value}"'
            return f'{key} = {value}'
        return None
