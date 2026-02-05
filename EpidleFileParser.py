import json
from pathlib import Path

class FileSystemConnector:
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.projects_path = self.base_path / "projects"
        self.coding_style_path = self.base_path / "coding-style"
        self.pool_path = self.base_path / "pool"
        
        if not self.projects_path.exists():
            raise FileNotFoundError(f"Projects directory not found: {self.projects_path}")
        if not self.coding_style_path.exists():
            raise FileNotFoundError(f"Coding style directory not found: {self.coding_style_path}")
        if not self.pool_path.exists():
            raise FileNotFoundError(f"Pool path not found: {self.pool_path}")

    def load_json(self, filepath: Path) -> dict:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_all_projects(self) -> list:
        projects = []
        required_fields = ["name", "emoji", "semester"]

        for module_dir in self.projects_path.iterdir():
            if not module_dir.is_dir():
                continue
            
            module_name = module_dir.name
            
            desc_file = module_dir / "DESC.md"
            module_type = None
            if desc_file.exists():
                with open(desc_file, 'r', encoding='utf-8') as f:
                    module_type = f.read().strip()
            else:
                print(f"Warning: Could not load projects of {module_name} as DESC.md (module name), is missing")
                continue
            for project_dir in module_dir.iterdir():
                if not project_dir.is_dir():
                    continue
                object_file = project_dir / "object.json"
                if object_file.exists():
                    project_data = self.load_json(object_file)
                    isValid = True
                    for required_field in required_fields:
                        if required_field not in project_data:
                            print(f"Warning: Could not load project {project_dir.name} as mandatory key {required_field} in 'object.json' does not exist")
                            isValid = False
                    if isValid:
                        project_data['id'] = f"{module_name}/{project_dir.name}"
                        project_data['module'] = module_type
                        projects.append(project_data)
                else:
                    print(f"Warning: Could not load project on {project_dir.name} as 'object.json' is missing")
                    continue
        projects.sort(key=lambda p: p.get('name', ''))
        return projects
    
    def get_all_pool_days(self) -> list:
        days = []
        required_fields = ["name", "number", "language"]
        language_order = {
            'Shell': 0,
            'C': 1,
            'Haskell': 2,
            'C++': 3
        }

        for module_dir in self.pool_path.iterdir():
            if not module_dir.is_dir():
                continue
            for day_dir in module_dir.iterdir():
                if not day_dir.is_dir():
                    continue
                object_file = day_dir / "object.json"
                if not object_file.exists():
                    print(f"Warning: Could not load pool day on {day_dir.name} as 'object.json' is missing")
                    continue
                day_data = self.load_json(object_file)
                isValid = True
                for required_field in required_fields:
                    if required_field not in day_data:
                        print(f"Warning: Could not load pool day {day_dir.name} as mandatory key {required_field} in 'object.json' does not exist")
                        isValid = False
                if isValid:
                    day_data['id'] = f"{day_data['language']}/{day_dir.name}"
                    days.append(day_data)
        days.sort(key=lambda d: (language_order.get(d['language'], 999), d['number']))
        return days
    
    def get_all_functions(self) -> list:
        functions = []
        function_id = 1
        required_fields = ["name", "prototype", "description", "task_number"]

        for module_dir in self.pool_path.iterdir():
            if not module_dir.is_dir():
                continue
            for day_dir in module_dir.iterdir():
                if not day_dir.is_dir():
                    continue
                object_file = day_dir / "object.json"
                if not object_file.exists():
                    print(f"Warning: Could not load functions on {day_dir.name} as 'object.json' is missing")
                    continue
                day_data = self.load_json(object_file)
                functions_file = day_dir / "functions.json"
                if functions_file.exists():
                    day_functions = self.load_json(functions_file)
                    for func in day_functions:
                        isValid = True
                        for required_field in required_fields:
                            if required_field not in func:
                                print(f"Warning: Could not load function in {day_dir.name} as mandatory key {required_field} in 'functions.json' is missing")
                                isValid = False
                        if isValid:
                            func['id'] = function_id
                            func['day_id'] = f"{day_data['language']}/{day_dir.name}"
                            functions.append(func)
                            function_id += 1
        return functions
    
    def get_all_coding_styles(self) -> list:
        errors = []
        required_fields = ["name", "description", "type"]

        for category_dir in self.coding_style_path.iterdir():
            if not category_dir.is_dir():
                continue
            desc_file = category_dir / "DESC.md"
            category_name = ""
            if desc_file.exists():
                with open(desc_file, 'r', encoding='utf-8') as f:
                    category_name = f.read().strip()
            else:
                print(f"Warning: Could not load errors of {category_dir.name} as DESC.md (category name), is missing")
                continue
            for error_dir in category_dir.iterdir():
                if not error_dir.is_dir():
                    continue
                object_file = error_dir / "object.json"
                if object_file.exists():
                    error_data = self.load_json(object_file)
                    isValid = True
                    for required_field in required_fields:
                        if required_field not in error_data:
                            print(f"Warning: Could not load coding style on {error_dir.name} as mandatory key {required_field} in 'object.json' does not exist")
                            isValid = False
                    if isValid:
                        error_data['category'] = category_name   
                        errors.append(error_data)
                else:
                    print(f"Warning: could not load coding style {error_dir.name} as 'object.json' does not exist.")
        errors.sort(key=lambda e: e.get('name', ''))
        return errors

    def get_all_coding_style_codes(self) -> list:
        codes = []
        required_fields = ["name", "description", "type"]
        
        for category_dir in self.coding_style_path.iterdir():
            if not category_dir.is_dir():
                continue
            for error_dir in category_dir.iterdir():
                if not error_dir.is_dir():
                    continue
                object_file = error_dir / "object.json"
                if not object_file.exists():
                    print(f"Warning: could not load coding style codes of {error_dir.name} as 'object.json' does not exist.")
                    continue
                object_json = self.load_json(object_file)
                isValid = True
                for required_field in required_fields:
                    if required_field not in object_json    :
                        print(f"Warning: Could not load coding style codes on {error_dir.name} as mandatory key {required_field} in 'object.json' does not exist")
                        isValid = False
                if not isValid:
                    continue
                examples_dir = error_dir / "examples"
                if examples_dir.exists():
                    for example_file in sorted(examples_dir.iterdir()):
                        if example_file.suffix in ['.c', '.cpp']:
                            with open(example_file, 'r', encoding='utf-8') as f:
                                code_content = f.read()
                            codes.append({
                                'error_name': object_json["name"],
                                'code': code_content
                            })
        return codes
    
    def get_all_project_codes(self) -> list:
        codes = []

        for module_dir in self.projects_path.iterdir():
            if not module_dir.is_dir():
                continue
            for project_dir in module_dir.iterdir():
                if not project_dir.is_dir():
                    continue
                examples_dir = project_dir / "examples"
                if examples_dir.exists():
                    for example_file in sorted(examples_dir.iterdir()):
                        if example_file.suffix in ['.c', '.cpp']:
                            with open(example_file, 'r', encoding='utf-8') as f:
                                code_content = f.read()
                            codes.append({
                                'project_id': f"{module_dir.name}/{project_dir.name}",
                                'code': code_content
                            })
        
        return codes
