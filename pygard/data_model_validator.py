from pydantic import ValidationError

class DataValidator:
    def __init__(self, model_loader):
        self.model_loader = model_loader

    def validate_data(self, data):
        results = {}

        for model_name, model_data in data.items():
            try:
                model = self.model_loader.load_model(model_name)
                validated_data = model(**model_data)
                results[model_name] = {"valid": True, "data": validated_data.dict()}
            except (ValidationError, FileNotFoundError, AttributeError) as e:
                results[model_name] = {"valid": False, "error": str(e)}

        return results

    def check_output_for_sensitive_data(self, data):
        