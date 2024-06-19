import importlib.util
import os

class DataModelLoader:
    def __init__(self, cache_dir, custom_model_paths=None):
        self.cache_dir = cache_dir
        self.custom_model_paths = custom_model_paths or []

    def load_model(self, model_name):
        # Search for the model in the cache directory
        model_file = os.path.join(self.cache_dir, f"{model_name}.py")
        if os.path.exists(model_file):
            return self._load_module(model_name, model_file)

        # Search for the model in the custom model paths
        for path in self.custom_model_paths:
            model_file = os.path.join(path, f"{model_name}.py")
            if os.path.exists(model_file):
                return self._load_module(model_name, model_file)

        raise FileNotFoundError(f"Model file {model_name}.py not found")

    def _load_module(self, model_name, model_file):
        spec = importlib.util.spec_from_file_location(model_name, model_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        model = getattr(module, model_name, None)
        if model is None:
            raise AttributeError(f"Model {model_name} not found in {model_file}")
        return model
