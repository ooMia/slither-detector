from typing import List
from slither.core.declarations.function import Function
from slither.core.solidity_types.elementary_type import ElementaryType
from slither.utils.output import Output
from slither.detectors.abstract_detector import (
    AbstractDetector,
    DetectorClassification,
    DETECTOR_INFO,
)
from slither.core.cfg.node import Node


class HelloWorldDetector(AbstractDetector):
    ARGUMENT = "hello-world"
    HELP = "Check if the function returns 'Hello, World!'"
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.HIGH
    WIKI = "none"
    WIKI_TITLE = "none"
    WIKI_DESCRIPTION = "none"
    WIKI_EXPLOIT_SCENARIO = "none"
    WIKI_RECOMMENDATION = "none"

    def _detect(self) -> List[Output]:
        """
        문자열 "Hello, World!"만을 반환하는 함수가 있는지 검사합니다.
        """
        results = []
        for contract in self.contracts:

            string_return_functions = [
                function
                for function in contract.functions
                if self._is_function_returns_string(function)
            ]
            for function in string_return_functions:

                hello_world_nodes = [
                    node for node in function.nodes if self._is_hello_world_node(node)
                ]
                if hello_world_nodes:
                    info: DETECTOR_INFO = ["returns 'Hello, World!' ", function, "\n"]
                    res = self.generate_result(info)
                    results.append(res)
        return results

    def _is_function_returns_string(self, function: Function) -> bool:
        """
        함수가 문자열 하나를 반환하는지 확인합니다.
        """
        return (
            function.return_type is not None
            and len(function.return_type) == 1
            and isinstance(function.return_type[0], ElementaryType)
            and function.return_type[0].type == "string"
        )

    def _is_hello_world_node(self, node: Node) -> bool:
        """
        노드가 'Hello, World!' 문자열을 반환하는지 확인합니다.
        """
        return node.will_return and str(node.expression) == "Hello, World!"
