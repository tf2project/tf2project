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
        self.root = TerraformObject()
        self._load_data()
        self._fetch_target_values()
        self._parse_modules(
            self.root,
            self._target_values["root_module"],
        )
        self._parse_outputs()

    def _load_data(self):
        self._data = self._loader_instance.load()

    def _fetch_target_values(self):
        loader_type = self._loader_instance.loader_type
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
            for module in target_module["child_modules"]:
                module_name = module["address"].split(".")[-1].replace("-", "_")
                setattr(target_object.modules, module_name, TerraformObject())
                self._parse_modules(
                    getattr(target_object.modules, module_name),
                    module,
                )

    def _parse_resources(self, target_object, resources):
        for resource in resources:
            if resource["mode"] == "managed":
                if hasattr(target_object, "resources") is False:
                    target_object.resources = TerraformObject()
                target_object = target_object.resources
            elif resource["mode"] == "data":
                if hasattr(target_object, "data") is False:
                    target_object.data = TerraformObject()
                target_object = target_object.data
            else:
                raise Exception("Invalid terraform resource mode.")
            if hasattr(target_object, resource["type"]) is False:
                setattr(target_object, resource["type"], TerraformObject())
            resource_type_object = getattr(target_object, resource["type"])
            resource_name = resource["name"].replace("-", "_")
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

    def _parse_outputs(self):
        if "outputs" not in self._target_values:
            return None
        self.outputs = TerraformObject()
        # FIXME: if the key consists of dashes, it will be cracked.
        for key, value in self._target_values["outputs"].items():
            setattr(self.outputs, key, TerraformObject())
            target_object = getattr(self.outputs, key)
            target_object.sensitive = value["sensitive"]
            target_object.type = match_regex(
                "<class '(.*)'>",
                str(type(value["value"])),
            )[1]
            if type(value["value"]) is dict:
                target_object.value = TerraformObjectParser(
                    value["value"], testable=False
                )
            else:
                target_object.value = value["value"]
