from EpidleFileParser import FileSystemConnector

class DataLoader:

    def __init__(self) -> None:
        self.projects = []
        self.poolDays = []
        self.functions = []
        self.poolFunctionsDay = []
        self.coding_styles = []
        self.coding_styles_codes = []
        self.project_codes = []
        self.fs = FileSystemConnector(".") 
        self.cache()

    def cache_projects(self):
        self.projects = self.fs.get_all_projects()

    def get_projects(self, withEmoji=True):
        if withEmoji:
            return self.projects
        else:
            return list(map(
                lambda d: {k: v for k, v in d.items() if k != "emoji"}, 
                self.projects
            ))

    def cache_pool_days(self):
        self.poolDays = self.fs.get_all_pool_days()

    def get_pool_days(self):
        return self.poolDays

    def cache_functions(self):
        self.functions = self.fs.get_all_functions()

    def get_function_by_id(self, id):
        for func in self.functions:
            if "id" in func and func["id"] == id:
                return func
        return None
    
    def get_pool_day_by_id(self, id):
        for day in self.poolFunctionsDay:
            if "id" in day and day["id"] == id:
                return day
        return None
    
    def get_day_by_id(self, id):
        for day in self.poolDays:
            if "id" in day and day["id"] == id:
                return day
        return None

    def cache_pool_functions_day(self):
        self.poolFunctionsDay = []

        if len(self.functions) == 0:
            self.cache_functions()
        for func in self.functions:
            day_id = func.get("day_id")
            if not day_id:
                continue
            
            poolDay = next(
                (d for d in self.poolFunctionsDay if d['id'] == day_id), 
                None
            )
            if not poolDay:
                poolDay = {
                    "id": day_id,
                    "functions": []
                }
                self.poolFunctionsDay.append(poolDay)
            poolDay["functions"].append(func)

    def get_pool_functions_day(self):
        return self.poolFunctionsDay

    def get_functions(self):
        return self.functions
    
    def get_coding_styles(self):
        return self.coding_styles
    
    def get_coding_styles_codes(self):
        return self.coding_styles_codes
    
    def get_project_codes(self):
        return self.project_codes

    def get_function_day_name(self, functionToSearch):
        for day in self.poolFunctionsDay:
            for function in day["functions"]:
                if function["id"] == functionToSearch["id"]:
                    return day["id"]
        return None
    
    def compareDays(self, day1, day2):
        return {
            "language": day2 is not None and day1["language"] == day2["language"],
            "number": day2 is not None and day1["number"] == day2["number"]
        }

    def is_function_from_day(self, functionId, dayName):
        specifiedDay = self.get_pool_day_by_id(dayName)
        if specifiedDay == None:
            return False
        
        for functionObject in specifiedDay["functions"]:
            if functionObject["id"] == functionId:
                return True 
        
        return False
    
    def cache_coding_styles(self):
        self.coding_styles = self.fs.get_all_coding_styles()
    
    def cache_coding_style_codes(self):
        self.coding_styles_codes = self.fs.get_all_coding_style_codes()

    def cache_project_codes(self):
        self.project_codes = self.fs.get_all_project_codes()

    def cache(self):
        self.cache_projects()
        print(f"{len(self.projects)} projets cached.")
        self.cache_pool_days()
        print(f"{len(self.poolDays)} pool days cached.")
        self.cache_functions()
        print(f"{len(self.functions)} functions cached.")
        self.cache_pool_functions_day()
        print(f"{len(self.poolFunctionsDay)} days with functions cached.")
        self.cache_coding_styles()
        print(f"{len(self.coding_styles)} coding-style cached.")
        self.cache_coding_style_codes()
        print(f"{len(self.coding_styles_codes)} coding-style codes cached.")
        self.cache_project_codes()
        print(f"{len(self.project_codes)} project codes cached")
        print("✨ Finished caching")
