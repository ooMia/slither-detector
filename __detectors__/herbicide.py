import re
from typing import List
from slither.core.declarations.function import Function
from slither.core.solidity_types.user_defined_type import UserDefinedType
from slither.core.solidity_types.elementary_type import ElementaryType
from slither.utils.output import Output
from slither.detectors.abstract_detector import (
    AbstractDetector,
    DetectorClassification,
    DETECTOR_INFO,
)
from slither.core.solidity_types.type import Type
from slither.core.cfg.node import Node, NodeType
from slither.core.declarations import Contract
from slither.core.declarations.structure import Structure
from slither.core.declarations.structure_contract import StructureContract


class HerbicideDetector(AbstractDetector):
    ARGUMENT = "herbicide"
    HELP = "none"
    IMPACT = DetectorClassification.MEDIUM
    CONFIDENCE = DetectorClassification.HIGH
    WIKI = "none"
    WIKI_TITLE = "none"
    WIKI_DESCRIPTION = "none"
    WIKI_EXPLOIT_SCENARIO = "none"
    WIKI_RECOMMENDATION = "none"

    def _detect(self) -> List[Output]:
        """
        Detects contracts inheriting BaseHook and validates hook permissions.
        This detector performs the following checks:
            1. Identifies if contract inherits from BaseHook
            2. Validates getHookPermissions() function returns correct Hooks.Permissions struct
            3. Verifies that corresponding hook functions exist for enabled permissions
        """

        results = []
        for contract in self.contracts:
            if not self._is_contract_inherits_BaseHook(contract):
                continue

            permission_set = set()
            function_set = set()
            for function in contract.functions_declared:
                match function.name:
                    case "getHookPermissions":
                        if self._is_valid_getHookPermissions(function):
                            perms: list = self._get_active_permissions(function)
                            permission_set = set([f"_{perm}" for perm in perms])
                    case _:
                        function_set.add(function.name)

            if permission_set - function_set:
                # Add permissions that are not implemented to the results
                for perm in permission_set - function_set:
                    info: DETECTOR_INFO = [
                        "Permission not implemented: ",
                        perm,
                        " in contract ",
                        contract,
                        "\n",
                    ]
                    res = self.generate_result(info)
                    results.append(res)
        return results

    def _is_contract_inherits_BaseHook(self, contract: Contract) -> bool:
        """
        Base assumption of the contract:
            1. The contract inherits `BaseHook`
        """
        for contract in contract.inheritance:
            if contract.name == "BaseHook":
                return True
        return False

    def _is_valid_getHookPermissions(self, function: Function) -> bool:
        """
        Base assumption of the function `getHookPermissions`:
            1. The function is public
            2. The function overrides a function from `BaseHook`
            3. The function returns a inline struct of type Hooks.Permissions
        """
        is_public = function.visibility == "public"
        is_override = function.is_override
        is_return_struct = (
            function.return_type is not None
            and len(function.return_type) == 1
            and isinstance(function.return_type[0], UserDefinedType)
            and isinstance(function.return_type[0].type, StructureContract)
        )
        if not all([is_public, is_override, is_return_struct]):
            return False

        for node in function.nodes:
            if node.type != NodeType.RETURN:
                continue
            return (
                re.search(r"Hooks\.Permissions\(\{[\w\:,]+\}\)", str(node.expression))
                is not None
            )
        return False

    def _get_active_permissions(self, function: Function) -> List[str]:
        """
        Returns a list of active permissions from the getHookPermissions() function.
        """
        for node in function.nodes:
            if node.type == NodeType.RETURN:
                matches = re.findall(r"(\w+)\s*:\s*true", str(node.expression))
                filtered_matches = [match for match in matches if "Delta" not in match]
                return filtered_matches
        return []
