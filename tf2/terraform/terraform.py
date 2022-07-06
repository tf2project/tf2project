# Terraform Test Framework
# https://github.com/tf2project/tf2

from re import match as match_regex

from .loader import TerraformStateLoader
from .object import TerraformObject, TerraformObjectParser


class Terraform:
    def __init__(self, loader_instance=None):
        if loader_instance is None:
            self._loader_instance = TerraformStateLoader()
        else:
            self._loader_instance = loader_instance
        self.resources = TerraformObject()
        self.data = TerraformObject()
        self.outputs = TerraformObject()
        self._load_data()
        self._fetch_target_values()
        self._parse_root_module_resources()
        self._parse_child_modules_resources()
        self._parse_outputs()

    def _load_data(self):
        self._terraform_data = self._loader_instance.load()

    def _fetch_target_values(self):
        current_loader_type = self._loader_instance.loader_type
        if current_loader_type == "planloader":
            self._target_values = self._terraform_data["planned_values"]
        elif current_loader_type == "stateloader":
            self._target_values = self._terraform_data["values"]
        else:
            raise Exception("Invalid terraform resource loader.")

    def _parse_root_module_resources(self):
        if "resources" not in self._target_values["root_module"]:
            return None
        self._parse_resources(
            "root_module", self._target_values["root_module"]["resources"]
        )

    def _parse_child_modules_resources(self):
        if "child_modules" not in self._target_values["root_module"]:
            return None
        for module in self._target_values["root_module"]["child_modules"]:
            module_name = module["address"].removeprefix("module.").replace("-", "_")
            self._parse_resources(
                "_".join((module_name, "module")),
                module["resources"],
            )

    def _parse_resources(self, module_name, resources):
        for resource in resources:
            if resource["mode"] == "managed":
                if hasattr(self.resources, module_name) is False:
                    setattr(self.resources, module_name, TerraformObject())
                module_object = getattr(self.resources, module_name)
            elif resource["mode"] == "data":
                if hasattr(self.data, module_name) is False:
                    setattr(self.data, module_name, TerraformObject())
                module_object = getattr(self.data, module_name)
            else:
                raise Exception("Invalid terraform resource mode.")
            resource_type = resource["type"]
            if hasattr(module_object, resource_type) is False:
                setattr(module_object, resource_type, TerraformObject())
            resource_type_object = getattr(module_object, resource_type)
            resource_name = resource["name"].replace("-", "_")
            if "index" not in resource:
                setattr(
                    resource_type_object,
                    resource_name,
                    TerraformObjectParser(resource),
                )
            else:
                if hasattr(resource_type_object, resource_name) is False:
                    setattr(resource_type_object, resource_name, TerraformObject())
                resource_name_object = getattr(resource_type_object, resource_name)
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

    def _parse_outputs(self):
        if "outputs" not in self._target_values:
            return None
        # FIXME: if the key consists of dashes, it will be cracked.
        for key, value in self._target_values["outputs"].items():
            setattr(self.outputs, key, TerraformObject())
            output_object = getattr(self.outputs, key)
            output_object.sensitive = value["sensitive"]
            output_type = match_regex("<class '(.*)'>", str(type(value["value"])))
            output_object.type = output_type[1]
            if type(value["value"]) is dict:
                output_object.value = TerraformObjectParser(
                    value["value"], testable=False
                )
            else:
                output_object.value = value["value"]
