# Terraform Test Framework
# https://github.com/tf2project/tf2project

from .local import TerraformStateLoader
from .object import TerraformObject, TerraformObjectParser
from .util import get_attr_name, get_output_type


class Terraform:
    def __init__(self, loader_instance=None):
        if loader_instance is None:
            self._loader_instance = TerraformStateLoader()
        else:
            self._loader_instance = loader_instance
        self._load_data()
        self._fetch_target_values()
        self._parse_modules(self, self._target_values["root_module"])
        self._parse_outputs()

    def get_loader_instance(self):
        return self._loader_instance

    def get_data(self):
        if hasattr(self, "_data") is False:
            raise Exception("Data is not loaded.")
        return self._data

    def _load_data(self):
        self._data = self._loader_instance.load()

    def _fetch_target_values(self):
        loader_type = self._loader_instance.get_loader_type()
        if loader_type == "planloader":
            self._target_values = self._data["planned_values"]
        elif loader_type == "stateloader":
            self._target_values = self._data["values"]
        else:
            raise Exception("Invalid terraform resource loader.")

    def _parse_modules(self, target_object, target_module):
        if "resources" in target_module:
            self._parse_resources(target_object, target_module["resources"])
        if "child_modules" in target_module:
            target_object.modules = TerraformObject()
            target_object.modules.__all__ = {}
            for module in target_module["child_modules"]:
                module_name = get_attr_name(module["address"].split(".")[-1])
                setattr(target_object.modules, module_name, TerraformObject())
                module_object = getattr(target_object.modules, module_name)
                target_object.modules.__all__[module_name] = module_object
                self._parse_modules(module_object, module)

    def _parse_resources(self, target_object, resources):
        for resource in resources:
            if resource["mode"] == "managed":
                if hasattr(target_object, "resources") is False:
                    target_object.resources = TerraformObject()
                    target_object.resources.__all__ = {}
                resource_mode_object = target_object.resources
            elif resource["mode"] == "data":
                if hasattr(target_object, "data") is False:
                    target_object.data = TerraformObject()
                    target_object.data.__all__ = {}
                resource_mode_object = target_object.data
            else:
                raise Exception("Invalid terraform resource mode.")
            if hasattr(resource_mode_object, resource["type"]) is False:
                setattr(
                    resource_mode_object,
                    resource["type"],
                    TerraformObject(),
                )
            resource_type_object = getattr(
                resource_mode_object,
                resource["type"],
            )
            if resource["type"] not in resource_mode_object.__all__:
                resource_mode_object.__all__[resource["type"]] = resource_type_object
                resource_type_object.__all__ = {}
            resource_name = get_attr_name(resource["name"])
            if "index" in resource:
                if hasattr(resource_type_object, resource_name) is False:
                    setattr(
                        resource_type_object,
                        resource_name,
                        TerraformObject(),
                    )
                resource_name_object = getattr(
                    resource_type_object,
                    resource_name,
                )
                if type(resource["index"]) is str:
                    if hasattr(resource_name_object, "instances") is False:
                        setattr(resource_name_object, "instances", {})
                    resource_name_object.instances.update(
                        {resource["index"]: TerraformObjectParser(resource)}
                    )
                elif type(resource["index"]) is int:
                    if hasattr(resource_name_object, "instances") is False:
                        setattr(resource_name_object, "instances", [])
                    resource_name_object.instances.append(
                        TerraformObjectParser(resource)
                    )
                else:
                    raise Exception("Invalid terraform resource index.")
            else:
                setattr(
                    resource_type_object,
                    resource_name,
                    TerraformObjectParser(resource),
                )
                resource_name_object = getattr(
                    resource_type_object,
                    resource_name,
                )
            if resource_name not in resource_type_object.__all__:
                resource_type_object.__all__[resource_name] = resource_name_object

    def _parse_outputs(self):
        if "outputs" not in self._target_values:
            return None
        self.outputs = TerraformObject()
        self.outputs.__all__ = {}
        for _key, value in self._target_values["outputs"].items():
            key = get_attr_name(_key)
            setattr(self.outputs, key, TerraformObject())
            target_object = getattr(self.outputs, key)
            self.outputs.__all__[key] = target_object
            target_object.sensitive = value["sensitive"]
            if "value" in value:
                target_object.type = get_output_type(value["value"])
                if type(value["value"]) is dict:
                    target_object.value = TerraformObjectParser(
                        data=value["value"], is_testable=False
                    )
                else:
                    target_object.value = value["value"]
            else:
                target_object.type = target_object.value = None
