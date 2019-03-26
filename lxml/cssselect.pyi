from typing import Dict, List, Optional, Union

from lxml import etree


_DictAnyStr = Union[Dict[str, str], Dict[bytes, bytes]]


class CSSSelector(etree.XPath):
    def __init__(self,
                 css: str,
                 namespaces: Optional[_DictAnyStr] = ...,
                 translator: str = ...): ...
    def __call__(self, element: etree._Element) -> List[etree._Element]: ...
